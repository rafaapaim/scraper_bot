import PySimpleGUI as sg
from time import sleep

from product import ProductScraper
from globals import *
from util import *


driver = ProductScraper().driver

class Screen:
    def __init__(self) -> None:
        sg.theme('LightBlue')
        layout = [
            [sg.Text('Product Scraper', size=(50,0))],
            [sg.Text('Products', size=(10,0))],
            [sg.Input(size=(30,0), key='product1', border_width=1)],
            [sg.Input(size=(30,0), key='product2', border_width=1)],
            [sg.Input(size=(30,0), key='product3', border_width=1)],
            [sg.Button('Search', border_width=1), sg.Button('Cancel', border_width=1)],
        ]

        window = sg.Window(f'Product Scraper v{TOOL_VERSION}', size=(400, 300)).layout(layout)
                
        while True:
            self.event, self.values = window.read()
            if self.event == sg.WIN_CLOSED or self.event == 'Cancel':
                break
            if self.event:
                self.exec()
                self.scrape()
                self.close()

    def exec(self):
        PRODUCT_LIST.append(self.values['product1'])
        PRODUCT_LIST.append(self.values['product2'])
        PRODUCT_LIST.append(self.values['product3'])
        
        if '' in PRODUCT_LIST   :
            sg.popup_ok('The products fields must be filled...')
            
    def make_search(self, driver, products):
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
    
    def scrape(self):
        products = []

        driver.get(URL)
        products = self.make_search(driver, products)
        create_file(products)

    def close(self):
        driver.quit()
    

if __name__ == "__main__":
    screen = Screen()
    screen.exec()
    # screen.make_search()
