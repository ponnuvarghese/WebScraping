
import scrapy

class Carbon38Spider(scrapy.Spider):
    name = 'carbon38'
    start_urls = ['https://carbon38.com/en-in/collections/tops?filter.p.m.custom.available_or_waitlist=1']

    def parse(self, response):
        # Extracting product information
        products = response.css('div.ProductItem')

        for product in products:
            image_url = product.css('.ProductItem__Image::attr(src)').get()
            designer = product.css('.ProductItem__Designer::text').get()
            name = product.css('h2.ProductItem__Title a::text').get() 
            price = product.css('span.ProductItem__Price.Price::text').get()
            
            sizes = product.css('div.ProductItem__SizeVariants a.add-size-to-cart::text').getall()           

            # Extracting the product detail page URL
            product_detail_url = product.css('h2.ProductItem__Title a::attr(href)').get()

            # Make a request to the product detail page to fetch additional details including color
            yield scrapy.Request(url=response.urljoin(product_detail_url), callback=self.parse_product_detail, meta={
                'image_url': image_url.strip() if image_url else None,
                'brand': designer.strip() if designer else None,
                'product_name': name.strip() if name else None,
                'price': price.strip() if price else None,
                'sizes': [size.strip() for size in sizes if size],
            })

        # Follow pagination link to the next page if available
        next_page_url = response.css('a.Pagination__NavItem[rel="next"]::attr(href)').get()
        if next_page_url:
            yield scrapy.Request(url=response.urljoin(next_page_url), callback=self.parse)

    def parse_product_detail(self, response):

         # Extracting the description from the product detail page
        description = response.css('.Faq__Answer.Rte span[data-mce-fragment="1"]::text').get()

        # Check if description is available
        if description:
            description = description.strip()
        else:
            description = "No description available"

        
        # Extracting color information from the product detail page
        color = response.css('span.ProductForm__SelectedValue::text').get()

        # Extracting product ID
        product_id = response.css('input[name="product-id"]::attr(value)').get()

         

        # Get the product information from the meta data passed in the request
        product_info = {
            'image_url': response.meta['image_url'],
            'brand': response.meta['brand'],
            'product_name': response.meta['product_name'],
            'price': response.meta['price'],
            'sizes': response.meta['sizes'],
            'color': color.strip() if color else None,
            #'description': description.strip() if description else None
            'description': description,
            'product_id': product_id.strip() if product_id else None,
            
            
        }

        yield product_info


