from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import csv
import pandas as pd


def find_link_by_href(driver, link):
    elements = driver.find_elements(By.TAG_NAME, 'a')
    for element in elements:
        try:    
            if link[:5] in element.get_attribute('href'):
                return element
        except:
            continue

def create_file(products):
    headers = ['Product', 'Price', 'E-Commerce', 'Link']
    with open('data.csv', 'w', newline='', encoding='utf-8') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(headers)
        csvwriter.writerows(products)
    
    file = pd.read_csv('data.csv')
    file.to_csv('data.csv', header=headers, index=False)
