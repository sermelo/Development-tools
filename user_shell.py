#!/usr/bin/env python

file="/etc/passwd"
username=""

f = open(file, 'r')
dic={}
print "Method one:"
for line in f:
    line=line.strip()
    line=line.split(":")
    dic[line[0]]=line[6]
#Method one 
#Here we don't need to control errors
    if username==line[0]:
       print line[0]+" -> "+line[6]
#End method one

#Method two(expected method)
print "\nMethod two:"
try:
    print username+" -> "+dic[username]
except KeyError:
    if username=="":
        print "Input username is empty"
    else:
        print "Input username doesn't exist"
#End method two
f.close
