#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup as Soup
import urllib2
import argparse
import sys
import os


complete_list=[]

def read_web(urlweb,n,total_levels):
    global complete_list
    global repeated
    global tree_mode
    urlweb2=urlweb.rstrip("/")
    for i in range(total_levels-n+1):
        try:
            complete_list[i].index(urlweb2)
            repeated+=1
            return
        except ValueError:
            continue
    if tree_mode:
        print "-"*(total_levels-n)+urlweb2

    complete_list[total_levels-n].append(urlweb2)
    if n!=0:

        user_agent = "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari /534.7 "
        opener = urllib2.build_opener()
        opener.addheaders=[('User-agent',user_agent)]

        try:
            raw_code = opener.open(urlweb,"",6).read()
        except:
            print "\nWe could not open this url:"+urlweb
            return
        try:
            soup_code = Soup (raw_code)
        except UnicodeEncodeError:
            print "Unicode Error in the html web: "+urlweb
        n=n-1
        for link in soup_code.findAll('a'):
            if link.has_key("href"):
                if n>=0:
                    try:
                        auxlink=str(link['href'])
                        auxlink=link['href']
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
                    elif auxlink[0]=='?':
                        read_web(urlweb+auxlink,n,total_levels)
                    elif auxlink.rfind("http")==-1:
                        num=-1
                        done=False
                        for i in range(3):
                            num+=1
                            try:
                              #  print urlweb
			        num=urlweb.index("/",num)
                            except ValueError:
                                done=True
                                break
                        if done==True:
                            read_web(urlweb+auxlink,n,total_levels)
                        else:
                            read_web(urlweb[0:num]+auxlink,n,total_levels)
                    else:
                        read_web(auxlink,n,total_levels)
    if not tree_mode:
        show_summary()


def init_list(n):
    global complete_list
    complete_list=[]
    for i in range(n+1):
        complete_list.append([])

def show_summary():
    global complete_list
    os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
    print "\n\nThis is the sumary:"
    counter=0
    for level in complete_list:
        print "Level "+str(counter)+": "+str(len(level))
        counter=counter+1
    print "Repeate links: "+str(repeated)

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
parser.add_argument('-t','--tree-mode',action='store_true',help="Tree mode active",required=False)
args=parser.parse_args()
repeated=0
init_list(args.number_of_levels)
tree_mode=args.tree_mode

read_web(args.url.pop(),args.number_of_levels,args.number_of_levels)
show_links()









