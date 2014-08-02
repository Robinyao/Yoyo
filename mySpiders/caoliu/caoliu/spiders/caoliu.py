#!/usr/bin/env python
# coding=utf-8
from scrapy.spider import Spider
from scrapy.selector import Selector

class CaoliuSpider(Spider):
    name = "caoliu"
    allowed_domains = ['10240.com.ar']
    start_urls = ['http://10240.com.ar/thread0806.php?fid=20']
    filename = 'data.txt'
    f = open(filename, 'wb')

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//tbody/tr[@class="tr3 t_one"]/td/h3/a/@href').extract()

        for site in sites:
            site = '10240.com.ar' + site
            self.f.write(site)
            self.f.write('\r\n')

