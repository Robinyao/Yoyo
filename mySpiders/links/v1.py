#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from links.items import LinksItem

class LinksSpider(Spider):
    """ scrapy links of tests """
    name = "v1"
    allowed_domains = ["http://www.wangxiao.cn"]
    start_urls = ["http://www.wangxiao.cn/zcj/moni/739"]

    # def start_requests(self):
    #     f = open('testsLinks.txt', 'r')
    #     try:
    #         for line in f:
    #             self.start_urls.append(line)
    #
    #         for url in self.start_urls:
    #             yield self.make_requests_from_url(url)
    #     finally:
    #         f.close()
    #
    # def parse(self, response):
    #     sel = Selector(response)
    #     items = []
    #     urls = sel.xpath('//a[@class="pNext"]/@href').extract()
    #     for i in urls:
    #         url = 'http://www.wangxiao.cn/zcj/moni/739/' + i
    #         items.append(url)
    #     for item in items:
    #         yield Request(url=item, meta={'item':item}, callback=self.parse_item, dont_filter=True)

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="newsList"]/ul[2]/li')
        items = []

        for site in sites:
            item = LinksItem()

            test_links = site.xpath('a/@href').extract()
            test_title = site.xpath('a/@title').extract()
            test_time = site.xpath('span/font/text() | span/text()').extract()

            item['test_links'] = [l.encode('utf-8') for l in test_links]
            item['test_title'] = [t.encode('utf-8') for t in test_title]
            item['test_time'] = [i.encode('utf-8') for i in test_time]
            
            items.append(item)
        return items

