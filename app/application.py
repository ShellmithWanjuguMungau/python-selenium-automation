from Pages.base_page import Page
from Pages.cart_page import Cart
from Pages.header import Header
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.search_results_page import SearchResultsPage

#umbrella class has links to all pages
class Application:
    def __init__(self,driver):
        self.driver = driver
        self.base_page = Page(driver)
        self.cart_page = Cart(driver)
        self.header = Header(driver)
        self.login_page = LoginPage(driver)
        self.main_page= MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)