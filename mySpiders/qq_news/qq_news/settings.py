# -*- coding: utf-8 -*-

# Scrapy settings for qq_news project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'qq_news'

SPIDER_MODULES = ['qq_news.spiders']
NEWSPIDER_MODULE = 'qq_news.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'qq_news (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4'
