CHROME_DRIVER_PATH = '/Users/v.konyashina/автоматизация/chromedriver'
BASE_URL = 'https://www.cian.ru/'

def update_locator(locator, text):
    return locator.format(text)