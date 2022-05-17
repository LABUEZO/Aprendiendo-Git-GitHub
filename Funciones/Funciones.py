import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class FuncionesGlobales:

    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tie):
        t=time.sleep(tie)
        return t

    def Navegar(self, url, tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Abriendo la url {}".format(url))
        t=time.sleep(tiempo)
        return t

    def Salida(self):
        print("Finalizó la prueba Exitosamente.")

    def Select_Xpath(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element_by_xpath(elemento)
        return val

    def Select_ByID(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID, elemento)
        return val

    def Upload_Xpath(self, xpath, ruta, tiempo):
        try:
            val = self.Select_Xpath(ruta)
            val.send_keys(ruta)
            print("Se carga la imagen {}".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento: ", xpath)


    def Upload_ID(self, id, ruta, tiempo):
        try:
            val = self.Select_ByID(ruta)
            val.send_keys(ruta)
            print("Se carga la imagen {}".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento: ", id)


    def Check_Xpath(self, xpath, tiempo):
        try:
            val = self.Select_Xpath(xpath)
            val.click()
            print("Click en el elemento {}".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento: ", xpath)


    def Check_ID(self, id, tiempo):
        try:
            val = self.Select_ByID(id)
            val.click()
            print("Click en el elemento {}".format(id))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento: ", id)


    def Check_Xpath_Multiples(self, tiempo, *args):
        try:
            for num in args:
                val = self.Select_Xpath(num)
                val.click()
                print("Click en el elemento {}".format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontró el elemento: ", num)



    def Text_Mixto(self, tipo, selector, texto, tiempo):
        if (tipo=="xpath"):
            try:
                val = self.Select_Xpath(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto: {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)
        elif (tipo=="id"):
            try:
                val = self.Select_ByID(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)

    def Click_Mixto(self, tipo, selector, tiempo):
        if (tipo=="xpath"):
            try:
                val = self.Select_Xpath(selector)
                val.click()
                print("Hacemos click en botón: {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)
        elif (tipo=="id"):
            try:
                val = self.Select_ByID(selector)
                val.click()
                print("Hacemos click en botón: {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)

    def Select_Mixto(self, tip, selector, tipo, dato, tiempo):
        if (tip=="xpath"):
            try:
                val = self.Select_Xpath(selector)
                val = Select(val)
                if (tipo=="text"):
                    val.select_by_visible_text(dato)
                elif (tipo=="index"):
                    val.select_by_index(dato)
                elif (tipo=="value"):
                    val.select_by_value(dato)
                print("El campo seleccionado es {}".format(dato))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)
        elif (tip=="id"):
            try:
                val = self.Select_ByID(selector)
                val = Select(val)
                if (tipo=="text"):
                    val.select_by_visible_text(dato)
                elif (tipo=="index"):
                    val.select_by_index(dato)
                elif (tipo=="value"):
                    val.select_by_value(dato)
                print("El campo seleccionado es {}".format(dato))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)


    def Existe(self, tipo, selector, tiempo):
        if(tipo == "xpath"):
            try:
                val = self.Select_Xpath(selector)
                print("El elemento {} existe.".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)
                return "No existe"
        elif (tipo == "id"):
            try:
                val = self.Select_ByID(selector)
                print("El elemento {} existe.".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)
                return "No existe"


    def Mouse_Double_Click(self, tipo, selector, tiempo=0.5):
        if (tipo=="xpath"):
            try:
                val = self.Select_Xpath(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("Double Click en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)
        elif (tipo=="id"):
            try:
                val = self.Select_ByID(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("Double Click en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)


    def Mouse_Derecho(self, tipo, selector, tiempo=0.5):
        if (tipo=="xpath"):
            try:
                val = self.Select_Xpath(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Mouse Click derecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)
        elif (tipo=="id"):
            try:
                val = self.Select_ByID(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Mouse Click derecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)


    def Mouse_DragAndDrop(self, tipo, selector, destino, tiempo=0.5):
        if (tipo=="xpath"):
            try:
                val = self.Select_Xpath(selector)
                val2 = self.Select_Xpath(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Se soltó el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)
        elif (tipo=="id"):
            try:
                val = self.Select_ByID(selector)
                val2 = self.Select_Xpath(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Se soltó el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)


    def Mouse_DragAndDrop_XY(self, tipo, selector, x, y, tiempo=0.5):
        if (tipo=="xpath"):
            try:
                self.driver.switch_to.frame(0)
                val = self.Select_Xpath(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val, x, y).perform()
                print("Se soltó el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)
        elif (tipo=="id"):
            try:
                self.driver.switch_to.frame(0)
                val = self.Select_ByID(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val, x, y).perform()
                print("Se soltó el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento: ", selector)


    def ClickXY(self, tipo, selector, x, y, tiempo=0.5):
        if (tipo == "xpath"):
            try:
                val = self.Select_Xpath(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento{} coordenada {}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.Select_ByID(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento{} coordenada {}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
