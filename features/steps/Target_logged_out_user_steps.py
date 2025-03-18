from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target.com')
def open_targetmain_page(context):
    context.driver.get('https://www.target.com/')
    sleep(3)


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(5)

@when ('From right side navigation menu, click Sign In')
def sign_in_from_side_navigation(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()

    sleep(5)

@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    actual_text=context.driver.find_element(By.CSS_SELECTOR,"h1.styles_ndsHeading__HcGpD.styles_fontSize2__8Iex_").text
    expected_text='Sign into your Target account'
    sleep(5)

    assert actual_text in expected_text ,f'Error. {actual_text} not found in expected text {expected_text}'
    print('Test passed 🤩')



