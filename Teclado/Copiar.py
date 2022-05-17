import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from Funciones.Funciones import FuncionesGlobales
from selenium.webdriver import ActionChains, Keys

t=2

class BaseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        f.Navegar("https://demoqa.com/automation-practice-form",t)

        f.Text_Mixto("xpath","//input[contains(@id,'firstName')]","Juan",t)

        act=ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys("a").send_keys(Keys.CONTROL).perform()
        time.sleep(2)
        act.key_down(Keys.CONTROL).send_keys("c").send_keys(Keys.CONTROL).perform()
        act.send_keys(Keys.TAB)
        act.key_down(Keys.CONTROL).send_keys("v").send_keys(Keys.CONTROL).perform()
        time.sleep(2)

    def tearDown(self) -> None:
        d = self.driver
        d.close()

if __name__ == "__main__":
    unittest.main()

