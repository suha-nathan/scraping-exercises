import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  

#load variables from .env file
load_dotenv()

driver_path = os.getenv("DRIVER_PATH")

# Setup options to run headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox") # bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage") # Overcome limited resource probs

service = Service(driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options) 

driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)

print(driver.find_element(By.ID,'content').text)

time.sleep(3)

driver.quit()