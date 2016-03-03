
import pymongo
from scrapy import log
from scrapy.conf import settings
from scrapy.exceptions import DropItem

class MongoDbPipeline(object):

    def __init__(self):
        self.server = settings['MONGODB_SERVER']
        self.port = settings['MONGODB_PORT']
        self.db = settings['MONGODB_DB']
        self.col = settings['MONGODB_COLLECTION']

        connection = pymongo.Connection(self.server, self.port)
        db = connection[self.db]
        self.collection = db[self.col]

    def process_item(self, item, spider):
        err_msg = ''
        for field, data in item.items():
            if not data:
                err_msg += 'Missing %s of poem from %s\n' % (field, item['url'])

        if err_msg:
            raise DropItem(err_msg)

        self.collection.insert(dict(item))
        log.msg('Item written to MongoDB database %s%s'
                % (self.db, self.col), level=log.DEBUG,
                spider=spider)
        return item