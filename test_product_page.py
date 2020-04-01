from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
class TestAddToBasketFromProductPage:

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()

        page.should_be_elements_before_add_to_basket()

        # get price and name of product before clicking add-to-basket button,
        # because page may be changed after click

        product_name = page.get_name_of_product()
        price = page.get_price_of_product()

        page.add_to_basket()
        page.solve_quiz_and_get_code()

        page.should_be_elements_after_add_to_basket()

        product_name_in_message = page.get_name_of_product_from_message()
        price_in_message = page.get_total_cost_from_message()

        page.product_name_in_message_equivalent_added_product_name(product_name, product_name_in_message)
        page.total_cost_in_message_equivalent_price_of_product(price, price_in_message)

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.sucsess_message_should_disappeared()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
class TestCanGoToLoginPageFromProductPage:

    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
@pytest.mark.go_to_basket
class TestGoToBasketFromProductPage:
    def test_guest_should_see_basket_button_on_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_button()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()

        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_is_empty_text()
        basket_page.should_not_be_basket_items_element()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
@pytest.mark.temp_marker
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, login_page_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()

        page.should_be_elements_before_add_to_basket()

        # get price and name of product before clicking add-to-basket button,
        # because page may be changed after click

        product_name = page.get_name_of_product()
        price = page.get_price_of_product()

        page.add_to_basket()
        page.solve_quiz_and_get_code()

        page.should_be_elements_after_add_to_basket()

        product_name_in_message = page.get_name_of_product_from_message()
        price_in_message = page.get_total_cost_from_message()

        page.product_name_in_message_equivalent_added_product_name(product_name, product_name_in_message)
        page.total_cost_in_message_equivalent_price_of_product(price, price_in_message)
