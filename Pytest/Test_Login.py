import pytest
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Pytest.Funciones import FuncionesGlobales

t=0.5

def test_login1():
    global driver
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    f=FuncionesGlobales(driver)
    f.Navegar("https://demo.nopcommerce.com/login",t)
    driver.maximize_window()
    f.Text_Mixto("id","Email","luisbuezo2011@gmail.com",t)
    f.Text_Mixto("id","Password","admin123",t)
    f.Click_Mixto("path","//button[@type='submit'][contains(.,'Log in')]",t)
    e1 = f.SEX("//li[contains(.,'No customer account found')]")
    e1 = e1.text
    print(e1)
    driver.close()

