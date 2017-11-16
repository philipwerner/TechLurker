
settings = {'AJAXCRAWL_ENABLED': False,
 'AUTOTHROTTLE_DEBUG': False,
 'AUTOTHROTTLE_ENABLED': False,
 'AUTOTHROTTLE_MAX_DELAY': 60.0,
 'AUTOTHROTTLE_START_DELAY': 5.0,
 'AUTOTHROTTLE_TARGET_CONCURRENCY': 1.0,
 'BOT_NAME': 'my_scraper',
 'CLOSESPIDER_ERRORCOUNT': 0,
 'CLOSESPIDER_ITEMCOUNT': 0,
 'CLOSESPIDER_PAGECOUNT': 20,
 'CLOSESPIDER_TIMEOUT': 0,
 'COMMANDS_MODULE': '',
 'COMPRESSION_ENABLED': True,
 'CONCURRENT_ITEMS': 100,
 'CONCURRENT_REQUESTS': 16,
 'CONCURRENT_REQUESTS_PER_DOMAIN': 8,
 'CONCURRENT_REQUESTS_PER_IP': 0,
 'COOKIES_DEBUG': False,
 'COOKIES_ENABLED': False,
 'DEFAULT_ITEM_CLASS': 'scrapy.item.Item',
 'DEFAULT_REQUEST_HEADERS': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                             'Accept-Language': 'en'},
 'DEPTH_LIMIT': 0,
 'DEPTH_PRIORITY': 0,
 'DEPTH_STATS': True,
 'DNSCACHE_ENABLED': True,
 'DNSCACHE_SIZE': 10000,
 'DNS_TIMEOUT': 60,
 'DOWNLOADER': 'scrapy.core.downloader.Downloader',
 'DOWNLOADER_CLIENTCONTEXTFACTORY': 'scrapy.core.downloader.contextfactory.ScrapyClientContextFactory',
 'DOWNLOADER_CLIENT_TLS_METHOD': 'TLS',
 'DOWNLOADER_HTTPCLIENTFACTORY': 'scrapy.core.downloader.webclient.ScrapyHTTPClientFactory',
 'DOWNLOADER_MIDDLEWARES': {},
 'DOWNLOADER_MIDDLEWARES_BASE': {'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
                                 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
                                 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 400,
                                 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
                                 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
                                 'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
                                 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
                                 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
                                 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
                                 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
                                 'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
                                 'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
                                 'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
                                 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 500},
 'DOWNLOADER_STATS': True,
 'DOWNLOAD_DELAY': 0,
 'DOWNLOAD_FAIL_ON_DATALOSS': True,
 'DOWNLOAD_HANDLERS': {},
 'DOWNLOAD_HANDLERS_BASE': {'data': 'scrapy.core.downloader.handlers.datauri.DataURIDownloadHandler',
                            'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
                            'ftp': 'scrapy.core.downloader.handlers.ftp.FTPDownloadHandler',
                            'http': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
                            'https': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
                            's3': 'scrapy.core.downloader.handlers.s3.S3DownloadHandler'},
 'DOWNLOAD_MAXSIZE': 1073741824,
 'DOWNLOAD_TIMEOUT': 180,
 'DOWNLOAD_WARNSIZE': 33554432,
 'DUPEFILTER_CLASS': 'scrapy.dupefilters.RFPDupeFilter',
 'EDITOR': 'vi',
 'EXTENSIONS': {'scrapy.telnet.TelnetConsole': None},
 'EXTENSIONS_BASE': {'scrapy.extensions.closespider.CloseSpider': 0,
                     'scrapy.extensions.corestats.CoreStats': 0,
                     'scrapy.extensions.feedexport.FeedExporter': 0,
                     'scrapy.extensions.logstats.LogStats': 0,
                     'scrapy.extensions.memdebug.MemoryDebugger': 0,
                     'scrapy.extensions.memusage.MemoryUsage': 0,
                     'scrapy.extensions.spiderstate.SpiderState': 0,
                     'scrapy.extensions.telnet.TelnetConsole': 0,
                     'scrapy.extensions.throttle.AutoThrottle': 0},
 'FEED_EXPORTERS': {},
 'FEED_EXPORTERS_BASE': {'csv': 'scrapy.exporters.CsvItemExporter',
                         'jl': 'scrapy.exporters.JsonLinesItemExporter',
                         'json': 'scrapy.exporters.JsonItemExporter',
                         'jsonlines': 'scrapy.exporters.JsonLinesItemExporter',
                         'marshal': 'scrapy.exporters.MarshalItemExporter',
                         'pickle': 'scrapy.exporters.PickleItemExporter',
                         'xml': 'scrapy.exporters.XmlItemExporter'},
 'FEED_EXPORT_ENCODING': None,
 'FEED_EXPORT_FIELDS': None,
 'FEED_EXPORT_INDENT': 0,
 'FEED_FORMAT': 'jsonlines',
 'FEED_STORAGES': {},
 'FEED_STORAGES_BASE': {'': 'scrapy.extensions.feedexport.FileFeedStorage',
                        'file': 'scrapy.extensions.feedexport.FileFeedStorage',
                        'ftp': 'scrapy.extensions.feedexport.FTPFeedStorage',
                        's3': 'scrapy.extensions.feedexport.S3FeedStorage',
                        'stdout': 'scrapy.extensions.feedexport.StdoutFeedStorage'},
 'FEED_STORE_EMPTY': False,
 'FEED_TEMPDIR': None,
 'FEED_URI': None,
 'FEED_URI_PARAMS': None,
 'FILES_STORE_S3_ACL': 'private',
 'FTP_PASSIVE_MODE': True,
 'FTP_PASSWORD': 'guest',
 'FTP_USER': 'anonymous',
 'HTTPCACHE_ALWAYS_STORE': False,
 'HTTPCACHE_DBM_MODULE': 'dbm',
 'HTTPCACHE_DIR': 'httpcache',
 'HTTPCACHE_ENABLED': False,
 'HTTPCACHE_EXPIRATION_SECS': 0,
 'HTTPCACHE_GZIP': False,
 'HTTPCACHE_IGNORE_HTTP_CODES': [],
 'HTTPCACHE_IGNORE_MISSING': False,
 'HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS': [],
 'HTTPCACHE_IGNORE_SCHEMES': ['file'],
 'HTTPCACHE_POLICY': 'scrapy.extensions.httpcache.DummyPolicy',
 'HTTPCACHE_STORAGE': 'scrapy.extensions.httpcache.FilesystemCacheStorage',
 'HTTPPROXY_AUTH_ENCODING': 'latin-1',
 'HTTPPROXY_ENABLED': True,
 'IMAGES_STORE_S3_ACL': 'private',
 'ITEM_PIPELINES': {'my_scraper.pipelines.AddTablePipeline': 800},
 'ITEM_PIPELINES_BASE': {},
 'ITEM_PROCESSOR': 'scrapy.pipelines.ItemPipelineManager',
 'LOGSTATS_INTERVAL': 60.0,
 'LOG_DATEFORMAT': '%Y-%m-%d %H:%M:%S',
 'LOG_ENABLED': True,
 'LOG_ENCODING': 'utf-8',
 'LOG_FILE': None,
 'LOG_FORMAT': '%(asctime)s [%(name)s] %(levelname)s: %(message)s',
 'LOG_FORMATTER': 'scrapy.logformatter.LogFormatter',
 'LOG_LEVEL': 'DEBUG',
 'LOG_SHORT_NAMES': False,
 'LOG_STDOUT': False,
 'MAIL_FROM': 'scrapy@localhost',
 'MAIL_HOST': 'localhost',
 'MAIL_PASS': None,
 'MAIL_PORT': 25,
 'MAIL_USER': None,
 'MEMDEBUG_ENABLED': False,
 'MEMDEBUG_NOTIFY': [],
 'MEMUSAGE_CHECK_INTERVAL_SECONDS': 60.0,
 'MEMUSAGE_ENABLED': True,
 'MEMUSAGE_LIMIT_MB': 0,
 'MEMUSAGE_NOTIFY_MAIL': [],
 'MEMUSAGE_WARNING_MB': 0,
 'METAREFRESH_ENABLED': True,
 'METAREFRESH_MAXDELAY': 100,
 'NEWSPIDER_MODULE': 'my_scraper.spiders',
 'RANDOMIZE_DOWNLOAD_DELAY': True,
 'REACTOR_THREADPOOL_MAXSIZE': 10,
 'REDIRECT_ENABLED': True,
 'REDIRECT_MAX_TIMES': 20,
 'REDIRECT_PRIORITY_ADJUST': 2,
 'REFERER_ENABLED': True,
 'REFERRER_POLICY': 'scrapy.spidermiddlewares.referer.DefaultReferrerPolicy',
 'RETRY_ENABLED': True,
 'RETRY_HTTP_CODES': [500, 502, 503, 504, 408],
 'RETRY_PRIORITY_ADJUST': -1,
 'RETRY_TIMES': 2,
 'ROBOTSTXT_OBEY': True,
 'SCHEDULER': 'scrapy.core.scheduler.Scheduler',
 'SCHEDULER_DEBUG': False,
 'SCHEDULER_DISK_QUEUE': 'scrapy.squeues.PickleLifoDiskQueue',
 'SCHEDULER_MEMORY_QUEUE': 'scrapy.squeues.LifoMemoryQueue',
 'SCHEDULER_PRIORITY_QUEUE': 'queuelib.PriorityQueue',
 'SETTINGS_MODULE': 'my_scraper.settings',
 'SPIDER_CONTRACTS': {},
 'SPIDER_CONTRACTS_BASE': {'scrapy.contracts.default.ReturnsContract': 2,
                           'scrapy.contracts.default.ScrapesContract': 3,
                           'scrapy.contracts.default.UrlContract': 1},
 'SPIDER_LOADER_CLASS': 'scrapy.spiderloader.SpiderLoader',
 'SPIDER_LOADER_WARN_ONLY': False,
 'SPIDER_MIDDLEWARES': {},
 'SPIDER_MIDDLEWARES_BASE': {'scrapy.spidermiddlewares.depth.DepthMiddleware': 900,
                             'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,
                             'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 500,
                             'scrapy.spidermiddlewares.referer.RefererMiddleware': 700,
                             'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': 800},
 'SPIDER_MODULES': ['my_scraper.spiders'],
 'STATSMAILER_RCPTS': [],
 'STATS_CLASS': 'scrapy.statscollectors.MemoryStatsCollector',
 'STATS_DUMP': True,
 'TELNETCONSOLE_ENABLED': 1,
 'TELNETCONSOLE_HOST': '127.0.0.1',
 'TELNETCONSOLE_PORT': [6023, 6073],
 'TEMPLATES_DIR': '/home/hb7/codefellows/401/TechLurker/ENV/lib/python3.5/site-packages/scrapy/templates',
 'URLLENGTH_LIMIT': 2083,
 'USER_AGENT': 'Scrapy/1.4.0 (+http://scrapy.org)'}
