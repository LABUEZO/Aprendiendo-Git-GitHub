import sqlite3

database = "database.db"

class DB:
    def ejecutar_consulta(self, consulta, parametros=()):
        with sqlite3.connect(database) as conn:
            self.cursor = conn.cursor()
            datos = self.cursor.execute(consulta, parametros)
            conn.commit()
            return datos

"""
db = DB()
result = db.ejecutar_consulta("SELECT * FROM fichero")
print(result.fetchall())
"""

