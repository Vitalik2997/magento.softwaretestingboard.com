from pages.base_page import BasePage
from locators import sign_in_page_locators as sipl


class SignIn(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_sign_page(self):
        self.driver.get(self.sign_in_page_url)

    def enter_login_details_click_sign_in(self, email, passwd):
        self.find(sipl.email_address).send_keys(email)
        self.find(sipl.password).send_keys(passwd)
        self.find(sipl.sign_in_button).click()

    def enter_email_field(self, email):
        self.find(sipl.email_address).send_keys(email)

    def enter_passwd_field(self, passwd):
        self.find(sipl.password).send_keys(passwd)

    def click_sign_in_button(self):
        self.find(sipl.sign_in_button).click()

    def check_that_login_is_not_correct(self):
        log_not_correct = self.find(sipl.login_is_not_correct)
        return 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.' in log_not_correct.text

    def check_passwd_alert(self):
        alert_passwd = self.find(sipl.passwd_alert)
        return 'This is a required field.' in alert_passwd.text

    def check_that_logged_in_acc(self):
        logged_in = self.find(sipl.check_that_logged_in_acc)
        return 'Welcome, Vitali Zalutski!' in logged_in.text

    def check_that_contact_information(self):
        contact_info = self.find(sipl.check_that_contact_info)
        return 'Vitali Zalutski', 'test12345@mail.ru' in contact_info.text

    def click_button_action_switch_my_acc(self):
        self.find(sipl.button_action_switch).click()
        self.find(sipl.button_my_acc).click()


