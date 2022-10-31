"""
TODO: PRIMERO SE INSTALA SELENIUM
pip install selenium
url: https://pypi.org/project/selenium/
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

#TODO: Aqui puedes usar webdriver.Edge()
driver_google = "chromedriver.exe"
driver_path = os.path.abspath(driver_google)

print("[INFO] Ruta: ", driver_path)
driver = webdriver.Chrome(driver_path)

# Abrir una url
driver.get("https://google.com") 

#Para confirmar que si es google
assert driver.title == "Google"

# Tiempo de espera 1 segundo
driver.implicitly_wait(4)

#TODO: Acciones con selenium
search_selenium = driver.find_element(by=By.NAME, value="q")
button_search = driver.find_element(by=By.CLASS_NAME, value="gNO89b")
driver.implicitly_wait(5)
search_selenium.send_keys("Selenium")
button_search.click()

#TODO: Traer un valor de un campo
search_selenium = driver.find_element(by=By.NAME, value="q")
assert search_selenium.get_attribute("value") == "Selenium"

#Cerrar el navegador
driver.quit()
