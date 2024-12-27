from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Browser\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service_obj)
###########Child Window handling ################

# driver.get("https://the-internet.herokuapp.com/windows")
# driver.find_element(By.LINK_TEXT,"Click Here").click()
#
# WindowOpened = driver.window_handles
# driver.switch_to.window(WindowOpened[2])
#
# print(driver.find_element(By.TAG_NAME,"h3").text)
# driver.switch_to.window(WindowOpened[1])
# print(driver.find_element(By.TAG_NAME,"h3").text)

#####frames Handling##################
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to Automate the frame")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
