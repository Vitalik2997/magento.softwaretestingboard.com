from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

button_men = (By.CSS_SELECTOR, 'a[id="ui-id-5"]')
button_tops = (By.CSS_SELECTOR, 'a[id="ui-id-17"]')
button_jackets = (By.CSS_SELECTOR, 'a[id="ui-id-19"]')
button_sort_items = (By.CSS_SELECTOR, 'a[id="mode-list"]')
button_size_selection = (By.CSS_SELECTOR, 'div[id="option-label-size-143-item-167"]')
button_color_selection = (By.CSS_SELECTOR, 'div[id="option-label-color-93-item-49"]')
button_add_product_to_cart = (By.CSS_SELECTOR, 'button[class="action tocart primary"]')
button_cart = (By.CSS_SELECTOR, 'a[class="action showcart"]')
button_proceed_to_checkout = (By.XPATH, '//button[@id="top-cart-btn-checkout"]')
button_next = (By.CSS_SELECTOR, 'button[class="button action continue primary"]')
button_view_items = (By.XPATH, '//div[@class="block items-in-cart"]')
button_view_details = (By.XPATH, '//div[@class="product options"]')
button_place_order = (By.CSS_SELECTOR, 'button[class="action primary checkout"]')
check_products_per_page = (By.CSS_SELECTOR, 'p[class="toolbar-amount"]')
check_that_items_in_cart = (By.CSS_SELECTOR, 'div[class="items-total"]')
check_name_last_name = (By.CSS_SELECTOR, 'div[class="shipping-address-item selected-item"]')
check_that_product_name_block = (By.CSS_SELECTOR, 'div[class="product-item-name-block"]')
check_product_size = (By.CSS_SELECTOR, 'dd[class="values"]')
check_product_color = (By.CSS_SELECTOR, 'dd[class="values"]')
check_product_details = (By.XPATH, '//dl[@class="item-options"]')
check_product_details_titles = (By.TAG_NAME, 'dt')
check_product_details_values = (By.TAG_NAME, 'dd')
check_that_place_order_continue = (By.CSS_SELECTOR, 'div[class="checkout-success"]')


class Men(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_men_page(self):
        self.driver.get(self.men_page_url)
        sleep(1)

    def open_shipping_page(self):
        self.driver.get(self.shipping_address_url)

    def button_men(self):
        men = self.find(button_men)
        tops = self.find(button_tops)
        jackets = self.find(button_jackets)
        ActionChains(self.driver).move_to_element(men).move_to_element(tops).move_to_element(jackets).click().perform()

    def check_that_products_per_page(self):
        check = self.find(check_products_per_page)
        return '11 Items' in check.text

    def click_button_sort_items(self):
        self.find(button_sort_items).click()

    def click_button_size_and_color_selection(self):
        self.find(button_size_selection).click()
        self.find(button_color_selection).click()

    def click_button_add_product_to_cart(self):
        self.find(button_add_product_to_cart).click()

    def click_button_cart(self):
        self.find(button_cart).click()
        sleep(1)

    def click_button_cart_wait(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(button_cart)),
                   )
        return True

    def check_that_product_in_cart(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(check_that_items_in_cart)),
                   message='Item in Cart')
        return True

    def click_button_proceed_to_checkout(self):
        self.find(button_proceed_to_checkout).click()
        sleep(2)

    def check_name_in_address(self):
        check = self.find(check_name_last_name)
        return 'Vitali Zalutski' in check.text

    def check_that_info_product(self):
        check = self.find(check_that_product_name_block)
        return 'Proteus Fitness Jackshirt' in check.text

    def click_button_view_items(self):
        self.find(button_view_items).click()

    def button_view_items_wait(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.element_located_to_be_selected(button_view_items)),
                   )
        return True

    def click_button_view_details(self):
        self.find(button_view_details).click()
        sleep(1)

    def click_button_next(self):
        self.find(button_next).click()

    def click_button_place_order(self):
        self.find(button_place_order).click()

    def button_place_order_wait(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(button_place_order)),
                   )
        return True

    def check_that_title_wrapper(self):
        check = self.find(check_that_place_order_continue)
        return "We'll email you an order confirmation with details and tracking info." in check.text




