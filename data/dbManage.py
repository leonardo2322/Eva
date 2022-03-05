
import psycopg2 as pg
from psycopg2 import Error
from passlib.hash import pbkdf2_sha256

class DbUser():
    def __init__(self, *args, **kwargs):
        self.posg = pg

    def Conexion(self):
        try:
            credentials ={
                "dbname": "administracion",
                "user": "postgres",
                "password": "$pbkdf2-sha256$29000$vPe.t1YKodT6X.vdu/d.rw$fK/D3HICs4jiNrLAag0N36iJsLKicnizOllrL8qtOO4",
                "host": "localhost",
                "port": 5432
            }
            self.conexion = self.posg.connect(**credentials)
            self.query = self.conexion.cursor()
            
        except Error as e:
            print("ocurrio un error en la conexion", e)
        except:
            print('error interno abre el servidor de la bbdd')
            return 0
        return self.conexion, self.query

    def usersInit(self,*args):
        usuario = (args)
        

        try:
            sql = ''' SELECT * FROM usuarios WHERE usuario='%s' '''%(usuario)
            connection = self.Conexion()
            connection[1].execute(sql)
            self.datas = connection[1].fetchone()
            connection[0].commit()
            return self.datas

        except Error as e:
            print('ocurrio un error', e) 

        except:
            print('ocurrio un error') 
            
        finally:
            connection[1].close()    
            connection[0].close()
    def SelectFromDB(self, *arg, **kwargs):
        
        connection = self.Conexion()

        try:
            sqlSelect = ''' SELECT * FROM productoscyg  '''
            connection[1].execute(sqlSelect)
            self.data = connection[1].fetchall()
            connection[0].commit()
            
        except connection[0].Error as e:
            return e
        except:
            print('error de conexion con la base de datos')
        finally:
            connection[1].close()    
            connection[0].close()
        return self.data
    def QueryInsert(self, materiaprima, proveedor, costo, *args, **kwargs):

        connect = self.Conexion()
        costInt = int(costo)
        try:
            sqlInsertData = ''' INSERT INTO productoscyg (materiaprima,proveedor,costo ) VALUES('%s','%s','%s') '''%(materiaprima, proveedor, costInt)  
            connect[1].execute(sqlInsertData)
            connect[0].commit()
        except connect[0].Error as e:
            return e
        except:
            print('error de conexion con la base de datos')
        finally:
            connect[1].close()    
            connect[0].close()


    def QueryDelete(self,*args, **kwargs):
        sqlDelete = ''' DELETE FROM productoscyg where id='%s' '''% args
        connect = self.Conexion()
        try:
            connect[1].execute(sqlDelete)
            connect[0].commit()
        except connect[0].Error as e:
            return e
        except:
            print('error de conexion con la base de datos')


    def QueryUpdate(self,*args, **kwargs):
        pass

