import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Browser\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service_obj)
#driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")


########Link TEXT#################
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("hello@gmail.com")
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("hello@gmail.com") # different way of writing of line 17
#driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("12345")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("12345") # CSS format for last line
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("12345")
#driver.find_element(By.CSS_SELECTOR,"button[type = 'submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
time.sleep(5)

