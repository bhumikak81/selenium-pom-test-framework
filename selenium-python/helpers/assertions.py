import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Assertions:
    """Custom assertion methods for test validation"""
    
    @staticmethod
    @allure.step('Assert element is displayed')
    def assert_element_displayed(driver, locator, timeout=10):
        """Assert that an element is displayed"""
        try:
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            assert False, f"Element {locator} is not displayed within {timeout} seconds"
    
    @staticmethod
    @allure.step('Assert element is not displayed')
    def assert_element_not_displayed(driver, locator, timeout=10):
        """Assert that an element is not displayed"""
        try:
            WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located(locator))
            return True
        except:
            assert False, f"Element {locator} is still displayed after {timeout} seconds"
    
    @staticmethod
    @allure.step('Assert text contains expected value')
    def assert_text_contains(actual_text, expected_text):
        """Assert that actual text contains expected text"""
        assert expected_text.lower() in actual_text.lower(), \
            f"Expected '{expected_text}' to be in '{actual_text}'"
    
    @staticmethod
    @allure.step('Assert text equals expected value')
    def assert_text_equals(actual_text, expected_text):
        """Assert that actual text equals expected text"""
        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but got '{actual_text}'"
    
    @staticmethod
    @allure.step('Assert list is not empty')
    def assert_list_not_empty(items_list, message="List should not be empty"):
        """Assert that a list is not empty"""
        assert len(items_list) > 0, message
    
    @staticmethod
    @allure.step('Assert list has expected length')
    def assert_list_length(items_list, expected_length, message=None):
        """Assert that a list has the expected length"""
        if message is None:
            message = f"Expected {expected_length} items, but got {len(items_list)}"
        assert len(items_list) == expected_length, message
    
    @staticmethod
    @allure.step('Assert value is greater than')
    def assert_greater_than(actual_value, expected_value, message=None):
        """Assert that actual value is greater than expected value"""
        if message is None:
            message = f"Expected {actual_value} to be greater than {expected_value}"
        assert actual_value > expected_value, message
    
    @staticmethod
    @allure.step('Assert value is less than')
    def assert_less_than(actual_value, expected_value, message=None):
        """Assert that actual value is less than expected value"""
        if message is None:
            message = f"Expected {actual_value} to be less than {expected_value}"
        assert actual_value < expected_value, message
    
    @staticmethod
    @allure.step('Assert URL contains expected path')
    def assert_url_contains(driver, expected_path):
        """Assert that current URL contains expected path"""
        current_url = driver.current_url
        assert expected_path in current_url, \
            f"Expected URL to contain '{expected_path}', but got '{current_url}'"
    
    @staticmethod
    @allure.step('Assert page title contains expected text')
    def assert_title_contains(driver, expected_text):
        """Assert that page title contains expected text"""
        actual_title = driver.title
        assert expected_text.lower() in actual_title.lower(), \
            f"Expected title to contain '{expected_text}', but got '{actual_title}'"
    
    @staticmethod
    @allure.step('Assert element is clickable')
    def assert_element_clickable(driver, locator, timeout=10):
        """Assert that an element is clickable"""
        try:
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
            return True
        except:
            assert False, f"Element {locator} is not clickable within {timeout} seconds"
