#https://www.youtube.com/watch?v=Gm38NKZ_v7Y&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=18
import unittest
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

PATH = "C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com")
time.sleep(3)
element = driver.find_element_by_link_text("Privacidad")
hover = ActionChains(driver).move_to_element(element)
hover.perform()