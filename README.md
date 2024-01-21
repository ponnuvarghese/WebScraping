# Web Scraping Project for Extracting Product Information from Carbon38

The objective of this project is to create a web scraping tool using the Scrapy framework to extract product information from the Carbon38 website. Carbon38 is an online platform that offers a variety of activewear and lifestyle products. The goal is to collect detailed information about different products, including images, brand, name, price, sizes, color, description, and product ID.

## Project Components:

    ## Scrapy Spider:
    The core of the project is a Scrapy spider named Carbon38Spider. This spider navigates through the product     listings pages on Carbon38, extracts relevant information, and follows links to individual product detail      pages for more detailed data.

    ## Data Extraction:
    The spider utilizes XPath selectors to extract data from the HTML structure of the Carbon38 website.           Information such as image URLs, designer names, product names, prices, sizes, descriptions, colors, 
    and product IDs is collected.

    Pagination Handling:
    The spider is designed to handle pagination by following links to the next pages and continuing the data extraction process until there are no more pages available.

    Meta Information:
    The spider makes use of Scrapy's meta feature to pass information between different callback functions. This allows for the association of data from product listings pages with details extracted from individual product detail pages.

    Pipeline (Not Explicitly Shown):
    Typically, in a Scrapy project, a pipeline would be implemented to process and store the extracted data. This could involve storing the data in a database, writing it to a json or CSV file, or utilizing other storage solutions.

