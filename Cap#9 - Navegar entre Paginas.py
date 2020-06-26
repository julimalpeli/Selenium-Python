#https://www.youtube.com/watch?v=ha= "C:\Program Files\chromedriver.exe"a4uWun2Sg&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=10
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files\chromedriver.exe"

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(PATH)

	def test_pagina_siguiente_anterior(self):
		driver = self.driver
		driver.get("http://www.gmail.com")
		time.sleep(2)
		driver.get("http://www.google.com")
		time.sleep(2)
		driver.get("http://www.youtube.com")
		time.sleep(2)
		driver.back()
		time.sleep(2)
		driver.forward()
		time.sleep(2)
if __name__ == '__main__':
	unittest.main()
