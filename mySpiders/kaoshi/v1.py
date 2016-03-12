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

    start_urls = [
        'http://www.kaoshi100.com/kaoshi/list_500401_MN500401_1.html',
        'http://www.kaoshi100.com/kaoshi/list_500402_MN500402_1.html',
        'http://www.kaoshi100.com/kaoshi/list_500403_MN500403_1.html',
        'http://www.kaoshi100.com/kaoshi/list_500404_MN500404_1.html',
        'http://www.kaoshi100.com/kaoshi/list_500405_MN500405_1.html',
        'http://www.kaoshi100.com/kaoshi/list_500406_MN500406_1.html',
    ]

    # automatical scrapy next page
    rules = [
        Rule(LinkExtractor(allow=('kaoshi100.com'),\
             restrict_xpaths=('http://www.kaoshi100.com'+'//div[@class="pager"]/div/a[last()]/@href')),
             callback='parse_item',
             follow=True)
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//tr[1]')
        items = []

        # test info scrapy in item
        for site in sites:
            item = KaoshiItem()
            test_links = site.xpath('td[1]/a/@href').extract()
            test_title = site.xpath('td[1]/a/text()').extract()
            test_time = site.xpath('td[3]/text()').extract()

            item['test_links'] = [l.encode('utf-8') for l in test_links]
            item['test_title'] = [t.encode('utf-8') for t in test_title]
            item['test_time'] = [i.encode('utf-8').strip() for i in test_time]
            items.append(item)
        return items
