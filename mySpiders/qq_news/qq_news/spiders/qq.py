#!/usr/bin/env python
# coding=utf-8
from scrapy.spider import Spider
from scrapy.selector import Selector

class qqSpider(Spider):
    name = 'qq_news'
    allowed_domains = ['qq.com']
    start_urls = ['http://tech.qq.com']
    
    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="Q-tpListInner"]/h3')

        for site in sites:
            title = site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()
            for t in title:
                print t.encode('utf-8'),link
