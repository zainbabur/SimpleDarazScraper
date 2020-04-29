'''
This script takes your favourite shopping categories and returns
a csv file with all available items, their urls and prices
Made by Zain
'''
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import pandas as pd
import time

#!Path to read/write files
dest_path = 'xyz:\\SimpleDarazScraper\\'

#!basic url of daraz.pk, queries will be added to it
basic_url = 'https://www.daraz.pk/catalog/?q='

#!number of pages you want to scrape for each query
max_page = 1

#!making chrome headless to save ram/cpu
options = webdriver.ChromeOptions()
options.add_argument('--headless')


#!Opening a context for queries file
with open(dest_path+'Queries.txt', 'r') as text:
    
    #!iterating over each line
    for line in text:
        query = ''

        #!adding '+' between words of one query so it can be added to basic url
        for part in line.strip().split():
            query += part + '+'
        
        #!there will always be one extra '+' at the end so removing it
        query = query[:-1]
        
        #!defining lists for url, name and price
        products_name_list = []
        current_price_list = []
        products_url_list = []

        #!for each page
        for page in range(1,max_page+1):

            #!adding queries and page number to url
            url = basic_url+query+'&page='+ str(page)

            #!opening a context for webdriver
            with webdriver.Chrome("C:\\ChromeDriver\\chromedriver.exe", chrome_options=options) as driver:    
        
                #!open url and wait 20 seconds for it to fully load
                driver.get(url)
                time.sleep(20)

                #!get html from the page
                my_html = driver.page_source

                #!passing html to beautifulsoup 
                my_soup = soup(my_html, "html.parser")
            
            #!scraping divs with required information and making lists
            items = my_soup.find_all("div", class_="c2prKC")
            
            for item in items:
                products_url_list.append(item.find("a")['href'])

            items = my_soup.find_all("div", class_="c16H9d")

            for item in items:
                products_name_list.append(item.text)

            items = my_soup.find_all("span", class_="c13VH6")

            for item in items:
                current_price_list.append([float(price) for price in item.text.replace(',','').split() if price.isdigit()][0])
        
        #!initializing an empty dataframe
        df = pd.DataFrame()

        #!filling columns
        df['ItemName'] = products_name_list
        df['URL'] = products_url_list
        df['CurrentPrice'] = current_price_list

        #!writing to csv
        df.to_csv(dest_path+query+'.csv', index=False)

        