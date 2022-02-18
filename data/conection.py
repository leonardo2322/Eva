import psycopg2 as pg

class DbUser():
    def __init__(self):
        self.posg = pg
        try:
            credentials ={
                "dbname": "administracion",
                "user": "postgres",
                "password": "$pbkdf2-sha256$29000$vPe.t1YKodT6X.vdu/d.rw$fK/D3HICs4jiNrLAag0N36iJsLKicnizOllrL8qtOO4",
                "host": "localhost",
                "port": 5432
            }
            conexion = self.posg.connect(**credentials)
            print(conexion)
            self.query = self.posg.cursor()

        except self.posg.Error as e:
            print("ocurrio un error en la conexion", e)
        finally:
            conexion.close()


    def SelectFromDB(self):
        pass

    def QueryInsert(self):
        pass

    def QueryDelete(self):
        pass

    def QueryUpdate(self):
        pass