import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from Pytest.Funciones import FuncionesGlobales

t=0.5
driver=""
f=""

def setup_function(function):
    global driver,f
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    f = FuncionesGlobales(driver)
    f.Text_Mixto("id", "user-name", "problem_user", t)
    f.Text_Mixto("id", "password", "secret_sauce", t)
    f.Click_Mixto("id", "login-button", t)
    print("Iniciando el test.")

def teardown_function(function):
    print("Fin del Test")
    driver.close()


def test1():
    f.Click_Mixto("id", "add-to-cart-sauce-labs-backpack", t)
    f.Click_Mixto("xpath", "//a[contains(@class,'shopping_cart_link')]", t)
    f.Click_Mixto("id", "checkout", t)




