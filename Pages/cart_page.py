from symtable import Class

from Pages.base_page import Page
from selenium.webdriver.common.by import By

class Cart(Page):
    EMPTY_TEXT_TITLE = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_empty_cart(self):
        actual_text=self.find_element(*self.EMPTY_TEXT_TITLE).text

        expected_text = 'Your cart is empty'
        assert actual_text in expected_text, f'Error. {actual_text} is not in {expected_text}'



