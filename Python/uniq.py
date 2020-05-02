import argparse
import os, sys
#repeat_check func
def repeat_check(index,lines):
    count=0
    for i in range(index,len(lines)):
        if lines[i].rstrip()==lines[index].rstrip():
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
def read_line(input_file,counting,only_dup,all_dup):
    filepath = sys.stdin if input_file=='standard input' else open(input_file,'r')
    lines=filepath.readlines()
    index=0
    while True:
        if index==len(lines):
            break
        count,new_index=repeat_check(index,lines)
        if only_dup:
            if count==1:
                index=new_index
                continue
        no_times=1
        if all_dup:
            no_times=count
        for _ in range(no_times):
            printing_line(index,lines,counting,count)
        index =new_index
#setup_parser
def setup_parser():
    parser=argparse.ArgumentParser(prog='uniq',description='Filter adjacent matching lines from INPUT (or standard input)'\
        'writing to output (or standard output)',
        usage='uniq [OPTIONS]... [INPUT]')

    parser.add_argument('-c','--count',action='store_true',help='prefix lines with the no of occurence')
    parser.add_argument('-d','--repeated',action='store_true',help='only prints duplicate lines, one for each group')
    parser.add_argument('-D',action='store_true',help='print all duplicate lines')
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
    all_dup= args.D
    if counting and all_dup:
        print('uniq: printing all duplicate lines and repeat counts is meaningless')
        print("try python 'uniq.py --help' for more help")
        exit(-1)
    read_line(input_file,counting,only_dup,all_dup)

main()
