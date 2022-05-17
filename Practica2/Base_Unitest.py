import time
import unittest

from selenium import webdriver

class base_test(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()
        t = 2

    def test1(self):
        d = self.driver
        d.get("https://demoqa.com/")
        time.sleep(2)

    def tearDown(self) -> None:
        d = self.driver
        d.close()

if __name__ == "__main__":
    unittest.main()
