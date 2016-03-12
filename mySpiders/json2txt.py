#-*- coding: UTF-8 -*-
import json

data = []
inFile = raw_input('Select the json file: ')
with open(inFile) as f:
    for line in f:
        data.append(json.loads(line))

#print json.dumps(data, ensure_ascii=False)

import codecs
outFile = raw_input('Input the txt filename: ')
file_object = codecs.open(outFile, 'w' ,"utf-8")
for item in data:
    #print json.dumps(item)
    str = "%s#_#%s#_#%s#_#%s\r\n" % (item['title'],item['link'],item['desc'],item['listUrl'])
    file_object.write(str)

file_object.close()
print "Mission info : json ---> txt done successfully."
