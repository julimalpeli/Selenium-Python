#https://www.youtube.com/watch?v=XN6FwRV6FvE&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=14
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files\chromedriver.exe"

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(PATH)

	def test_usando_toggle(self):
		driver = self.driver
		driver.get("https://juridicosqa.afip.gob.ar/atenea/Ingreso_Sistemas_LDAP_2.2/InicioBD.aspx?idUser=20319407368")
		time.sleep(3)
		toggle = driver.find_element_by_xpath("//*[@id='details-button']")
		toggle.click()
		toggle = driver.find_element_by_xpath("//*[@id='ctl00_VentanaPrincipal_lugarAccesoIng']")
		toggle.click()
		time.sleep(2)
		toggle.click()
		time.sleep(3)
	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()