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
    name = "alls"
    allowed_domains = ["wangxiao.cn"]
    start_urls = [
        "http://www.wangxiao.cn/zcj/moni/739",
        "http://www.wangxiao.cn/zcj/moni/740",
        "http://www.wangxiao.cn/zcj/moni/741",
        "http://www.wangxiao.cn/zcj/moni/742",
        "http://www.wangxiao.cn/zcj/moni/743",
        "http://www.wangxiao.cn/zcj/moni/744",
        "http://www.wangxiao.cn/zcj/moni/745",
        "http://www.wangxiao.cn/zcj/moni/746",
        "http://www.wangxiao.cn/zcj/moni/747",
    ]

    # automatical scrapy next page
    rules = [
        Rule(LinkExtractor(allow=('wangxiao.cn/zcj/moni'),
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
            test_links = site.xpath('a/@href').extract()
            test_title = site.xpath('a/@title').extract()
            test_time = site.xpath('span/font/text() | span/text()').extract()

            item['test_links'] = [l.encode('utf-8') for l in test_links]
            item['test_title'] = [t.encode('utf-8') for t in test_title]
            item['test_time'] = [i.encode('utf-8') for i in test_time]
            yield item
