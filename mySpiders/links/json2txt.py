#-*- coding: UTF-8 -*-
import json

data = []
try:
    inFile = raw_input('Select the json file: ')
    fo = open(inFile, 'r')
    for line in fo.readline().strip('\n'):
        data.append(json.loads(line))
except IOError, e:
    print e
    exit(1)
#print json.dumps(data, ensure_ascii=False)

import codecs

try:
    outFile = raw_input('Input the txt filename: ')
    file_object = codecs.open(outFile, 'w' ,"utf-8")
    for item in data:
        #print json.dumps(item)
        str = "%s#_#%s#_#%s\r\n" %\
            (item['test_title'],item['test_links'],item['test_time'])
#        d = json.dumps(str, ensure_ascii=False)
        file_object.write(str)
except IOError, e:
    print e
    exit(1)

file_object.close()
print "Mission info : json ---> txt done successfully."
