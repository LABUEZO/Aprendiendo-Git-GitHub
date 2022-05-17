import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://www.upo.es/biblioteca/servicios/pubdig/propiedadintelectual/tutoriales/derechos_autor/htm_03.htm")
driver.maximize_window()
#driver.implicitly_wait(10)
t=3

links=driver.find_elements(By.TAG_NAME,"a")
print("El número de links que hay en la página es: ", len(links))

for num in links:
    print(num.text)

driver.find_element_by_link_text("Introducción").click()

time.sleep(t)
driver.close()
