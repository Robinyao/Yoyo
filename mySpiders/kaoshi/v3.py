#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from kaoshi.items import KaoshiItem

class LinksSpider(CrawlSpider):
    """ scrapy links of tests """
    name = "kaoshi"
    allowed_domains = ["kaoshi100.com"]

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
        Rule(LinkExtractor(allow=('kaoshi100.com'),\
             restrict_xpaths=('//div[@class="pager"]/div/a[last()]')),
             follow=True,
             callback='parse_item')
    ]

    # solve the "dont't crawl first page" problem
    def parse_start_url(self, response):
        return self.parse_item(response)

    def parse_item(self, response):
        sel = Selector(response)
        sites = sel.xpath('//tr[1]')
        items = []

        # question belongs
        ty = sel.xpath('//div[@class="left"]/h1/a/text()').extract()[0]

        # test info scrapy in item
        for site in sites:
            item = KaoshiItem()
            test_links = site.xpath('td[1]/a/@href').extract()
            test_title = site.xpath('td[1]/a/text()').extract()
            test_time = site.xpath('td[3]/text()').extract()

            item['test_links'] = [l.encode('utf-8') for l in test_links]
            item['test_title'] = [t.encode('utf-8') for t in test_title]
            item['test_time'] = [i.encode('utf-8').strip() for i in test_time]
            item['test_type'] = ty.encode('utf-8').strip()
            items.append(item)
        return items
