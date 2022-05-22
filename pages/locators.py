from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form[id='login_form']")
    REGISTER_FORM = (By.CSS_SELECTOR, "form[id='register_form']")


class AddButton():
    BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")


class ProductPageLocators:
    PRODUCT_MAIN = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner strong")
    COST_BASKET = (By.CSS_SELECTOR,'.alert-info .alertinner strong')
    PRICE = (By.CSS_SELECTOR,'.col-sm-6>.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-success.fade.in')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
