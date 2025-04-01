from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

VARIANT_IMAGE=(By.CSS_SELECTOR,"[class*='styles_variantImage']")
ACTUAL_COLOR_TEXT=(By.CSS_SELECTOR, "[aria-label*='color']")

@given('Open target product {product_id} page')
def open_target_product(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')


@then('Verify user can click through colors')
def verify_user_colors(context):
    #actual_colors_imgs=context.driver.find_elements(*VARIANT_IMAGE)
    actual_colors_imgs=context.driver.wait.until(EC.visibility_of_all_elements_located (VARIANT_IMAGE))
    print(len(actual_colors_imgs))
    actual_color_list = []
    # sleep(4)

    for actual_color in actual_colors_imgs:
        sleep(1)
        actual_color.click()
        color_text=context.driver.wait.until(EC.visibility_of_element_located(ACTUAL_COLOR_TEXT)).text
        # color_text=context.driver.find_element(*ACTUAL_COLOR_TEXT).text
        color=color_text.split('\n')
        actual_color_list.append(color[1])

    # expected_colors=['Blue Tint','Denim Blue','Marine','Raven']
    expected_colors=['black','black pu','blue','cognac','grey','red','silver','taupe']
    assert actual_color_list==expected_colors ,f'Error: The expected colors are{expected_colors} but got {actual_color_list}'

    print(actual_color_list)


# sleep(5)