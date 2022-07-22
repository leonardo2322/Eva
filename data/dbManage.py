
import pymysql
from datetime import date
from decouple import config
class db():
    def __init__(self):
        self.MDataBase = pymysql.connect
        try:
            credentials = {
                "host":config('SQL_LOCAL_HOST'),
                "user": config('SQL_USER'),
                "password": config('SQL_PASSWORD'),
            }
            self.conexion =self.MDataBase(**credentials)
            manage =self.conexion.cursor()

            database = """CREATE DATABASE IF NOT EXISTS administracion"""
            use = "use administracion"


            if manage.execute(database):
                print('base de datos creada')
            else:
                print('la base de datos ya esta creada')
            manage.execute(use)
            tableuser = """create table if not exists  usuarios(
	                        id integer auto_increment,
                            nombre varchar(20),
                            passwor varchar(250),
                            primary key(id)
                        );
                        """
            manage.execute(tableuser)
            useradmin = """insert into usuarios  (nombre, passwor) select * from (select '%s','%s') as new_value
                             where not exists (select nombre from usuarios where nombre='admin')limit 1;"""% (config('USER_ADMIN'),config('USER_PASSWORD'))

            if manage.execute(useradmin):
                print('usuario administrador insertado')
            else:
                print('ya esta registrado el usuario admin')
            tablecyg = """create table if not exists productoscyg(
                id bigint auto_increment,
                fecha date,
                materiaprima varchar(70) not null,
                proveedor varchar(20) not null,
                costo bigint not null,
                primary key(id)
                )
            """

            if manage.execute(tablecyg):
                print('tabla creada')
            else:
                print('ya esta creada la tabla')
        except Exception as e:
            print(e)



class DbUser():
    def __init__(self, *args, **kwargs):
        self.posg = pymysql.connect

    def Conexion(self):
        try:
            credentials ={
                "host":config('SQL_LOCAL_HOST'),
                "user": config('SQL_USER'),
                "password": config('SQL_PASSWORD'),
                "db":"administracion"
            }
            self.conexion = self.posg(**credentials)
            print(credentials)
            print('se establecio conexion')
            self.query = self.conexion.cursor()
           
            
        except :
            print('error interno abre el servidor de la bbdd')
            return 0
        return self.conexion, self.query

    def usersInit(self,*args):
        usuario = (args[0])
        

        try:
            
            sql = ''' SELECT * FROM usuarios  WHERE nombre='%s' '''%(usuario)
            connection = self.Conexion()
            connection[1].execute(sql)
            self.datas = connection[1].fetchone()
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
            sqlSelect = '''SELECT * FROM productoscyg'''
            connection[1].execute(sqlSelect)
            
            
            self.data = connection[1].fetchall()
            connection[0].commit()

            
            
        except:
            print('error de conexion con la base de datos al seleccionar')
        finally:
            connection[1].close()    
            connection[0].close()
        return self.data
    def QueryInsert(self, materiaprima, proveedor, costo, *args, **kwargs):
        connect = self.Conexion()
        costInt = int(costo)
        fecha = date.today()

        try:
            sqlInsertData = ''' INSERT INTO productoscyg (fecha,materiaprima,proveedor,costo ) VALUES('%s','%s','%s','%s') '''%(fecha,materiaprima, proveedor, costInt)  
            connect[1].execute(sqlInsertData)
            connect[0].commit()
        except:
            print('error de conexion con la base de datos al insertar')
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
            print('error de conexion con la base de datos al eliminar')


    def QueryUpdate(self,*args, **kwargs):
        pass

