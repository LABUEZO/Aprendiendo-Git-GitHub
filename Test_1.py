import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

non=driver.find_element(By.XPATH, "//input[contains(@id,'userName')]")
non.send_keys("Rodrigo")
time.sleep(1)
driver.find_element_by_xpath("//input[contains(@id,'userEmail')]").send_keys("rodrigo@mail.com")
time.sleep(1)
driver.find_element_by_xpath("//textarea[contains(@id,'currentAddress')]").send_keys("Dirección 1234")
time.sleep(1)
driver.find_element_by_xpath("//textarea[contains(@id,'permanentAddress')]").send_keys("Dirección 5678")
time.sleep(1)

driver.execute_script("window.scrollTo(0,360)")
time.sleep(2)

driver.find_element_by_xpath("//button[contains(@id,'submit')]").click()
time.sleep(2)




driver.close()
