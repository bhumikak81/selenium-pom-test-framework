import allure
from base.base_page import BasePage
from locators.cart_page_locators import CartPageLocators
from selenium.webdriver.common.alert import Alert

class CartPage(BasePage):

    @allure.step('Get cart items')
    def get_cart_items(self):
        """Get all item rows in the cart"""
        return self.find_elements(CartPageLocators.CART_ITEM_ROWS)

    @allure.step('Get cart item names')
    def get_cart_item_names(self):
        """Get names of all items in cart"""
        elements = self.find_elements(CartPageLocators.CART_ITEM_NAME_CELLS)
        return [element.text for element in elements]

    @allure.step('Get cart item prices')
    def get_cart_item_prices(self):
        """Get numeric prices of all items in cart"""
        elements = self.find_elements(CartPageLocators.CART_ITEM_PRICE_CELLS)
        prices = []
        for el in elements:
            try:
                prices.append(int(el.text.strip()))
            except Exception:
                continue
        return prices

    @allure.step('Get cart total')
    def get_cart_total(self):
        """Get the total amount in cart"""
        # wait for total to populate with a non-empty numeric value
        self.wait_for_element_visible(CartPageLocators.TOTAL_AMOUNT, timeout=10)
        import time
        end = time.time() + 10
        while time.time() < end:
            text = self.get_element_text(CartPageLocators.TOTAL_AMOUNT).strip()
            if text.isdigit():
                return text
            time.sleep(0.5)
        return self.get_element_text(CartPageLocators.TOTAL_AMOUNT).strip()

    @allure.step('Click place order button')
    def click_place_order(self):
        """Click the place order button"""
        self.click_element(CartPageLocators.PLACE_ORDER_BUTTON)
        self.wait_for_element_visible(CartPageLocators.ORDER_MODAL)

    @allure.step('Fill order form')
    def fill_order_form(self, name, country, city, credit_card, month, year):
        """Fill the order form with provided details"""
        self.send_keys_to_element(CartPageLocators.ORDER_NAME_INPUT, name)
        self.send_keys_to_element(CartPageLocators.ORDER_COUNTRY_INPUT, country)
        self.send_keys_to_element(CartPageLocators.ORDER_CITY_INPUT, city)
        self.send_keys_to_element(CartPageLocators.ORDER_CREDIT_CARD_INPUT, credit_card)
        self.send_keys_to_element(CartPageLocators.ORDER_MONTH_INPUT, month)
        self.send_keys_to_element(CartPageLocators.ORDER_YEAR_INPUT, year)

    @allure.step('Click purchase button')
    def click_purchase(self):
        """Click the purchase button"""
        self.click_element(CartPageLocators.PURCHASE_BUTTON)
        # Handle any alert gracefully
        try:
            Alert(self.driver).accept()
        except Exception:
            pass

    @allure.step('Close order modal')
    def close_order_modal(self):
        """Close the order modal"""
        self.click_element(CartPageLocators.CLOSE_ORDER_BUTTON)

    @allure.step('Delete item from cart')
    def delete_item_from_cart(self, item_index=0):
        """Delete an item from cart by index"""
        delete_buttons = self.find_elements(CartPageLocators.DELETE_BUTTONS)
        if delete_buttons and len(delete_buttons) > item_index:
            initial_count = len(self.get_cart_items())
            delete_buttons[item_index].click()
            # wait for row count to decrease
            import time
            end = time.time() + 10
            while time.time() < end:
                if len(self.get_cart_items()) < initial_count:
                    break
                time.sleep(0.5)

    @allure.step('Get cart item count')
    def get_cart_item_count(self):
        """Get the number of items in cart"""
        items = self.get_cart_items()
        return len(items)

    @allure.step('Verify cart is empty')
    def verify_cart_is_empty(self):
        """Verify that the cart is empty (no item rows)"""
        return len(self.get_cart_items()) == 0

    @allure.step('Verify place order button is present')
    def verify_place_order_button_present(self):
        """Verify place order button is present"""
        return self.is_element_displayed(CartPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Complete purchase process')
    def complete_purchase(self, name, country, city, credit_card, month, year):
        """Complete the entire purchase process"""
        self.click_place_order()
        self.fill_order_form(name, country, city, credit_card, month, year)
        self.click_purchase()

    @allure.step('Clear cart')
    def clear_cart(self):
        """Remove all items from cart"""
        # Keep deleting the first item until no rows remain, with a safety cap
        safety_cap = 20
        while safety_cap > 0:
            rows = self.get_cart_items()
            if not rows:
                break
            self.delete_item_from_cart(0)
            safety_cap -= 1
