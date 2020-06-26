import unittest
from selenium import webdriver
import HtmlTestRunner
import time

PATH = "C:\Program Files\chromedriver.exe"

class usando_unittest(unittest.TestCase):
	
	def setUp(self):
	    self.driver = webdriver.Chrome(PATH)

	def test_assertEquial (self):
		driver = self.driver
		driver.get("https://www.google.com")
		titulo=driver.title
		time.sleep(2)
		self.assertEqual ("Googlerrrr", titulo)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = 'Result of Automation Test Suit'))