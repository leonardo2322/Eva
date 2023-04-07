import psycopg2 as pg 

class Data():
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
            self.FullData()
            
            

        except self.posg.Error as e:
            print("ocurrio un error en la conexion",e)
        finally:
            self.conexion.close()
    def FullData(self):
        cursor = self.conexion.cursor()

        try:
            tablaUsuarios = """
            CREATE TABLE IF NOT EXISTS Usuarios (
            idUser serial,
            nombre varchar, 
            password varchar(255),
            email varchar,
            primary key(idUser)
            )
            """
            cursor.execute(tablaUsuarios)
            tableIngresosDiarios = """ CREATE TABLE IF NOT EXISTS IngresosDiarios (
            idIngresos serial,
            Fecha timestamp,
            TipoDePago varchar,
            Categoria varchar,
            Valor integer,
            Descripcion varchar,
            idUser integer REFERENCES Usuarios(idUser) ON DELETE RESTRICT,
            primary key(idIngresos)

            ) """
            cursor.execute(tableIngresosDiarios)
            tableGastosDiarios = """ CREATE TABLE IF NOT EXISTS GastosDiarios (
            idGastos serial,
            Fecha timestamp,
            TipoDePago varchar,
            Categoria varchar,
            Valor integer,
            Descripcion varchar,
            idUser integer REFERENCES Usuarios(idUser) ON DELETE RESTRICT,
            primary key(idGastos)

            ) """

            cursor.execute(tableGastosDiarios)

            tableProveedores = """
            CREATE TABLE IF NOT EXISTS Proveedores (
                idProveedor serial,
                empresa varchar,
                fechaPedido timestamp,
                fechaEntrega timestamp,
                metodoDePago varchar,
                productos varchar,
                status boolean,
                primary key(idProveedor)

            )            
            """
            cursor.execute(tableProveedores)
            print("table created success")
        except self.posg.Error as e:
             print(e)

Data()