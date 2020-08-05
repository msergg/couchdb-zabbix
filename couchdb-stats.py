#!/bin/python
import sys
import json
import urllib2
import  base64

def getFromDict(dataDict, mapList):
    for k in mapList:
        try:
            dataDict = dataDict[k]
        except:
            sys.exit("ERROR: No key " + sys.argv[1])
    return dataDict

if len(sys.argv[1]) < 1:
    print 'please, specify a metric.'
    print ' ex: ./couchdb-stats.py couchdb.httpd.aborted_requests.value'

try:
    couch_node='couchdb@127.0.0.1'
    req = urllib2.Request('http://127.0.0.1:5984/_node/{}/_stats'.format(couch_node))
    username = 'user'
    password = 'password'

    base64string = base64.b64encode('%s:%s' % (username, password))
    req.add_header("Authorization", "Basic %s" % base64string)

    stats_json = urllib2.urlopen(req)
except urllib2.URLError, e:
    print e.reason
    exit(1)

metric = sys.argv[1].split('.')

res = getFromDict(json.load(stats_json), metric)
try:
    print int(res)
except:
    sys.exit('ERROR: Return value cant be converted to int... Value:' + str(res))
