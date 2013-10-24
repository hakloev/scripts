import urllib2
import hashlib
import os
import time
import sys
from BeautifulSoup import BeautifulSoup

def getResponseAndMd5():
    response = urllib2.urlopen('http://store.apple.com/us/buy-iphone/iphone5s')
    html = response.read()
    response.close()

    soup = BeautifulSoup(html)

    md5 = ""
    for tag in soup.findAll('span'):
        if tag.has_key('class'):
            if tag['class'] == 'shipping':
                return str(hashlib.md5(str(tag)).hexdigest())

if __name__ == '__main__':
    if len(sys.argv) > 1:
        interval = float(sys.argv[1])
    else:
        interval = float(raw_input('Hvor langt oppdateringsintervall vil du ha i hele minutter? '))
    
    while True:
        md5 = getResponseAndMd5()
        if md5 == 'fa82cd05451f41b7c6cd51e6ce3d1ba9':
            print 'Ikke lansert enda!'
        else:
            os.system('say Something has changed on Apples webpage!')
            os.system('open -a Safari http://store.apple.com/no/buy-iphone/iphone5s')
            print 'Lansert, eller noe er i det minste endret!'
            print 'Den nye md5-summen: ', md5
            break
        
        if interval <= 1:
            print 'Sover i', interval, 'minutt'
        else:
            print 'Sover i', interval, 'minutter'
        time.sleep(interval * 60)