from .pages.main_page import MainPage

from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    url_link = 'http://selenium1py.pythonanywhere.com/'
    # инициализиру Page Object, передаю в конструктор экземпляр драйвера и url-адрес:
    page = MainPage(browser, url_link)
    # открываю страницу:
    page.open()
    # выполняю метод страницы - перехожу на страницу логина:
    page.go_to_login_page()
