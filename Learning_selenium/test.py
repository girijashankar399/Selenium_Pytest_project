from selenium import webdriver

from selenium.webdriver.chrome.service import Service




service_obj = Service("C:\\Browser\\chromedriver.exe")
driver_1 = webdriver.Chrome(service=service_obj)
driver_1.get("https://hi.wikipedia.org/wiki/%E0%A4%A6%E0%A4%BF%E0%A4%A8%E0%A5%87%E0%A4%B6_%E0%A4%B2%E0%A4%BE%E0%A4%B2_%E0%A4%AF%E0%A4%BE%E0%A4%A6%E0%A4%B5")
