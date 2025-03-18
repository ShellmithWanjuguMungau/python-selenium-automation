from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#Css by ID
driver.find_element(By.CSS_SELECTOR,'#twotabsearchtextbox')

#CSS by id and tag
driver.find_element(By.CSS_SELECTOR,'input#twotabsearchtextbox')

#css selectors by class
driver.find_element(By.CSS_SELECTOR,".icp-nav-flag-us")
driver.find_element(By.CSS_SELECTOR,".icp-nav-flag-us.icp-nav-flag")

#css selectors by tag & class
driver.find_element(By.CSS_SELECTOR,"span.icp-nav-flag-us.icp-nav-flag")

#css selectors by ID & Class
driver.find_element(By.CSS_SELECTOR,"input#twotabsearchtextbox.nav-input.nav-progressive-attribute")

#css selectors by attributes []
driver.find_element(By.CSS_SELECTOR,"[name='field-keywords']")
driver.find_element(By.CSS_SELECTOR,"[placeholder='Search Amazon']")
#tags and attributes
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search Amazon']")
#class & attribute
driver.find_element(By.CSS_SELECTOR,".nav-input[placeholder='Search Amazon']")

#css attributes , contains * useful for classes with long names
driver.find_element(By.CSS_SELECTOR,"[aria-label*='Amazon']")

#Note css cannot connect to tetx.



