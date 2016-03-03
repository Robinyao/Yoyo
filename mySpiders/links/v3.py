#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from links.items import LinksItem

class LinksSpider(CrawlSpider):
    """ scrapy links of tests """
    name = "tests"
    allowed_domains = ["wangxiao.cn"]
    start_urls = ["http://www.wangxiao.cn/zcj/moni/739"]

    rules = [
        Rule(LinkExtractor(allow=('wangxiao.cn/zcj/moni/739'),
             restrict_xpaths=('//a[@class="pNext"]')),
             callback='parse_item',
             follow=True)
    ]

    def parse_item(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="newsList"]/ul[2]/li')

        # test info scrapy
        for site in sites:
            item = LinksItem()
            test_title = site.xpath('a/@title').extract()

            item['test_title'] = [t.encode('utf-8') for t in test_title]
            item['test_links'] = site.xpath('a/@href').extract()
            item['test_time'] = site.xpath('span/font/text() | span/text()').extract()
            yield item
