from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep



class SearchResultsPage(Page):
    SEARCH_RESULT_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CART = (By.XPATH, "//button[text()='Add to cart']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[class*='ModalDrawer'] [class*='styles_fontSize4__FN7fp']")
    ADD_TO_CART_SIDE_BTN = (By.CSS_SELECTOR, "[class*='BaseModalDrawer'] [id*='addToCartButton']")
    VIEW_CART_AND_CHECKOUT = (By.CSS_SELECTOR, "[href='/cart']")
    ADDED_TO_CART_TEXT=(By.CSS_SELECTOR, "[data-test='modal-drawer-heading'] [class*=text]")

    # //span[contains(@class, 'h-text-bs')]

    def verify_search_results(self,expected_result):
        # actual_text = self.find_element(*self.SEARCH_RESULT_TEXT).text
        # assert actual_text in expected_result, f'error: {actual_text} does not match with  {expected_result}'
        self.verify_partial_text(expected_result, *self.SEARCH_RESULT_TEXT)
        sleep(10)

    def verify_search_results_url(self,expected_partial_url):
        self.verify_partial_url(expected_partial_url)

    def click_product_add_to_cart_btn(self):
        self.wait_until_clickable_click(*self.ADD_TO_CART)

    def store_product_name(self):
        product_name=self.wait_until_visible(*self.SIDE_NAV_PRODUCT_NAME)
        print(product_name)
        return product_name

    def click_add_to_cart_from_side_navigation(self):
        self.wait_until_clickable_click(*self.ADD_TO_CART_SIDE_BTN)

    def verify_added_to_cart_msg(self):
        self.wait_until_visible(*self.ADDED_TO_CART_TEXT)
        self.verify_text('Added to cart',*self.ADDED_TO_CART_TEXT)




