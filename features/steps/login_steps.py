from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SIGN_IN_TEXT=(By.CSS_SELECTOR,"[class*='Heading'] ,h1")

@then('Verify "Sign in or create account" message is shown')
def verify_login_page_opens(context):

    # actual_text=context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_TEXT)).text
    # expected_text='Verify "Sign in or create account" message is shown'
    # # sleep(5)
    #
    # assert actual_text in expected_text ,f'Error. {actual_text} not found in expected text {expected_text}'

    context.app.login_page.verify_login_page_opens()