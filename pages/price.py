from pages.page import BasePage
from pages.region_value import RegionValueClass


class PricePageLocators:
    Price_Page_Header = "//div[contains(@class,'cf_header--embedded')]"
    Price_Page_Banner = "//div[@class='banner-top']"
    Price_Page_Banner_Capital = "//img[contains(@src, 'subscriptions-banner')]"
    Price_Page_Banner_Region = "//img[contains(@src, 'free-in-regions-banner')]"
    Price_Page_MainBlock = "//div[@class='price-page']"
    Price_Page_ChooseRegionBlock = "//select[@id ='body_ddlRegions']"
    Price_Page_ChooseRegionItem = "//option[@value ='{}']"
    Price_Page_ChooseRegionItemSelected = "//option[@value ='{}'][@selected='selected']/ancestor::*[@class='dmSelect']"
    Price_Page_SubscriptionBlock = "//a[@href='https://promo.cian.ru/ciansubscriptions']/ancestor::*[@class='c_mt15']"
    Price_Page_PricesBlock = "//table[@class = 'publishPrices']"
    Price_Page_TarifBlock = "//table[@id = 'tarif']"
    Price_Page_Footer = "//div[@class = 'cf-footer']"

    @staticmethod
    def update_locator(locator, text):
        return locator.format(text)


class PricePageActions(BasePage):

    def choose_region(self, poligon_id):
        locator_Moscow = PricePageLocators.update_locator(PricePageLocators.Price_Page_ChooseRegionItemSelected,
                                                          RegionValueClass.moscow)
        locator_poligon = PricePageLocators.update_locator(PricePageLocators.Price_Page_ChooseRegionItem, poligon_id)
        locator_poligon_selected = PricePageLocators.update_locator(
            PricePageLocators.Price_Page_ChooseRegionItemSelected, poligon_id)
        self.find_element(PricePageLocators.Price_Page_MainBlock)
        self.find_element(PricePageLocators.Price_Page_ChooseRegionBlock)
        self.click_to_element(locator_Moscow)
        self.click_to_element(locator_poligon)
        self.find_element(locator_poligon_selected)
        assert (self.driver.current_url, self.base_url + "price/?polygonId=" + poligon_id)

    def check_capital_price(self, poligon_id):
        locator_poligon = PricePageLocators.update_locator(PricePageLocators.Price_Page_ChooseRegionItemSelected,
                                                           poligon_id)
        self.find_element(PricePageLocators.Price_Page_MainBlock)
        self.find_element(PricePageLocators.Price_Page_ChooseRegionBlock)
        self.find_element(locator_poligon)
        self.find_element(PricePageLocators.Price_Page_SubscriptionBlock)
        self.find_element(PricePageLocators.Price_Page_Footer)

    def check_region_price(self, poligon_id):
        locator_poligon = PricePageLocators.update_locator(PricePageLocators.Price_Page_ChooseRegionItemSelected,
                                                           poligon_id)
        self.find_element(PricePageLocators.Price_Page_Banner)
        self.find_element(PricePageLocators.Price_Page_Banner_Region)
        self.find_element(PricePageLocators.Price_Page_MainBlock)
        self.find_element(PricePageLocators.Price_Page_ChooseRegionBlock)
        self.find_element(locator_poligon)
        self.find_elements(PricePageLocators.Price_Page_PricesBlock)
        self.find_element(PricePageLocators.Price_Page_TarifBlock)
        self.find_element(PricePageLocators.Price_Page_Footer)
