from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    #проверка пустоты корзины
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "Should be empty basket"
