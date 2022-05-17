import time

from selenium import webdriver


driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
t=2
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
time.sleep(t)

driver.find_element_by_xpath("//button[contains(@id,'alertButton')]").click()

time.sleep(t)




driver.close()
