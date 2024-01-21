# Web Scraping Project for Extracting Product Information from Carbon38

The objective of this project is to create a web scraping tool using the Scrapy framework to extract product information from the Carbon38 website. Carbon38 is an online platform that offers a variety of activewear and lifestyle products. The goal is to collect detailed information about different products, including images, brand, name, price, sizes, color, description, and product ID.

## Project Components:

 ### 1.Scrapy Spider:
 The core of the project is a Scrapy spider named Carbon38Spider. This spider navigates through the product     listings pages on Carbon38, extracts relevant information, and follows links to individual product detail      pages for more detailed data.

 ### 2.Data Extraction:
The spider utilizes XPath selectors to extract data from the HTML structure of the Carbon38 website. Information such as image URLs, designer names, product names, prices, sizes, descriptions, colors, and product IDs is collected.

### 3.Pagination Handling:
The spider is designed to handle pagination by following links to the next pages and continuing the data extraction process until there are no more pages available. In our website only 3 pages are avilable.

### 4.Meta Information:
The spider makes use of Scrapy's meta feature to pass information between different callback functions. This allows for the association of data from product listings pages with details extracted from individual product detail pages.

### 5.Pipeline (Not Explicitly Shown):
Typically, in a Scrapy project, a pipeline would be implemented to process and store the extracted data. This could involve storing the data in a database, writing it to a CSV or json file, or utilizing other storage solutions.

## Extraction steps

In the provided Scrapy spider code, the extraction of data from the navigation pages involves two key components: the parse method and the parse_product_detail method. These methods work together to navigate through the list of products on each page and retrieve detailed information from individual product pages.

In parse method,the spider extracts basic product information such as image URL, designer, name, price, sizes, and the URL of the product detail page from the product listings page. For each product, it then makes a request to the corresponding product detail page using the parse_product_detail callback. Finally, the spider checks for a pagination link to the next page and continues crawling if available.

In parse_product_detail method, the spider handles the response from the requests made to individual product detail pages. It extracts additional details such as description, color, and product ID using XPath selectors. The spider then accesses the product information passed as metadata in the original request from the parse method. Finally, the spider yields a dictionary containing all the collected information for each product.

By combining the information extracted from the product listings page (parse method) and the additional details obtained from individual product detail pages (parse_product_detail method), the spider can build a comprehensive dataset with details about multiple products across different navigation pages. This process repeats until there are no more pagination links to follow. 

Our website consits of only 3 navigation page, so data to scrape is very less that is below 250 data. The extracted information,including both the information from the detail page and the metadata, is yielded as a dictionary.

## Conclusion

This web scraping project serves as a practical example of how to use Scrapy to collect structured data from a website. By adapting the spider code to other websites with similar structures, users can create customized scraping tools for various purposes. It demonstrates the power and flexibility of Scrapy in handling web scraping tasks efficiently.

