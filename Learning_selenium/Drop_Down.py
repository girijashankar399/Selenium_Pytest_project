import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Browser\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service_obj)
#driver = webdriver.Chrome(service=service_obj)




# ###########Static Drop down##############################
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
# #dropdown.select_by_index(1)  #select by index
# dropdown.select_by_visible_text("Female")  #Select by visible text



###############Dynamic dropdown############
# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# driver.find_element(By.ID, "autosuggest").send_keys("ind")
# time.sleep(3)
# countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
# print(countries)
# print(len(countries))
# for country in countries:
#     if country.text == "India":
#         country.click()
#         break
# #print(driver.find_element(By.ID,"autosuggest").text)
# #print(driver.find_element(By.ID,"autosuggest").get_attribute("value")) # this is for checking the right countty name choosen or not
# assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"  #test case for selected expected result



#Goolge Dymanic Drop down
driver.get("https://www.google.com/")
driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("indi")
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR, "div[role='presentation'] span")
print(countries)
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
#print(driver.find_element(By.ID,"autosuggest").text)
#print(driver.find_element(By.ID,"autosuggest").get_attribute("value")) # this is for checking the right countty name choosen or not
#assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"  #test case for selected expected result








# Handing the checkBox Dynamically

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# #driver.find_element(By.XPATH,'//input[@value="option2"]').click()
# checkboxs = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
# print(len(checkboxs))
#
# for checkbox in checkboxs:
#     if checkbox.get_attribute("value") == "option2":
#         checkbox.click()
#         assert checkbox.is_selected()
#         break


#radio buttton selection automation:

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# radiobutton = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
# radiobutton[2].click()
# assert radiobutton[2].is_selected()
#
# assert driver.find_element(By.ID,"displayed-text").is_displayed()
# driver.find_element(By.ID, "hide-textbox").click()
# assert not driver.find_element(By.ID,"displayed-text").is_displayed()

#Handing Java script Alert
#
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.CSS_SELECTOR,"#name").send_keys("raghav")
# driver.find_element(By.ID,"alertbtn").click()
# alert = driver.switch_to.alert
# Alert_text = alert.text
#
# assert "raghav" in Alert_text
# time.sleep(5)
# alert.accept()




