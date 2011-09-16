#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup as Soup
import urllib2

urlweb="http://www.wired.com/"

_opener = urllib2.build_opener()
raw_code = _opener.open(urlweb).read()

soup_code = Soup ( raw_code )
#links=[link["href"] for link
#	in soup_code.findAll('a')
#	if link.has_key("href")]

for link in soup_code.findAll('a'):
    if link.has_key("href"):
        print link["href"]
