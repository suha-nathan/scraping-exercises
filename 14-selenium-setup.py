from selenium import webdriver
import os
from dotenv import load_dotenv

#load variables from .env file
load_dotenv()

print(os.getenv("DRIVER_PATH"))
# Initialize the Chrome driver
driver = webdriver.Chrome(executable_path=os.getenv("DRIVER_PATH"))

# Navigate to the URL
# driver.get('https://google.com')

# It's a good practice to close the browser when done
# driver.quit()