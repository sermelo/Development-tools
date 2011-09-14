#!/usr/bin/env python

file="/etc/passwd"


f = open(file, 'r')
for line in f:
    line=line.strip()
    line=line.split(":")
    print line[0]+" -> "+line[6]

f.close
