import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(5)
t=1

driver.find_element_by_xpath("//input[contains(@id,'firstName')]").send_keys("Luis Alberto")
driver.find_element_by_xpath("//input[contains(@id,'lastName')]").send_keys("Buezo")
driver.find_element_by_xpath("//input[contains(@id,'userEmail')]").send_keys("luis_buezo@yahoo.com.ar")
driver.find_element_by_xpath("//label[@for='gender-radio-1'][contains(.,'Male')]").click()
driver.find_element_by_xpath("//input[contains(@id,'userNumber')]").send_keys("43939931")

driver.execute_script("window.scrollTo(0,300)")
time.sleep(t)


try:
    btn_uno = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='hobbies-checkbox-1'][contains(.,'Sports')]")))
    btn_uno.click()
except TimeoutException as e:
    print(e.msg)
    print("El elemento no está disponible.")

try:
    Buscar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'uploadPicture')]")))
    Buscar = driver.find_element_by_xpath("//input[contains(@id,'uploadPicture')]")
    Buscar.send_keys("C://Users//luis_//PycharmProjects//Curso_selenium//images//demo1.jpg")
    time.sleep(t)
except TimeoutException as e:
    print(e.msg)
    print("El elemento no está disponible.")

driver.find_element_by_xpath("//textarea[contains(@id,'currentAddress')]").send_keys("Prueba número 1 de Testing")

time.sleep(t)
driver.close()


"""

"""