# import pytest
# from scrapy.http import TextResponse, Request
# import sys
# sys.path.insert(0, '/home/adnanrp/Projects/web-scraper-analytics/')
# from src.scraper.spiders.ecommerce_spider import EcommerceSpider

# def mock_response(file_name):
#     """Create a mock response from a HTML file"""
#     with open(f'tests/fixtures/{file_name}', 'r') as f:
#         content = f.read()
#     return TextResponse(url='http://example.com', 
#                        body=content.encode('utf-8'),
#                        encoding='utf-8')

# def test_parse_product():
#     """Test product parsing logic"""
#     # Create spider instance
#     spider = EcommerceSpider()
    
#     # Get mock response
#     response = mock_response('product_page.html')
    
#     # Parse the response
#     results = list(spider.parse(response))
    
#     # Verify results
#     assert len(results) == 2  # Should find 2 products
    
#     # Check first product
#     product = results[0]
#     assert 'title' in product
#     assert 'price' in product
#     assert 'description' in product
#     assert 'category' in product
#     assert 'url' in product
    
#     # Verify data
#     assert product['title'] == 'Test Product 1'
#     assert product['price'] == 29.99
#     assert product['description'] == 'Product description 1'
#     assert product['category'] == 'Electronics'
#     assert product['url'] == 'http://example.com/product1'

# if __name__ == "__main__":
#     pytest.main([__file__])

from scrapy.crawler import CrawlerProcess
import sys
sys.path.insert(0, '/home/adnanrp/Projects/web-scraper-analytics/')
from src.scraper.spiders.ecommerce_spider import EcommerceSpider

def run_spider():
    # Configuration
    process = CrawlerProcess(
        settings={
            'FEEDS': {
                'data/raw/products.json': {
                    'format': 'json',
                    'overwrite': True
                }
            },
            'ROBOTSTXT_OBEY': True,
            'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'DOWNLOAD_DELAY': 1,
            'RANDOMIZED_DOWNLOAD_DELAY': True,
            'CONCURRENT_REQUESTS_PER_DOMAIN': 8,
            'LOG_LEVEL': 'INFO',
            'DOWNLOADER_MIDDLEWARES': {
                'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
                'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
            },
            'RETRY_TIMES': 3,
            'RETRY_HTTP_CODES': [500, 502, 503, 504, 400, 403, 404, 408]
        }
    )

    # Run the spider
    process.crawl(EcommerceSpider)
    process.start()

if __name__ == "__main__":
    run_spider()