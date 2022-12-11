from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


button_manage_addresses = (By.LINK_TEXT, 'Manage Addresses')
click_button_edit_billing_address = (By.XPATH, '//a[@class="action edit" and @data-ui-id="default-billing-edit-link"]')
click_button_edit_shipping_address = (By.XPATH, '//a[@class="action edit" and @data-ui-id="default-shipping-edit-link"')
enter_company = (By.XPATH, '//input[@type="text" and @id="company"]')
enter_phone = (By.XPATH, '//input[@type="text" and @name="telephone"]')
enter_street_address = (By.XPATH, '//input[@name="street[]" and @id="street_1"]')
enter_city = (By.XPATH, '//input[@type="text" and @name="city"]')
enter_postal_code = (By.XPATH, '//input[@type="text" and @id="zip"]')
enter_country = (By.NAME, 'country_id')
click_button_save_address = (By.XPATH, '//button[@type="submit" and @class="action save primary"]')
check_address_info = (By.XPATH, '//div[@class="box-content"]')
message_your_address_save = (By.XPATH, '//div[@role="alert" and @class="messages"]')


class AddressBook(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_my_acc_page(self):
        self.driver.get(self.my_acc_page_url)

    def click_button_edit_billing_address(self):
        self.find(click_button_edit_billing_address).click()

    def click_button_manage_addresses(self):
        self.find(button_manage_addresses).click()

    def click_button_edit_shipping_address(self):
        self.find(click_button_edit_shipping_address).click()

    def enter_contact_information(self, comp: object, phone: object, street: object, city: object, postal: object, country: object) -> object:
        self.find(enter_company).send_keys(comp)
        self.find(enter_phone).send_keys(phone)
        self.find(enter_street_address).send_keys(street)
        self.find(enter_city).send_keys(city)
        self.find(enter_postal_code).send_keys(postal)
        self.find(enter_country).send_keys(country)
        self.find(click_button_save_address).click()

    def check_that_address_info(self):
        address_info = self.find(check_address_info)
        return 'Vitali Zalutski', 'QAP' in address_info.text

    def check_that_saved_address(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(message_your_address_save)),
                   message='You saved the address.')
        return True

