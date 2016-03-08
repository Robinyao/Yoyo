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
    name = "links"
    allowed_domains = ["wangxiao.cn"]

    # use file as input data
    try:
        data_file = raw_input("Select the links file : ").strip()
        fo = open(data_file, 'r')
    except IOError:
        print "File is not exist."
        exit(1)
    else:
        start_urls = []
        for l in fo.readlines():
            link = l.strip()
            start_urls.append(link)
        fo.close()

    # automatical scrapy next page
    rules = [
        Rule(LinkExtractor(allow=('wangxiao.cn'),
             restrict_xpaths=('//a[@class="pNext"]')),
             callback='parse_item',
             follow=True)
    ]

    def parse_item(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="newsList"]/ul[2]/li')
        items = []

        # test info scrapy in item
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
