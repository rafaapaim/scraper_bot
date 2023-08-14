from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
import pandas as pd

from globals import *


def find_link_by_href(driver, link):
    elements = driver.find_elements(By.TAG_NAME, 'a')
    for element in elements:
        try:    
            if link[:5] in element.get_attribute('href'):
                return element
        except:
            continue

def make_search(driver, products):
    for product in PRODUCT_LIST:
        search_field = driver.find_element(By.XPATH, XPATHS['SEARCH'])
        search_field.clear()
        search_field.send_keys(product)
        search_field.send_keys(Keys.ENTER)
        sleep(TIME_SLEEP)

        shopping_button = driver.find_element(By.XPATH, XPATHS['SHOPPING'])
        shopping_button.click()
        sleep(TIME_SLEEP)
        
        sale_text = driver.find_element(By.XPATH, XPATHS['SALE']).text
        if 'promo' not in sale_text.lower():
            driver.find_element(By.XPATH, XPATHS['OTHER_SALE_FIELD']).click()
        else:
            driver.find_element(By.XPATH, XPATHS['SALE']).click()

        for item in range(0, 3):
            description = driver.find_element(By.XPATH, DESCRIPTION_XPATHS[item]).text
            price = driver.find_element(By.XPATH, PRICE_XPATHS[item]).text
            ecommerce = driver.find_element(By.XPATH, ECOMMERCE_XPATHS[item]).text
            link = find_link_by_href(driver, ecommerce.lower())
            link_href = link.get_attribute('href')[31:]

            products.append([description, price, ecommerce, link_href])

        driver.get(URL)
        
    return products

def create_file(products):
    headers = ['Product', 'Price', 'E-Commerce', 'Link']
    with open('data.csv', 'w', newline='', encoding='utf-8') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(headers)
        csvwriter.writerows(products)
    
    file = pd.read_csv('data.csv')
    file.to_csv('data.csv', header=headers, index=False)