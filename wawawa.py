#!/usr/bin/python
import re, urllib2, argparse, StringIO

# args
parser = argparse.ArgumentParser()
parser.add_argument('--url', action='store', dest='url', help='Url to check')
arg = parser.parse_args()

if not arg.url:
    parser.print_help()
    exit(1)

# return url content
def geturl(url):
    usock = urllib2.urlopen(url)
    page = usock.read()
    usock.close()
    return page

# find links in page content
regexlinks = re.compile(r"(https?://[^\"\' >]+)")
links = { arg.url : '1'}

def findlinks(content):
    page = StringIO.StringIO(content)
    
    for line in page.readlines():
        match = regexlinks.search(line)
        if match:
            urlfound = match.group(1)
            if urlfound not in links.keys():
                links[urlfound] = 0
    return links

#####################################################

page = geturl(arg.url)
links_collection = findlinks(page)

for link in links_collection:
    page = geturl(arg.url)
    links_collection = findlinks(page)

print links_collection
#for link in links_collection.popitem():
#    if not links[link]:
#        page = geturl(link)
#        links_parse = findlinks(page)
#        links_collection[link] = 1

#links_collection = findlinks(page)
     
#for k,v in links_collection.items():
#    print "%s = %s" % (k,v)

