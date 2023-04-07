import psycopg2 as pg

class DbUser():
    def __init__(self):
        self.posg = pg
        self.conexion=None
        try:
            credentials ={
                "database": "EvaLibroDiario",
                "user": "Eva",
                "password": "leonardo25537/*",
                "host": "localhost",
                "port": 5432
            }
            self.conexion = self.posg.connect(**credentials)
            print("conexion success")
            self.conexion.autocommit = True

        except self.posg.Error as e:
            print("ocurrio un error en la conexion",e)
        finally:
            self.conexion.close()
      
    

    def SelectFromDB(self):
        cursor = self.conexion.cursor()


    def QueryInsert(self):
        pass

    def QueryDelete(self):
        pass

    def QueryUpdate(self):
        pass

DbUser()