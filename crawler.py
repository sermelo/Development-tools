#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup as Soup
import urllib2
import argparse

urlweb="http://www.wired.com/"

complete_list=[]

def read_web(urlweb,n,total_levels):
    global complete_list
    complete_list[total_levels-n].append(urlweb)
    print urlweb
    if n!=0:
        _opener = urllib2.build_opener()
        try:
            raw_code = _opener.open(urlweb,"",5).read()
        except:
            print "We could not open this url:"+urlweb
            return
        soup_code = Soup ( raw_code )
        n=n-1
        for link in soup_code.findAll('a'):
            if link.has_key("href"):
                if n>=0:
                    try:
                        auxlink=str(link['href'])
                    except UnicodeEncodeError:
                        print "UnicodeError captured"
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


parser=argparse.ArgumentParser(description="This is a crawler")
parser.add_argument('-n','--number-of-levels',type=int,default=1,help="Number of desired depth")
parser.add_argument('url',nargs=1,help="target URL")
args=parser.parse_args()
init_list(args.number_of_levels)
read_web(args.url.pop(),args.number_of_levels,args.number_of_levels)
#print complete_list
#print complete_list[0][0]
#print complete_list[0][1]









