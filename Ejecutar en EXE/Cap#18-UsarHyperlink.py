from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.w3schools.com/")
time.sleep(3)
buscar_hyperlink = driver.find_element_by_link_text('Learn PHP')
buscar_hyperlink.click()
time.sleep(4)
driver.close()