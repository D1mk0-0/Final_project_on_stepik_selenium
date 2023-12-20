from .pages.main_page import MainPage
from .pages.product_page import ProductPage

url_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, url_link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    product_page.should_not_be_success_message()

def test_guest_see_success_message(browser):
    page = MainPage(browser, url_link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, url_link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    product_page.should_disappear_success_message()

