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
                if n>=0:
                    auxlink=str(link['href'])
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
                        read_web(urlweb+link['href'],n)
                    else:
                        read_web(auxlink,n)
            

parser=argparse.ArgumentParser(description="This is a crawler")
parser.add_argument('-n','--number-of-levels',type=int,default=1,help="Number of desired depth")
parser.add_argument('url',nargs=1,help="target URL")
args=parser.parse_args()
read_web(args.url.pop(),args.number_of_levels)
