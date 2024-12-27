import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Browser\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service_obj)
#driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "input[name= 'name']").send_keys("Rahul")
driver.find_element(By.ID, "exampleCheck1").click()

time.sleep(10)
#for Xpath define and CSSselector
# Xpath  ---> "//tagname[@attribute = 'value']"
#CSSselector ----> "tagname[attribute = 'value']"

driver.find_element(By.XPATH,"//input[@id='inlineRadio2']").click()   #Radio Button handle
time.sleep(3)
driver.find_element(By.XPATH, "//input[@type= 'submit']").click()
#driver.find_element(By.CLASS_NAME, "alert-success")

message = driver.find_element(By.CLASS_NAME, "alert-success").text
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Able to enter")
print(message)
assert "Success!" in message

time.sleep(8)
driver.close()
#assert "Success56" in message


