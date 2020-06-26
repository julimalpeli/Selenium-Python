from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

sleep(5)

driver.quit()