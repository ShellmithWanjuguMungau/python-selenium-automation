from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SIGN_IN_TEXT=(By.CSS_SELECTOR,"[class*='Heading'] ,h1")

@then('Verify Sign In form opened')
def verify_sign_in_form(context):

    actual_text=context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_TEXT)).text
    expected_text='Sign into your Target account'
    # sleep(5)

    assert actual_text in expected_text ,f'Error. {actual_text} not found in expected text {expected_text}'