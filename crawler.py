#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup as Soup
import urllib2
import argparse

urlweb="http://www.wired.com/"

def read_web(urlweb,n):
    _opener = urllib2.build_opener()
    try:
        raw_code = _opener.open(urlweb).read()
    except:
        print "We could not open this url:"+urlweb
        return
    n=n-1
    soup_code = Soup ( raw_code )
    for link in soup_code.findAll('a'):
        if link.has_key("href"):
            print link["href"]
            if n!=0:
                read_web(link['href'],n)
            

parser=argparse.ArgumentParser(description="This is a crawler")
parser.add_argument('-n','--number-of-levels',type=int,default=1,help="Number of desired depth")
parser.add_argument('url',nargs=1,help="target URL")
args=parser.parse_args()
print args.number_of_levels
#print args.url.pop()
read_web(args.url.pop(),args.number_of_levels)
