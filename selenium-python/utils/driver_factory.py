from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import json
import os

class DriverFactory:
    def __init__(self):
        self.config = self._load_config()
    
    def _load_config(self):
        """Load configuration from config.json"""
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"browser": "chrome", "base_url": "https://www.demoblaze.com"}
    
    def get_driver(self, browser=None):
        """Get WebDriver instance for specified browser"""
        if browser is None:
            browser = self.config.get('browser', 'chrome')
        
        browser = browser.lower()
        
        if browser == 'chrome':
            return self._get_chrome_driver()
        elif browser == 'firefox':
            return self._get_firefox_driver()
        elif browser == 'edge':
            return self._get_edge_driver()
        else:
            raise Exception(f'Browser {browser} not supported')
    
    def _get_chrome_driver(self):
        """Get Chrome WebDriver with optimized options"""
        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        # Avoid chrome closing due to background tab throttling
        options.add_argument('--disable-features=CalculateNativeWinOcclusion,TranslateUI')
        options.add_argument('--disable-background-timer-throttling')
        options.add_argument('--disable-backgrounding-occluded-windows')
        
        # Add headless option if specified in config
        if self.config.get('headless', False):
            options.add_argument('--headless=new')
            options.add_argument('--hide-scrollbars')
            options.add_argument('--mute-audio')
        
        try:
            driver = webdriver.Chrome(options=options)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            # Use reasonable timeouts
            driver.set_page_load_timeout(self.config.get('page_load_timeout', 30))
            driver.implicitly_wait(self.get_implicit_wait())
            return driver
        except Exception as e:
            raise Exception(f'Failed to initialize Chrome driver: {str(e)}')
    
    def _get_firefox_driver(self):
        """Get Firefox WebDriver with optimized options"""
        options = FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        
        # Add headless option if specified in config
        if self.config.get('headless', False):
            options.add_argument('--headless')
        
        try:
            driver = webdriver.Firefox(options=options)
            return driver
        except Exception as e:
            raise Exception(f'Failed to initialize Firefox driver: {str(e)}')
    
    def _get_edge_driver(self):
        """Get Edge WebDriver with optimized options"""
        options = EdgeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')
        
        # Add headless option if specified in config
        if self.config.get('headless', False):
            options.add_argument('--headless')
        
        try:
            driver = webdriver.Edge(options=options)
            return driver
        except Exception as e:
            raise Exception(f'Failed to initialize Edge driver: {str(e)}')
    
    def get_base_url(self):
        """Get base URL from configuration"""
        return self.config.get('base_url', 'https://www.demoblaze.com')
    
    def get_implicit_wait(self):
        """Get implicit wait time from configuration"""
        return self.config.get('implicit_wait', 10)
    
    def get_explicit_wait(self):
        """Get explicit wait time from configuration"""
        return self.config.get('explicit_wait', 10)
