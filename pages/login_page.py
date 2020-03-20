from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert LoginPageLocators.LOGIN_URL in login_url, "URL does not contain '/login/'"

    def should_be_login_form_on_login_page(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented on login page"

    def should_be_register_form_on_login_page(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented on login page"
