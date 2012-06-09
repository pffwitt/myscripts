#!/usr/bin/python
##################################################
# Website crawler
##################################################
import re, urllib2, argparse, StringIO

# Args
parser = argparse.ArgumentParser()
parser.add_argument('--url', action='store', dest='url', help='Url to check')
arg = parser.parse_args()

def geturl(url):
    usock = urllib2.urlopen(url)
    page = usock.read()
    usock.close()
    return page

links = []
def findlinks(data):
    page = StringIO.StringIO(data)
    regexlinks = re.compile(r"(https?://[^\"\' >]+)")
    for line in page.readlines():
        match = regexlinks.search(line)
        if match:
            urlfound = match.group(1)
            if urlfound not in links:
                links.append(urlfound)
    return links

def followlinks(links):
    for link in links:
        print "[found link] : " + link
    
page = geturl(arg.url)
blabla = findlinks(page)
followlinks(blabla)
