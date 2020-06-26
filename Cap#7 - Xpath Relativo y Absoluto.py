#https://www.youtube.com/watch?v=FBCWmE-ILhQ&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=7
#xPath es una estructura de direcciones similar al dico c, esto es una estructura xml
#Existen dos tipos: 
#xPath Relativo - Tiene ventaja sobre el absoluto, parte de un nodo especifico, xpad del buscardor de google: //*[@id="fakebox-input"]
#xPAth Absoluto - Es toda la ruta, y busca el ultimo nodo. EL relavito busca el nodo en cualquier lugar

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files\chromedriver.exe"

class usando_unittest(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Chrome(PATH)

	def test_buscar_por_xpath(self):
		driver = self.driver
		driver.get("http://www.google.com")
		time.sleep(3)
		buscar_por_xpath = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
		time.sleep(3)
		buscar_por_xpath.send_keys("selenium", Keys.ARROW_DOWN)
		time.sleep(4)

	def tearDown(self):
		self.driver.close

if __name__ == '__main__':
	unittest.main()
