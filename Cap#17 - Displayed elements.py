#https://www.youtube.com/watch?v=xYN4Ts6CRjQ&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=19
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com")
displayelement = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[2]")
print(displayelement.is_displayed())#retorna true or false si cargo el elemento
print(displayelement.is_enabled())#retorna true o false si el elemento esta disponible

driver.close()