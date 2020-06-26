from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://juridicosqa.afip.gob.ar/atenea/Ingreso_Sistemas_LDAP_2.2/InicioBD.aspx?idUser=20319407368")
time.sleep(2)
confiAvan= driver.find_element_by_id("details-button")
confiAvan.click()
link=driver.find_element_by_id("proceed-link")
link.click()
sucu= driver.find_element_by_id("ctl00_VentanaPrincipal_lugarAccesoIng")
usuario.send_keys("AABE0A0000")
time.sleep(3)
clave = driver.find_element_by_id("password")
clave.send_keys("jmalpeli3194")
time.sleep(2)
