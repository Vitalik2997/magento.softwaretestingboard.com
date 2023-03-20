from pages.base_page import BasePage
from locators import my_account_page_locators as mapl
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddressBook(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_my_acc_page(self):
        self.driver.get(self.my_acc_page_url)

    def click_button_edit_billing_address(self):
        self.find(mapl.click_button_edit_billing_address).click()

    def click_button_manage_addresses(self):
        self.find(mapl.button_manage_addresses).click()

    def click_button_edit_shipping_address(self):
        self.find(mapl.click_button_edit_shipping_address).click()

    def enter_contact_information(self, comp: object, phone: object, street: object, city: object, postal: object, country: object) -> object:
        self.find(mapl.enter_company).send_keys(comp)
        self.find(mapl.enter_phone).send_keys(phone)
        self.find(mapl.enter_street_address).send_keys(street)
        self.find(mapl.enter_city).send_keys(city)
        self.find(mapl.enter_postal_code).send_keys(postal)
        self.find(mapl.enter_country).send_keys(country)
        self.find(mapl.click_button_save_address).click()

    def check_that_address_info(self):
        address_info = self.find(mapl.check_address_info)
        return 'Vitali Zalutski', 'QAP' in address_info.text

    def check_that_saved_address(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(mapl.message_your_address_save)),
                   message='You saved the address.')
        return True

