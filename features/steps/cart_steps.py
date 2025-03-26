from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then

CART_ITEM_TITLE=(By.CSS_SELECTOR,"[data-test='cartItem-title']")
EMPTY_TEXT_TITLE=(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']")

@then('verify “Your cart is empty” message is shown')
def verify_your_cart_is_empty(context):
    actual_text=context.driver.wait.until(EC.visibility_of_element_located(EMPTY_TEXT_TITLE),message='text not found').text
    # actual_text=context.driver.find_element(By.CSS_SELECTOR,".styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt").text
    print(actual_text)
    expected_text='Your cart is empty'
    assert actual_text in expected_text, f'Error. {actual_text} is not in {expected_text}'
    # sleep(10)

# @then('verify {expected_product} is  added to cart')
# def verify_item_added(context,expected_product):
#     actual_text=context.driver.find_element(By.CSS_SELECTOR,"[data-test='cartItem-title']").text
#     print(actual_text)
#     # expected_text='Hefty Party On! Disposable Cups - 80ct/16oz'
#     assert actual_text in expected_product, f'Error. Text {expected_product} not in {actual_text}'
#     sleep(10)

@then('verify cart has correct product')
def verify_cart_has_item(context):
    actual_name_in_cart=context.driver.find_element(*CART_ITEM_TITLE).text
    assert context.product_name == actual_name_in_cart, \
        f'Error. {context.product_name} not in {actual_name_in_cart}'

