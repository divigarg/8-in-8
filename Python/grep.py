import argparse
import sys
import os
RED="\033[1;31m"
BLUE="\033[1;34m"
END="\033[0m"


def index_pattern(line,pattern,word_only):
    lst=[]
    for i in range(len(line)):
        for j in range(len(pattern)):
            if line[i+j]!=pattern[j]:
                break
            if j==len(pattern)-1:
                if not word_only:
                    lst.append(i)
                else:
                    if (i==0 or line[i-1]==' ') and (i+j+1==len(line) or line[i+j+1]==' '):
                        lst.append(i)
    return lst

def color_pattern(line,len_pattern,lst_index):
    result=line
    count=0
    for index in lst_index:
        index_new=index+count*11
        result=result[:index_new]+RED+result[index_new:index_new+len_pattern]+END+result[index_new+len_pattern:]
        count+=1
    return result
#def get_match
def get_match(line,pattern,word_only,line_only):
    if line_only==True:
        if line.strip()!=pattern:
            return ''
    if pattern in line:
        colored=color_pattern(line,len(pattern),index_pattern(line,pattern,word_only))
        return colored
    else:
        return ''

#def print_result
def print_result(file,result,lineno,line_no):
    if lineno==True:
        result=BLUE+str(line_no)+END+" "+result
    sys.stdout.write(result)

#def grep_file
def grep_file(file,pattern,word_only,line_only,lineno):
    file_open= sys.stdin if file=='(standard input)' else open(file,'r')
    line=file_open.readline()
    line_no=1
    while line:
        result = get_match(line,pattern,word_only,line_only)
        if len(result)>0:
            print_result(file,result,lineno,line_no)
        line=file_open.readline()
        line_no+=1
    file_open.close()


#define grep_files
def grep_files(files,pattern,word_only,line_only,lineno):
    for file in files:
        if os.path.isfile(file) or file=='(standard input)':
            grep_file(file,pattern,word_only,line_only,lineno)
        else:
            sys.stdout.write('grep: %s: Is a directory\n' % file)

#define parser
def setup_parser():
    parser=argparse.ArgumentParser(prog='grep',description='Find matches of patterns'\
        'in the lines of file(s)')
    
    parser.add_argument('-w','--word-regexp',action='store_true',help='match only whole words')
    parser.add_argument('-x','--line-regexp',action='store_true',help='match only whole lines')
    parser.add_argument('-n','--line-number',action='store_true',help='print line number with output lines')
    parser.add_argument('pattern',type=str,help='the pattern to find')
    parser.add_argument('files',metavar='Files',nargs='*',default=['-'],help='the file(s) to search')
    return parser


# main fun
def main():
    parser=setup_parser()
    args=parser.parse_args()
    pattern=args.pattern
    word_only=args.word_regexp
    line_only=args.line_regexp
    lineno=args.line_number
    files = [file if file!='-' else '(standard input)' for file in args.files]

    grep_files(files,pattern,word_only,line_only,lineno)

main()