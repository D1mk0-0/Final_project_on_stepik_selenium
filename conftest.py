import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='--browser_name позволяет выбрать браузер: "chrome" или "firefox"')
    parser.addoption('--language', action='store', default='en',
                     help='--language позволяет выбрать язык в формате: "en", "fr", "ru"...')

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None
    options_chrome = OptionsChrome()
    options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options_firefox = OptionsFirefox()
    options_firefox.set_preference('intl.accept_languages', user_language)
    if browser_name == 'chrome':
        print('\nСтарт браузера Chrome для теста..')
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == 'firefox':
        print('\nСтарт браузера Firefox для теста..')
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError('--browser_name может быть только "chrome" или "firefox"')
    yield browser
    print('\nЗавершение работы браузера.')
    browser.quit()