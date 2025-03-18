from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#define steps
@given('Open Jumia main page')
def open_jumia_page(context):
    context.driver.get('https://jumia.com/')
    sleep(1)


@given('Close newsletter popup')
def close_popup(context):
    context.driver.find_element(By.XPATH, "//button[@aria-label='newsletter_popup_close-cta']").click()
    sleep(3)

@when('Search for books')
def search_books(context):
    # #find  the search bar element by ID
    context.driver.find_element(By.ID, 'fi-q').send_keys('books')
    sleep(3)
    # find the search button element by XPATH
    context.driver.find_element(By.XPATH, "//button[@class='btn _prim _md -mls -fsh0']").click()
    sleep(5)

@then('Verify correct results shown')
def verify_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//p[contains(text(),'products found')]").text
    expected_text = '254123 products found'
    print(actual_text)
    sleep(3)
    assert expected_text in actual_text, f'Error. Text:{expected_text} not in {actual_text}'
    print('Test passed 🤩')


