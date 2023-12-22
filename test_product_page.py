import pytest
import time

from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

URL_DATASET = [
    ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'],
    ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'],
    ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2'],
    ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3'],
    ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4'],
    ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5'],
    ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6'],
    ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7'],
    ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8'],
    ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9']
]

url_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

@pytest.mark.parametrize(
    argnames=['url_link'],
    argvalues=URL_DATASET
)
def test_guest_can_add_product_to_basket(browser, url_link):
    if url_link == 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7':
        pytest.xfail(f'Страница с неверным товаром: {url_link}')
        return
    page = MainPage(browser, url_link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()
    product_page.save_name_and_price_product()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_send_add_to_basket()

@pytest.mark.link
def test_guest_should_see_login_link_on_product_page(browser):
    url_link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, url_link)
    page.open()
    page.should_be_login_link()

@pytest.mark.link
def test_guest_can_go_to_login_page_from_product_page(browser):
    url_link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, url_link)
    page.open()
    page.go_to_login_page()

@pytest.mark.check_empty_basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, url_link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()

@pytest.mark.user_add_product
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())

        self.page = ProductPage(browser, url_link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, url_link)
        self.login_page.should_be_login_page()
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()

    def test_user_see_success_message(self, browser):
        page = ProductPage(browser, url_link)
        page.open()
        page.should_not_be_success_message()

    def test_guest_can_add_product_to_basket(self, browser):
        url_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser, url_link)
        page.open()
        page.should_be_product_page()
        page.save_name_and_price_product()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_send_add_to_basket()






