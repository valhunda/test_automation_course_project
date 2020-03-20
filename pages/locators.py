from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, ".login_form")
    LOGIN_URL="/login/"
    REGISTER_FORM=(By.CSS_SELECTOR, ".register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON_SELECTOR=(By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_ELEMENT_SELECTOR=(By.CSS_SELECTOR, ".product_main h1")
    PRICE_ELEMENT_SELECTOR=(By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_ADD_TO_BASKET_MESSAGE_SELECTOR=(By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner strong")
    TOTAL_COST_OF_BASKET_MESSAGE_SELECTOR = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3)>.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner")
