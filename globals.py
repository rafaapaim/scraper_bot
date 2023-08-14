# Globals config
TIME_SLEEP = 3

# URLs and list of products
URL = 'https://www.google.com/'
PRODUCT_LIST = ['cadeira gamer', 'placa de video', 'monitor 21 pol']

# XPaths to elements
XPATHS = {
    'SEARCH': '//*[@id="APjFqb"]',
    'SHOPPING': '//*[@id="bqHHPb"]/div/div/a[1]/div/span',
    'SALE': '//*[@id="rcnt"]/div[2]/div/div/div[2]/div[2]/div/div/div/span/div/a/span[3]/span',
    'OTHER_SALE_FIELD': '//*[@id="rcnt"]/div[2]/div/div/div[2]/div[2]/div/div/div/span[2]/div/a/span[3]/span'
}

DESCRIPTION_XPATHS = [
    '//*[@id="rso"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/span/a/div/h3', 
    '//*[@id="rso"]/div[1]/div[2]/div/div[2]/div[1]/div[2]/span/a/div/h3',
    '//*[@id="rso"]/div[1]/div[2]/div/div[3]/div[1]/div[2]/span/a/div/h3'
]

PRICE_XPATHS = [
    '//*[@id="rso"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span[1]',
    '//*[@id="rso"]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span',
    '//*[@id="rso"]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span'
]

ECOMMERCE_XPATHS = [
    '//*[@id="rso"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]',
    '//*[@id="rso"]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]',
    '//*[@id="rso"]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]'
]

LINK_XPATHS = [
    '//*[@id="rso"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/span/a',
    '//*[@id="rso"]/div[1]/div[2]/div/div[2]/div[1]/div[2]/span/a',
    '//*[@id="rso"]/div[1]/div[2]/div/div[3]/div[1]/div[2]/span/a'
]

MIN_PRICE = [0, 0, 0]
MAX_PRICE = [400, 800, 300]

MIN_XPATH = '//*[@id="rcnt"]/div[2]/div/div/div[3]/div[2]/div/div/div/span[6]/form/div[1]/div[1]/div/g-text-field/div/div[2]/input'
MAX_XPATH = '//*[@id="rcnt"]/div[2]/div/div/div[3]/div[2]/div/div/div/span[6]/form/div[1]/div[2]/div/g-text-field/div/div[2]/input'