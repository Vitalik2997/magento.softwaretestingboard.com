from pages.men_page import Men
import pytest
import allure


@allure.feature('Men')
@pytest.mark.men
def test_category_selection(driver):
    men = Men(driver)
    men.open_men_page()
    men.button_men()
    assert men.check_that_products_per_page()


@allure.feature('Men')
@pytest.mark.men
def test_product_selection(driver):
    men = Men(driver)
    men.open_men_page()
    men.button_men()
    men.click_button_sort_items()
    men.click_button_size_and_color_selection()
    men.click_button_add_product_to_cart()
    men.click_button_cart()
    assert men.check_that_product_in_cart()


@allure.feature('Men')
@pytest.mark.men
def test_proceed_to_checkout(driver):
    men = Men(driver)
    men.open_men_page()
    men.click_button_cart_wait()
    men.click_button_cart()
    men.click_button_proceed_to_checkout()
    assert men.check_name_in_address()


@allure.feature('Men')
@pytest.mark.men
def test_shipping_address(driver):
    men = Men(driver)
    men.open_shipping_page()
    assert men.check_that_info_product()
    men.scroll_page_to_bottom()
    men.click_button_next()
    men.button_place_order_wait()
    men.click_button_place_order()
    assert men.check_that_title_wrapper()
