import time
from selenium.webdriver.common.by import By


class TestExistence:
    def test_add_to_cart_button_existence(self, browser):
        assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
