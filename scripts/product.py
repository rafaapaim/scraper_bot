from selenium import webdriver
from pathlib import Path


class ProductScraper():
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()

        drive_path = Path("C:\\")
        user_data_dir = f'user-data-dir={drive_path.home()}\\AppData\\Local\\Google\\Chrome\\User Data'

        options.add_argument(user_data_dir)
        self.driver = webdriver.Chrome(options=options)
    