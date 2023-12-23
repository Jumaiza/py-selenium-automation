from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import os
import time
import json

chrome_profile_path = r"C:\Users\Zaid\AppData\Local\Google\Chrome\User Data"

def get_private_party_value(vin):
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=" + chrome_profile_path)
    chrome_options.add_argument(r'--profile-directory=Profile 24')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://members.manheim.com/members/results#/results?filters=ShowOnlyWorkbookListingss:T")
    time.sleep(5)
    div_elements = driver.find_elements(By.TAG_NAME, 'div')
    for element in div_elements:
        if element.get_attribute('data-test-id') == "listings":
            listings = element.find_elements(By.XPATH,"./*")
            for listing in listings:
                if listing.get_attribute('data-vin') == vin:
                    jsonData_element = listing.find_elements(By.TAG_NAME,"div")[0]
                    vehicleData = json.loads(jsonData_element.get_attribute('textContent'))
                    time.sleep(2)
                    
                    driver.get("https://www.kbb.com/whats-my-car-worth/")
                    driver.delete_all_cookies()
                    time.sleep(1)
                    driver.refresh()
                    time.sleep(3)

                    vin_input_div = driver.find_element(By.ID, 'vinNumberInput')
                    vin_input_element = vin_input_div.find_elements(By.XPATH,"./*")[0].find_elements(By.XPATH,"./*")[0]
                    vin_input_element.send_keys(vehicleData['vin'])
                    time.sleep(2)

                    button_elements = driver.find_elements(By.TAG_NAME, 'button')
                    for button in button_elements:
                        if button.get_attribute('data-testid') == "vinSubmitBtn":
                            button.click()
                            break
                    time.sleep(10)


    time.sleep(10)
    
    driver.quit()

    # driver.get("https://www.kbb.com/whats-my-car-worth/")

    # vin_input_div = driver.find_element(By.ID, 'vinNumberInput')
    # vin_input_element = vin_input_div.find_elements(By.XPATH,"./*")[0].find_elements(By.XPATH,"./*")[0]
    # vin_input_element.send_keys(vin)
    # time.sleep(2)

    # button_element = driver.find_elements(By.TAG_NAME, 'button')[0]
    # button_element.click()
    # time.sleep(2)

    print(f"Private party value for VIN {vin}: $20,000\n")

# Main loop
while True:

    vin_input = input("Enter VIN (type 'stop' to end): ")
    if vin_input.lower() == 'stop':
        print("Program terminated.")
        break

    private_party_value = get_private_party_value(vin_input)

# driver = webdriver.Chrome()
# driver.get("https://generalssb-prod.ec.njit.edu/BannerExtensibility/customPage/page/stuRegCrseSched")
# time.sleep(3)

