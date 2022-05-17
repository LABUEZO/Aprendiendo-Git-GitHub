import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from Funciones.Funciones import FuncionesGlobales
from selenium.webdriver import ActionChains

t=1.5

class BaseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        f.Navegar("https://demoqa.com/buttons",t)

        f.Mouse_Derecho("id","rightClickBtn",t)


    def tearDown(self) -> None:
        d = self.driver
        d.close()

if __name__ == "__main__":
    unittest.main()