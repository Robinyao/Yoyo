# -*- coding: utf-8 -*-

# Scrapy settings for links project

BOT_NAME = 'links'

SPIDER_MODULES = ['links.spiders']
NEWSPIDER_MODULE = 'links.spiders'
COOKIES_ENABLED = False

ITEM_PIPELINES = {'links.pipelines.LinksPipeline': 300}