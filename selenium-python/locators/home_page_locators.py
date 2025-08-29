from selenium.webdriver.common.by import By

class HomePageLocators:
    # Navigation elements
    NAVBAR_BRAND = (By.CLASS_NAME, "navbar-brand")
    HOME_LINK = (By.XPATH, "//a[contains(text(), 'Home')]")
    CONTACT_LINK = (By.XPATH, "//a[contains(text(), 'Contact')]")
    CONTACT_MODAL = (By.ID, "exampleModal")
    CONTACT_MODAL_CLOSE_X = (By.XPATH, "//div[@id='exampleModal']//button[@class='close']")
    CONTACT_MODAL_CLOSE_BUTTON = (By.XPATH, "//div[@id='exampleModal']//button[contains(text(),'Close')]")
    ABOUT_US_LINK = (By.XPATH, "//a[contains(text(), 'About us')]")
    ABOUT_US_VIDEO_MODAL = (By.ID, "videoModal")
    ABOUT_US_VIDEO_CLOSE = (By.XPATH, "//div[@id='videoModal']//button[@class='close']")
    CART_LINK = (By.ID, "cartur")
    LOGIN_LINK = (By.ID, "login2")
    SIGNUP_LINK = (By.ID, "signin2")
    
    # Product elements
    PRODUCT_CARDS = (By.CLASS_NAME, "card")
    PRODUCT_TITLES = (By.CLASS_NAME, "card-title")
    PRODUCT_PRICES = (By.CLASS_NAME, "card-text")
    PRODUCT_IMAGES = (By.CLASS_NAME, "card-img-top")
    
    # Categories
    PHONES_CATEGORY = (By.XPATH, "//a[contains(text(), 'Phones')]")
    LAPTOPS_CATEGORY = (By.XPATH, "//a[contains(text(), 'Laptops')]")
    MONITORS_CATEGORY = (By.XPATH, "//a[contains(text(), 'Monitors')]")
    
    # Modal elements
    LOGIN_MODAL = (By.ID, "logInModal")
    SIGNUP_MODAL = (By.ID, "signInModal")
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "btn-secondary")
    LOGIN_MODAL_CLOSE_X = (By.XPATH, "//div[@id='logInModal']//button[@class='close']")
    SIGNUP_MODAL_CLOSE_X = (By.XPATH, "//div[@id='signInModal']//button[@class='close']")
    
    # Footer elements
    FOOTER = (By.ID, "fotcont")
    COPYRIGHT_TEXT = (By.XPATH, "//div[@id='fotcont']//*[contains(.,'Copyright') or contains(.,'PRODUCT STORE') or self::p or self::small]")
