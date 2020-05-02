import sys,os
import argparse
parser=argparse.ArgumentParser(prog='find',description='To find all the files with specific property')
args=parser.parse_args()
path='.'
f = []
print(list(os.walk(path)))