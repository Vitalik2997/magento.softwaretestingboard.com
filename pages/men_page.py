from pages.base_page import BasePage
from locators import men_page_locators as mpl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Men(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_men_page(self):
        self.driver.get(self.men_page_url)
        sleep(1)

    def open_shipping_page(self):
        self.driver.get(self.shipping_address_url)

    def button_men(self):
        men = self.find(mpl.button_men)
        tops = self.find(mpl.button_tops)
        jackets = self.find(mpl.button_jackets)
        ActionChains(self.driver).move_to_element(men).move_to_element(tops).move_to_element(jackets).click().perform()

    def check_that_products_per_page(self):
        check = self.find(mpl.check_products_per_page)
        return '11 Items' in check.text

    def click_button_sort_items(self):
        self.find(mpl.button_sort_items).click()

    def click_button_size_and_color_selection(self):
        self.find(mpl.button_size_selection).click()
        self.find(mpl.button_color_selection).click()

    def click_button_add_product_to_cart(self):
        self.find(mpl.button_add_product_to_cart).click()

    def click_button_cart(self):
        self.find(mpl.button_cart).click()
        sleep(1)

    def click_button_cart_wait(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(mpl.button_cart)),
                   )
        return True

    def check_that_product_in_cart(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(mpl.check_that_items_in_cart)),
                   message='Item in Cart')
        return True

    def click_button_proceed_to_checkout(self):
        self.find(mpl.button_proceed_to_checkout).click()
        sleep(2)

    def check_name_in_address(self):
        check = self.find(mpl.check_name_last_name)
        return 'Vitali Zalutski' in check.text

    def check_that_info_product(self):
        check = self.find(mpl.check_that_product_name_block)
        return 'Proteus Fitness Jackshirt' in check.text

    def click_button_view_items(self):
        self.find(mpl.button_view_items).click()

    def button_view_items_wait(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.element_located_to_be_selected(mpl.button_view_items)),
                   )
        return True

    def click_button_view_details(self):
        self.find(mpl.button_view_details).click()
        sleep(1)

    def click_button_next(self):
        self.find(mpl.button_next).click()

    def click_button_place_order(self):
        self.find(mpl.button_place_order).click()

    def button_place_order_wait(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(mpl.button_place_order)),
                   )
        return True

    def check_that_title_wrapper(self):
        check = self.find(mpl.check_that_place_order_continue)
        return "We'll email you an order confirmation with details and tracking info." in check.text




