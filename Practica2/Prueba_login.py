import time
import unittest

from selenium import webdriver

class PruebaLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()
        t = 1

    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        non = driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave = driver.find_element_by_xpath("//input[contains(@id,'password')]")
        btn = driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        non.send_keys("rodrigo")
        clave.send_keys("admin123")
        btn.click()
        error = driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error = error.text
        #print(error)
        if(error == "Epic sadface: Username and password do not match any user in this service"):
            print("Los datos ingresados no son correctos.")
            print("Prueba 1 test ok.")
        time.sleep(2)

    def test_login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        non = driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave = driver.find_element_by_xpath("//input[contains(@id,'password')]")
        btn = driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        non.send_keys("")
        clave.send_keys("admin123")
        btn.click()
        error = driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error = error.text
        #print(error)
        if(error == "Epic sadface: Username is required"):
            print("Nombre de usuario No Ingresado.")
            print("Prueba 2 test ok.")
        time.sleep(2)

    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        non = driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave = driver.find_element_by_xpath("//input[contains(@id,'password')]")
        btn = driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        non.send_keys("rodrigo")
        clave.send_keys("")
        btn.click()
        error = driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error = error.text
        #print(error)
        if(error == "Epic sadface: Password is required"):
            print("Password No Ingresado")
            print("Prueba 3 test ok.")
        time.sleep(2)

    def test_login4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        non = driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave = driver.find_element_by_xpath("//input[contains(@id,'password')]")
        btn = driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        non.send_keys("")
        clave.send_keys("")
        btn.click()
        error = driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error = error.text
        #print(error)
        if(error == "Epic sadface: Username is required"):
            print("Usuario y Password No Ingresado.")
            print("Prueba 4 test ok.")
        time.sleep(2)

    def test_login5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        non = driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave = driver.find_element_by_xpath("//input[contains(@id,'password')]")
        btn = driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        non.send_keys("standard_user")
        clave.send_keys("secret_sauce")
        btn.click()

        elemento = driver.find_element_by_xpath("//div[contains(@class,'app_logo')]")
        elemento = elemento.is_enabled()
        print("El elemento es: ", elemento)

        time.sleep(2)

    def tearDown(self) -> None:
        driver = self.driver
        driver.close()

if __name__ == "__main__":
    unittest.main()
