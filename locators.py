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

driver.get("https://www.google.com")

#find element by ID
driver.find_element(By.ID,'twotabsearchtextbox')
driver.find_element(By.ID,'nav-search-submit-button')

#find element by XPath
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@role='searchbox']")

#find element by XPATH multiple attributes
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon' and @role='searchbox']")
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon' and @role='searchbox'and @tabindex='0']")

#find element by XPath without a tag
driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon']") #anytag

#find element by Xpath using text
driver.find_element(By.XPATH, "//a[text()='Customer Service']")
driver.find_element(By.XPATH, '//a[text()="Today\'s Deals"]') ###ASK THIS PART
driver.find_element(By.XPATH,"//a[text()='Customer Service' and @class='nav-a']")
driver.find_element(By.XPATH,"//h2[text()='Results']")

#Contains partial text match
driver.find_element(By.XPATH, "//h2[contains(text(), 'Luxury bestsellers')])")
driver.find_element(By.XPATH, "//h2[contains (text(), 'teens')]") #partial text match




