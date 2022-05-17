import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://seleniumeasy.com/test/basic-first-form-demo.html")
driver.maximize_window()
t=6
time.sleep(t)

#https://www.seleniumeasy.com/test/basic-checkbox-demo.html

driver.close()
