from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("driver/chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument("--incognito") 

bot = webdriver.Chrome(service=service, options=chrome_options)
bot.maximize_window()

bot.get("https://www.viajesexito.com/")
time.sleep(5)


try:
    iframe = WebDriverWait(bot, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#e9fb4a0d-0e45-4a5f-996c-fe6e4c4e72d5 > div > iframe"))
    )
    bot.switch_to.frame(iframe)

    closeButton = WebDriverWait(bot, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "bhr-ip__c__close"))
    )
    closeButton.click()
    print("Anuncio cerrado con éxito")

    bot.switch_to.default_content()

except Exception as e:
    print("Error al cerrar el anuncio: {e}")

fligth = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]/a')
time.sleep(3)
fligth.click()
time.sleep(5)

input = "José María Cordova (MDE)"
airport = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')
time.sleep(10)
airport.click()
airport.send_keys(input)
print(airport.get_attribute('value'))
time.sleep(10)
#airport.send_keys(Keys.DOWN)
#airport.send_keys(Keys.ENTER) 
#airport.send_keys(Keys.ENTER)
#time.sleep(10)