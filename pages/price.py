from pages.page import BasePage
from pages.region_value import RegionValueClass
from helpers import update_locator

class PricePageLocators:
    PRICE_PAGE_HEADER = "//div[contains(@class,'cf_header--embedded')]"
    PRICE_PAGE_BANNER = "//div[@class='banner-top']"
    PRICE_PAGE_BANNER_CAPITAL = "//img[contains(@src, 'subscriptions-banner')]"
    PRICE_PAGE_BANNER_REGION = "//img[contains(@src, 'free-in-regions-banner')]"
    PRICE_PAGE_MAIN_BLOCK = "//div[@class='price-page']"
    PRICE_PAGE_CHOOSE_REGION_BLOCK= "//select[@id ='body_ddlRegions']"
    PRICE_PAGE_CHOOSE_REGION_ITEM = "//option[@value ='{}']"
    PRICE_PAGE_CHOOSE_REGION_ITEM_SELECTED = "//option[@value ='{}'][@selected='selected']/ancestor::*[@class='dmSelect']"
    PRICE_PAGE_SUBSCRIPTION_BLOCK = "//a[@href='https://promo.cian.ru/ciansubscriptions']/ancestor::*[@class='c_mt15']"
    PRICE_PAGE_PRICE_BLOCK = "//table[@class = 'publishPrices']"
    PRICE_PAGE_TARIFF_BLOCK = "//table[@id = 'tarif']"
    PRICE_PAGE_FOOTER = "//div[@class = 'cf-footer']"

class PricePageActions(BasePage):

    def choose_region(self, poligon_id):
        locator_Moscow = update_locator(PricePageLocators.PRICE_PAGE_CHOOSE_REGION_ITEM_SELECTED,
                                                          RegionValueClass.moscow)
        locator_poligon = update_locator(PricePageLocators.PRICE_PAGE_CHOOSE_REGION_ITEM, poligon_id)
        locator_poligon_selected = update_locator(
            PricePageLocators.PRICE_PAGE_CHOOSE_REGION_ITEM_SELECTED, poligon_id)
        self.find_element(PricePageLocators.PRICE_PAGE_MAIN_BLOCK)
        self.find_element(PricePageLocators.PRICE_PAGE_CHOOSE_REGION_BLOCK)
        self.click_to_element(locator_Moscow)
        self.click_to_element(locator_poligon)
        self.find_element(locator_poligon_selected)
        assert (self.driver.current_url, self.base_url + "price/?polygonId=" + poligon_id)

    def check_capital_price(self, poligon_id):
        locator_poligon = update_locator(PricePageLocators.PRICE_PAGE_CHOOSE_REGION_ITEM_SELECTED,
                                                           poligon_id)
        self.find_element(PricePageLocators.PRICE_PAGE_MAIN_BLOCK)
        self.find_element(PricePageLocators.PRICE_PAGE_CHOOSE_REGION_BLOCK)
        self.find_element(locator_poligon)
        self.find_element(PricePageLocators.PRICE_PAGE_SUBSCRIPTION_BLOCK)
        self.find_element(PricePageLocators.PRICE_PAGE_FOOTER)

    def check_region_price(self, poligon_id):
        locator_poligon = update_locator(PricePageLocators.PRICE_PAGE_CHOOSE_REGION_ITEM_SELECTED,
                                                           poligon_id)
        self.find_element(PricePageLocators.PRICE_PAGE_BANNER)
        self.find_element(PricePageLocators.PRICE_PAGE_BANNER_REGION)
        self.find_element(PricePageLocators.PRICE_PAGE_MAIN_BLOCK)
        self.find_element(PricePageLocators.PRICE_PAGE_CHOOSE_REGION_BLOCK)
        self.find_element(locator_poligon)
        self.find_elements(PricePageLocators.PRICE_PAGE_PRICE_BLOCK)
        self.find_element(PricePageLocators.PRICE_PAGE_TARIFF_BLOCK)
        self.find_element(PricePageLocators.PRICE_PAGE_FOOTER)
