import scrapy

class Carbon38Spider(scrapy.Spider):
    name = 'carbon38'
    start_urls = ['https://carbon38.com/en-in/collections/tops']

    def parse(self, response):
        # Extracting product information
        products = response.xpath('//div[contains(@class, "ProductItem")]')

        for product in products:
            image_url = product.xpath('.//img[contains(@class, "ProductItem__Image")]/@src').get()
            designer = product.xpath('//h3[@class="ProductItem__Designer"]/text()').get()

            name = product.xpath('.//h2[contains(@class, "ProductItem__Title")]/a/text()').get() 
            price = product.xpath('.//span[contains(@class, "ProductItem__Price")]/text()').get()
            
            sizes = product.xpath('.//div[contains(@class, "ProductItem__SizeVariants")]/a[contains(@class, "add-size-to-cart")]/text()').getall()           

            # Extracting the product detail page URL
            product_detail_url = product.xpath('.//h2[contains(@class, "ProductItem__Title")]/a/@href').get()

            # Make a request to the product detail page to fetch additional details including color
            yield scrapy.Request(url=response.urljoin(product_detail_url), callback=self.parse_product_detail, meta={
                'image_url': image_url.strip() if image_url else None,
                'brand': designer.strip() if designer else None,
                'product_name': name.strip() if name else None,
                'price': price.strip() if price else None,
                'sizes': [size.strip() for size in sizes if size],
            })

        # Follow pagination link to the next page if available
        next_page_url = response.xpath('//a[contains(@class, "Pagination__NavItem") and @rel="next"]/@href').get()
        if next_page_url:
            yield scrapy.Request(url=response.urljoin(next_page_url), callback=self.parse)

    def parse_product_detail(self, response):
        # Extracting the description from the product detail page
        description = response.xpath('//span[@data-mce-fragment="1"]/text()').get()

        # Extracting color information from the product detail page
        color = response.xpath('//span[contains(@class, "ProductForm__SelectedValue")]/text()').get()

        # Extracting product ID
        product_id = response.xpath('//input[@name="product-id"]/@value').get()

        # Get the product information from the meta data passed in the request
        product_info = {
            'image_url': response.meta['image_url'],
            'brand': response.meta['brand'],
            'product_name': response.meta['product_name'],
            'price': response.meta['price'],
            'sizes': response.meta['sizes'],
            'color': color.strip() if color else None,
            'description': description.strip() if description else None,
            'product_id': product_id.strip() if product_id else None,
        }

        yield product_info



        


