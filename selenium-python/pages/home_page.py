import allure
from base.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.product_page_locators import ProductPageLocators
from selenium.webdriver.common.alert import Alert

class HomePage(BasePage):

    @allure.step('Verify page title')
    def get_title(self):
        return self.driver.title

    @allure.step('Get all product cards')
    def get_product_cards(self):
        """Get all product cards on the page"""
        return self.find_elements(HomePageLocators.PRODUCT_CARDS)

    @allure.step('Get product titles')
    def get_product_titles(self):
        """Get all product titles"""
        # Clear any unexpected alert before reading the list
        self.handle_any_alert()
        elements = self.find_elements(HomePageLocators.PRODUCT_TITLES)
        return [element.text for element in elements]

    @allure.step('Get product prices')
    def get_product_prices(self):
        """Get all product prices"""
        self.handle_any_alert()
        elements = self.find_elements(HomePageLocators.PRODUCT_PRICES)
        return [element.text for element in elements]

    @allure.step('Click on product by name')
    def click_product_by_name(self, product_name):
        """Click on a specific product by name"""
        products = self.find_elements(HomePageLocators.PRODUCT_TITLES)
        for product in products:
            if product_name.lower() in product.text.lower():
                original_handles = self.driver.window_handles[:]
                # Clear any alert before navigation
                self.handle_any_alert()
                try:
                    product.click()
                except Exception:
                    # scroll and JS click fallback
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", product)
                    self.driver.execute_script("arguments[0].click();", product)
                # If click opened a new window/tab, switch to it
                self.wait_for_new_window_and_switch(original_handles, timeout=5)
                # Clear any alert that might have popped during navigation
                self.wait_for_alert_and_accept(timeout=2)
                # wait for product page to load by waiting for product name or URL
                if not self.wait_for_url_contains("prod.html", timeout=5):
                    self.wait_for_element_visible(ProductPageLocators.PRODUCT_NAME, timeout=10)
                break

    @allure.step('Click on category')
    def click_category(self, category_name):
        """Click on a specific category"""
        if category_name.lower() == "phones":
            self.click_element(HomePageLocators.PHONES_CATEGORY)
        elif category_name.lower() == "laptops":
            self.click_element(HomePageLocators.LAPTOPS_CATEGORY)
        elif category_name.lower() == "monitors":
            self.click_element(HomePageLocators.MONITORS_CATEGORY)

    @allure.step('Open login modal')
    def open_login_modal(self):
        """Open the login modal"""
        self.click_element(HomePageLocators.LOGIN_LINK)
        self.wait_for_element_visible(HomePageLocators.LOGIN_MODAL)

    @allure.step('Open signup modal')
    def open_signup_modal(self):
        """Open the signup modal"""
        # Close login modal first if open to avoid intercepted click
        if self.is_element_displayed(HomePageLocators.LOGIN_MODAL):
            # Try close X first, then secondary button
            try:
                self.click_element(HomePageLocators.LOGIN_MODAL_CLOSE_X)
            except Exception:
                self.click_element(HomePageLocators.MODAL_CLOSE_BUTTON)
        self.click_element(HomePageLocators.SIGNUP_LINK)
        self.wait_for_element_visible(HomePageLocators.SIGNUP_MODAL)

    @allure.step('Open cart')
    def open_cart(self):
        """Open the shopping cart"""
        # Dismiss possible alert leftovers
        try:
            Alert(self.driver).dismiss()
        except Exception:
            pass
        # Also use base alert handler to ensure no blocking alert
        self.handle_any_alert()
        self.click_element(HomePageLocators.CART_LINK)

    @allure.step('Navigate to contact page')
    def navigate_to_contact(self):
        """Navigate to contact page"""
        self.click_element(HomePageLocators.CONTACT_LINK)
        if self.wait_for_element_visible(HomePageLocators.CONTACT_MODAL, timeout=5):
            # Close contact modal to avoid intercepting other clicks
            try:
                self.click_element(HomePageLocators.CONTACT_MODAL_CLOSE_X)
            except Exception:
                try:
                    self.click_element(HomePageLocators.CONTACT_MODAL_CLOSE_BUTTON)
                except Exception:
                    pass

    @allure.step('Navigate to about us page')
    def navigate_to_about_us(self):
        """Navigate to about us page"""
        self.click_element(HomePageLocators.ABOUT_US_LINK)
        # If video modal opens, close it
        if self.wait_for_element_visible(HomePageLocators.ABOUT_US_VIDEO_MODAL, timeout=5):
            try:
                self.click_element(HomePageLocators.ABOUT_US_VIDEO_CLOSE)
            except Exception:
                pass

    @allure.step('Verify navigation elements are present')
    def verify_navigation_elements(self):
        """Verify all navigation elements are present"""
        elements_to_check = [
            HomePageLocators.NAVBAR_BRAND,
            HomePageLocators.HOME_LINK,
            HomePageLocators.CONTACT_LINK,
            HomePageLocators.ABOUT_US_LINK,
            HomePageLocators.CART_LINK,
            HomePageLocators.LOGIN_LINK,
            HomePageLocators.SIGNUP_LINK
        ]
        
        for locator in elements_to_check:
            if not self.is_element_displayed(locator):
                return False
        return True

    @allure.step('Get product count')
    def get_product_count(self):
        """Get the total number of products displayed"""
        products = self.get_product_cards()
        return len(products)

    @allure.step('Verify footer is present')
    def verify_footer_present(self):
        """Verify footer is present on the page"""
        # Scroll to bottom to ensure footer is in viewport
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.is_element_displayed(HomePageLocators.FOOTER)

    @allure.step('Get copyright text')
    def get_copyright_text(self):
        """Get copyright text from footer"""
        return self.get_element_text(HomePageLocators.COPYRIGHT_TEXT)
