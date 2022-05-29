import math
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators, BasketPageLocators, MainPageLocators


class BasePage():
    #инициализация экземпляра BasePage
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    #открытие ссылка
    def open(self):
        self.browser.get(self.url)

    #решение задачи и получение кода
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    #проверка отсутствия элемента
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    #проверка наличия элемента
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    #проверка исчезновения сообщения
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    #переход на страницу авторизации
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    #test link
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    #переход в корзину
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        link.click()

    #проверка авторизации пользователя
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                             " probably unauthorised user"
