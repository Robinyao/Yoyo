#!/usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from bysj.items import BysjItem

class TestSpider(Spider):
    """ tests spider """
    name = "Tests"

    allowed_domains = []