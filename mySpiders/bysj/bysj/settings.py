# -*- coding: utf-8 -*-

# Scrapy settings for bysj project
#

BOT_NAME = 'bysj'

SPIDER_MODULES = ['bysj.spiders']
NEWSPIDER_MODULE = 'bysj.spiders'
COOKIES_ENABLED = False

ITEM_PIPELINES = {'bysj.pipelines.BysjPipeline':300}