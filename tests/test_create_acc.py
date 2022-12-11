import pytest
import allure
from pages.create_acc_page import CreateAcc


CREDENTIALS = [
    {'email': 'test112@mail.ru', 'passwd': '123451'},
    {'email': 'тест@mail.ru', 'passwd': '123456qwer'},
    {'email': 'test111@mail.ru', 'passwd': '123456789вит'},
    {'email': 'test1234@mail.ru', 'passwd': '   '}
]


@allure.feature('Create')
@pytest.mark.create
@pytest.mark.parametrize('creds', CREDENTIALS)
def test_create_acc_failed(driver, creds):
    create_page = CreateAcc(driver)
    create_page.open_create_page()
    create_page.enter_personal_info_detail(first='Vitali', last='Zalutski')
    create_page.enter_sign_in_info(email=creds['email'], passwd=creds['passwd'])
    assert create_page.check_that_alert_displayed_min_length()\
           or create_page.check_that_alert_displayed_min_dif_classes()\
           or create_page.check_that_alert_displayed_required_field()


@allure.feature('Create')
@pytest.mark.create
def test_create_acc_passed(driver):
    create_page = CreateAcc(driver)
    create_page.open_create_page()
    create_page.enter_personal_info_detail(first='Vitali', last='Zalutski')
    create_page.enter_email(email='test12345@mail.ru')
    create_page.enter_passwd(passwd='123456789Qawsedrf')
    create_page.click_create_acc()
    assert create_page.check_that_account_exists()
