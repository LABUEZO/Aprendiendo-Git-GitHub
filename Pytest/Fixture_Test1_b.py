import time

from selenium.webdriver import ActionChains, Keys
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
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin")
    driver.maximize_window()
    f = FuncionesGlobales(driver)
    f.Text_Mixto("id", "Email", "admin@yourstore.com", t)
    f.Text_Mixto("id", "Password", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("Iniciando el test.")

def teardown_function(function):
    print("Fin del Test")
    driver.close()


def test1():
    f = FuncionesGlobales(driver)
    f.Click_Mixto("xpath", "(//p[contains(.,'Catalog')])[1]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.Text_Mixto("xpath","//input[contains(@id,'SearchProductName')]","computer",t)
    f.Click_Mixto("xpath","//button[contains(@id,'search-products')]",t)

def test2():
    f = FuncionesGlobales(driver)
    f.Click_Mixto("xpath", "(//p[contains(.,'Catalog')])[1]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.Click_Mixto("xpath","//a[@href='/Admin/Product/Create']",t)
    f.Text_Mixto("xpath","//input[@id='Name']","Laptop Dell",t)
    f.Text_Mixto("xpath","//textarea[contains(@id,'ShortDescription')]","computadora portátil",t)
    f.Click_Mixto("xpath","//span[@class='tox-mbtn__select-label'][contains(.,'File')]",t)
    f.Click_Mixto("xpath","//div[@class='tox-collection__item-label'][contains(.,'New document')]",t)
    driver.switch_to.frame(0)
    f.Text_Mixto("id","tinymce","Descripción larga",t)
    campo=driver.find_element(By.ID,"tinymce")
    campo.send_keys("Descripción larga" + Keys.TAB + "35546").time.sleep(t)







