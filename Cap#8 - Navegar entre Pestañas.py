#https://www.youtube.com/watch?v=qVVmqHtu66c&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=9
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files\chromedriver.exe"

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(PATH)

	def test_pestañas(self):
		driver = self.driver
		driver.get("http://www.google.com")
		time.sleep(3)
		driver.execute_script("window.open('');")
		time.sleep(2)
		driver.switch_to_window(driver.window_handles[1])
		driver.get("http://stackoverflow.com")
		time.sleep(2)
		driver.switch_to_window(driver.window_handles[0])
		time.sleep(1)
		abrir_nueva = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
		abrir_nueva.send_keys("programar en python")
		abrir_nueva.send_keys(Keys.RETURN)
		time.sleep(2)
if __name__ == '__main__':
	unittest.main()