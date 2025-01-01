import scrapy
from scrapy import Request
import time
import random

import sys


sys.path.insert(0, '/home/adnanrp/Projects/web-scraper-analytics/')
from src.utils.database import insert_product

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'

    # def __init__(self, start_urls=None, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.start_urls = start_urls.split(',') if start_urls else []

    custom_settings={
            'FEEDS': {
                'data/raw/products.json': {
                    'format': 'json',
                    'overwrite': True
                }
            },
            'DOWNLOAD_DELAY': 1,
            'RANDOMIZED_DOWNLOAD_DELAY': True,
            'COOKIES_ENABLED': True,
            'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
            'LOG_LEVEL': 'DEBUG',
            'ROBOTSTXT_OBEY': False,
            'DOWNLOADER_MIDDLEWARES': {
                'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
                'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
                'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': None,
            },
            'RETRY_TIMES': 3,
            'RETRY_HTTP_CODES': [500, 502, 503, 504, 400, 403, 404, 408],
            'TELNETCONSOLE_ENABLED': False,  # Disable telnet console to avoid the error
            'DOWNLOAD_HANDLERS': {
            'https': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
        }
        }
    
    def start_requests(self):
        self.logger.info("Starting requests")
        url = ''

        headers = {
            'User-Agent': 'Mozilla./5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }

        self.logger.info(f"Requesting URL: {url}")
        yield Request(
            url=url,
            callback=self.parse,
            headers=headers,
            dont_filter=True
        )
        

    def parse(self, response):
        self.logger.info(f"Protocol used: {response.protocol}")
        self.logger.info(f"Received response: {response.status}")
        self.logger.info(f"URL: {response.url}")
        self.logger.info(f"Headers: {response.headers}")
        # Selectors
        products = response.css('div.sc-d1c9c193-7.uXkhJ.grid')

        for product in products:
            data = {
                'title': product.css('div[data-qa="product-name"]').get(),
                # 'price': float(product.css('span.a-price-whole::text').get().strip('$')),
                # 'description': product.css('h2.a-size-base-plus.a-spacing-none.a-color-base.a-text-normal::text').get(),
                # 'category': 'Computers',
                # 'url': product.css('a.a-link-normal.s-no-outline::attr(href)').get()
            }

            print(data)
    #         # follow the product detail URL to get full description
    #         yield response.follow(data['url'],
    #                               callback=self.parse,
    #                               meta={'book_data': data})

    #     # Pagination
    #     next_page = response.css('a.next-page::attr(href)').get()
    #     if next_page:
    #         yield response.follow(next_page, self.parse_product_detail)

    # def parse_product_detail(self, response):
    #     product_data = response.meta['product_data']

    #     # Extract description from detail page
    #     description = response.css('div.feature-bullets::text').get()

    #     if description:
    #         product_data['description'] = description.strip()

    #     yield product_data

# For Test purposes and sample HTML

# import scrapy
# import sys
# sys.path.insert(0, '/home/adnanrp/Projects/web-scraper-analytics/')
# from src.utils.database import insert_product

# class EcommerceSpider(scrapy.Spider):
#     name = 'ecommerce'
    
#     def __init__(self, start_urls=None, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.start_urls = start_urls.split(',') if start_urls else []

#     def parse(self, response):
#         # Find all product items
#         products = response.css('div.product-item')
        
#         for product in products:
#             # Extract product data
#             data = {
#                 'title': product.css('h2.title::text').get(),
#                 'price': float(product.css('span.price::text').get().strip('$')),
#                 'description': product.css('div.description::text').get(),
#                 'category': product.css('span.category::text').get(),
#                 'url': product.css('a::attr(href)').get()
#             }
            
#             yield data

#         # Follow pagination if needed
#         next_page = response.css('a.next-page::attr(href)').get()
#         if next_page:
#             yield response.follow(next_page, self.parse)