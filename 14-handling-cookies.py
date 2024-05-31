import os
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#load variables from .env file
load_dotenv()

driver_path = os.getenv("DRIVER_PATH")

# Setup options to run headless
chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service(driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options) 

driver.get('http://pythonscraping.com')

driver.implicitly_wait(1)
saved_cookies = driver.get_cookies()
print(saved_cookies)

driver2 = webdriver.Chrome(service=service, options=chrome_options)
driver2.get('http://pythonscraping.com') #must load the site first before cookies are added. so that domain the cookies belong to is known
driver2.delete_all_cookies()

# second driver adds all the same cookies as the first. second webdriver is now identical to the first one and will be tracked the same way.
# if the first driver was logged into a site, the second will be as well.
for cookie in saved_cookies:
    driver2.add_cookie(cookie)
    
driver2.get('http://pythonscraping.com')
driver2.implicitly_wait(1)
print(driver2.get_cookies())