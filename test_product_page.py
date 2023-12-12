from .pages.main_page import MainPage
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    url_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = MainPage(browser, url_link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()
    product_page.save_name_and_price_product()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_the_code_with_wait_method()
    product_page.should_be_send_add_to_basket()
