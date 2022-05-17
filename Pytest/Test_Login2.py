import pytest
import time

from selenium import webdriver
from Pytest.Page_Login import Funciones_Login

t=0.5

def test_login1():
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    fl=Funciones_Login(driver)
    fl.L1("","secret_sauce","Epic sadface: Username is required")
    fl.L2("luisbuezo","secret_sauce","Epic sadface: Username and password do not match any user in this service")
    fl.L3("standard_user","","Epic sadface: Password is required")
    fl.L4("standard_user","admin123","Epic sadface: Username and password do not match any user in this service")


def test_login2():
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    fl = Funciones_Login(driver)
    fl.L5("standard_user", "secret_sauce", "PRODUCTS")
