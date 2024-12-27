import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Browser\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.jiocinema.com/")

time.sleep(3)

driver.find_element(By.XPATH, "//button[@aria-label='Cricket']").click()

time.sleep(10)

driver.close()