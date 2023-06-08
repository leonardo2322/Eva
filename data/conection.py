import psycopg2 as pg
from decouple import config
from data.methods import methodsUSER as method, methodINSERT as ins, current_date_format
from datetime import datetime 
import re
import math
patron = re.compile('([0-9]+)')
class DbUser():
    def __init__(self):
        super(DbUser,self)
        self.posg = pg
        self.conexion=None
        self.conection()
        self.cursor = None
        self.name = None
        self.bolivares = 1
        self.Pesos = 1
        self.euros = 1
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
                for value in result:
                    d = {}
                    for i in range(0,len(value)):
                        key = names[i]
                        d['{}'.format(key)] = value[i]                                       
                    data.append(d)
                if SelectTable == 'divisas':
                     return data
                else:
                    if d['Divisa'] == 'Bolivares':
                        d['Valor'] = round(float(d['Valor']) * self.bolivares,2)
                    if d['Divisa'] == 'Pesos':
                        d['Valor'] = round(self.Pesos * d['Valor'],3)
                        print(d['Valor'],self.Pesos)
                    if d['Divisa'] == 'Euros':
                        d['Divisa'] = round(int(d['Valor']) * self.euros,2)  
                    print(d['Valor'])
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
            print(result)
            return result
    
    def Selectionfromdivisa(self):
         divisas = ['Bolivares','Pesos', 'Euros']
         try:
            for i in divisas:
                
                query = f"SELECT nombre,valor FROM divisas WHERE fecha = (SELECT MAX(fecha) FROM divisas WHERE nombre = '{i}')"
                self.cursor.execute(query)
                result = self.cursor.fetchone()
                if result[0] == 'Bolivares':
                    self.bolivares = result[1]
                elif result[0] == 'Pesos':
                    self.Pesos = result[1]
                elif result[0] == 'Euros':
                    self.euros = result[1]
                print(self.euros, self.bolivares, self.Pesos)
         except Exception as e:
             print(e)

    def QueryInsert(self,  types = ins['ing'], datos = [],*args,**kwarsg):
        if types == ins['ing']:
            self.conection()

            try:
                ResulTValue = None    
                if datos[0]['divisa'] == 'Bolivares':
                    ResulTValue = float(datos[0]['valor']) / float(self.bolivares)
                elif datos[0]['divisa'] == 'Pesos':
                    ResulTValue = float(datos[0]['valor']) / float(self.Pesos)
                    print(ResulTValue)
                elif datos[0]['divisa'] == 'Euros':
                    ResulTValue = float(datos[0]['valor']) / float(self.euros)
                else:
                    print('nada')
                    ResulTValue = datos[0]['valor']
                self.cursor.execute("""INSERT INTO ingresosdiarios (fecha, tipodepago, categoria,divisa, valor, descripcion, iduser) values ('{}', '{}', '{}','{}', {}, '{}', {})""".format(datos[0]['fecha'], datos[0]['tipodepago'], datos[0]['categoria'],datos[0]['divisa'], round(ResulTValue,2), datos[0]['descripcion'], datos[0]['iduser'] ))
                print('insertion success')
                self.SumaTotalIngGas(datos[0]['iduser'],datos[0]['descripcion'])

                return 'ok'
            except self.posg.Error as e :
                    print(e)
                    return 'error'
        
        elif types == ins['gas']:
                self.conection()
                try:
                    ResulTValue = None    
                    if datos[0]['divisa'] == 'Bolivares':
                        ResulTValue = float(datos[0]['valor']) / float(self.bolivares)
                    elif datos[0]['divisa'] == 'Pesos':
                        ResulTValue = float(datos[0]['valor']) / float(self.Pesos)
                    elif datos[0]['divisa'] == 'Euros':
                        ResulTValue = float(datos[0]['valor']) / float(self.euros)
                    else:
                        print('nada')
                        ResulTValue = datos[0]['valor']
                    self.cursor.execute("""INSERT INTO gastosdiarios (fecha, tipodepago, categoria,divisa, valor, descripcion, iduser) values ('{}', '{}', '{}','{}', {}, '{}', {})""".format(datos[0]['fecha'], datos[0]['tipodepago'], datos[0]['categoria'],datos[0]['divisa'],round(ResulTValue,2), datos[0]['descripcion'], datos[0]['iduser'] ))
                    print('insertion success')
                    self.SumaTotalIngGas(datos[0]['iduser'], datos[0]['descripcion'])
                    return 'ok'
                except Exception as e :
                    print(e)
                    return 'error'
        elif types == 'divisa':
           
            try:
                time = current_date_format(datetime.now())
                query = """INSERT INTO divisas (fecha, nombre, valor,iduser) VALUES
                ('{}','{}',{},{})""".format(time,kwarsg['div'],kwarsg['val'],kwarsg['id'])
                self.cursor.execute(query)
                if kwarsg['div'] == 'Bolivares':
                     self.bolivares = kwarsg['val']
                elif kwarsg['div'] == 'Pesos':
                     self.Pesos = kwarsg['val']
                elif kwarsg['div'] == 'Euros':
                     self.euros = kwarsg['val']
                print(self.bolivares,self.euros,self.Pesos)
                return 'success', kwarsg
            except Exception as e:
                print(e)
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

