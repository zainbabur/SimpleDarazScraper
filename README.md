# SimpleDarazScraper
This python-based web scraper takes categories as input and scrapes Daraz.pk, an ecommerce website for those items.
You may define as many categories as you want in the Queries.txt file, with one category in each line and as many words in one category a you want. Examples are men shoes, women dresses, cheap analog watch, etc.
Inside the code, you can define how many pages it should scrape for each category.
The output is a .csv file for each category with names, urls and prices of each item.
Libararies used: pandas, selenium, BeautifulSoup, time.
