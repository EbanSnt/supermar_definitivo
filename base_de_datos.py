import sqlite3

class BaseDatos:
    def crear_base_usuarios(self):
        self.conexion = sqlite3.connect("./base_datos/usuarios.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS USUARIOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NOMBRE TEXT,
                APELLIDO TEXT,
                DNI TEXT,
                TELEFONO INTEGER,
                DIRECCION TEXT,
                CORREO TEXT,
                ROL INTEGER,
                CONTRA TEXT)""")
        self.conexion.commit()
        self.conexion.close()

    def crear_base_productos(self):
        self.conexion = sqlite3.connect("./base_datos/productos.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS PRODUCTOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                CODIGO TEXT,
                PRODUCTO TEXT,
                MARCA TEXT,
                SECCION TEXT,
                PRECIO REAL,
                STOCK INTEGER,
                DESCRIPCION TEXT )""")
        self.conexion.commit()
        self.conexion.close()

    def crear_base_ventas(self):
        self.conexion = sqlite3.connect("./base_datos/ventas.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS VENTAS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NOMBRE TEXT,
                APELLIDO TEXT,
                DNI TEXT,
                TOTAL_COMPRA REAL,
                COMPROBANTE TEXT,
                FECHA TEXT,
                DESCRIPCION TEXT )""")
        self.conexion.commit()
        self.conexion.close()

    def insertar_datos_usuarios(self,nombre,apellido,dni,telefono,direccion,correo,rol,password):
        self.conexion = sqlite3.connect("./base_datos/usuarios.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"INSERT INTO USUARIOS VALUES (NULL,'{nombre}','{apellido}','{dni}'" 
                            f",{telefono},'{direccion}','{correo}',{rol},'{password}')")
        self.conexion.commit()
        self.conexion.close()

    def insertar_datos_productos(self,codigo,producto,marca,seccion,precio,stock,descripcion):
        self.conexion = sqlite3.connect("./base_datos/productos.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"INSERT INTO PRODUCTOS VALUES  (NULL,'{codigo}','{producto}','{marca}'"
                            f",'{seccion}',{precio},{stock},'{descripcion}')")
        self.conexion.commit()
        self.conexion.close()

    def insertar_datos_ventas(self,nombre,apellido,dni,total,comprobante,fecha,descripcion):
        self.conexion = sqlite3.connect("./base_datos/ventas.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"INSERT INTO VENTAS VALUES (NULL,'{nombre}','{apellido}','{dni}'"
                            f",{total},'{comprobante}','{fecha}','{descripcion}')")
        self.conexion.commit()
        self.conexion.close()

    def actualizar_datos_usuarios(self,nombre,apellido,dni,telefono,direccion,correo,rol,password):
        self.conexion = sqlite3.connect("./base_datos/usuarios.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM USUARIOS")
        consulta = """UPDATE USUARIOS SET NOMBRE = ?, APELLIDO = ?, TELEFONO = ?, DIRECCION = ?, CORREO = ?, ROL = ?, CONTRA = ? WHERE DNI = ?"""
        parametros = (nombre,apellido,telefono,direccion,correo,rol,password,dni)
        self.cursor.execute(consulta,parametros)
        self.conexion.commit()
        self.conexion.close()

    def actualizar_datos_productos(self,codigo,producto,marca,seccion,precio,stock,descripcion):
        self.conexion = sqlite3.connect("./base_datos/productos.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM PRODUCTOS")
        consulta = """ UPDATE PRODUCTOS SET PRODUCTO = ? , MARCA = ?, PRECIO = ?, SECCION = ?, STOCK = ?,DESCRIPCION = ? WHERE CODIGO = ? """
        parametros = (producto,marca,precio,seccion,stock,descripcion,codigo)
        self.cursor.execute(consulta,parametros)
        self.conexion.commit()
        self.conexion.close()

    def actualizar_datos_productos_usuarios_menos(self,codigo):
        self.conexion = sqlite3.connect("./base_datos/productos.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM PRODUCTOS")
        consulta = """ UPDATE PRODUCTOS SET STOCK = STOCK - 1 WHERE CODIGO = ? """
        parametros = codigo,
        self.cursor.execute(consulta,parametros)
        self.conexion.commit()
        self.conexion.close()
    def actualizar_datos_productos_usuarios_mas(self,codigo):
        self.conexion = sqlite3.connect("./base_datos/productos.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM PRODUCTOS")
        consulta = """ UPDATE PRODUCTOS SET STOCK = STOCK + 1 WHERE CODIGO = ? """
        parametros = codigo,
        self.cursor.execute(consulta,parametros)
        self.conexion.commit()
        self.conexion.close()


