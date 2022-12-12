import pytest
from pages.sign_in_page import SignIn
import allure

CREDENTIALS = [
    {'email': 'test1123123@mail.ru', 'passwd': '1234512qweqwe'},
    {'email': 'test123123@mail.ru', 'passwd': '   '}
]


@allure.feature('Login')
@pytest.mark.skipif  #появляется капча
@pytest.mark.parametrize('creds', CREDENTIALS)
@pytest.mark.login
def test_sign_in_failed(driver, creds):
    sign_in = SignIn(driver)
    sign_in.open_sign_page()
    sign_in.enter_login_details_click_sign_in(email=creds['email'], passwd=creds['passwd'])
    assert sign_in.check_that_login_is_not_correct() or sign_in.check_passwd_alert()


@allure.feature('Login')
@pytest.mark.login
def test_sign_in_passed(driver):
    sign_in = SignIn(driver)
    sign_in.open_sign_page()
    sign_in.enter_login_details_click_sign_in(email='test12345@mail.ru', passwd='123456789Qawsedrf')
    sign_in.click_button_action_switch_my_acc()
    assert sign_in.check_that_contact_information()


