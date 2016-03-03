#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from bysj.items import BysjItem

class LinksSpider(CrawlSpider):
    """ scrapy links of tests """
    name = "bysj"
    allowed_domains = ["wangxiao.cn"]
    start_urls = [
        "http://www.wangxiao.cn/zcj/89228922437.html",
    ]

    # automatical scrapy next page
    # rules = [
    #     Rule(LinkExtractor(allow=('wangxiao.cn/zcj/moni'),
    #          restrict_xpaths=('//a[@class="pNext"]')),
    #          callback='parse_item',
    #          follow=True)
    # ]
    


    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="newsCon"]/p[not(child::*)]')

        # test info scrapy
        for site in sites:
            item = BysjItem()

            test_question = site.xpath('text()').extract()
            item['test_question'] = [q.encode('utf-8') for q in test_question]

            yield item
