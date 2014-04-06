#!/usr/bin/env python
# encoding: utf-8

"""
Script to update a given domain record at Digital Ocean whenever the IP changes. Also sends an email to given email-address.
The script is made in such a way that the possibility to add more functionality like selecting record type or record id etc will be easy.

Version 1.0
 
Created by Håkon Ødegård Løvdal on 2014-04-06
"""

import urllib2, re, datetime, json

old = 'lastip.txt'
history = 'iphistory.txt'

clientid = 'YOUR CLIENT ID'
apikey = 'YOUR API KEY'
# If you want to hardcode it use these fields
recordid = 'ID' 
recordtype = 'TYPE'
domainid = 'ID' # loevdal.net

baseurl = 'https://api.digitalocean.com/domains/%s' % (domainid)

def getip():
    connection = urllib2.urlopen('http://checkip.dyndns.com/')
    data = connection.read()
    connection.close()
    ipmatch = re.search("(\\d{1,3}).(\\d{1,3}).(\\d{1,3}).(\\d{1,3}).(\\d{1,3})", data)
    return ipmatch.group(0)
    #return '192.168.1.6'

def getlastip():
    lastipfile = open(old, 'r')
    lastip = lastipfile.read()
    lastipfile.close()
    return lastip.strip('\n')

def setlastip(ip):
    lastipfile = open(old, 'w')
    lastipfile.write(ip + '\n')
    lastipfile.close()

def appendtoiphistory(type, ip):
    historyfile = open(history, 'a')
    if type == 1:
        now = datetime.datetime.now().ctime()
        historyfile.write("At %s did the IP change to %s\n" % (now, ip)) 
    elif type == 2:
        statusdict = ip['record']
        toappend = ("Updated Digital Ocaen | DomainID: %s | RecordID: %s | RecordTYPE: %s | IP: %s\n") % (statusdict['domain_id'], statusdict['id'], statusdict['record_type'], statusdict['data'])
        historyfile.write(toappend)
    historyfile.close()

def sendmail(ip):
    pass

def updatednsrecord(ip):
    #update record tupple (record_id, client_id, api_key, record_type, data)
    endofurl = '/records/%s/edit?client_id=%s&api_key=%s&record_type=%s&data=%s' % (recordid, clientid, apikey, recordtype, ip)
    connection = urllib2.urlopen(baseurl + endofurl)
    response = json.loads(connection.read())
    connection.close()
    if response['status'] == 'OK':
        print "Updated IP @ Digital Ocean"
        appendtoiphistory(2, response)
    else:
        print "Something went wrong during update to Digital Ocean"

if __name__ == '__main__':
    currip = getip()
    lastip = getlastip()
    
    if currip == lastip:
        print 'No change in IP'
    else:
        print 'IP changed, updating files'
        appendtoiphistory(1, currip)
        setlastip(currip)
        updatednsrecord(currip)
        sendmail(currip)
