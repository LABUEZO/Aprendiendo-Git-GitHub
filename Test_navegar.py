import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

t=3

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

driver.get("https://balanz.com/")
time.sleep(t)

driver.get("https://www.portfoliopersonal.com/")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.close()