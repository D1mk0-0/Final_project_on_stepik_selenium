from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CLASS_NAME, 'btn-group')

class BasketPageLocators():
    BASKET_PRODUCT = (By.CLASS_NAME, 'basket-items')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    # Красный локатор
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]//h1')
    PRODUCT_PRICE = (By.CLASS_NAME, 'price_color')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    BASKET_SUM = (By.XPATH, '//*[@id="messages"]/div[3]//strong')
    SEND_ADD_PRODUCT_NAME = (By.XPATH, '//*[@id="messages"]/div[1]//strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]//*[@class="alertinner "]')