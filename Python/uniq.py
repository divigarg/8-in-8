import argparse
import os, sys
#repeat_check func
def repeat_check(index,lines):
    if index!=len(lines)-1 and lines[index]==lines[index+1]: 
        return True
    else:
        return False

#printing_line definiition
def printing_line(index,lines,counting,count):
    result=''
    if counting:
        result=result+str(count)+' '
    result=result+lines[index]
    sys.stdout.write(result)

#read lines file
def read_line(input_file,counting):
    filepath = sys.stdin if input_file=='standard input' else open(input_file,'r')
    lines=filepath.readlines()
    count=1
    for index in range(len(lines)):
        if not repeat_check(index,lines):
            printing_line(index,lines,counting,count)
            count=1
        else:
            count+=1
    print()
#setup_parser
def setup_parser():
    parser=argparse.ArgumentParser(prog='uniq',description='Filter adjacent matching lines from INPUT (or standard input)'\
        'writing to output (or standard output)')
    parser.add_argument('-c','--count',action='store_true',help='prefix lines with the no of occurence')
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
    read_line(input_file,counting)

hello=True
print("hello")
main()
