import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from Funciones.Funciones import FuncionesGlobales
from selenium.webdriver import ActionChains

t=2

class BaseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        f.Navegar("https://demoqa.com/buttons",t)

        f.Mouse_Double_Click("id","doubleClickBtn",t)

        """
        elemento=driver.find_element(By.ID, "doubleClickBtn")
        act=ActionChains(driver)
        act.double_click(elemento).perform()
        """
        time.sleep(t)

    def tearDown(self) -> None:
        d = self.driver
        d.close()

if __name__ == "__main__":
    unittest.main()

