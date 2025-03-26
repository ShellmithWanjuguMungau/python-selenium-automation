from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

from selenium.webdriver.support.expected_conditions import element_to_be_clickable

ADD_TO_CART=(By.XPATH, "//button[text()='Add to cart']")
# ADD_TO_CART=([id*='addToCartButton'])
ADD_TO_CART_SIDE_BTN=(By.CSS_SELECTOR,".styles_ndsBaseButton__W8Gl7.styles_mdGap__9J0yq.styles_fullWidth__3XX6f.styles_ndsButtonPrimary__tqtKH")
#ADD_TO_CART_SIDE_BTN=("[class*='BaseModalDrawer'] [id*='addToCartButton']")
VIEW_CART_AND_CHECKOUT=(By.CSS_SELECTOR, "[href='/cart']")
SEARCH_RESULT_TEXT=(By.XPATH, "//div[@data-test='lp--resultsCount']")
SIDE_NAV_PRODUCT_NAME=(By.CSS_SELECTOR,"[class*='ModalDrawer'] [class*='styles_fontSize4__FN7fp']")
SPONSORED_TEXT=(By.CSS_SELECTOR,"[data-test='sponsored-text']")

@when('click on add to cart button')
def click_add_to_cart(context):
    add_to_cart_button=context.driver.wait.until(EC.element_to_be_clickable (ADD_TO_CART), message="Add to cart button is not visible")

    #scrolls the page to center.
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)

    add_to_cart_button.click()
    # # c [1].click() will clock 2nd add to cart button

@when('Store product name')
def store_product_name(context):
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME), message='element not found')

    context.product_name =context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'product name: {context.product_name}')


@when('click add to cart from side navigation')
def click_add_to_cart_from_navigation(context):
    button= context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_SIDE_BTN),message='element is not clickable')
    button.click()
    # context.driver.find_element(*ADD_TO_CART_SIDE_BTN).click()

@when('click on view cart and checkout')
def close_side_navigation(context):
    context.driver.find_element(*VIEW_CART_AND_CHECKOUT).click()


@then('Verify correct search results for {expected_text}')
def verify_search_results(context, expected_text):
    actual_text = (context.driver.wait.until(EC.visibility_of_element_located(SEARCH_RESULT_TEXT),message='element not available')).text
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
    # sleep(30)

