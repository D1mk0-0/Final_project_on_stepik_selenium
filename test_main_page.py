<<<<<<< HEAD
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
=======
from selenium.webdriver.common.by import By

url_link = 'http://selenium1py.pythonanywhere.com/'

# def test_guest_can_to_login_page(browser):
#     url_link = 'http://selenium1py.pythonanywhere.com/'
#     browser.get(url_link)
#     login_link = browser.find_element(By.CSS_SELECTOR, '#login_link')
#     login_link.click()

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, '#login_link')
    login_link.click()

def test_guest_can_to_login_page(browser):
    browser.get(url_link)
    go_to_login_page(browser)
>>>>>>> b8e4e5f76f1dfc37355871b640064a2a36ccc4d8
