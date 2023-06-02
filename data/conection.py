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
        self.cursor = None
        self.name = None
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
         
    def SumaTotalIngGas(self,id,desc):
        query = (""" SELECT SUM(valor) FROM ingresosdiarios """,
                 
                """SELECT SUM(valor) FROM gastosdiarios""",
                )
        data = []
        
        try:
            for i in query:
                self.cursor.execute(i)
                result = self.cursor.fetchone()
                print(result)
                if result not in data:
                    data.append(result[0])
            if data[1] == None :
                 data[1] = 0
                 saldo = data[0] 
            elif  data[0] == None:
                 data[0] = 0
                 saldo = data[1]
            else:
                 saldo = data[0] - data[1]
            self.cursor.execute("""INSERT INTO DetallesIngGastos (cantidadGastos, cantidadIngresos, saldo,description, iduser)
                VALUES({},{},{},'{}',{})  """.format(data[1],data[0],saldo,desc,id))
        except self.posg.Error as e:
            print(e)
            return e
    def SelectFromDB(self, name=None, selection = None , tableSearch=None,SelectTable=None,names=None, ID=None, *args,**kwargs):
        if selection == method['USER'] and name is not None:
            
                self.conection()
            
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
                self.name = name
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
        elif selection == method['ing']['ing']:
            try:
                query = """ SELECT * FROM {} """.format(SelectTable)
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                data = []
                name = names
                for res in result:
                    d = {}
                    for i in range(0,len(res)):
                        stre = names[i]
                        d['{}'.format(stre)] = res[i]                                       
                    data.append(d)
                        
                return data
            except self.posg.Error as e:
                    print("ocurrio un error en la conexion",e)
                    return 'error'
            finally:
                    self.cursor.close()
                    self.conexion.close()
        elif selection == method['search']:
            query = """ SELECT * FROM {} WHERE {} = {} """.format(SelectTable,kwargs['ide'],ID)
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result


        elif selection == 'balance':
            query = "SELECT * FROM {} ORDER BY {} DESC LIMIT 1".format(SelectTable, ID)
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result

    def QueryInsert(self,  types = ins['ing'], datos = [],*args):
        if types == ins['ing']:
            self.conection()

            try:
                    self.cursor.execute("""INSERT INTO ingresosdiarios (fecha, tipodepago, categoria,divisa, valor, descripcion, iduser) values ('{}', '{}', '{}','{}', {}, '{}', {})""".format(datos[0]['fecha'], datos[0]['tipodepago'], datos[0]['categoria'],datos[0]['divisa'], datos[0]['valor'], datos[0]['descripcion'], datos[0]['iduser'] ))
                    print('insertion success')
                    self.SumaTotalIngGas(datos[0]['iduser'],datos[0]['descripcion'])

                    return 'ok'
            except self.posg.Error as e :
                    print(e)
                    return 'error'
        
        elif types == ins['gas']:
                self.conection()
                try:
                    self.cursor.execute("""INSERT INTO gastosdiarios (fecha, tipodepago, categoria,divisa, valor, descripcion, iduser) values ('{}', '{}', '{}','{}', {}, '{}', {})""".format(datos[0]['fecha'], datos[0]['tipodepago'], datos[0]['categoria'],datos[0]['divisa'], datos[0]['valor'], datos[0]['descripcion'], datos[0]['iduser'] ))
                    print('insertion success')
                    self.SumaTotalIngGas(datos[0]['iduser'], datos[0]['descripcion'])
                    return 'ok'
                except Exception as e :
                    print(e)
                    return 'error'
        else :
            return 'error'
    def QueryDelete(self, tabla, id, idTabla,userId):
        try:
            query = """ DELETE FROM {} WHERE {} = {} """.format(tabla,idTabla,id)
            self.cursor.execute(query)
            query2 = """ DELETE FROM detallesinggastos WHERE description = '{}' """.format(self.name)
            self.cursor.execute(query2)
            self.SumaTotalIngGas(userId, 'eliminaciones')
            return 'success'
        except self.posg.Error as e :
            print("ocurrio un error en la conexion",e)
            return 'error'
        finally:
            self.cursor.close()
            self.conexion.close()
          

    def QueryUpdate(self, Id, idtable,idID,data = []):
        try:
            query ="UPDATE {} SET fecha ='{}', tipodepago='{}' , categoria='{}', divisa='{}',valor={},descripcion='{}' WHERE {} = {} ".format(idtable, data[0],data[1],data[2],data[3],data[4],data[5],idID,Id)
            self.cursor.execute(query)
            return 'ok'
        except self.posg.Error as e:
            print(e)
            return 'error'
        finally:
            self.cursor.close()
            self.conexion.close()

