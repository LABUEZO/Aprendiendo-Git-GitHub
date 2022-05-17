import time
import unittest
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Funciones.Funciones import FuncionesGlobales

class PaginaLogin:

    def __init__(self, driver):
        self.driver = driver

    def Login_Master(self, url, name, clave, t):
        driver = self.driver
        f = FuncionesGlobales(driver)
        f.Navegar(url, t)
        f.Text_Xpath_Valida("//input[contains(@id,'user-name')]", name, t)
        f.Text_Xpath_Valida("//input[contains(@id,'password')]", clave, t)
        f.Click_Xpath_Valida("//input[contains(@id,'login-button')]", t)
        f.Salida()

