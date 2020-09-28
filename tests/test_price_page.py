from pages.price import PricePageActions


class TestCianPrice:
    def test_price_region_page(self, browser):
        price_main_page = PricePageActions(browser)
        price_main_page.open_page("price")
        price_main_page.choose_region
