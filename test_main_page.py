from selenium.webdriver.common.by import By

def test_guest_can_to_login_page(browser):
    url_link = 'http://selenium1py.pythonanywhere.com/'
    browser.get(url_link)
    login_link = browser.find_element(By.CSS_SELECTOR, '#login_link')
    login_link.click()