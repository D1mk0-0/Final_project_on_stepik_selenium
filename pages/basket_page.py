import pytest

from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_down_if_product_in_page()
        self.should_be_down_if_not_product_in_page()

    def should_be_down_if_product_in_page(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), \
            'Корзина не пуста, хотя должна быть пуста'

    def should_be_down_if_not_product_in_page(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_PRODUCT), \
            'Тест падает потому-что товара нет в корзине'