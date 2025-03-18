from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')
    sleep(10)

@when('click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartLink']").click()
    sleep(10)

@then('verify “Your cart is empty” message is shown')
def verify_your_cart_is_empty(context):
    actual_text=context.driver.find_element(By.CSS_SELECTOR,".styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt").text
    print(actual_text)
    expected_text='Your cart is empty'
    assert actual_text in expected_text, f'Error. {actual_text} is not in {expected_text}'
    sleep(5)
    print('Test passed 🤩')
