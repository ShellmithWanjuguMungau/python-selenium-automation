from time import sleep
from behave import *

@given ('Open Target App page')
def open_target_app_page(context):
    context.app.target_app_page.open_target_app()

@given ('Store original window')
def store_original_window(context):
    context.original_window=context.app.base_page.current_window_handle()
    print("Original window is:", context.original_window)

@when ('Click Privacy Policy link')
def click_privacy_policy_link(context):
    context.app.target_app_page.click_privacy_policy_link()

@when('Switch to new window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()

@then('Verify Privacy Policy page opened')
def verify_privacy_policy_opened(context):
    context.app.target_app_page.verify_privacy_policy_opened()

@then('Close current page')
def close_current_page(context):
    context.app.base_page.close()

@then('return to original window')
def return_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)



