import scrapy
import sys

sys.path.insert(0, '/home/adnanrp/Projects/web-scraper-analytics/')
from src.utils.database import insert_product

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'

    def __init__(self, start_urls=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = start_urls.split(',') if start_urls else []

    def parse(self, response):
        # Selectors
        products = response.css('div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16')

        for product in products:
            data = {
                'title': product.css('h2.a-size-base-plus.a-spacing-none.a-color-base.a-text-normal::text').get(),
                'price': float(product.css('span.a-price-whole::text').get().strip('$')),
                # 'description': product.css('h2.a-size-base-plus.a-spacing-none.a-color-base.a-text-normal::text').get(),
                'category': product.css('span.category::text').get(),
                'url': product.css('a::attr(href)').get()
            }

            print(data)
            # # store in database
            # product_id = insert_product(data)

            # # store raw html for backup
            # yield {
            #     'product_id': product_id,
            #     'raw_html': product.get()
            # }

        # Pagination
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

        