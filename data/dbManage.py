
import pymysql
class DbUser():
    def __init__(self, *args, **kwargs):
        self.posg = pymysql.connect

    def Conexion(self):
        try:
            credentials ={
                "host":"localhost",
                "user": "root",
                "password": "leonardo25537/*",
                "db":"administracion"
            }
            self.conexion = self.posg(**credentials)
            print('se establecio conexion')
            self.query = self.conexion.cursor()
           
            
        except :
            print('error interno abre el servidor de la bbdd')
            return 0
        return self.conexion, self.query

    def usersInit(self,*args):
        usuario = (args[0])
        

        try:
            
            sqlprueba = "select * from usuarios"
            sql = ''' SELECT * FROM usuarios  WHERE nombre='%s' '''%(usuario)
            connection = self.Conexion()
            print(usuario)
            connection[1].execute(sql)
            self.datas = connection[1].fetchone()
            print(self.datas)
            connection[0].commit()
            return self.datas


        except Exception as e:
            print(e) 
            
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
            sqlInsertData = ''' INSERT INTO productoscyg (producto,proveedor,costo ) VALUES('%s','%s','%s') '''%(materiaprima, proveedor, costInt)  
            connect[1].execute(sqlInsertData)
            connect[0].commit()
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
        except:
            print('error de conexion con la base de datos')


    def QueryUpdate(self,*args, **kwargs):
        pass

