#!/usr/bin/python
################################################################
# Web Spidering / Crawling
#
################################################################
import StringIO, argparse, re, urllib2

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('--url', action='store', dest='url', help='Url to check')
arg = parser.parse_args()

if not arg.url:
    parser.print_help()
    exit(1)

# Functions
def geturl(url):
    '''Return a web page content'''
    usock = urllib2.urlopen(url)
    page = usock.read()
    usock.close()
    return StringIO.StringIO(page)

# find links in page content
regexlinks = re.compile(r"(https?://[^\"\'<>\s]+)")

links_found = []

def findlinks(page):
    links = []
    
    for line in page.readlines():
        match = regexlinks.search(line)
        if match:
            urlfound = match.group(1)
            if urlfound not in links:
                links.append(urlfound)
    return links

# base page
page = geturl(arg.url)

# base page links
links_collection = findlinks(page)
links_visited = []

# recursive link search
while len(links_collection) > 0:
    link = links_collection.pop()
    links_visited.append(link)
    link_content = geturl(link)
    crawl_links = findlinks(link_content)
    for crawl_link in crawl_links:
        if crawl_link not in links_visited and crawl_link not in links_collection:
            links_collection.append(crawl_link)

# report
print "The following links have been crawled :\n"
for link_visited in links_visited:
    print "\t- %s" % link_visited