from selenium.webdriver.common.by import By

class ProductPageLocators:
    # Product details
    PRODUCT_NAME = (By.CLASS_NAME, "name")
    PRODUCT_PRICE = (By.CLASS_NAME, "price-container")
    PRODUCT_DESCRIPTION = (By.ID, "more-information")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "#imgp img, .product-image img, .img-responsive, .img-fluid")
    
    # Action buttons
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[contains(text(), 'Add to cart')]")
    BACK_TO_PRODUCTS_BUTTON = (By.XPATH, "//a[contains(text(), 'Add to cart')]/following-sibling::a")
    
    # Product specifications (fallback generic content area)
    PRODUCT_SPECS = (By.ID, "more-information")
    SPECS_TAB = (By.ID, "specs")
    REVIEWS_TAB = (By.ID, "reviews")
    
    # Navigation
    BREADCRUMB_HOME = (By.XPATH, "//a[contains(text(), 'Home')]")
    BREADCRUMB_CATEGORY = (By.CLASS_NAME, "breadcrumb-item")
