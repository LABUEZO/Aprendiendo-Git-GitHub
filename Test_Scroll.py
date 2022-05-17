import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://pixabay.com/es/")
driver.maximize_window()
#driver.implicitly_wait(10)
t=3


try:
    Buscar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/es/images/search/?order=ec']")))
    Buscar = driver.find_element_by_xpath("//a[@href='/es/images/search/?order=ec']")
    ir = driver.execute_script("arguments[0].scrollIntoView();", Buscar)
    time.sleep(t)
except TimeoutException as e:
    print(e.msg)
    print("El elemento no está disponible.")


time.sleep(t)
driver.close()
