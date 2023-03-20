from pages.base_page import BasePage
from locators import home_page_locators as hpl
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.driver.get(self.base_url)

    def create_acc_is_displayed(self):
        button_create_acc = self.find(hpl.create_acc_clickable)
        return button_create_acc.is_displayed()

    def create_acc_clickable(self):
        self.find(hpl.create_acc_clickable).click()

    def sign_in_acc_is_displayed(self):
        sign_in = self.find(hpl.button_sign_in)
        return sign_in.is_displayed()

    def search_field_is_displayed(self):
        search = self.find(hpl.search_field)
        return search.is_displayed()

    def cart_is_displayed(self):
        cart = self.find(hpl.button_cart)
        return cart.is_displayed()

    def whats_new_is_displayed(self):
        whats_new = self.find(hpl.button_whats_new)
        return whats_new.is_displayed()

    def women_is_displayed(self):
        women = self.find(hpl.button_women)
        return women.is_displayed()

    def men_is_displayed(self):
        men = self.find(hpl.button_men)
        return men.is_displayed()

    def gear_is_displayed(self):
        gear = self.find(hpl.button_gear)
        return gear.is_displayed()

    def training_is_displayed(self):
        training = self.find(hpl.button_training)
        return training.is_displayed()

    def sale_is_displayed(self):
        sale = self.find(hpl.button_sale)
        return sale.is_displayed()

    def return_home_page_is_displayed(self):
        home_page = self.find(hpl.button_return_home_page)
        return home_page.is_displayed()

    def click_search_terms(self):
        self.find(hpl.button_search_terms).click()

    def search_terms_popular_is_displayed(self):
        popular_search = self.find(hpl.search_terms_title)
        return 'Popular Search Terms' in popular_search.text

    def click_button_action_switch(self):
        self.find(hpl.button_action_switch).click()

    def click_button_sign_out(self):
        self.find(hpl.button_sign_out).click()

    def check_that_sign_out_in_acc(self):
        check = self.find(hpl.check_that_sign_out)
        return 'You are signed out' in check.text

    def input_email_for_subscribe(self, email):
        self.find(hpl.input_field_for_subscription).send_keys(email)

    def click_button_subscribe(self):
        self.find(hpl.button_subscribe).click()

    def alert_email_already_subscribed(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(hpl.alert_message_email_already_subscribed)),
                   message='This email address is already subscribed.')
        return True

