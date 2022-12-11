from pages.gear_page import Gear
from time import sleep
import pytest
import allure


@allure.feature('Gear_page')
@pytest.mark.gear
def test_bags_page(driver):
    bags = Gear(driver)
    bags.open_gear_page()
    bags.click_button_bags()
    bags.click_sort_items()
    bags.click_shopping_options_details()
    assert bags.check_that_items_on_page()
    bags.products_add_to_cart()
    # sleep(3)   #for demonstration
    bags.click_cart()
    # assert bags.cart_check()
    assert bags.check_cart()


@allure.feature('Gear_page')
@pytest.mark.gear
def test_cart(driver):
    bags = Gear(driver)
    bags.open_gear_page()
    sleep(3)   #for demonstration
    bags.click_cart()
    bags.remove_items()
    bags.deletion_warning()
    # bags.click_cart()
    assert bags.check_that_no_items_in_cart_waiting()
    # assert bags.check_that_no_have_items_in_cart()


@allure.feature('Gear_page')
@pytest.mark.gear
def test_add_to_compare(driver):
    watches = Gear(driver)
    watches.open_gear_page()
    watches.click_watches_button()
    watches.click_sort_items()
    watches.watches_add_to_compare()
    sleep(3)
    # assert watches.watches_check_product_in_compare()
    # sleep(3)
    watches.watches_clear_to_compare_click()
    # sleep(3)
    # assert watches.message_compare_clear()
    assert watches.watches_check_that_compare_clear()


@allure.feature('Gear_page')
@pytest.mark.gear
def test_add_product_to_wish_list(driver):
    fit = Gear(driver)
    fit.open_gear_page()
    fit.click_button_fitness_equip()
    fit.click_sort_items()
    fit.fit_click_add_to_wish_list()
    # sleep(3)
    # assert fit.check_that_wish_list()
    assert fit.check_that_wish_list_waiting()


@allure.feature('Gear_page')
@pytest.mark.gear
def test_remove_items_from_wish_list(driver):
    wish = Gear(driver)
    wish.open_wishlist_page()
    wish.scroll_page_to_bottom()
    sleep(2)
    wish.click_remove_item_wish_list()
    sleep(2)
    assert wish.check_clear_wish_list()


