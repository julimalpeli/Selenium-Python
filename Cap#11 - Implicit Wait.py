#https://www.youtube.com/watch?v=_h8xeeg4uyg&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=12
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files\chromedriver.exe"

class usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(PATH)

	def test_usando_implicit_wait(self):
		driver = self.driver
		driver.implicitly_wait(5) #segundos
		driver.get("http://www.google.com")
		myDynamicElement = driver.find_elements_by_name("q")

if __name__ == '__main__':
	unittest.main()
