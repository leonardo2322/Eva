import psycopg2 as pg 
from decouple import config

class Data():
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
            self.FullData()
            
            

        except (Exception, self.posg.DatabaseError) as error:
            print("ocurrio un error en la conexion",error)
        finally:
            if self.conexion is not None:
                print("finally conexion")
                self.conexion.close()
    def FullData(self):
        cursor = self.conexion.cursor()

        try:

            commands = ("""
            CREATE TABLE  Usuarios (
            idUser serial,
            nombre varchar, 
            password varchar(255),
            email varchar,
            status boolean,
            primary key(idUser)
            )
            """,
              """ CREATE TABLE  IngresosDiarios (
            idIngresos serial,
            Fecha timestamp,
            TipoDePago varchar,
            Categoria varchar,
            Valor decimal,
            Descripcion varchar,
            idUser integer REFERENCES Usuarios(idUser) ON UPDATE CASCADE ON DELETE RESTRICT,
            primary key(idIngresos)

            ) """,
              """ CREATE TABLE GastosDiarios (
            idGastos serial,
            Fecha timestamp,
            TipoDePago varchar,
            Categoria varchar,
            Valor decimal,
            Descripcion varchar,
            idUser integer REFERENCES Usuarios(idUser) ON UPDATE CASCADE  ON DELETE RESTRICT,
            primary key(idGastos)

            ) """,
            """ CREATE TABLE DetallesIngGastos (
            idDetailIngGasto serial,
            cantidadGastos decimal,
            cantidadIngresos decimal,
            saldo decimal,
            idGastos integer REFERENCES GastosDiarios(idGastos) ON UPDATE CASCADE  ON DELETE RESTRICT,
            idIngresos integer REFERENCES IngresosDiarios(idIngresos) ON UPDATE CASCADE  ON DELETE RESTRICT
            )
            """
            ,


             """
            CREATE TABLE  Proveedores (
                idProveedor serial,
                empresa varchar,
                productos varchar,
                status boolean,
                idUser integer REFERENCES Usuarios(idUser) ON UPDATE CASCADE ON DELETE RESTRICT,
                primary key(idProveedor)

            )       

            """,


             """
            CREATE TABLE OrdenProveedoresDetalles (
                idPedido serial,
                fechaPedido timestamp,
                fechaEntrega timestamp,
                metodoDePago varchar,
                idProveedor integer REFERENCES Proveedores(idProveedor) ON UPDATE CASCADE ON DELETE RESTRICT,
                idUser integer REFERENCES Usuarios(idUser) ON UPDATE CASCADE ON DELETE RESTRICT,
                primary key(idPedido)
            )
            """,

             """ CREATE TABLE ordenDetalle (
             
                idCliente serial,
                nombre varchar,
                cantidad integer,
                idProducto integer,
                primary key(idCliente)
                )

            """,

            """ CREATE TABLE Productos (
            idProducto serial,
            Nombre varchar,
            precio decimal,
            status boolean,
            idProveedor integer REFERENCES Proveedores(idProveedor) ON UPDATE CASCADE ON DELETE RESTRICT,
            primary key(idProducto)
            )
            """,
            """ CREATE TABLE Inventario (
             idinventario serial, 
	         precio decimal,
             peso integer,
             unidadMedida varchar,
             status boolean,
             idProveedor integer REFERENCES Proveedores(idProveedor) ON UPDATE CASCADE ON DELETE RESTRICT,
            idProducto integer REFERENCES Productos(idProducto) ON UPDATE CASCADE ON DELETE RESTRICT,
            primary key(idinventario)
            )
            
            """,
            """
            ALTER TABLE ordendetalle ADD FOREIGN KEY (idproducto) 
            REFERENCES productos(idproducto)
            """,
            """
            CREATE TABLE costosproductos (
            idcostop serial,
            gramo decimal,
            valorkg decimal,
            valorIng decimal,
            valortotal decimal,
            status boolean,
            idinventario integer REFERENCES Inventario(idinventario) ON UPDATE CASCADE ON DELETE RESTRICT,
            PRIMARY KEY(idcostop)
            )
            """,
            """ CREATE TABLE valortotalreceta (
            
                idvalortreceta serial,
                valorTotal decimal,
                idcostop integer REFERENCES costosproductos(idcostop) ON UPDATE CASCADE ON DELETE RESTRICT,
                primary key(idvalortreceta)

            )
            
            """

            
            )
            for command in commands:
                cursor.execute(command)

            self.conexion.commit()
            cursor.close()
            print("table created success")
        except self.posg.Error as e:
             print(e)
        finally:
            if self.conexion is not None:
                print("finally ejecucion")
                self.conexion.close()
                print('Database connection closed.')


Data()