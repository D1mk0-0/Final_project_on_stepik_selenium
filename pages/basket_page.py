from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), \
            'Корзина не пуста, хотя должна быть пуста'
        print('Корзина пуста - так и должно быть')








