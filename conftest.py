from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import settings
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture(scope='function')
def driver():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('start-maximized')
    # options.add_argument(r'user-data-dir=C:\Пользователи\Виталик\projects\magento.softwaretestingboard.com\info_session')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    try:
        login = driver.find_element(By.CSS_SELECTOR, 'li[class="authorization-link"]')
        login.click()
        email_field = driver.find_element(By.XPATH, '//input[@type="email" and @name="login[username]"]')
        email_field.send_keys(settings.email)
        password_field = driver.find_element(By.XPATH, '//input[@type="password" and @name="login[password]"]')
        password_field.send_keys(settings.password)
        password_field.send_keys(Keys.ENTER)
    except NoSuchElementException:
        return False
    return True
