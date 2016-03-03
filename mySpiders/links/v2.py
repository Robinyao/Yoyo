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
    name = "links"
    allowed_domains = ["http://www.wangxiao.cn"]
    start_urls = ["http://www.wangxiao.cn/zcj/moni/739"]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="newsList"]/ul[2]/li')

        # test info scrapy
        for site in sites:
            item = LinksItem()

            item['test_links'] = site.xpath('a/@href').extract()
            item['test_title'] = site.xpath('a/@title').extract()
            item['test_time'] = site.xpath('span/font/text() | span/text()').extract()

            yield item

        # next page
        urls = sel.xpath('//a[@class="pNext"]/@href').extract()
        for url in urls:
            url = "http://www.wangxiao.cn/zcj/moni/739/" + url
            yield Request(url, callback=self.parse, dont_filter=True)
