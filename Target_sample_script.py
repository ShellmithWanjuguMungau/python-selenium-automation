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

#open the url
driver.get('https://www.jumia.co.ke/')

#close the newsletter popup
driver.find_element(By.XPATH,"//button[@aria-label='newsletter_popup_close-cta']").click()

# #find  the search bar element by ID
driver.find_element(By.ID,'fi-q').send_keys('books')
sleep(3)

#find the search button element by XPATH
driver.find_element(By.XPATH, "//button[@class='btn _prim _md -mls -fsh0']").click()
sleep(5)

#verification
#confirm the number of products found
Actual_text=driver.find_element(By.XPATH, "//p[contains(text(),'products found')]").text
Expected_text='254123 products found'
print(Actual_text)
sleep(3)

assert Expected_text in Actual_text ,f'Error. Text:{Expected_text} not in {Actual_text}'
print('Test passed 🤩')
# driver.find_element(By.XPATH, "//a[@href='/phones-tablets/']").click()
# sleep(3)

#verification
# driver.find_element(By.XPATH, '//a[text()="Phones & Tablets" and @class="cbs"]')
# print('test case passed')

#verification using an assertion
# actual_text=driver.find_element(By.XPATH, '//a[text()="Phones & Tablets" and @class="cbs"]').text
#
# expected_text='Phoesmjg & Tabets' #made sure it fails
# assert expected_text in actual_text, f'Error. Text "{expected_text}" not found in {actual_text}'
# print('Test case passed')
#
sleep(20)







