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

#open url
driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
sleep(20)

#Amazon link logo
driver.find_element(By.CSS_SELECTOR,'i.a-icon.a-icon-logo')

#Create account text
driver.find_element(By.CSS_SELECTOR,'h1.a-spacing-small')

#Name field
driver.find_element(By.CSS_SELECTOR,'#ap_customer_name').send_keys('cugu')

#Email field
driver.find_element(By.CSS_SELECTOR,'#ap_email').send_keys('shell@gmail.com')

#password field
driver.find_element(By.CSS_SELECTOR,'#ap_password').send_keys('1223@de')

#password requirements
driver.find_element(By.CSS_SELECTOR,'#auth-password-requirement-info')

#Re-enter password
driver.find_element(By.CSS_SELECTOR,'#ap_password_check').send_keys('1223@de')

#Create your Amazon Account button/continue button
driver.find_element(By.CSS_SELECTOR,'#continue')

#conditions of use link
driver.find_element(By.XPATH,'//a[contains(@href, "register_notification_condition_of_use")]')

#Privacy Notice link
driver.find_element(By.XPATH,'//a[contains(@href, "register_notification_privacy_notice")]')

#Signin link
driver.find_element(By.CSS_SELECTOR,'a.a-link-emphasis')

sleep(10)