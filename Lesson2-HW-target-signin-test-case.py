from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


#get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

#create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#1. Open the target.com
driver.get('https://www.target.com/')
sleep(2)

#2. Click the signin button
driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()
sleep(10)

#3. Click SignIn from side navigation
driver.find_element(By.XPATH, "//button[@class='styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButtonPrimary__tqtKH h-margin-t-x2 h-margin-b-default']").click()
sleep(10)

#4. Verify SignIn page opened:

#“Sign into your Target account” text is shown,
actual_text=driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text
expected_text='Sign into your Target account'

assert actual_text in expected_text, f'Error. {actual_text} does not match the {expected_text}'


#SignIn button is shown
driver.find_element(By.ID, 'login').click()

print('Test case passed')