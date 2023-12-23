from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from twilio.rest import Client

account_sid = 'AC9cf1494d172ae56e599c7d228d14fcd6'
auth_token = 'e23a2d1ec4c92c30dd178c7d6ccb8d2a'
twilio_phone_number = '+18336693441'
your_phone_number = '+19084056267'
client = Client(account_sid, auth_token)

driver = webdriver.Chrome()
driver.get("https://mcat.aamc.org/mrs/#/dashboard/16023856")
time.sleep(60)
#login and go go to exam appointments page within a minute 

while True:
    date_element = driver.find_element(By.ID, 'preferredDateHidden')
    date='01/18/2024'
    driver.execute_script("arguments[0].setAttribute('value',arguments[1])", date_element, date)
    time.sleep(5)
    
    search_button = driver.find_element(By.ID, 'addressSearch')
    search_button.click()
    time.sleep(10)
    
    input_elements = driver.find_elements(By.TAG_NAME, 'input')
    for element in input_elements:
        value_att = element.get_attribute('value')
        if value_att is not None and value_att == '8:00 AM':
            print(f"MCAT Exam Appointment Found on {date}!")
            message = client.messages.create(
                from_=twilio_phone_number,
                body=f"MCAT Exam Appointment Found on {date}!",
                to=your_phone_number
            )
            print(message.sid)
    time.sleep(60)
    driver.refresh()

driver.quit()
