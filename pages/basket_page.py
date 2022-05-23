from base_page import BasePage
from pages.locators import BasketPageLocator


class BasketPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocator.BASKET), \
            "Should be empty basket"
