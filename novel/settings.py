# -*- coding: utf-8 -*-

# Scrapy settings for novel project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'novel'

SPIDER_MODULES = ['novel.spiders']
NEWSPIDER_MODULE = 'novel.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'cookie':'user_trace_token=20170719161518-66ebd4bd-6c5a-11e7-ab59-5254005c3644; LGUID=20170719161518-66ebdac9-6c5a-11e7-ab59-5254005c3644; _ga=GA1.2.807863775.1500452120; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216c8901308d6a-065b90b05336fa-3c375f0d-1049088-16c8901308e53%22%2C%22%24device_id%22%3A%2216c8901308d6a-065b90b05336fa-3c375f0d-1049088-16c8901308e53%22%7D; LG_LOGIN_USER_ID=e2159407feac991bb8eb3cfe6aacf6e5292f5d10e212ff2a; LG_HAS_LOGIN=1; index_location_city=%E6%9D%AD%E5%B7%9E; JSESSIONID=ABAAABAABEEAAJA494C27582913A8254EC8326164E60078; WEBTJ-ID=20190903150417-16cf5f03d43497-0e4c653a0044c2-3c375c0f-1049088-16cf5f03d4487d; _gid=GA1.2.1438445325.1567494260; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1565666641,1565862127,1567058634,1567494260; TG-TRACK-CODE=search_code; LGSID=20190903154445-b2dc007d-ce1e-11e9-a508-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=http%3A%2F%2Flocalhost%2Fnovel%2Fa.html%3F_ijt%3Dl8tasvi14h8e6npn2mc4uckqg9; X_MIDDLE_TOKEN=88603a0f803891d320c2c1c371eaea28; X_HTTP_TOKEN=39a0bbd91813374106869476518ad2d96733cfa11d; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1567496863; LGRID=20190903154741-1be74d0e-ce1f-11e9-a508-5254005c3644; SEARCH_ID=7d145c000ebd4215b244b33bcdf183a2'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'novel.middlewares.NovelSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'novel.middlewares.NovelDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'novel.pipelines.JiPiaoPipeLines':300
}
IMAGES_STORE = 'D:\ImageSpider'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
