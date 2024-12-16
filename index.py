from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time 

service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service = service)
bot.maximize_window()
time.sleep(1)
bot.get("https://www.viajesexito.com/")
time.sleep(10)

popup = bot.find_element(By.XPATH, '/html/body/div/div/div/div[1]/svg/path')
time.sleep(10)
popup.click()
time.sleep(10)

#vuelo + hotel
fligth = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]/a')
time.sleep(3)
fligth.click()
time.sleep(5)

