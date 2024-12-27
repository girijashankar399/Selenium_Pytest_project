import time

from selenium import webdriver
from selenium.webdriver.chrome.service import   Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_Obj = Service("C:\\Browser\\chromedriver.exe")
driver = webdriver.Chrome(service=service_Obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


#Static Drop Down
drop_down = Select(driver.find_element(By.ID, "dropdown-class-example"))
#drop_down.select_by_index(0)
#drop_down.select_by_visible_text("Option3")
drop_down.select_by_value(2)


time.sleep(5)




driver.close()