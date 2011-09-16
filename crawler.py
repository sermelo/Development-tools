#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup as Soup
import urllib2
import argparse

urlweb="http://www.wired.com/"

def read_web(urlweb,n):
    if n==0:
        print urlweb
    else:
        _opener = urllib2.build_opener()
        try:
            raw_code = _opener.open(urlweb).read()
        except:
            print "We could not open this url:"+urlweb
            return
        soup_code = Soup ( raw_code )
        n=n-1
        for link in soup_code.findAll('a'):
            if link.has_key("href"):
               # print link["href"]
                if n>=0:
                    auxlink=str(link['href'])
                    auxlink=auxlink.strip()
                    if auxlink=="":
                        continue
                    elif auxlink[0]=="/":
                        read_web(urlweb+link['href'],n)
                    elif auxlink[0]=="#":
                        continue
                    else:
                        read_web(auxlink,n)
            

parser=argparse.ArgumentParser(description="This is a crawler")
parser.add_argument('-n','--number-of-levels',type=int,default=1,help="Number of desired depth")
parser.add_argument('url',nargs=1,help="target URL")
args=parser.parse_args()
print args.number_of_levels
#print args.url.pop()
read_web(args.url.pop(),args.number_of_levels)
