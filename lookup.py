import re
import argparse
# from argparse import ArgumentParser


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("word",help='Specify word to be searched ')
    parser.add_argument("fname",help="Specify file name to search")
    args = parser.parse_args()
    searchfile=open(args.fname,"r")
    linenum=0

    for line in searchfile.readlines():
        line=line.strip('\n\r')
        linenum+=1
        searchres=re.search(args.word,line,re.M|re.I)
        if searchres:
            print(str(linenum)+" : "+line)

if __name__ == '__main__':
    main()
