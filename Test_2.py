import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

non=driver.find_element_by_id("userName")
non.send_keys("Rodrigo")
time.sleep(1)
driver.find_element_by_id("userEmail").send_keys("rodrigo@gmail.com")
time.sleep(1)
driver.find_element_by_id("currentAddress").send_keys("Dirección 1234")
time.sleep(1)
driver.find_element_by_id("permanentAddress").send_keys("Dirección 5678")
time.sleep(1)

driver.execute_script("window.scrollTo(0,360)")
time.sleep(2)

driver.find_element_by_id("submit").click()
time.sleep(2)

driver.close()
