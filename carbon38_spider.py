
import scrapy

class Carbon38Spider(scrapy.Spider):
    name = 'carbon38'
    start_urls = ['https://carbon38.com/en-in/collections/tops?filter.p.m.custom.available_or_waitlist=1']

    def parse(self, response):
        # Extracting product information
        products = response.css('div.ProductItem')

        for product in products:
            name = product.css('h2.ProductItem__Title a::text').get() 
            price = product.css('span.ProductItem__Price.Price::text').get()
            sizes = product.css('div.ProductItem__SizeVariants a.add-size-to-cart::text').get()
            image_url = product.css('.ProductItem__Image::attr(src)').get()
            designer = product.css('.ProductItem__Designer::text').get()

            yield {
                'name': name.strip() if name else None,
                'price': price.strip() if price else None,
                'size': sizes.strip() if sizes else None,
                'image_url': image_url.strip() if image_url else None,
                'brand': designer.strip() if designer else None,
            }

        # Follow pagination link to the next page if available
        next_page_url = response.css('a.Pagination__NavItem[rel="next"]::attr(href)').get()
        if next_page_url:
            yield scrapy.Request(url=response.urljoin(next_page_url), callback=self.parse)
