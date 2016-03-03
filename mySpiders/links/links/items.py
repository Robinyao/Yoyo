# -*- coding: utf-8 -*-

# Define here the models for your scraped items

from scrapy.item import Item, Field


class LinksItem(Item):
    # test title
    test_title = Field()
    # test link
    test_links = Field()
    # test upload time
    test_time = Field()
    # next web page
    next_link = Field()