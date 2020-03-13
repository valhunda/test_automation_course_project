from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self):
        login_url=self.browser.current_url
        assert LoginPageLocators.LOGIN_URL in login_url, "URL does not contain '/login/'"

    def should_be_elements_on_login_page(self):
        self.should_be_an_element(LoginPageLocators.LOGIN_FORM, "Login form is not presented")
        self.should_be_an_element(LoginPageLocators.REGISTER_FORM, "Register form is not presented")

