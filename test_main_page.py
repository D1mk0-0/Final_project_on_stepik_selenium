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