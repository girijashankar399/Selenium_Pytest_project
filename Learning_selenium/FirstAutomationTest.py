import time

from selenium import webdriver

# driver = webdriver.Chrome(executable_path="C:\\Browser\\chromedriver.exe")
#
# driver.get("https://www.rcvacademy.com")
# driver.maximize_window()
# print(driver.title)
# driver.close()

from selenium.webdriver.chrome.service import Service
#-------Chrome-----------
service_obj = Service("C:\\Browser\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)


#--------------FireFox------------------------
# service_obj = Service("C:\\Browser\\geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)
time.sleep(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)   #print title on terminal
print(driver.current_url)  #print url on terminal

time.sleep(5)
driver.get("https://en.wikipedia.org/wiki/Regine_Velasquez")
driver.minimize_window()

