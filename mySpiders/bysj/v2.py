#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from bysj.items import BysjItem

class LinksSpider(CrawlSpider):
    """ scrapy questions and answers of tests """
    name = "bysj"
    allowed_domains = ["wangxiao.cn"]

    # use the links in file
    fo = open('only_links.txt', 'r')
    start_urls = []
    for l in fo.readlines():
        link = l.strip()
        start_urls.append(link)
    fo.close()

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="newsCon"]/p[not(child::*)]')

        # test info scrapy
        for site in sites:
            item = BysjItem()

            test_question = site.xpath('text()').extract()
            item['test_question'] = [q.encode('utf-8') for q in test_question]

            yield item
