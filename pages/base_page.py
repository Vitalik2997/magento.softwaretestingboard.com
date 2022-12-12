from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = 'https://magento.softwaretestingboard.com/'
        self.create_page_url = 'https://magento.softwaretestingboard.com/customer/account/create/'
        self.sign_in_page_url = 'https://magento.softwaretestingboard.com/customer/account/login/'
        self.my_acc_page_url = 'https://magento.softwaretestingboard.com/customer/account/'
        self.gear_page_url = 'https://magento.softwaretestingboard.com/gear.html'
        self.wish_list_url = 'https://magento.softwaretestingboard.com/wishlist'
        self.men_page_url = 'https://magento.softwaretestingboard.com/men.html'
        self.shipping_address_url = 'https://magento.softwaretestingboard.com/checkout/#shipping'

    def find(self, args: tuple):
        by_name, by_val = args
        return self.driver.find_element(by_name, by_val)

    def finds(self, args: tuple):
        by_name, by_val = args
        return self.driver.find_elements(by_name, by_val)

    def scroll_page_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
