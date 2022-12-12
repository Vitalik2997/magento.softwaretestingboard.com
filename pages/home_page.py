from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


create_acc_clickable = (By.LINK_TEXT, 'Create an Account')
search_field = (By.CSS_SELECTOR, 'input[id="search"]')
button_sign_in = (By.CSS_SELECTOR, 'li[class="authorization-link"]')
button_cart = (By.CSS_SELECTOR, 'a[class="action showcart"]')
button_whats_new = (By.CSS_SELECTOR, 'a[id="ui-id-3"]')
button_women = (By.CSS_SELECTOR, 'a[id="ui-id-4"]')
button_men = (By.CSS_SELECTOR, 'a[id="ui-id-5"]')
button_gear = (By.CSS_SELECTOR, 'a[id="ui-id-6"]')
button_training = (By.CSS_SELECTOR, 'a[id="ui-id-7"]')
button_sale = (By.CSS_SELECTOR, 'a[id="ui-id-8"]')
button_return_home_page = (By.CSS_SELECTOR, 'a[class="logo"]')
button_search_terms = (By.LINK_TEXT, 'Search Terms')
button_action_switch = (By.CSS_SELECTOR, 'button[class="action switch"]')
button_sign_out = (By.CSS_SELECTOR, 'li[class="authorization-link"]')
button_subscribe = (By.CSS_SELECTOR, 'button[class="action subscribe primary"]')
search_terms_title = (By.CSS_SELECTOR, 'div[class="page-title-wrapper"]')
check_that_sign_out = (By.CSS_SELECTOR, 'div[class="page-title-wrapper"]')
input_field_for_subscription = (By.ID, 'newsletter')
alert_message_email_already_subscribed = (By.XPATH, '//div[@role="alert" and @class="messages"]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.driver.get(self.base_url)

    def create_acc_is_displayed(self):
        button_create_acc = self.find(create_acc_clickable)
        return button_create_acc.is_displayed()

    def create_acc_clickable(self):
        self.find(create_acc_clickable).click()

    def sign_in_acc_is_displayed(self):
        sign_in = self.find(button_sign_in)
        return sign_in.is_displayed()

    def search_field_is_displayed(self):
        search = self.find(search_field)
        return search.is_displayed()

    def cart_is_displayed(self):
        cart = self.find(button_cart)
        return cart.is_displayed()

    def whats_new_is_displayed(self):
        whats_new = self.find(button_whats_new)
        return whats_new.is_displayed()

    def women_is_displayed(self):
        women = self.find(button_women)
        return women.is_displayed()

    def men_is_displayed(self):
        men = self.find(button_men)
        return men.is_displayed()

    def gear_is_displayed(self):
        gear = self.find(button_gear)
        return gear.is_displayed()

    def training_is_displayed(self):
        training = self.find(button_training)
        return training.is_displayed()

    def sale_is_displayed(self):
        sale = self.find(button_sale)
        return sale.is_displayed()

    def return_home_page_is_displayed(self):
        home_page = self.find(button_return_home_page)
        return home_page.is_displayed()

    def click_search_terms(self):
        self.find(button_search_terms).click()

    def search_terms_popular_is_displayed(self):
        popular_search = self.find(search_terms_title)
        return 'Popular Search Terms' in popular_search.text

    def click_button_action_switch(self):
        self.find(button_action_switch).click()

    def click_button_sign_out(self):
        self.find(button_sign_out).click()

    def check_that_sign_out_in_acc(self):
        check = self.find(check_that_sign_out)
        return 'You are signed out' in check.text

    def input_email_for_subscribe(self, email):
        self.find(input_field_for_subscription).send_keys(email)

    def click_button_subscribe(self):
        self.find(button_subscribe).click()

    def alert_email_already_subscribed(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(alert_message_email_already_subscribed)),
                   message='This email address is already subscribed.')
        return True

