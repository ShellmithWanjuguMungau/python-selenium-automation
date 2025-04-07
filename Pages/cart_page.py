from symtable import Class

from Pages.base_page import Page
from Pages.search_results_page import SearchResultsPage
from selenium.webdriver.common.by import By

class Cart(Page):
    EMPTY_TEXT_TITLE = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_empty_cart(self):
        # actual_text=self.find_element(*self.EMPTY_TEXT_TITLE).text
        #
        # expected_text = 'Your cart is empty'
        # assert actual_text in expected_text, f'Error. {actual_text} is not in {expected_text}'
        self.verify_text('Your cart is empty', *self.EMPTY_TEXT_TITLE)

    def verify_cart_page_opens(self):
        self.verify_url(f'{self.base_url}cart')

    def verify_correct_product_name(self):
        self.wait_until_visible(*self,*self.CART_ITEM_TITLE)
        expected_text=self.store_product_name()
        self.verify_text(expected_text, *self.CART_ITEM_TITLE)


