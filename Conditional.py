import time

from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
t = 2
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(t)

titular = driver.find_element_by_xpath("//img[@src='/images/Toolsqa.jpg']")
print(titular.is_displayed())

btn1 = driver.find_element_by_xpath("(//div[contains(@class,'card-up')])[1]")

if (titular.is_displayed()==True):
    print("Existe la imagen")
    btn1.click()
else:
    print("No existe la imagen")


time.sleep(t)
driver.close()
