import time
import unittest

from selenium import webdriver
from Funciones.Funciones import FuncionesGlobales
from Funciones.Page_Login import PaginaLogin

tg=3

class base_test(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()
        t = 2

    def test1(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        pg = PaginaLogin(driver)
        f.Navegar("https://www.intelinvert.com/formulario-kyc/", tg)
        f.Select_Mixto("id", "field-wnd_SelectboxField_429486750", "text", "Desempleado", tg)

    def tearDown(self) -> None:
        d = self.driver
        d.close()

if __name__ == "__main__":
    unittest.main()
