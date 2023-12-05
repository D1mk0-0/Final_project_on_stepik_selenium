from .pages.main_page import MainPage

def test_guest_should_see_login_link(browser):
    url_link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, url_link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    url_link = 'http://selenium1py.pythonanywhere.com/'
    # Инициализирую Page Object, передаю в конструктор экземпляр драйвера и url-адрес:
    page = MainPage(browser, url_link)
    # Открываю страницу:
    page.open()
    # Выполняю метод страницы - перехожу на страницу логина
    page.go_to_login_page()