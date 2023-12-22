from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.fill_register_email(email)
        self.fill_register_pass(password)
        self.fill_confirm_pass(password)
        self.confirm_registered()
        self.should_be_success_icon()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def confirm_registered(self):
        conf_button = self.browser.find_element(*LoginPageLocators.REGISTERED_BUTTON)
        conf_button.click()

    def fill_register_email(self, email):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        email_input.clear()
        print(f'Логин юзера : {email}')
        email_input.send_keys(email)

    def fill_register_pass(self, password):
        pass_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        pass_input.clear()
        print(f'Пароль юзера : {password}')
        pass_input.send_keys(password)

    def fill_confirm_pass(self, password):
        conf_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        conf_input.clear()
        conf_input.send_keys(password)

    def should_be_login_url(self):
        assert self.browser.current_url.find('login') != -1, 'Страница "Войти или зарегистрироваться" не открыта'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Форма "Войти" не найдена'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Форма "Зарегистрироваться" не найдена'

    def should_be_success_icon(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_REGISTER_ICON), \
            'Регистрация не была успешной'