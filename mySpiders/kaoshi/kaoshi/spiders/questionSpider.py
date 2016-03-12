#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys, json, scrapy
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from kaoshi.items import KaoshiItem

class LinksSpider(CrawlSpider):
    """ scrapy links of tests """
    name = "jsspider"
    allowed_domains = ["kaoshi100.com"]

    start_urls = [
        'http://www.kaoshi100.com/kaoshi/list_100101_MN100101_1.html'
    ]

    def parse(self, response):
        for url in self.start_urls:
            script = '''
            function main(splash)
                splash:autoload("https://googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js")
                splash:runjs("$('').click()")
                return splash:html()
            end
            '''
            yield scrapy.Request(url, self.parse_link, meta={
                'splash': {
                    'args': {'lua': script},
                    'endpoint': 'execute',
                }
            })

    def parse_link(self, response):
        res = json.loads(response.body)
        print(res['log']['pages'])
