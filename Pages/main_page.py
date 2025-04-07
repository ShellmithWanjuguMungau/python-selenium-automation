from Pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')

    def open_main_page(self):
        self.open_url('https://www.target.com/')
        self.wait_until_clickable(*self.SEARCH_FIELD)



