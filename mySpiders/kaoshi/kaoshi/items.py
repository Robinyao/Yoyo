# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class KaoshiItem(Item):
    # test title
    test_title = Field()
    # test link
    test_links = Field()
    # test upload time
    test_time = Field()
    # test type
    test_type = Field()
