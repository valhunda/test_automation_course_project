from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON_SELECTOR)
        add_to_basket_button.click()

    def get_name_of_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ELEMENT_SELECTOR).text

    def get_price_of_product(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_ELEMENT_SELECTOR).text

    def get_name_of_product_from_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_MESSAGE_SELECTOR).text

    def get_total_cost_from_message(self):
        return self.browser.find_element(*ProductPageLocators.TOTAL_COST_OF_BASKET_MESSAGE_SELECTOR).text

    def product_name_in_message_equivalent_added_product_name(self, name, name_in_message):
        assert name == name_in_message, f"Name of added product is '{name_in_message}', should be '{name}'"

    def total_cost_in_message_equivalent_price_of_product(self, price, price_in_message):
        assert price == price_in_message, f"Cost of basket is '{price_in_message}', should be '{price}'"

    def wait_for_elements_after_add_to_basket_visibility(self):
        self.WebDriverWait(self.browser, 30).until(
            self.EC.visibility_of_element_located(ProductPageLocators.PRODUCT_ADD_TO_BASKET_MESSAGE_SELECTOR))

    def should_be_elements_before_add_to_basket(self):
        self.should_be_an_element(ProductPageLocators.PRODUCT_NAME_ELEMENT_SELECTOR, "Name of product is not presented")
        self.should_be_an_element(ProductPageLocators.PRICE_ELEMENT_SELECTOR, "Price of product is not presented")
        self.should_be_an_element(ProductPageLocators.ADD_TO_BASKET_BUTTON_SELECTOR,
                                  "Add-to-basket button is not presented")

    def should_be_elements_after_add_to_basket(self):
        self.should_be_an_element(ProductPageLocators.PRODUCT_ADD_TO_BASKET_MESSAGE_SELECTOR,
                                  "Product-add-to-basket message is not presented")
        self.should_be_an_element(ProductPageLocators.TOTAL_COST_OF_BASKET_MESSAGE_SELECTOR,
                                  "Total-cost-of-basket message is not presented")
