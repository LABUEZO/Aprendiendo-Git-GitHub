import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from Pytest.Funciones import FuncionesGlobales

t=0.5

@pytest.fixture(scope="module")
def setup_login_uno():
    print("Empezando el login del sistema")
    yield
    print("Saliendo del sistema, prueba OK")

@pytest.fixture(scope="module")
def setup_login_dos():
    print("Empezando la prueba del sistema dos")
    yield
    print("Saliendo de la prueba del sistema dos.")


def test_uno(setup_login_uno):
    print("Empezando la prueba del sistema uno.")

def test_dos(setup_login_dos):
    print("esto es para la prueba dos")

@pytest.mark.usefixtures("setup_login_dos")
def test_tres(setup_login_dos):
    print("Prueba tres del módulo login dos")