from Pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIDE_NAV_SIGNIN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")


    def search(self,search_word):
        self.input_text(search_word, *self.SEARCH_FIELD )
        self.click(*self.SEARCH_BTN)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def click_signin(self):
        self.click(*self.SIGN_IN)

    def click_side_drawer_signin(self):
       self.wait_until_clickable_click(*self.SIDE_NAV_SIGNIN_BTN)



