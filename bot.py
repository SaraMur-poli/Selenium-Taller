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

try:

    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#\\39 9b8a2c4-84a1-445d-89e3-c7c1ca9a7f65 > div > iframe"))
    )
    driver.switch_to.frame(iframe) 
    print("Switch to the Pop-up iframe")

    closeButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "bhr-ip__c__close"))
    )
    closeButton.click()
    print("Pop-up closed successfully")

    driver.switch_to.default_content()

    time.sleep(3) 

    fligth = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="paquetesTooltips"]/a'))
    )
    fligth.click()
    print("Click made in flight+hotel")

    time.sleep(3) 

    fligthOriginText = "José María Cordova"
    pyperclip.copy(fligthOriginText)  

    fligthOrigin = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="CityPredictiveFrom_netactica_airhotel"]'))
    )
    fligthOrigin.click()  

    time.sleep(3) 

    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    print("Pasted text  y enter pressed in the city of origin")

    time.sleep(3) 

    fligthArrivalText = "(CUN-Aeropuerto Internacional de Cancún)"
    pyperclip.copy(fligthArrivalText) 

    fligthArrival = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="CityPredictiveTo_netactica_airhotel"]'))
    )
    fligthArrival.click()  

    time.sleep(3) 

    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    print("Pasted text and click on the destination city")

    time.sleep(3) 

    xpath_airport = "//li[@item-name='Cancún, Quintana Roo (CUN-Aeropuerto Internacional de Cancún)']"
    airport_element = driver.find_element(By.XPATH, xpath_airport)
    airport_element.click()

    time.sleep(3) 

    departureDate_js = """
        let departureDate = document.getElementById('DateFrom_netactica_airhotel');
        departureDate.value = '26-12-2024';
        departureDate.dispatchEvent(new Event('change', { bubbles: true }));
    """
    driver.execute_script(departureDate_js)
    print("Departure date: 26-12-2024")

    time.sleep(3)

    arrivalDate_js = """
        let arrivalDate = document.getElementById('DateTo_netactica_airhotel');
        arrivalDate.value = '05-01-2025';
        arrivalDate.dispatchEvent(new Event('change', { bubbles: true }));
    """
    driver.execute_script(arrivalDate_js)
    print("Return date: 05-01-2025")

    time.sleep(5)
    addRoom_js = """
        let button = document.getElementById('btbAddRoomtwopaquetes');
        button.click();
    """
    time.sleep(5)
    driver.execute_script(addRoom_js)
    print("A second room was added")

    time.sleep(5)

    room1_js = """
        let room1 = document.querySelector('#ddlAirHotelNumberAdults');
        room1.value = '2';
        room1.dispatchEvent(new Event('change', { bubbles: true }));
    """
    time.sleep(3)
    driver.execute_script(room1_js)
    print("First room configured for 2 people")

    room2_js = """
        let room2 = document.getElementById('ddlAirHotelNumberAdultsDos');
        room2.value = '3';
        room2.dispatchEvent(new Event('change', { bubbles: true }));
    """
    driver.execute_script(room2_js)
    print("Second room configured for 3 people")
    time.sleep(5)


    searchButton_js = """
    let searchButton = document.getElementById('sbm_netactica_airhotel');
    searchButton.click();
    """
    driver.execute_script(searchButton_js)
    print("Click on the search button")

except Exception as e:
    print(f"Error filling in the fields: {e}")