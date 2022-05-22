from .base_page import BasePage
from .locators import AddButton, ProductPageLocators


class PageObject(BasePage):
    def add_button(self):
        button = self.browser.find_element(*AddButton.BUTTON)
        button.click()

    def should_be_product_name_eq_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_MAIN)
        print(product_name.text)
        product_message = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE)
        print(product_message.text)
        assert product_message.text == product_name.text, 'The message is not equal to the product name'

    def should_be_price_eq_cost_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        print(price.text)
        cost_basket = self.browser.find_element(*ProductPageLocators.COST_BASKET)
        print(cost_basket.text)
        assert price.text == cost_basket.text, 'The price is not equal to the cost of the bascet'