import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Browser\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")#return list
time.sleep(3)
count = driver.find_elements(By.XPATH, "//div[@class='products']/div")
#print(len(count))
assert len(count) > 0

for result in count:
    result.find_element(By.XPATH,"div/button").click()

product_list  = driver.find_elements(By.XPATH,"//h4[@class = 'product-name']")
list = []
for product_name in product_list:
    list.append(product_name.text)

print("List of product:", list)
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text() = 'PROCEED TO CHECKOUT']").click()
#time.sleep(5)


#sum validation
prices = driver.find_elements(By.CSS_SELECTOR,"td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
amount = float(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == amount

driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
#time.sleep(5)
#Explicit wait
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.XPATH,"//span[@class='promoInfo']").text)

#validate the amount after discount always less than total amount

Afterdiscount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert amount > Afterdiscount