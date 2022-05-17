import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=3

time.sleep(t)
try:
    buscar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]")))
    buscar = driver.find_element_by_xpath("//input[contains(@id,'fileinput')]")
    buscar.send_keys("C://Users//luis_//PycharmProjects//Curso_selenium//images//demo1.jpg")
    time.sleep(t)
    driver.find_element_by_xpath("//input[contains(@id,'itsanimage')]").click()
    driver.find_element_by_xpath("//input[contains(@type,'submit')]").click()
    time.sleep(t)

except TimeoutException as e:
    print(e.msg)
    print("El elemento no está disponible.")

time.sleep(t)
driver.close()
