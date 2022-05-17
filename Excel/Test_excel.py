import unittest
from Funciones.Funciones import FuncionesGlobales
from selenium import webdriver
from Funciones_Excel import *

tg = 1

class BaseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

    def test1(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        fe = Funexcel(driver)
        f.Navegar("https://demoqa.com/text-box", tg)
        ruta = "C://Users//luis_//Documents//Datos_ok.xlsx"
        filas = fe.getRowCount(ruta, "Hoja1")

        for r in range(2, filas+1):
            nombre = fe.readData(ruta,"Hoja1",r,1)
            email = fe.readData(ruta,"Hoja1",r,2)
            dir1 = fe.readData(ruta,"hoja1",r,3)
            dir2 = fe.readData(ruta,"Hoja1",r,4)

        f.Text_Mixto("id","userName", nombre, tg)
        f.Text_Mixto("id","userEmail", email, tg)
        f.Text_Mixto("id","currentAddress", dir1, tg)
        f.Text_Mixto("id","permanentAddress", dir2, tg)
        f.Click_Mixto("id","submit", tg)

        e = f.Existe("id", "name", tg)
        if (e=="Existe"):
            print("El elemento se insertó correctamente")
            fe.writeData(ruta, "Hoja1", r, 5, "Insertado")
        else:
            print("No se insertó")
            fe.writeData(ruta, "Hoja1", r, 5, "Error")

