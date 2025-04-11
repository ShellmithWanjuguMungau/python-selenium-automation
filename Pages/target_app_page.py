from selenium.webdriver.common.by import By

from Pages.base_page import Page

class TargetAppPage(Page):
    PRIVACY_POLICY_LINK=(By.CSS_SELECTOR, "[aria-label*='privacy policy']")

    def open_target_app(self):
        self.open_url("https://www.target.com/c/target-app/")

    def click_privacy_policy_link(self):
        self.click(*self.PRIVACY_POLICY_LINK)

    def verify_privacy_policy_opened(self):
        self.verify_partial_url('/target-privacy-policy')




