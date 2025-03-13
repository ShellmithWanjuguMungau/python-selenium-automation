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
driver.get('https://target.com/')

#search for items on target
driver.find_element(By.XPATH, "//input [@aria-label='What can we help you find? suggestions appear below']").send_keys('perfume')
sleep(3)

#click the search button
driver.find_element(By.XPATH, "//button[@aria-label='search']").click()
sleep(5)

#verification
Actual_text=driver.find_element(By.XPATH,"//span[@class='h-text-bs h-display-flex h-flex-align-center h-text-grayDark h-margin-l-x2']").text
# print(Actual_text)
Expected_text='for “perfume”'

assert Actual_text in Expected_text, f'Error. {Expected_text}  not found in {Actual_text} '

print('Testcase passed 😊')


