import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from Pytest.Funciones import FuncionesGlobales


class Funciones_Login:

    def __init__(self, driver):
        self.driver = driver

    def L1(self, user, password, message, t=0.5):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        f = FuncionesGlobales(driver)
        f.Navegar("https://www.saucedemo.com/", t)
        driver.maximize_window()
        f.Text_Mixto("id", "user-name", user, t)
        f.Text_Mixto("id", "password", password, t)
        f.Click_Mixto("id", "login-button", t)
        e1 = f.SEX("//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
        e1 = e1.text
        print(e1)
        if (e1 == message):
            print("Prueba de validación sin usuario es exitosa")
        else:
            print("La prueba de validación sin usuario es incorrecta.")
        driver.close()

    def L2(self, user, password, message, t=0.5):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        f = FuncionesGlobales(driver)
        f.Navegar("https://www.saucedemo.com/", t)
        driver.maximize_window()
        f.Text_Mixto("id", "user-name", user, t)
        f.Text_Mixto("id", "password", password, t)
        f.Click_Mixto("id", "login-button", t)
        e1 = f.SEX("//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]")
        e1 = e1.text
        print(e1)
        if (e1 == message):
            print("Prueba de validación con usuario incorrecto es exitosa")
        else:
            print("La prueba de validación con usuario incorrecto es incorrecta.")
        driver.close()

    def L3(self, user, password, message, t=0.5):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        f = FuncionesGlobales(driver)
        f.Navegar("https://www.saucedemo.com/", t)
        driver.maximize_window()
        f.Text_Mixto("id", "user-name", user, t)
        f.Text_Mixto("id", "password", password, t)
        f.Click_Mixto("id", "login-button", t)
        e1 = f.SEX("//h3[@data-test='error'][contains(.,'Epic sadface: Password is required')]")
        e1 = e1.text
        print(e1)
        if (e1 == message):
            print("Prueba de validación sin password es exitosa")
        else:
            print("La prueba de validación sin password es incorrecta.")
        driver.close()

    def L4(self, user, password, message, t=0.5):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        f = FuncionesGlobales(driver)
        f.Navegar("https://www.saucedemo.com/", t)
        driver.maximize_window()
        f.Text_Mixto("id", "user-name", user, t)
        f.Text_Mixto("id", "password", password, t)
        f.Click_Mixto("id", "login-button", t)
        e1 = f.SEX("//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]")
        e1 = e1.text
        print(e1)
        if (e1 == message):
            print("Prueba de validación con password incorrecto es exitosa")
        else:
            print("La prueba de validación con password incorrecto es incorrecta.")
        driver.close()

    def L5(self, user, password, message, t=0.5):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        f = FuncionesGlobales(driver)
        f.Navegar("https://www.saucedemo.com/", t)
        driver.maximize_window()
        f.Text_Mixto("id", "user-name", user, t)
        f.Text_Mixto("id", "password", password, t)
        f.Click_Mixto("id", "login-button", t)
        e1 = f.SEX("//span[@class='title'][contains(.,'Products')]")
        e1 = e1.text
        print(e1)
        if (e1 == message):
            print("Prueba de validación de ingreso correcto es exitosa")
        else:
            print("La prueba de validación de ingreso correcto es incorrecta.")
        driver.close()
