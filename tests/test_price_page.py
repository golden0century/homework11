import pytest

from pages.price import PricePageActions
from pages.region_value import RegionValueClass


class TestCianPrice:
    @pytest.mark.parametrize("poligon_id, status", [(RegionValueClass.moscow, 'capital'), (
            RegionValueClass.bmo, 'capital'), (RegionValueClass.dmo, 'capital'), (RegionValueClass.sp, 'capital'),
                                                    (RegionValueClass.lo, 'capital'),
                                                    (RegionValueClass.adygea, 'region'),
                                                    (RegionValueClass.altai, 'region'),
                                                    (RegionValueClass.altaiski_krai, 'region'),
                                                    (RegionValueClass.amurskaya_oblast, 'region'),
                                                    (RegionValueClass.arhangelsk_oblast, 'region'),
                                                    (RegionValueClass.astrakhan_oblast, 'region'),
                                                    (RegionValueClass.bashkortostan, 'region'),
                                                    (RegionValueClass.belgorod, 'region'),
                                                    (RegionValueClass.belgorodskaya_oblast, 'region'),
                                                    (RegionValueClass.bolshoi_sochi, 'region'),
                                                    (RegionValueClass.bryanskaya_oblast, 'region'),
                                                    (RegionValueClass.buriatiya, 'region'),
                                                    (RegionValueClass.vladimir, 'region'),
                                                    (RegionValueClass.vladimirskaya_oblast, 'region'),
                                                    (RegionValueClass.volgograd, 'region'),
                                                    (RegionValueClass.volgogradskaya_oblast, 'region'),
                                                    (RegionValueClass.voronezh, 'region'),
                                                    (RegionValueClass.voronezhskaya_oblast, 'region')])
    def test_price_region_page(self, browser, poligon_id, status):
        price_main_page = PricePageActions(browser)
        price_main_page.open_page("price/?polygonId=" + poligon_id)
        if status == 'capital':
            price_main_page.check_capital_price(poligon_id)
        elif status == 'region':
            price_main_page.check_region_price(poligon_id)

    @pytest.mark.parametrize("poligon_id",
                             [RegionValueClass.bmo, RegionValueClass.moscow, RegionValueClass.dmo, RegionValueClass.sp,
                              RegionValueClass.lo, RegionValueClass.adygea, RegionValueClass.altai,
                              RegionValueClass.altaiski_krai, RegionValueClass.amurskaya_oblast,
                              RegionValueClass.arhangelsk_oblast, RegionValueClass.astrakhan_oblast,
                              RegionValueClass.bashkortostan, RegionValueClass.belgorod,
                              RegionValueClass.belgorodskaya_oblast, RegionValueClass.bolshoi_sochi,
                              RegionValueClass.bryanskaya_oblast, RegionValueClass.buriatiya, RegionValueClass.vladimir,
                              RegionValueClass.vladimirskaya_oblast, RegionValueClass.volgograd,
                              RegionValueClass.volgogradskaya_oblast, RegionValueClass.voronezh,
                              RegionValueClass.voronezhskaya_oblast])
    def test_price_change_region(self, browser, poligon_id):
        price_main_page = PricePageActions(browser)
        price_main_page.open_page("price")
        price_main_page.choose_region(poligon_id)
