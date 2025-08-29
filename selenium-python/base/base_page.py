from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.common.exceptions import UnexpectedAlertPresentException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def open(self, url):
        """Open the specified URL"""
        with allure.step(f"Opening URL: {url}"):
            self.driver.get(url)

    def get_title(self):
        """Get the page title"""
        return self.driver.title

    def get_current_url(self):
        """Get the current URL"""
        return self.driver.current_url

    def find_element(self, locator):
        """Find element with explicit wait"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except UnexpectedAlertPresentException:
            # Dismiss unexpected alerts and retry once
            self.handle_any_alert()
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f"Element not found: {locator}")

    def find_elements(self, locator):
        """Find multiple elements with explicit wait"""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except UnexpectedAlertPresentException:
            self.handle_any_alert()
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []

    def click_element(self, locator):
        """Click element with explicit wait"""
        with allure.step(f"Clicking element: {locator}"):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
            except UnexpectedAlertPresentException:
                self.handle_any_alert()
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()

    def send_keys_to_element(self, locator, text):
        """Send keys to element with explicit wait"""
        with allure.step(f"Sending keys '{text}' to element: {locator}"):
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)

    def get_element_text(self, locator):
        """Get text from element"""
        element = self.find_element(locator)
        return element.text

    def is_element_displayed(self, locator):
        """Check if element is displayed"""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def wait_for_element_visible(self, locator, timeout=10):
        """Wait for element to be visible"""
        try:
            try:
                WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            except UnexpectedAlertPresentException:
                self.handle_any_alert()
                WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_alert_and_accept(self, timeout=5):
        """Wait for a JavaScript alert and accept it if present"""
        try:
            end_time = __import__("time").time() + timeout
            handled = False
            while __import__("time").time() < end_time:
                try:
                    WebDriverWait(self.driver, 1).until(EC.alert_is_present())
                    alert = self.driver.switch_to.alert
                    alert.accept()
                    handled = True
                    break
                except Exception:
                    pass
            if handled:
                self.wait_until_no_alert(timeout=3)
                return True
            return False
        except Exception:
            return False

    def handle_any_alert(self) -> bool:
        """Accept or dismiss any open alert if present."""
        try:
            alert = self.driver.switch_to.alert
            try:
                alert.accept()
            except Exception:
                try:
                    alert.dismiss()
                except Exception:
                    pass
            self.wait_until_no_alert(timeout=2)
            return True
        except Exception:
            return False

    def wait_until_no_alert(self, timeout: int = 3) -> bool:
        """Wait until there is no alert present."""
        import time
        end = time.time() + timeout
        while time.time() < end:
            try:
                # Accessing alert when none present raises
                _ = self.driver.switch_to.alert.text
                time.sleep(0.2)
            except Exception:
                return True
        return False

    def scroll_to_element(self, locator):
        """Scroll to element"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def hover_over_element(self, locator):
        """Hover over element"""
        element = self.find_element(locator)
        self.actions.move_to_element(element).perform()

    def take_screenshot(self, name="screenshot"):
        """Take screenshot for debugging"""
        self.driver.save_screenshot(f"reports/{name}.png")

    def refresh_page(self):
        """Refresh the current page"""
        self.driver.refresh()

    def go_back(self):
        """Go back to previous page"""
        self.driver.back()

    def go_forward(self):
        """Go forward to next page"""
        self.driver.forward()

    def wait_for_url_contains(self, fragment: str, timeout: int = 10) -> bool:
        """Wait until current URL contains the given fragment"""
        try:
            def _cond(driver):
                try:
                    current = driver.current_url or ""
                except UnexpectedAlertPresentException:
                    self.handle_any_alert()
                    return False
                return fragment in current
            WebDriverWait(self.driver, timeout).until(_cond)
            return True
        except TimeoutException:
            return False

    def switch_to_latest_window(self, timeout: int = 5) -> None:
        """Switch focus to the most recently opened browser window/tab."""
        try:
            WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 0)
            latest = self.driver.window_handles[-1]
            self.driver.switch_to.window(latest)
        except Exception:
            # best-effort; keep current window if switching fails
            pass

    def wait_for_new_window_and_switch(self, original_handles: list[str], timeout: int = 10) -> bool:
        """Wait for a new window to open compared to original_handles and switch to it."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: len([h for h in d.window_handles if h not in original_handles]) > 0
            )
            new_handles = [h for h in self.driver.window_handles if h not in original_handles]
            if new_handles:
                self.driver.switch_to.window(new_handles[-1])
                return True
            return False
        except TimeoutException:
            return False
