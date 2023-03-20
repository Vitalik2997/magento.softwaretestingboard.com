from selenium.webdriver.common.by import By

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
