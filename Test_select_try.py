import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://www.intelinvert.com/formulario-kyc/")
driver.maximize_window()
driver.implicitly_wait(10)
t=1

driver.execute_script("window.scrollTo(0,360)")
time.sleep(t)
try:
    activ = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@id,'429486750')][@name='wnd_SelectboxField_429486750']")))
    act=Select(activ)
    act.select_by_visible_text("Desempleado")
    print("Escribió Desempleado")
    time.sleep(t)
    act.select_by_index(2)
    print("Escribió Jubilado")
    time.sleep(t)
    act.select_by_value("3")
    print("Escribió Ama de casa")
    time.sleep(t)
except TimeoutException as e:
    print(e.msg)
    print("El elemento no está disponible.")


driver.close()
