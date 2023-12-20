from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    preview_product_name = None
    preview_product_price = None

    def should_be_product_page(self):
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_add_to_basket_button()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'Наименование продукта не найдено'

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), 'Стоимость продукта не найдена'

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Кнопка "Добавить в корзину" не найдена'


    def save_name_and_price_product(self):
        self.preview_product_name = self.get_text_of_element(*ProductPageLocators.PRODUCT_NAME)
        self.preview_product_price = self.get_text_of_element(*ProductPageLocators.PRODUCT_PRICE)

    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def should_be_send_add_to_basket(self):
        self.should_be_send_product_name()
        self.should_be_send_basket_price()

    def should_be_send_product_name(self):
        assert self.get_text_of_element(*ProductPageLocators.SEND_ADD_PRODUCT_NAME) == self.preview_product_name, \
            f'Название продукта после добавления не соответствует добавляемому: {self.preview_product_name}'

    def should_be_send_basket_price(self):
        assert self.get_text_of_element(*ProductPageLocators.BASKET_SUM) == self.preview_product_price, \
            f'Сумма товаров в корзине отличается от цены добавленного товара: {self.preview_product_price}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Сообщение об успехе присутствует, хотя его не должно быть'

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Сообщение об успехе присутствует, хотя его не должно быть'




