from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep



class SearchResultsPage(Page):
    SEARCH_RESULT_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']//span[contains(@class, 'h-text-bs')]")

    def verify_search_results(self,expected_result):
        actual_text = self.find_element(*self.SEARCH_RESULT_TEXT).text
        # assert 'tea' in actual_text, f'Error. Text tea not in {actual_text}'
        assert actual_text in expected_result, f'error: {actual_text} does not match with  {expected_result}'
        sleep(10)
