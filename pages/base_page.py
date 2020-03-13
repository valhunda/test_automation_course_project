from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
# import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage():

    def __init__(self, browser, url, timeout=30):
        self.browser=browser
        self.url=url
        self.browser.implicitly_wait(timeout)
        self.EC=EC
        self.WebDriverWait=WebDriverWait
        self.By=By

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        # time.sleep(60)
        # WebDriverWait(self.browser, 30).until(EC.alert_is_present())
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_an_element(self, locator, assertion_message):
        assert self.is_element_present(*locator), assertion_message

