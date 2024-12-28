import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Browser\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.flipkart.com/")

driver.find_element(By.CLASS_NAME, value="_1TOQfO").click()





print("Hello Hi I have updated the code")
#This code Updated by user X 






time.sleep(2)
driver.find_element(By.XPATH, "//input[@class='r4vIwl BV+Dqf']").send_keys("raghav@gmail.com")

#driver.find_element(By.CLASS_NAME, value="I-qZ4M").send_keys("8982251617")

#driver.find_element(By.CLASS_NAME, value="r4vIwl").send_keys("8982251617")

time.sleep(10)
