import time

from selenium import webdriver
from selenium.webdriver import Keys


driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

non=driver.find_element_by_xpath("//input[@type='text' and @id='userName']")
non.send_keys("Rodrigo")
non.send_keys(Keys.TAB + "rodrigo@gmail.com" + Keys.TAB + "Dirección 123" + Keys.TAB + "Dirección 456" + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

driver.find_element_by_xpath("(//span[contains(@class,'text')])[2]").click()
time.sleep(2)

driver.close()
