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
        f.Navegar("https://opensource-demo.orangehrmlive.com/index.php/auth/login",t)

        f.Text_Mixto("id","txtUsername","Admin",t)
        f.Text_Mixto("id","txtPassword","admin123",t)
        f.Click_Mixto("id","btnLogin",t)

        admin=driver.find_element(By.ID, "menu_admin_viewAdminModule")
        sub1=driver.find_element(By.ID, "menu_admin_UserManagement")
        sub2=driver.find_element(By.ID, "menu_admin_viewSystemUsers")

        act=ActionChains(driver)
        act.move_to_element(admin).move_to_element(sub1).move_to_element(sub2).click().perform()

    def tearDown(self) -> None:
        d = self.driver
        d.close()

if __name__ == "__main__":
    unittest.main()

