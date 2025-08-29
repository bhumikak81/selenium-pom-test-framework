from selenium.webdriver.common.by import By

class CartPageLocators:
    # Cart table rows (Demoblaze uses class 'success' for item rows)
    CART_ITEM_ROWS = (By.XPATH, "//tr[@class='success']")
    CART_ITEM_NAME_CELLS = (By.XPATH, "//tr[@class='success']/td[2]")
    CART_ITEM_PRICE_CELLS = (By.XPATH, "//tr[@class='success']/td[3]")
    DELETE_BUTTONS = (By.XPATH, "//tr[@class='success']/td[4]//a[contains(text(), 'Delete')]")

    # Cart actions
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Place Order')]")

    # Order modal
    ORDER_MODAL = (By.ID, "orderModal")
    ORDER_NAME_INPUT = (By.ID, "name")
    ORDER_COUNTRY_INPUT = (By.ID, "country")
    ORDER_CITY_INPUT = (By.ID, "city")
    ORDER_CREDIT_CARD_INPUT = (By.ID, "card")
    ORDER_MONTH_INPUT = (By.ID, "month")
    ORDER_YEAR_INPUT = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[contains(text(), 'Purchase')]")
    CLOSE_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'modal') and contains(@class,'show')]//button[contains(text(),'Close')]")

    # Total
    TOTAL_AMOUNT = (By.ID, "totalp")

    # Empty cart heuristic: no rows present
