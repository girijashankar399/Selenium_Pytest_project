from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Browser\\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)

# chrome_option = webdriver.ChromeOptions()   ### line no 11 to 13 are used to run the chrome browser in hidden Mode
# chrome_option.add_argument("headless")
# driver = webdriver.Chrome(service=service_obj, options=chrome_option)

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")


# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# driver.get_screenshot_as_file("screenshot_1.png")


####################2nd##################################### sorting list

### logic to automate

## click on column
##collect all veggie name --> veggie list
## sort the list ---> sorted_list
### veggie List == sorted_list
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,'//span[text()="Veg/fruit name"]').click()
WebVegList = []
veggie_list = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggie_list:
    WebVegList.append(ele.text)

browserSortedList = WebVegList.copy()
WebVegList.sort()

assert  WebVegList == browserSortedList

