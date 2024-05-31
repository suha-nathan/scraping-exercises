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

# disables the Chrome sandbox. bypasses OS security model. use only if content is trusted/in a controlled environment
# chrome_options.add_argument("--no-sandbox") 

 # Overcome limited resource probs
# chrome uses /dev/shm memory space for temp files such as images, JS heap and other temp data. 
# can lead to errors and crashes when running multiple instances of Chrome or in headless mode. 
# chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options) 

driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3) #waiting for button/script to load - EXPLICIT wait

print(driver.find_element(By.ID,'content').text)

driver.quit()