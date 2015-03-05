# -*- coding: utf-8 -*-

# Scrapy settings for scraPost project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scraPost'

SPIDER_MODULES = ['scraPost.spiders']
NEWSPIDER_MODULE = 'scraPost.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scraPost (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
                  'scraPost.pipelines.jsonDumpPipeline' : 100,
                  }
LOG_ENABLED = True
LOG_LEVEL = 'INFO'
# USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

DOWNLOAD_DELAY = 2
RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408, 502]

DOWNLOADER_MIDDLEWARES = {
                        'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware' : 300,
                        'scraPost.randomproxy.RandomProxy' : 200,
                        'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware' : 400,
                        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
                        'scraPost.random_useragent.RandomUserAgentMiddleware':100,
                        }
PROXY_LIST = "scraPost/config/proxy_list.txt"

# add useragent randomization
USER_AGENT_LIST = "scraPost/config/user_agent_list.txt"