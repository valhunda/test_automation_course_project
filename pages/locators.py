from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn-default:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    LOGIN_URL = "/login/"
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='registration-password1']")
    CONFIRMATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON_SELECTOR = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_ELEMENT_SELECTOR = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_ELEMENT_SELECTOR = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_ADD_TO_BASKET_MESSAGE_SELECTOR = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner strong")
    TOTAL_COST_OF_BASKET_MESSAGE_SELECTOR = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3)>.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner")


class BasketPageLocators:
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner")
    BASKET_ITEMS_ELEMENT = (By.CSS_SELECTOR, ".basket-items")
