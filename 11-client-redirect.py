import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def waitForLoad(driver):
    elem = driver.find_element(By.TAG_NAME,"html")
    count = 0
    exit_flag = False
    while True:
        count += 1
        if count > 20:
            print('Timing out after 10 seconds and returning')
            return    
        else:    
            time.sleep(.2)
            try:
                elem == driver.find_element(By.TAG_NAME,"html")
            except StaleElementReferenceException:
                return

#load variables from .env file
load_dotenv()

driver_path = os.getenv("DRIVER_PATH")

# Setup options to run headless
chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service(driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options) 

driver.get('http://pythonscraping.com/pages/javascript/redirectDemo1.html')

waitForLoad(driver)

print(driver.page_source)

driver.quit()