# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json, codecs
from hashlib import md5
import MySQLdb.cursors, MySQLdb
from twisted.enterprise import adbapi

class KaoshiPipeline(object):

    def __init__(self):
        self.file = codecs.open('info.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class MysqldbPipeline(object):

    def __init__(self):
        # init mysql connection info
        self.dbpool = adbapi.ConnectionPool(
            dbapiName='MySQLdb',
            host='localhost',
            db='mydata',
            user='root',
            passwd='root',
            cursorclass=MySQLdb.cursors.DictCursor,
            charset='utf8',
            use_unicode=False,
        )

    def process_item(self, item, spider):
        # 递归调用 _conditional_insert
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    def _get_linkmd5(self, item):
        # get url md5 coding
        return md5(str(item['test_links'])).hexdigest()

    def _conditional_insert(self, ret, item):
        linkmd5 = self._get_linkmd5(item)

        # write items in a file
        try:
            f = open('mysql_dqs.txt', 'a')
            f.write(linkmd5 + str(item['test_title']) + '\r' + str(item['test_links'])\
                    + '\r' + str(item['test_time']) + str(item['test_type']) + '\n')
        except IOError, e:
            print e
            exit(1)

        # insert item into mysql db
        try:
            sql = 'insert INTO test_links VALUES (%s, %s, %s, %s, %s)'
            ret.execute(sql, (linkmd5, item['test_title'][0:],\
                item['test_links'][0:], item['test_time'][0:], item['test_type'][0:]))
        except:
            pass
