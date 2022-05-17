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


def get_Data():
	return [
		("rodrigo","1234"),
		("juan","1233234"),
		("pedro","12232334"),
		("erika","1234232"),
		("carlos","1234sdf"),
		("Admin","admin123")
	]

@pytest.mark.login
@pytest.mark.parametrize("user,clave",get_Data())
def test_login(user,clave):
	global driver, f
	driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
	driver.get("https://opensource-demo.orangehrmlive.com/")
	driver.maximize_window()
	driver.implicitly_wait(20)
	f = FuncionesGlobales(driver)
	f.Text_Mixto("id","txtUsername",user,t)
	f.Text_Mixto("id","txtPassword",clave,t)
	f.Click_Mixto("id","btnLogin",t)
	print("Entrando al sistema")


def teardow_function():
	print("Salida del test")
	driver.close()





