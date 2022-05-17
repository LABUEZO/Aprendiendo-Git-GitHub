from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demoqa.com/text-box")
print("Bienvenido a Selenium")
print("Importando webdriver")
print(driver.title)

driver.close()
