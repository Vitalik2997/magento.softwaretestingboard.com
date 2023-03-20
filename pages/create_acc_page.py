from pages.base_page import BasePage
from locators import create_acc_page_locators as capl


class CreateAcc(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_create_page(self):
        self.driver.get(self.create_page_url)

    def enter_personal_info_detail(self, first, last):
        self.find(capl.first_name).send_keys(first)
        self.find(capl.last_name).send_keys(last)

    def enter_sign_in_info(self, email, passwd):
        self.find(capl.email_address).send_keys(email)
        self.find(capl.password).send_keys(passwd)
        self.find(capl.confirm_password).send_keys(passwd)

    def enter_email(self, email):
        self.find(capl.email_address).send_keys(email)

    def enter_passwd(self, passwd):
        self.find(capl.password).send_keys(passwd)
        self.find(capl.confirm_password).send_keys(passwd)

    def click_create_acc(self):
        self.find(capl.create_button).click()

    def check_that_alert_displayed_min_dif_classes(self):
        alert_min_classes = self.find(capl.passwd_alert)
        return 'Minimum of different classes of characters in password is 3. Classes of characters: Lower Case, Upper Case, Digits, Special Characters.' in alert_min_classes.text

    def check_that_alert_displayed_min_length(self):
        alert_min_length = self.find(capl.passwd_alert)
        return 'Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored.' in alert_min_length.text

    def check_that_alert_displayed_required_field(self):
        alert_req_field = self.find(capl.passwd_alert)
        return 'This is a required field.' in alert_req_field.text

    def check_that_account_exists(self):
        acc_exists = self.find(capl.account_exists)
        return 'There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account.' in acc_exists.text




