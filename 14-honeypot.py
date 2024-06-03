import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

#load variables from .env file
load_dotenv()

driver_path = os.getenv("DRIVER_PATH")

# Setup options to run headless
chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service(driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options) 

driver.get('http://pythonscraping.com/pages/itsatrap.html')
links = driver.find_elements(By.TAG_NAME,'a')
for link in links:
    if not link.is_displayed():
        print('The link {} is a trap'.format(link.get_attribute('href')))

fields = driver.find_elements(By.TAG_NAME,'input')
for field in fields:
    if not field.is_displayed():
        print('Do not change value of {}'.format(field.get_attribute('name')))