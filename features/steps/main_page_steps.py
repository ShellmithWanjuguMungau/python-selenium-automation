from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

#variables
SEARCH_FIELD=(By.ID, 'search')
SEARCH_BTN=(By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON=(By.CSS_SELECTOR,"[data-test='@web/CartLink']")
HEADER_LINKS=(By.CSS_SELECTOR,"[data-test*='@web/GlobalHeader/UtilityHeader']")
ITEM_LINK=(By.CSS_SELECTOR,"[data-test='item-link']")
SIGN_IN=(By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
SIDE_NAV_SIGNIN_BTN=(By.CSS_SELECTOR, "[data-test='accountNav-signIn']")



@given('open target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when ('click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()


@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(5)

@when('Click Sign In')
def click_sign_in(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN)).click()


@when ('From right side navigation menu, click Sign In')
def sign_in_from_side_navigation(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_SIGNIN_BTN) ,message='element not clickable').click()


@then('Verify {link_count} header links are shown')
def verify_6_header_links(context, link_count):
    link_count=int(link_count)
    links=context.driver.find_elements(*HEADER_LINKS)
    assert len(links)== link_count ,f'Expected {link_count} links but got {len(links)}'
    print(links)

