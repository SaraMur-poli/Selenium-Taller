import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_argument("--start-maximized")  
chrome_options.add_argument("-5-incognito")
chrome_options.add_argument("--ignore-certificate-errors")  
chrome_options.add_argument("--disable-logging")  
chrome_options.add_argument("--log-level=3")

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service = service, options = chrome_options)

url = "https://www.viajesexito.com"
driver.get(url)

print(f"Open page: {driver.title}")