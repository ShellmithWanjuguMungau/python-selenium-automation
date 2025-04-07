from Pages.base_page import Page
from selenium.webdriver.common.by import By



class LoginPage(Page):
    SIGN_IN_TEXT = (By.CSS_SELECTOR, "[class*='Heading'] ,h1")

    def verify_login_page_opens(self):
        self.wait_until_visible(*self.SIGN_IN_TEXT)
        self.verify_text("Sign in or create account",*self.SIGN_IN_TEXT)
