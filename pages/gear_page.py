from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


button_bags = (By.LINK_TEXT, 'Bags')
sort_items = (By.CSS_SELECTOR, 'a[id="mode-list"]')
button_style_selection = (By.XPATH, '//div[@class="filter-options-title" and @data-role="title"]')
button_style_selection_duffel = (By.PARTIAL_LINK_TEXT, 'Duffel')
check_that_product_items = (By.CSS_SELECTOR, 'ol[class="products list items product-items"]')
add_product = (By.XPATH, '//button[@type="submit" and @title="Add to Cart"]')
click_cart = (By.CSS_SELECTOR, 'a[class="action showcart"]')
cart = (By.CSS_SELECTOR, 'div[class="minicart-items-wrapper"]')
remove_items = (By.XPATH, '//a[@class="action delete" and @title="Remove item"]')
no_items_in_cart = (By.CSS_SELECTOR, 'div[id="minicart-content-wrapper"]')
accept_alert = (By.CSS_SELECTOR, 'button[class="action-primary action-accept"]')
button_watches = (By.LINK_TEXT, 'Watches')
watches_product_selection = (By.CSS_SELECTOR, 'li[class="item product product-item"]')
watches_action_to_compare = (By.CSS_SELECTOR, 'a[class="action tocompare"]')
check_that_block_compare = (By.CSS_SELECTOR, '//div[@role="alert" and @class="messages"]')
button_clear_compare = (By.CSS_SELECTOR, 'a[id="compare-clear-all"]')
button_accept_clear_compare = (By.CSS_SELECTOR, 'button[class="action-primary action-accept"]')
check_that_compare_clear = (By.CSS_SELECTOR, 'div[class="empty"]')
message_clear_in_compare = (By.XPATH, '//div[@role="alert" and @class="messages"]')
button_fit_euip = (By.LINK_TEXT, 'Fitness Equipment')
button_add_product_to_wish_list = (By.CSS_SELECTOR, 'a[class="action towishlist"]')
check_added_product_to_wish_list = (By.XPATH, '//div[@role="alert" and @class="messages"]')
button_remove_from_wish_list = (By.XPATH, '//a[@title="Remove This Item"]')
message_no_items_in_wish_list = (By.XPATH, '//div[@role="alert" and @class="messages"]')
move_to_product_wish_list = (By.CSS_SELECTOR, 'div[class="product-item-info"]')
check_that_added_product_in_cart = (By.CSS_SELECTOR, '//div[@role="alert" and @class="messages"]')


class Gear(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_gear_page(self):
        self.driver.get(self.gear_page_url)
        sleep(1) #for demonstration

    def open_wishlist_page(self):
        self.driver.get(self.wish_list_url)

    def click_button_bags(self):
        self.find(button_bags).click()

    def click_sort_items(self):
        self.find(sort_items).click()

    def click_shopping_options_details(self):
        self.find(button_style_selection).click()
        self.find(button_style_selection_duffel).click()

    def check_that_items_on_page(self):
        check_product = self.find(check_that_product_items)
        return 'Overnight Duffle', 'Impulse Duffle' in check_product.text

    def products_add_to_cart(self):
       products = self.finds(add_product)
       products[0].click()

    def cart_check_waiting(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(check_that_added_product_in_cart)),
                   message='You added Overnight Duffle to your shopping cart.')
        return True

    def click_cart(self):
        self.find(click_cart).click()

    def check_cart(self):
        check_cart = self.find(cart)
        return 'Overnight Duffle' in check_cart.text

    def remove_items(self):
        self.find(remove_items).click()

    def deletion_warning(self):
        self.find(accept_alert).click()

    def check_that_no_have_items_in_cart(self):
        no_items = self.find(no_items_in_cart)
        return 'You have no items in your shopping cart.' in no_items.text

    def check_that_no_items_in_cart_waiting(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(no_items_in_cart)),
                   message='You have no items in your shopping cart.')
        return True

    def click_watches_button(self):
        self.find(button_watches).click()

    def watches_selection(self):
        self.find(watches_product_selection)

    def watches_add_to_compare(self):
        self.find(watches_action_to_compare).click()
        sleep(2) #for demonstration

    def watches_check_product_in_compare(self):
        check_product_name = self.find(check_that_block_compare)
        return 'You added product Didi Sport Watch to the comparison list.' in check_product_name.text

    def watches_clear_to_compare_click(self):
        self.find(button_clear_compare).click()
        self.find(button_accept_clear_compare).click()

    def watches_check_that_compare_clear(self):
        check_clear = self.find(check_that_compare_clear)
        return 'You have no items to compare.' in check_clear.text

    def message_compare_clear(self):
        check_clear = self.find(message_clear_in_compare)
        return 'You cleared the comparison list.' in check_clear.text

    def click_button_fitness_equip(self):
        self.find(button_fit_euip).click()

    def fit_click_add_to_wish_list(self):
        self.find(button_add_product_to_wish_list).click()

    def check_that_wish_list(self):
        wish = self.find(check_added_product_to_wish_list)
        return 'Sprite Yoga Companion Kit has been added to your Wish List. Click here to continue shopping.' in wish.text

    def check_that_wish_list_waiting(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(check_added_product_to_wish_list)),
                   message='Sprite Yoga Companion Kit has been added to your Wish List. Click here to continue shopping.')
        return True

    def click_remove_item_wish_list(self):
        remove = self.finds(button_remove_from_wish_list)
        remove[0].click()
        sleep(2)

    def check_clear_wish_list(self):
        cleared = self.find(message_no_items_in_wish_list)
        return 'Sprite Yoga Companion Kit has been removed from your Wish List.' in cleared.text

    def wait_remove_item_wish_list(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(button_remove_from_wish_list)),
                   )
        return True
