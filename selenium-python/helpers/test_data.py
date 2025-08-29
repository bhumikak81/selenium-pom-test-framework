import json
import random
import string

class TestData:
    """Test data for various test scenarios"""
    
    # User credentials
    VALID_USERNAME = "testuser"
    VALID_PASSWORD = "testpass123"
    INVALID_USERNAME = "invaliduser"
    INVALID_PASSWORD = "wrongpass"
    
    # Order information
    ORDER_DATA = {
        "valid_order": {
            "name": "John Doe",
            "country": "United States",
            "city": "New York",
            "credit_card": "1234567890123456",
            "month": "12",
            "year": "2025"
        },
        "invalid_order": {
            "name": "",
            "country": "",
            "city": "",
            "credit_card": "invalid",
            "month": "13",
            "year": "2020"
        }
    }
    
    # Product categories
    CATEGORIES = ["phones", "laptops", "monitors"]
    
    # Expected page titles
    PAGE_TITLES = {
        "home": "STORE",
        "contact": "Contact",
        "about": "About us",
        "cart": "Cart"
    }
    
    # Test messages
    MESSAGES = {
        "product_added": "Product added",
        "order_placed": "Thank you for your purchase!",
        "invalid_credentials": "Wrong password"
    }
    
    @staticmethod
    def generate_random_string(length=8):
        """Generate a random string of specified length"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    @staticmethod
    def generate_random_email():
        """Generate a random email address"""
        username = TestData.generate_random_string(8)
        domain = TestData.generate_random_string(6)
        return f"{username}@{domain}.com"
    
    @staticmethod
    def generate_random_phone():
        """Generate a random phone number"""
        return f"+1{random.randint(1000000000, 9999999999)}"
    
    @staticmethod
    def get_random_order_data():
        """Get random order data for testing"""
        base_data = TestData.ORDER_DATA["valid_order"].copy()
        base_data["name"] = f"Test User {TestData.generate_random_string(4)}"
        base_data["city"] = f"Test City {TestData.generate_random_string(4)}"
        return base_data
    
    @staticmethod
    def load_config():
        """Load configuration from config.json"""
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"browser": "chrome", "base_url": "https://www.demoblaze.com"}
