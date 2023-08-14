from selenium import webdriver
from globals import *
from util import *
from pathlib import Path


class ProductScraper():
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()

        drive_path = Path("C:\\")
        user_data_dir = f'user-data-dir={drive_path.home()}\\AppData\\Local\\Google\\Chrome\\User Data'

        options.add_argument(user_data_dir)
        self.driver = webdriver.Chrome(options=options)
    
    def scrape(self):
        products = []

        self.driver.get(URL)
        products = make_search(self.driver, products)
        create_file(products)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    scraper = ProductScraper()
    scraper.scrape()
    scraper.close()
