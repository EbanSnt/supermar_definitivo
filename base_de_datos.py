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
                ROL INTEGER,
                CONTRASEÑA TEXT)""")
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
                DESCRIPCION TEXT)""")
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
                DESCRIPCION TEXT)""")
        self.conexion.commit()
        self.conexion.close()

    def insertar_datos_usuarios(self,nombre,apellido,dni,telefono,direccion,rol,password):
        self.conexion = sqlite3.connect("./base_datos/usuarios.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"INSERT INTO USUARIOS VALUES (NULL,'{nombre}','{apellido}','{dni}'" 
                            f",{telefono},'{direccion}',{rol},'{password}')")
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
        self.cursor.execute(f"INSERT INTO PRODUCTOS VALUES (NULL,'{nombre}','{apellido}','{dni}'"
                            f",{total},'{comprobante}','{fecha}','{descripcion}')")
        self.conexion.commit()
        self.conexion.close()

    def actualizar_datos_usuarios(self,nombre,apellido,dni,telefono,direccion,rol,password):
        self.conexion = sqlite3.connect("./base_datos/usuarios.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM USUARIOS")
        self.cursor.execute(f"UPDATE USUARIOS"
                            f"SET NOMBRE = '{nombre}', SET APELLIDO = '{apellido}', SET DNI = '{dni}',"
                            f"SET TELEFONO = {telefono}, SET DIRECCION = '{direccion}', SET ROL = {rol}, SET CONTRASEÑA = '{password}';")
        self.conexion.commit()
        self.conexion.close()

    def actualizar_datos_productos(self,codigo,producto,marca,seccion,precio,stock,descripcion):
        self.conexion = sqlite3.connect("../base_datos/productos.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM PRODUCTOS")
        self.cursor.execute(f"UPDATE USUARIOS"
                            f"SET CODIGO = '{codigo}', SET PRODUCTO = '{producto}', SET MARCA = '{marca}',"
                            f"SET PRECIO = {precio},SET SECCION = '{seccion}' SET STOCK = {stock}, SET DESCRIPCION = '{descripcion}';")
        self.conexion.commit()
        self.conexion.close()

    def eliminar_datos_usuarios(self,dni,telefono):
        self.conexion = sqlite3.connect("usuarios.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM USUARIOS")
        self.cursor.execute(f"DELETE FROM USUARIOS WHERE DNI = '{dni}' , WHERE TELEFONO = {telefono}")
        self.conexion.commit()
        self.conexion.close()

    def eliminar_datos_productos(self,codigo,id):
        self.conexion = sqlite3.connect("productos.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM PRODUCTOS")
        self.cursor.execute(f"DELETE FROM PRODUCTOS WHERE DNI = '{codigo}' , WHERE ID = {id}")
        self.conexion.commit()
        self.conexion.close()

