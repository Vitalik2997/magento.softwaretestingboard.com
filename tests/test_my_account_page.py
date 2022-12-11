from pages.my_account_page import AddressBook
from time import sleep
import pytest
import allure


@allure.feature('Acc_page')
@pytest.mark.my_acc
def test_default_billing_address(driver):
    billing = AddressBook(driver)
    billing.open_my_acc_page()
    billing.check_that_address_info()
    billing.click_button_edit_billing_address()
    billing.enter_contact_information(comp='QAP', phone='+375333332211', street='Pushkina', city='Minsk', postal='220220', country='Belarus')
    assert billing.check_that_saved_address()
