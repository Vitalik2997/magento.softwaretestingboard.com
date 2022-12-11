from pages.home_page import HomePage
import pytest
import allure


@allure.feature('Home')
@pytest.mark.home
def test_clickable_create_acc(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    assert home_page.create_acc_is_displayed()


@allure.feature('Home')
@pytest.mark.home
def test_button_sign_in_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    assert home_page.sign_in_acc_is_displayed()


@allure.feature('Home')
@pytest.mark.home
def test_search_field_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    assert home_page.search_field_is_displayed()


@allure.feature('Home')
@pytest.mark.home
def test_cart_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    assert home_page.cart_is_displayed()


@allure.feature('Home')
@pytest.mark.home
def test_button_whats_new_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    assert home_page.whats_new_is_displayed()


@allure.feature('Home')
@pytest.mark.home
def test_button_women_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    assert home_page.women_is_displayed()


@allure.feature('Home')
@pytest.mark.home
def test_button_men_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    assert home_page.men_is_displayed()


@allure.feature('Home')
@pytest.mark.home
def test_button_gear_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    assert home_page.gear_is_displayed()


@allure.feature('Home')
@pytest.mark.home
def test_button_sale_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    assert home_page.sale_is_displayed()


@allure.feature('Home')
@pytest.mark.home
def test_button_luma_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    assert home_page.return_home_page_is_displayed()


@allure.feature('Home')
@pytest.mark.home
def test_button_search_terms(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.scroll_page_to_bottom()
    home_page.click_search_terms()
    assert home_page.search_terms_popular_is_displayed()



