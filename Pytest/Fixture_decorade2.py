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
def setup_login_uno():
	global driver,f
	driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
	driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin")
	driver.maximize_window()
	f = FuncionesGlobales(driver)
	f.Text_Mixto("id","Email","admin@yourstore.com",t)
	f.Text_Mixto("id","Password","admin",t)
	f.Click_Mixto("xpath","//button[@type='submit'][contains(.,'Log in')]",t)
	print("Entrando al sistema")
	yield
	print("Salida del login uno")


@pytest.fixture(scope='module')
def setup_login_dos():
	global driver,f
	driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
	driver.get("https://opensource-demo.orangehrmlive.com/")
	driver.maximize_window()
	f = FuncionesGlobales(driver)
	f.Text_Mixto("id","txtUsername","Admin",t)
	f.Text_Mixto("id","txtPassword","admin123",t)
	f.Click_Mixto("id","btnLogin",t)
	print("Entrando al sistema")
	yield
	print("Salida del login dos")


@pytest.mark.usefixtures('setup_login_uno')
def test_uno():
	print("Entrando al sistema uno")
	f.Click_Mixto("xpath","(//p[contains(.,'Customers')])[1]",t)
	f.Click_Mixto("xpath","(//p[contains(.,'Customers')])[2]",t)
	f.Text_Mixto("xpath","//input[contains(@id,'SearchFirstName')]","victoria",t)
	f.Click_Mixto("xpath","//button[contains(@id,'search-customers')]",t)
	#Creando un nuevo usuario
	f.Click_Mixto("xpath","//a[@href='/Admin/Customer/Create']",t)
	email=driver.find_element(By.XPATH, "//input[contains(@id,'Email')]")
	email.send_keys("juan@gmail.com"+Keys.TAB+"12345"+Keys.TAB+"Juan"+Keys.TAB+"Perez")
	time.sleep(3)
	f.Click_Mixto("xpath","//input[contains(@id,'Gender_Male')]",t)
	f.Text_Mixto("xpath","//input[contains(@id,'DateOfBirth')]","2/20/2019",t)
	driver.close()



@pytest.mark.usefixtures('setup_login_dos')
def test_dos():
	print("Entrando al sistema dos")
	f.Click_Mixto("xpath","//b[contains(.,'Admin')]",t)
	f.Click_Mixto("xpath","//a[contains(@id,'menu_admin_UserManagement')]",t)
	f.Text_Mixto("xpath","//input[contains(@id,'searchSystemUser_userName')]","adash",t)
	f.Click_Mixto("xpath","//input[contains(@id,'searchBtn')]",t)
	f.Click_Mixto("xpath","//input[contains(@id,'btnAdd')]",t)
	f.Select_Mixto("xpath","//select[contains(@id,'systemUser_userType')]","index",0,t)
	driver.close()
