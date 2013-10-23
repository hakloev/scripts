import urllib2
import hashlib
import os
import time
from BeautifulSoup import BeautifulSoup

def getResponseAndMd5():
    response = urllib2.urlopen('http://store.apple.com/no/buy-iphone/iphone5s')
    html = response.read()
    response.close()

    soup = BeautifulSoup(html)

    md5 = ""
    for tag in soup.findAll('span'):
        if tag.has_key('class'):
            if tag['class'] == 'shipping':
                return str(hashlib.md5(str(tag)).hexdigest())

if __name__ == '__main__':
    Flag = True
    while Flag:
        md5 = getResponseAndMd5()
        if md5 == '43d30f94f0fcde617a4eb441b37851fe':
            print 'Ikke lansert enda!'
        else:
            print 'Den nye md5-summen: ', md5
            print 'LANSERT'
            Flag = False
        print 'Sover i 10 sekunder'
        time.sleep(10)

