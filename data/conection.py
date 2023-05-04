import psycopg2 as pg
from decouple import config
from data.methods import methodsUSER as method, methodINSERT as ins
from datetime import datetime 
import re

patron = re.compile('([0-9]+)')
class DbUser():
    def __init__(self):
        self.posg = pg
        self.conexion=None
        try:
            credentials ={
               "database": config("DATABASE"),
                "user":config("USER") ,
                "password": config("SECRET_KEY") ,

                "host": "localhost",
                "port": 5432
            }
            self.conexion = self.posg.connect(**credentials)
            print("conexion success")
            self.conexion.autocommit = True
            self.cursor = self.conexion.cursor()
        except self.posg.Error as e:
            print("ocurrio un error en la conexion",e)
         
    

    def SelectFromDB(self, name=None, selection = method['USER']):
        if selection == method['USER'] and name is not None:
            try:
                self.cursor.execute("SELECT * FROM usuarios WHERE nombre = '{}' ".format(name))  
                query = self.cursor.fetchone()
                return query
            except self.posg.Error as e:
                print("ocurrio un error en la conexion",e)
            finally:
                self.cursor.close()
                self.conexion.close() 
        elif selection == method['ID']:
            print('id')

    def QueryInsert(self,  type = ins['ing'], datos = [],*args):
        if type == ins['ing']:
            
            try:
                self.cursor.execute("""INSERT INTO ingresosdiarios (fecha, tipodepago, categoria,divisa, valor, descripcion, iduser) values ('{}', '{}', '{}','{}', {}, '{}', {})""".format(datos[0]['fecha'], datos[0]['tipodepago'], datos[0]['categoria'],datos[0]['divisa'], datos[0]['valor'], datos[0]['descripcion'], datos[0]['iduser'] ))
                print('insertion success')
                return 'ok'
            except Exception as e :
                print(e)
                return 'error'
        
        elif type == ins['gas']:
            print('gas')
            try:
                self.cursor.execute("""INSERT INTO gastosdiarios (fecha, tipodepago, categoria,divisa, valor, descripcion, iduser) values ('{}', '{}', '{}','{}', {}, '{}', {})""".format(datos[0]['fecha'], datos[0]['tipodepago'], datos[0]['categoria'],datos[0]['divisa'], datos[0]['valor'], datos[0]['descripcion'], datos[0]['iduser'] ))
                print('insertion success')
                return 'ok'
            except Exception as e :
                print(e)
                return 'error'
        else :
            return 'error'
    def QueryDelete(self):
        pass

    def QueryUpdate(self):
        pass

