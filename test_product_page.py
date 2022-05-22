from .pages.product_page import PageObject


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = PageObject(browser, link)
    page.open()
    page.add_button()
    page.solve_quiz_and_get_code()
    page.should_be_product_name_eq_message()
    page.should_be_price_eq_cost_basket()
