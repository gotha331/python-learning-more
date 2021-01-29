# Scrapy settings for bossPro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bossPro'

SPIDER_MODULES = ['bossPro.spiders']
NEWSPIDER_MODULE = 'bossPro.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_LEVEL = 'ERROR'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Cookie': 'lastCity=101110100; __zp_seo_uuid__=68aac6df-7e80-43e4-a1ad-386a4d72c044; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1611903768; __fid=08714ac49c4e10d60eba54d13155e64c; __c=1611903768; __l=r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D8qAVeqKkllChb01_6e7-BpAh2qmVSfETW7T-PYqyiIMSxnE2W6x1aajArdG0ibYf%26wd%3D%26eqid%3Dc4c3a4740000a018000000066013b312&l=%2Fwww.zhipin.com%2Fc101110100%2F%3Fquery%3Dpython%26page%3D2&s=3&g=&friend_source=0&s=3&friend_source=0; __a=46063450.1611903768..1611903768.12.1.12.12; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1611907022; __zp_stoken__=4ae5bfDpJa1k%2Fa0twO0dJeDMuBXAkGmsgb2wIDiIvHkI%2FYD8wHlAwM3ZcYm43N1lAHmQHOzsTTjpOUG01OSFCS38PUUMDbB4vBDZXRHlXKF9FPztcQHxfUi8jBDAQQTQEGDUNAiBsP1tPVVFWLA%3D%3D; __zp_sseed__=UHY9FcbzxbTLvuyBfut8CBeXxO/aYYAXdGwfoF/dIMc=; __zp_sname__=844da516; __zp_sts__=1611907061766'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'bossPro.middlewares.BossproSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'bossPro.middlewares.BossproDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'bossPro.pipelines.BossproPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
