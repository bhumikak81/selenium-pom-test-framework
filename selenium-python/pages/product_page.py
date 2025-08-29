import allure
from base.base_page import BasePage
from locators.product_page_locators import ProductPageLocators
from selenium.webdriver.common.alert import Alert

class ProductPage(BasePage):

    @allure.step('Get product name')
    def get_product_name(self):
        """Get the product name"""
        # Ensure correct window and page are active
        self.switch_to_latest_window()
        if not self.wait_for_url_contains("prod.html", timeout=10):
            # fallback: still wait for key element
            self.wait_for_element_visible(ProductPageLocators.PRODUCT_NAME, timeout=10)
        else:
            self.wait_for_element_visible(ProductPageLocators.PRODUCT_NAME, timeout=10)
        return self.get_element_text(ProductPageLocators.PRODUCT_NAME)

    @allure.step('Get product price')
    def get_product_price(self):
        """Get the product price"""
        self.switch_to_latest_window()
        if not self.wait_for_url_contains("prod.html", timeout=5):
            self.wait_for_element_visible(ProductPageLocators.PRODUCT_PRICE, timeout=10)
        return self.get_element_text(ProductPageLocators.PRODUCT_PRICE)

    @allure.step('Get product description')
    def get_product_description(self):
        """Get the product description"""
        self.switch_to_latest_window()
        return self.get_element_text(ProductPageLocators.PRODUCT_DESCRIPTION)

    @allure.step('Add product to cart')
    def add_to_cart(self):
        """Add the current product to cart"""
        self.click_element(ProductPageLocators.ADD_TO_CART_BUTTON)
        # Handle confirmation alert
        self.wait_for_alert_and_accept(timeout=10)

    @allure.step('Go back to products')
    def go_back_to_products(self):
        """Go back to the products list"""
        # Prefer browser back due to site structure
        # Ensure any lingering alert is accepted before navigating back
        self.handle_any_alert()
        self.go_back()
        # Ensure we are back on the home page listing
        if not self.wait_for_url_contains("index.html", timeout=5):
            # some deployments don't show index.html, so wait for home locator
            from locators.home_page_locators import HomePageLocators
            self.wait_for_element_visible(HomePageLocators.PRODUCT_CARDS, timeout=10)

    @allure.step('Verify product image is displayed')
    def verify_product_image_displayed(self):
        """Verify product image is displayed"""
        # ensure we're on product page
        self.wait_for_url_contains("prod.html", timeout=10)
        # some images load late; try a short poll
        if self.wait_for_element_visible(ProductPageLocators.PRODUCT_IMAGE, timeout=10):
            return True
        # small scroll to trigger lazy load
        self.driver.execute_script("window.scrollBy(0, 200);")
        return self.wait_for_element_visible(ProductPageLocators.PRODUCT_IMAGE, timeout=5)

    @allure.step('Click on specs tab')
    def click_specs_tab(self):
        """Click on the specifications tab"""
        self.click_element(ProductPageLocators.SPECS_TAB)

    @allure.step('Click on reviews tab')
    def click_reviews_tab(self):
        """Click on the reviews tab"""
        self.click_element(ProductPageLocators.REVIEWS_TAB)

    @allure.step('Get product specifications')
    def get_product_specifications(self):
        """Get product specifications text"""
        return self.get_element_text(ProductPageLocators.PRODUCT_SPECS)

    @allure.step('Navigate to home via breadcrumb')
    def navigate_to_home_via_breadcrumb(self):
        """Navigate to home page via breadcrumb"""
        self.click_element(ProductPageLocators.BREADCRUMB_HOME)

    @allure.step('Verify add to cart button is present')
    def verify_add_to_cart_button_present(self):
        """Verify add to cart button is present"""
        return self.is_element_displayed(ProductPageLocators.ADD_TO_CART_BUTTON)

    @allure.step('Verify product details are loaded')
    def verify_product_details_loaded(self):
        """Verify all product details are loaded"""
        # Ensure we are on a product page; switch to latest window in case a new tab opened
        self.switch_to_latest_window()
        self.wait_for_url_contains("prod.html", timeout=10)
        name_visible = self.wait_for_element_visible(ProductPageLocators.PRODUCT_NAME, timeout=10)
        price_visible = self.wait_for_element_visible(ProductPageLocators.PRODUCT_PRICE, timeout=10)
        add_to_cart_visible = self.wait_for_element_visible(ProductPageLocators.ADD_TO_CART_BUTTON, timeout=10)
        return name_visible and price_visible and add_to_cart_visible
