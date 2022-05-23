from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form[id='login_form']")
    REGISTER_FORM = (By.CSS_SELECTOR, "form[id='register_form']")
    REGISTER_LOGIN = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, 'input[id="id_registration-password1"]')
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, 'input[id="id_registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    AUTHORIZATION_BUTTON = (By.CSS_SELECTOR, 'a[id = "login_link"]')


class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'span > a')
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > div.basket-title.hidden-xs')
