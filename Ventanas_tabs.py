from tkinter import ttk,messagebox
from tkinter import *
from PIL import ImageTk,Image
from productos_tab_admin import ProductosTabs
from usuarios_tab_admin import UsuariosTab
from ventas_realizadas_tab_admin import ComprasTabUsers
from productos_tab_user import  ProductosTabUsers
from base_de_datos import BaseDatos
import sqlite3


# Ventana de Login.
class VentanaLogin:
    def __init__(self):
        self.principal()

    def principal(self):
        base = BaseDatos()
        base.crear_base_usuarios()
        base.crear_base_productos()
        base.crear_base_ventas()
        # Configuracion de Ventana
        self.ventana = Tk()
        self.ventana.geometry("350x350")
        self.ventana.resizable(False, False)
        self.ventana.title("Supermark")
        self.imagen = Image.open("./imagenes/carrito_logo.png")
        self.imagen = self.imagen.resize((150, 150))
        self.imagen_inicio = ImageTk.PhotoImage(self.imagen)
        Label(self.ventana, image=self.imagen_inicio).place(x=100, y=20)

        # Entry de Logueo
        Label(self.ventana, text="DNI").place(x=100, y=180)
        self.usuario_login = Entry(self.ventana)
        self.usuario_login.place(x=100, y=200)

        Label(self.ventana, text="Contraseña").place(x=100, y=220)
        self.password_login = Entry(self.ventana)
        self.password_login.place(x=100, y=240)
        # Botones
        iniciar_sesion_boton = Button(self.ventana, text="Iniciar Sesion", justify="center", command=self.pasar_pagina)
        iniciar_sesion_boton.place(x=120, y=280)
        iniciar_sesion_boton["activebackground"] = "#000"
        iniciar_sesion_boton["activeforeground"] = "#fff"
        iniciar_sesion_boton["bg"] = "#A2E62E"

        registro_boton = Button(self.ventana, text="Registrarse", justify="center", command=self.registro_ventana)
        registro_boton.place(x=270, y=310)
        registro_boton["activebackground"] = "#000"
        registro_boton["activeforeground"] = "#fff"
        registro_boton["bg"] = "#D98C27"
        self.ventana.mainloop()

    def registro_ventana(self):
        self.ventana.destroy()
        self.ventana_registro = Tk()
        self.ventana_registro.geometry("350x450")
        self.ventana_registro.resizable(False, False)
        self.ventana_registro.title("Supermark")
        self.imagen = Image.open("./imagenes/carrito_logo.png")
        self.imagen = self.imagen.resize((80, 80))
        self.imagen_inicio = ImageTk.PhotoImage(self.imagen)
        Label(self.ventana_registro, image=self.imagen_inicio).place(x=40, y=20)

        # Entry y Label
        Label(self.ventana_registro,text="REGISTRO").place(x=180,y=20)
        Label(self.ventana_registro, text="Nombre").place(x=150, y=50)
        self.nombre_entry = Entry(self.ventana_registro)
        self.nombre_entry.place(x=150,y=70)

        Label(self.ventana_registro, text="Apellido").place(x=150, y=90)
        self.apellido_entry = Entry(self.ventana_registro)
        self.apellido_entry.place(x=150, y=110)

        Label(self.ventana_registro, text="DNI").place(x=150, y=130)
        self.dni_entry = Entry(self.ventana_registro)
        self.dni_entry.place(x=150, y=150)

        Label(self.ventana_registro, text="Telefono").place(x=150, y=170)
        self.telefono_entry = Entry(self.ventana_registro)
        self.telefono_entry.place(x=150, y=190)

        Label(self.ventana_registro, text="Direccion").place(x=150, y=210)
        self.direccion_entry = Entry(self.ventana_registro)
        self.direccion_entry.place(x=150, y=230)

        Label(self.ventana_registro, text="Correo").place(x=150, y=250)
        self.correo_entry = Entry(self.ventana_registro)
        self.correo_entry.place(x=150, y=270)

        Label(self.ventana_registro, text="Rol 1-Admin 2-Usuario").place(x=150, y=290)
        self.rol_entry = Entry(self.ventana_registro)
        self.rol_entry.place(x=150, y=310)

        Label(self.ventana_registro, text="Contraseña").place(x=150, y=330)
        self.password_entry = Entry(self.ventana_registro)
        self.password_entry.place(x=150, y=350)

        enviar_datos = Button(self.ventana_registro,text="Enviar datos",command=self.enviar_datos)
        enviar_datos.place(x=250,y=390)
        enviar_datos["activebackground"] = "#000"
        enviar_datos["activeforeground"] = "#fff"
        enviar_datos["bg"] = "#C84A2F"
        self.ventana_registro.mainloop()

    def validacion_datos(self):
        return not self.nombre_entry.get() or not self.apellido_entry.get() or not self.dni_entry.get() \
        or not self.telefono_entry.get() or not self.direccion_entry.get() or not self.correo_entry.get() \
        or not self.rol_entry.get() or not self.password_entry.get()
    def enviar_datos(self):
        if self.validacion_datos() == True:
            messagebox.showerror("Aviso","No deben quedar campos vacios")
        else:
            base = BaseDatos()
            base.insertar_datos_usuarios(self.nombre_entry.get(),self.apellido_entry.get(),
                                         self.dni_entry.get(),self.telefono_entry.get(),
                                         self.direccion_entry.get(),self.correo_entry.get(),
                                         self.rol_entry.get(),self.password_entry.get())

            messagebox.showinfo("Aviso","Envio exitoso")
            self.ventana_registro.destroy()
            self.principal()

    def pasar_pagina(self):
        self.nombre = self.usuario_login.get()
        self.password = self.password_login.get()
        base = BaseDatos()
        base.crear_base_usuarios()
        self.conexion = sqlite3.connect("./base_datos/usuarios.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"SELECT * FROM USUARIOS WHERE DNI = ? AND CONTRA = ? AND ROL = ?",(self.nombre,self.password,101))
        if self.nombre and self.password:
            if self.cursor.fetchone():
                messagebox.showinfo("Aviso", "Logueo exitoso (Administrador)")
                self.ventana.destroy()
                VentanaAdministrador()
            else:
                messagebox.showinfo("Aviso", "Logueo exitoso (Usuario)")
                self.ventana.destroy()
                VentanaUsuario()

        else:
            messagebox.showerror("Aviso", "DNI y/o Contraseña incorrecto/os")



class VentanaAdministrador:
    def __init__(self):
        base = BaseDatos()
        base.crear_base_productos()
        base.crear_base_usuarios()
        base.crear_base_ventas()
        self.principal()

    def principal(self):
        self.ventana = Tk()
        self.ventana.geometry("800x600")
        self.ventana.resizable(False,False)
        self.ventana.title("Supermark")
        # Falta Agregar icono a la ventana
        contenedor_logo = Frame(self.ventana,background="black")
        contenedor_logo.place(width=800,height=70,x=0,y=0)
        contenedor_tabs = Frame(self.ventana,background="blue")
        contenedor_tabs.place(x=0,y=75,width=800,height=510)
        # Pestañas (Configuracion)
        self.imagen = Image.open("./imagenes/carrito_logo.png")
        self.imagen = self.imagen.resize((50, 50))
        self.imagen_inicio = ImageTk.PhotoImage(self.imagen)
        Label(contenedor_logo,image=self.imagen_inicio).place(x=10,y=10)

        self.imagen2 = Image.open("./imagenes/logo_inicio.jpg")
        self.imagen2 = self.imagen2.resize((50, 50))
        self.imagen_inicio2 = ImageTk.PhotoImage(self.imagen2)
        Label(contenedor_logo, image=self.imagen_inicio2).place(x=730, y=10)
        Label(contenedor_logo, text="Esteban Santillan\n2022 CM1",font=("bold",8),background="black",foreground="white",justify="center").place(x=640, y=10)

        Label(contenedor_logo,text="GESTION SUPERMARKET (ADMIN)",font=("bold",20),background="black",foreground="White").place(x=100,y=20)
        tabs = ttk.Notebook(self.ventana)
        tabs.place(x=0,y=70,height=530,width=800)
        usuarios = Frame(tabs,background="blue")
        productos = Frame(tabs,background="black")
        ventas = Frame(tabs,background="black")
        tabs.add(productos,text="  Productos  ")
        tabs.add(usuarios,text="  Usuarios  ")
        tabs.add(ventas,text="  Ventas realizadas  ")
        # Se inicializan las pestañas
        productos_tab = ProductosTabs()
        productos_tab.principal(self.ventana,productos)
        usuarios_tab = UsuariosTab()
        usuarios_tab.principal(self.ventana,usuarios)
        ventas_tab = ComprasTabUsers()
        ventas_tab.principal(self.ventana,ventas)
        # Boton refrescar pagina
        refrescar_datos = Button(productos, text="Refrescar Pagina", justify="center", command=self.destruir_ventana)
        refrescar_datos.place(x=320, y=370)
        refrescar_datos["activebackground"] = "#000"
        refrescar_datos["activeforeground"] = "#fff"
        refrescar_datos["bg"] = "lightblue"
        refrescar_datos.config(height=2)

        refrescar_datos = Button(usuarios, text="Refrescar Pagina", justify="center", command=self.destruir_ventana)
        refrescar_datos.place(x=320, y=370)
        refrescar_datos["activebackground"] = "#000"
        refrescar_datos["activeforeground"] = "#fff"
        refrescar_datos["bg"] = "lightblue"
        refrescar_datos.config(height=2)

        self.ventana.mainloop()
    def destruir_ventana(self):
        self.ventana.destroy()
        self.principal()


class VentanaUsuario:
    def __init__(self):
        self.principal()
    def principal(self):
        self.ventana = Tk()
        self.ventana.geometry("850x600")
        self.ventana.resizable(False,False)
        self.ventana.title("Supermark")
        # Falta Agregar icono a la ventana
        contenedor_logo = Frame(self.ventana,background="BLACK")
        contenedor_logo.place(width=850,height=70,x=0,y=0)
        contenedor_tabs = Frame(self.ventana,background="black")
        contenedor_tabs.place(x=0,y=75,width=850,height=510)

        # Pestañas (Configuracion)
        self.imagen = Image.open("./imagenes/carrito_logo.png")
        self.imagen = self.imagen.resize((50, 50))
        self.imagen_inicio = ImageTk.PhotoImage(self.imagen)
        Label(contenedor_logo, image=self.imagen_inicio).place(x=10, y=10)

        self.imagen2 = Image.open("./imagenes/logo_inicio.jpg")
        self.imagen2 = self.imagen2.resize((50, 50))
        self.imagen_inicio2 = ImageTk.PhotoImage(self.imagen2)
        Label(contenedor_logo, image=self.imagen_inicio2).place(x=730, y=10)
        Label(contenedor_logo, text="Esteban Santillan\n2022 CM1", font=("bold", 8), background="black",
              foreground="white", justify="center").place(x=640, y=10)

        Label(contenedor_logo, text="BIENVENIDO A SUPERMARKET :)", font=("bold", 20), background="black",
              foreground="White").place(x=100, y=20)

        tabs = ttk.Notebook(self.ventana)
        tabs.place(x=0,y=70,height=530,width=850)
        productos = Frame(tabs,background="black")
        tabs.add(productos,text="  Productos  ")

        productos_tab = ProductosTabUsers()
        productos_tab.principal(self.ventana,productos)


        self.ventana.mainloop()

    def destruir_ventana(self):
        self.ventana.destroy()
        self.principal()

VentanaLogin()