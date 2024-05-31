import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service

#load variables from .env file
load_dotenv()

driver_path = os.getenv("DRIVER_PATH")
service = Service(driver_path)

driver = webdriver.Chrome(service=service) 

driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!

search_box = driver.find_element('name', 'q')
search_box.send_keys('ChromeDriver')
search_box.submit()

time.sleep(5) # Let the user actually see something!


driver.quit()