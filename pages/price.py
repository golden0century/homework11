from pages.page import BasePage


class PricePageLocators:
    Price_Page_Header = "//div[contains(@class,'cf_header--embedded')]"
    Price_Page_Banner = "//div[@class='banner-top']"
    Price_Page_Banner_Capital = "//img[contains(@src, 'subscriptions-banner')]"
    Price_Page_Banner_Region = "//img[contains(@src, 'free-in-regions-banner')]"
    Price_Page_MainBlock = "//div[@class='price-page']"
    Price_Page_ChooseRegionBlock = "//select[@id ='body_ddlRegions']"
    Price_Page_ChooseRegionItem = "//option[@value ='{}']"
    Price_Page_ChooseRegionItemSelected = "//option[@value ='{}'][@selected='selected']/ancestor::*[@class='dmSelect']"
    Price_Page_Footer = "//div[@class = 'cf-footer']"

    @staticmethod
    def update_locator(locator, text):
        return locator.format(text)


class PricePageActions(BasePage):

    def choose_region(self):
        new_locator = PricePageLocators.update_locator(PricePageLocators.Price_Page_ChooseRegionItemSelected, "2000")
        new_locator1 = PricePageLocators.update_locator(PricePageLocators.Price_Page_ChooseRegionItem, "1998")
        new_locator2 = PricePageLocators.update_locator(PricePageLocators.Price_Page_ChooseRegionItemSelected, "1998")
        self.find_element(PricePageLocators.Price_Page_Banner)
        self.find_element(PricePageLocators.Price_Page_MainBlock)
        self.find_element(PricePageLocators.Price_Page_Banner_Capital)
        self.find_element(PricePageLocators.Price_Page_ChooseRegionBlock)
        self.click_to_element(new_locator)
        self.click_to_element(new_locator1)
        self.find_element(new_locator2)
        self.find_element(PricePageLocators.Price_Page_Banner_Region)
