#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup as Soup
import urllib2
import argparse
import sys
import progressbar


complete_list=[]

def read_web(urlweb,n,total_levels):
    global complete_list
    for i in range(total_levels-n+1):
        try:
            complete_list[i].index(urlweb)
            return
        except ValueError:
            continue

    complete_list[total_levels-n].append(urlweb)
    sys.stdout.write(".")
    if n!=0:
        _opener = urllib2.build_opener()
        try:
            raw_code = _opener.open(urlweb,"",10).read()
        except:
            print "\nWe could not open this url:"+urlweb
            return
        soup_code = Soup ( raw_code )
        n=n-1
        for link in soup_code.findAll('a'):
            if link.has_key("href"):
                if n>=0:
                    try:
                        auxlink=str(link['href'])
                    except UnicodeEncodeError:
                        print "\nUnicodeError captured"
                        continue
                    auxlink=auxlink.strip()
                    auxlink=auxlink.lower()
                    if auxlink=="":
                        continue
                    elif auxlink.rfind("javascript")!=-1:
                        continue
                    elif auxlink[0]=="#":
                        continue
                    elif auxlink[0]=="/":
                        read_web(urlweb+link['href'],n,total_levels)
                    else:
                        read_web(auxlink,n,total_levels)

def init_list(n):
    global complete_list
    complete_list=[]
    for i in range(n+1):
        complete_list.append([])

def show_links():
    global complete_list
    counter=0
    for level in complete_list:
        print "\n\n\nLevel "+str(counter)+": "+str(len(level))
        counter=counter+1
        print "Do you want to see the links of this level?(Y/N)"
        show = sys.stdin.readline()
        show=show.lower()
        show=show.strip()
        if show=="y":
            for link in level:
                print link

parser=argparse.ArgumentParser(description="This is a crawler")
parser.add_argument('-n','--number-of-levels',type=int,default=1,help="Number of desired depth")
parser.add_argument('url',nargs=1,help="target URL")
args=parser.parse_args()
init_list(args.number_of_levels)
read_web(args.url.pop(),args.number_of_levels,args.number_of_levels)
show_links()









