from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SIGN_IN_TEXT=(By.CSS_SELECTOR,"[class*='Heading'] ,h1")

# @given('Open sign in page')
# def open_sign_in_page(context):
#     context.app.login_page.open_sign_in()

@given('enter test email')
def enter_test_email(context):
    context.app.login_page.enter_test_email()

@given('click continue to the signin page')
def click_continue_to_page(context):
    context.app.login_page.click_continue_to_the_signin_page()


@when('Click on terms and conditions link')
def click_terms_and_conditions_link(context):
    context.app.login_page.click_terms_and_conditions_link()

@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.login_page.verify_terms_and_conditions_page()

@then('Verify "Sign in or create account" message is shown')
def verify_login_page_opens(context):

    # actual_text=context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_TEXT)).text
    # expected_text='Verify "Sign in or create account" message is shown'
    # # sleep(5)
    #
    # assert actual_text in expected_text ,f'Error. {actual_text} not found in expected text {expected_text}'

    context.app.login_page.verify_login_page_opens()