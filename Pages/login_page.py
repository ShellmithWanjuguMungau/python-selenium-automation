from time import sleep

from Pages.base_page import Page
from selenium.webdriver.common.by import By



class LoginPage(Page):
    SIGN_IN_TEXT = (By.CSS_SELECTOR, "[class*='Heading'] ,h1")
    USERNAME_FIELD=(By.ID, "username")
    CONTINUE_BTN = (By.ID, "login")
    TERMS_AND_CONDITION = (By.CSS_SELECTOR, "[href*='terms-conditions']")
    TERMS_AND_CONDITION_TEXT=(By.CSS_SELECTOR, "[data-test='page-title']")




    def verify_login_page_opens(self):
        self.wait_until_visible(*self.SIGN_IN_TEXT)
        self.verify_text("Sign in or create account",*self.SIGN_IN_TEXT)

    def open_sign_in(self):
        self.open_url('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_request_username')

    def enter_test_email(self):
        self.input_text('testshelly29@gmail.com',*self.USERNAME_FIELD)

    def click_continue_to_the_signin_page(self):
       self.click(*self.CONTINUE_BTN)

    def click_terms_and_conditions_link(self):
       sleep(3)
       self.click(*self.TERMS_AND_CONDITION)

    def verify_terms_and_conditions_page(self):
       self.verify_text("Terms & Conditions",*self.TERMS_AND_CONDITION_TEXT)

