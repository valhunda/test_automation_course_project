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

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRMATION_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)
        registration_submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        registration_submit_button.click()
