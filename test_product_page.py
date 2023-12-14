import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage

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
    # Для стабильного ожидания второго окна alert использовать метод с ожиданием:
    #product_page.solve_quiz_and_get_the_code_with_wait_method()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_send_add_to_basket()


