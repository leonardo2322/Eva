import psycopg2 as pg
from decouple import config
from data.methods import methodsUSER as method, methodINSERT as ins
from datetime import datetime 
import re

patron = re.compile('([0-9]+)')
class DbUser():
    def __init__(self):
        super(DbUser,self)
        self.posg = pg
        self.conexion=None
        self.conection()
        # self.cursor = None
    def conection(self):
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
         
    

    def SelectFromDB(self, name=None, selection = method['USER'], tableSearch=None, *args):
        if selection == method['USER'] and name is not None:
            if self.cursor.closed == True:
                self.conection()
            else:
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
        
            try:
                query =   """ SELECT * FROM {} WHERE descripcion = '{}' """.format(tableSearch,name)
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                if result.__len__() > 0:
                   return  result[0], result[0][0]
                else:
                    return 'error'

            except Exception as e:
                    print("ocurrio un error en la conexion",e)
                    return 'error'
            finally:
                    self.cursor.close()
                    self.conexion.close()
          
                


    def QueryInsert(self,  type = ins['ing'], datos = [],*args):
        if type == ins['ing']:
            if self.cursor.closed == True:
                self.conection()
            else:
            
                try:
                    self.cursor.execute("""INSERT INTO ingresosdiarios (fecha, tipodepago, categoria,divisa, valor, descripcion, iduser) values ('{}', '{}', '{}','{}', {}, '{}', {})""".format(datos[0]['fecha'], datos[0]['tipodepago'], datos[0]['categoria'],datos[0]['divisa'], datos[0]['valor'], datos[0]['descripcion'], datos[0]['iduser'] ))
                    print('insertion success')
                    return 'ok'
                except Exception as e :
                    print(e)
                    return 'error'
        
        elif type == ins['gas']:
            if self.cursor.closed == True:
                self.conection()
            else:
                try:
                    self.cursor.execute("""INSERT INTO gastosdiarios (fecha, tipodepago, categoria,divisa, valor, descripcion, iduser) values ('{}', '{}', '{}','{}', {}, '{}', {})""".format(datos[0]['fecha'], datos[0]['tipodepago'], datos[0]['categoria'],datos[0]['divisa'], datos[0]['valor'], datos[0]['descripcion'], datos[0]['iduser'] ))
                    print('insertion success')
                    return 'ok'
                except Exception as e :
                    print(e)
                    return 'error'
        else :
            return 'error'
    def QueryDelete(self, tabla, id, idTabla):
        try:
            query = """ DELETE FROM {} WHERE {} = {} """.format(tabla,idTabla,id)
            self.cursor.execute(query)
            return 'success'
        except self.posg.Error as e :
            print("ocurrio un error en la conexion",e)
            return 'error'
        finally:
            self.cursor.close()
            self.conexion.close()
          

    def QueryUpdate(self):
        pass

