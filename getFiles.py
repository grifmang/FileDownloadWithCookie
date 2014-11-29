import urllib2
import urllib
from cookielib import CookieJar

files = 'http://www.nytimes.com/interactive/2014/11/25/us/evidence-released-in-michael-brown-case.html?_r=0'
slashpos = 0

def getLinks(url):
    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    p = opener.open(url)
    result = []
    for line in p:
        for element in line.split():
            if element.startswith('href="http://gr'):
                if element.endswith('pdf"') or element.endswith('png"') or element.endswith('jpg"'):
                    result.append(element[6:])
    for char in result:
        slashpos = char.rfind('/') + 1
        urllib.urlretrieve(char, char[slashpos:-1])

getLinks(files)

