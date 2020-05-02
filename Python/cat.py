import argparse
import sys
my_parser=argparse.ArgumentParser(
    prog='cat',
    description='Reads from stdin and print to stdout'
    )
my_parser.add_argument('path',nargs='*',help='path to the file to read')
my_parser.add_argument('-o','--output',help='to redirect printing to a file',action='store',metavar='path')
args=my_parser.parse_args()
paths=vars(args)['path']

if len(paths)==0:
    paths.append('-')

for path in paths:
    if path =='-':
        read=sys.stdin.read()
    else:
        with open(path,'r') as file:
            read=file.read()
        file.close()
    if vars(args)['output']==None:
        print(read)
    else:
        with open(vars(args)['output'],'a') as file:
            file.write(read)