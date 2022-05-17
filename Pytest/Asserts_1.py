import time
import pytest

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from Pytest.Funciones import FuncionesGlobales

t=0.5

@pytest.fixture(scope='module')
def setup_login():
	global driver,f
	driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
	driver.get("https://opensource-demo.orangehrmlive.com/")
	driver.maximize_window()
	f = FuncionesGlobales(driver)
	f.Text_Mixto("id","txtUsername","Admin",t)
	f.Text_Mixto("id","txtPassword","admin123",t)
	f.Click_Mixto("id","btnLogin",t)
	print("Entrando al sistema")


def teardown_function():
	print("Fin de todos los test.")
	driver.close()

@pytest.mark.login
@pytest.mark.usefixtures("setup_login")
def test_uno():
	etiqueta=f.SEX("//h1[contains(.,'Dashboard')]").text
	print(etiqueta)
	if (etiqueta=="Dashboard"):
		print("Adentro")
		assert etiqueta=="Dashboard"
	else:
		print("Afuera")
		assert etiqueta=="Dashboar", "No estas en la página de inicio"
