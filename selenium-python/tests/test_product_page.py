import pytest
import allure
from utils.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.product_page import ProductPage
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

@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)

@allure.epic("DemoBlaze E-commerce")
@allure.feature("Product Page")
class TestProductPage:
    
    @allure.story("Product Details")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_details_displayed(self, driver, home_page, product_page):
        """Test that product details are properly displayed"""
        with allure.step("Open home page"):
            home_page.open('https://www.demoblaze.com')
        
        with allure.step("Get first product name"):
            product_titles = home_page.get_product_titles()
            Assertions.assert_list_not_empty(product_titles)
            first_product = product_titles[0]
        
        with allure.step("Click on first product"):
            home_page.click_product_by_name(first_product)
        
        with allure.step("Verify product details are loaded"):
            assert product_page.verify_product_details_loaded(), "Product details not loaded properly"
        
        with allure.step("Get product information"):
            product_name = product_page.get_product_name()
            product_price = product_page.get_product_price()
            
            Assertions.assert_text_equals(product_name, first_product)
            Assertions.assert_text_contains(product_price, "$")

    @allure.story("Product Image")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_image_displayed(self, driver, home_page, product_page):
        """Test that product image is displayed"""
        with allure.step("Open home page"):
            home_page.open('https://www.demoblaze.com')
        
        with allure.step("Click on first product"):
            product_titles = home_page.get_product_titles()
            home_page.click_product_by_name(product_titles[0])
        
        with allure.step("Verify product image is displayed"):
            assert product_page.verify_product_image_displayed(), "Product image not displayed"

    @allure.story("Add to Cart Functionality")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_to_cart_button_present(self, driver, home_page, product_page):
        """Test that add to cart button is present on product page"""
        with allure.step("Open home page"):
            home_page.open('https://www.demoblaze.com')
        
        with allure.step("Click on first product"):
            product_titles = home_page.get_product_titles()
            home_page.click_product_by_name(product_titles[0])
        
        with allure.step("Verify add to cart button is present"):
            assert product_page.verify_add_to_cart_button_present(), "Add to cart button not present"

    @allure.story("Navigation")
    @allure.severity(allure.severity_level.NORMAL)
    def test_back_to_products_navigation(self, driver, home_page, product_page):
        """Test navigation back to products list"""
        with allure.step("Open home page"):
            home_page.open('https://www.demoblaze.com')
        
        with allure.step("Click on first product"):
            product_titles = home_page.get_product_titles()
            home_page.click_product_by_name(product_titles[0])
        
        with allure.step("Go back to products"):
            product_page.go_back_to_products()
        
        with allure.step("Verify we're back to home page"):
            current_url = home_page.get_current_url()
            Assertions.assert_text_contains(current_url, "demoblaze.com")


