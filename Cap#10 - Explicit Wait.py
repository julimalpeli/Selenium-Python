#https://www.youtube.com/watch?v=SNIeI3XLzxU&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=11
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files\chromedriver.exe"

class usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(PATH)

	def test_usando_explicit_wait(self):
		driver = self.driver
		driver.get("http://www.google.com")
		try:
			element = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.NAME,"q"))
				)
		finally:
			driver.quit()

if __name__ == '__main__':
	unittest.main()
