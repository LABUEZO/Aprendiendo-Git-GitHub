import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demoqa.com/checkbox")
driver.maximize_window()
driver.implicitly_wait(10)
t=5

btn_uno = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//svg[contains(@stroke,'currentColor')]")))
btn_uno.click()

time.sleep(t)

driver.close()
