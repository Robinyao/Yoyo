#!/usr/bin/env python
# coding=utf-8
from scrapy.spider import Spider
from scrapy.selector import Selector
from items import DoubanItem 

class DoubanSpider(Spider):
    name = "douban"
    allowed_domains = ['douban.com']
    start_urls = []
    f = open('links.txt', 'wb')
    
    for i in range(0, 1160, 40):
        start_urls.append('http://movie.douban.com/subject/7054604/photos?type=S&start=%d&sortby=vote&size=a&subtype=a' % i)

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li/div/a/img/@src').extract()
        items = []

        for site in sites:
            site = site.replace('thumb', 'raw')
            self.f.write(site)
            self.f.write('\r\n')
            item = DoubanItem()
            item['ImgAddress'] = site
            items.append(item)
        
        return items
