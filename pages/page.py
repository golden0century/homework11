from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import BASE_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, locator)),
                                                      message=f"Элемент {locator} не найден на странице")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located((By.XPATH, locator)),
                                                      message=f"Элементы {locator} не найден на странице")

    def click_to_element(self, locator):
        return self.find_element(locator, time=10).click()

    def open_page(self, append_name=None):
        return self.driver.get(self.base_url + append_name)
