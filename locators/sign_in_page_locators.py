from selenium.webdriver.common.by import By

email_address = (By.NAME, 'login[username]')
password = (By.XPATH, '//input[@name="login[password]"]')
sign_in_button = (By.XPATH, '//button[@id="send2" and @class="action login primary"]')
check_that_logged_in_acc = (By.CLASS_NAME, 'logged-in')
login_is_not_correct = (By.XPATH, '//div[@class="message-error error message"]')
passwd_alert = (By.XPATH, '//div[@class="mage-error"]')
check_that_contact_info = (By.XPATH, '//div[@class="box-content"]')
button_action_switch = (By.CSS_SELECTOR, 'button[class="action switch"]')
button_my_acc = (By.LINK_TEXT, 'My Account')
