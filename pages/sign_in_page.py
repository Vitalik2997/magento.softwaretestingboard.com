from pages.base_page import BasePage
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


class SignIn(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_sign_page(self):
        self.driver.get(self.sign_in_page_url)

    def enter_login_details_click_sign_in(self, email, passwd):
        self.find(email_address).send_keys(email)
        self.find(password).send_keys(passwd)
        self.find(sign_in_button).click()

    def enter_email_field(self, email):
        self.find(email_address).send_keys(email)

    def enter_passwd_field(self, passwd):
        self.find(password).send_keys(passwd)

    def click_sign_in_button(self):
        self.find(sign_in_button).click()

    def check_that_login_is_not_correct(self):
        log_not_correct = self.find(login_is_not_correct)
        return 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.' in log_not_correct.text

    def check_passwd_alert(self):
        alert_passwd = self.find(passwd_alert)
        return 'This is a required field.' in alert_passwd.text

    def check_that_logged_in_acc(self):
        logged_in = self.find(check_that_logged_in_acc)
        return 'Welcome, Vitali Zalutski!' in logged_in.text

    def check_that_contact_information(self):
        contact_info = self.find(check_that_contact_info)
        return 'Vitali Zalutski', 'test12345@mail.ru' in contact_info.text

    def click_button_action_switch_my_acc(self):
        self.find(button_action_switch).click()
        self.find(button_my_acc).click()
