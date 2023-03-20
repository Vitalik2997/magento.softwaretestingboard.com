from selenium.webdriver.common.by import By


first_name = (By.ID, 'firstname')
last_name = (By.ID, 'lastname')
email_address = (By.ID, 'email_address')
password = (By.ID, 'password')
confirm_password = (By.NAME, 'password_confirmation')
create_button = (By.XPATH, '//button[@type="submit" and @class="action submit primary"]')
passwd_alert = (By.ID, 'password-error')
account_exists = (By.XPATH, '//div[@class="message-error error message"]')