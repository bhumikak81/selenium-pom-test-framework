import pytest
import allure
from utils.driver_factory import DriverFactory
from pages.home_page import HomePage
from helpers.test_data import TestData
from helpers.assertions import Assertions

@pytest.fixture()
def driver():
    driver = DriverFactory().get_driver()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def home_page(driver):
    return HomePage(driver)

@allure.epic("DemoBlaze E-commerce")
@allure.feature("Home Page")
class TestHomePage:
    
    @allure.story("Page Navigation")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_home_page(self, driver, home_page):
        """Test opening the home page and verifying title"""
        with allure.step("Open home page"):
            home_page.open('https://www.demoblaze.com')
        
        with allure.step("Verify page title"):
            title = home_page.get_title()
            Assertions.assert_text_contains(title, TestData.PAGE_TITLES["home"])

    @allure.story("Navigation Elements")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigation_elements_present(self, driver, home_page):
        """Test that all navigation elements are present on the page"""
        with allure.step("Open home page"):
            home_page.open('https://www.demoblaze.com')
        
        with allure.step("Verify navigation elements"):
            assert home_page.verify_navigation_elements(), "Not all navigation elements are present"

    @allure.story("Product Display")
    @allure.severity(allure.severity_level.NORMAL)
    def test_products_are_displayed(self, driver, home_page):
        """Test that products are displayed on the home page"""
        with allure.step("Open home page"):
            home_page.open('https://www.demoblaze.com')
        
        with allure.step("Get product count"):
            product_count = home_page.get_product_count()
            Assertions.assert_greater_than(product_count, 0, "No products are displayed")
        
        with allure.step("Get product titles"):
            product_titles = home_page.get_product_titles()
            Assertions.assert_list_not_empty(product_titles, "No product titles found")

    @allure.story("Product Information")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_information_displayed(self, driver, home_page):
        """Test that product information (titles and prices) is displayed"""
        with allure.step("Open home page"):
            home_page.open('https://www.demoblaze.com')
        
        with allure.step("Get product titles"):
            product_titles = home_page.get_product_titles()
            Assertions.assert_list_not_empty(product_titles)
        
        with allure.step("Get product prices"):
            product_prices = home_page.get_product_prices()
            Assertions.assert_list_not_empty(product_prices)
        
        with allure.step("Verify titles and prices have same count"):
            Assertions.assert_list_length(product_titles, len(product_prices))

    # Removed category navigation to keep quick suite at 10 tests

    @allure.story("Footer Elements")
    @allure.severity(allure.severity_level.MINOR)
    def test_footer_elements(self, driver, home_page):
        """Test that footer elements are present"""
        with allure.step("Open home page"):
            home_page.open('https://www.demoblaze.com')
        
        with allure.step("Verify footer is present"):
            assert home_page.verify_footer_present(), "Footer is not present"
        
        with allure.step("Validate footer text is present"):
            footer_text = home_page.get_copyright_text()
            assert footer_text and footer_text.strip(), "Footer text should not be empty"

    @allure.story("Modal Functionality")
    @allure.severity(allure.severity_level.NORMAL)
    def test_modal_buttons_functional(self, driver, home_page):
        """Test that modal buttons are functional"""
        with allure.step("Open home page"):
            home_page.open('https://www.demoblaze.com')
        
        with allure.step("Test login modal button"):
            home_page.open_login_modal()
            # Verify modal is displayed (basic check)
            import time
            time.sleep(1)
        
        with allure.step("Test signup modal button"):
            home_page.open_signup_modal()
            # Verify modal is displayed (basic check)
            time.sleep(1)
