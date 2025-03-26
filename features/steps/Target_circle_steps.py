from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CELL_ITEM=By.CSS_SELECTOR,".cell-item-content"

@given('Open target circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

@then('verify there are {cells} benefit cells')
def verify_cells(context,cells):
    cell_items=context.driver.find_elements(*CELL_ITEM)
    cells=int(cells)
    # sleep(3)
    assert len(cell_items)> cells, f'Error : Expected {cells} Cell items but got {len(cell_items)}'
    print(len(cell_items))