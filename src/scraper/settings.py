BOT_NAME= 'webscraper'

SPIDER_MODULES = ['src.scraper.spiders']
NEWSPIDER_MODULE = 'src.scraper.spiders'

# Crawl responsible
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website
DOWNLOAD_DELAY = 3