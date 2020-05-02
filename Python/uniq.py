import argparse
import os, sys
#repeat_check func
def repeat_check(index,lines,icase,Nchars):
    count=0
    for i in range(index,len(lines)):
        line_1=lines[i][Nchars:].rstrip()
        line_2=lines[index][Nchars:].rstrip()
        if icase:
            line_1=line_1.lower()
            line_2=line_2.lower()
        if line_1==line_2:
            count+=1
        else:
            return count,i
    return count,len(lines)


#printing_line definiition
def printing_line(index,lines,counting,count):
    result=''
    if counting:
        result=result+str(count)+' '
    result=result+lines[index]
    sys.stdout.write(result)

#read lines file
def read_line(input_file,counting,only_dup,all_dup,icase,Nchars,only_nondup):
    filepath = sys.stdin if input_file=='standard input' else open(input_file,'r')
    lines=filepath.readlines()
    index=0
    while True:
        if index==len(lines):
            break
        count,new_index=repeat_check(index,lines,icase,Nchars)
        if only_dup:
            if count==1:
                index=new_index
                continue
        if only_nondup:
            if count!=1:
                index=new_index
                continue
        no_times=1
        if all_dup:
            no_times=count
        for i in range(index,index+no_times):
            printing_line(i,lines,counting,count)
        index =new_index
#setup_parser
def setup_parser():
    parser=argparse.ArgumentParser(prog='uniq',description='Filter adjacent matching lines from INPUT (or standard input)'\
        'writing to output (or standard output)',
        usage='uniq [OPTIONS]... [INPUT]')

    parser.add_argument('-c','--count',action='store_true',help='prefix lines with the no of occurence')
    d_u=parser.add_mutually_exclusive_group()
    d_u.add_argument('-d','--repeated',action='store_true',help='only prints duplicate lines, one for each group')
    d_u.add_argument('-u','--unique',action='store_true',help='only prints unique lines')
    parser.add_argument('-D',action='store_true',help='print all duplicate lines')
    parser.add_argument('-i','--ignore-case',action='store_true',help='ignore differences in case when comparing')
    parser.add_argument('-s','--skip-chars',metavar='N',action='store',default=0,type=int,help='avoid comparing the first N chars')
    parser.add_argument('input',metavar='INPUT',action='store',type=str,default='-',nargs='?',help='the file(s) to handle')
    return parser
#main func
def main():
    parser=setup_parser()
    args=parser.parse_args()
    input_file=args.input
    if input_file=='-':
        input_file='standard input'
    counting=args.count
    only_dup=args.repeated or args.D
    only_nondup=args.unique
    all_dup= args.D
    Nchars=args.skip_chars
    icase=args.ignore_case
    
    if counting and only_nondup:
        print('uniq: printing only unique lines and repeat counts is meaningless')
        print("try 'python uniq.py --help' for more help")
        exit(-1)
    
    if counting and all_dup:
        print('uniq: printing all duplicate lines and repeat counts is meaningless')
        print("try 'python uniq.py --help' for more help")
        exit(-1)
    read_line(input_file,counting,only_dup,all_dup,icase,Nchars,only_nondup)

main()
