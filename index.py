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
bot.get("https://www.google.com/aclk?sa=l&ai=DChcSEwiHyfqGkKWKAxW4ploFHb3nKnEYABAAGgJ2dQ&co=1&ase=2&gclid=EAIaIQobChMIh8n6hpCligMVuKZaBR295ypxEAAYASAAEgLHF_D_BwE&sig=AOD64_08T32SS9CJ43d0AP7Yjm0IurV8Ig&q&nis=4&adurl&ved=2ahUKEwjXkPWGkKWKAxXFs4QIHZjjFWQQ0Qx6BAgLEAE")
#bot.get("https://www.viajesexito.com/")
time.sleep(5)
'''
popup = bot.find_element(By.XPATH, '/html/body/div/div/div/div[1]')
time.sleep(10)
popup.click()
time.sleep(10) '''

#vuelo + hotel
fligth = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]/a')
time.sleep(3)
fligth.click()
time.sleep(5)

#buscar aero
input = "José María Cordova (MDE)"
airport = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')
time.sleep(3)
airport.click()
time.sleep(5)
airport.send_keys(input)
time.sleep(5)
airport.send_keys(Keys.ENTER)
time.sleep(5)