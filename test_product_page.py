from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import pytest


# import time

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    page.should_be_elements_before_add_to_basket()

    product_name = page.get_name_of_product()
    price = page.get_price_of_product()

    page.add_to_basket()
    page.solve_quiz_and_get_code()

    # wait after alert  for first message visibility (for firefox)
    page.wait_for_elements_after_add_to_basket_visibility()

    page.should_be_elements_after_add_to_basket()

    product_name_in_message = page.get_name_of_product_from_message()
    price_in_message = page.get_total_cost_from_message()

    # print(product_name)
    # print(price)
    # print(product_name_in_message)
    # print(price_in_message)
    # print(link)

    page.product_name_in_message_equivalent_added_product_name(product_name, product_name_in_message)
    page.total_cost_in_message_equivalent_price_of_product(price, price_in_message)
