from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
from base_de_datos import BaseDatos

import sqlite3

class VentanaLogin:
    def __init__(self):
        self.principal()
    def principal(self):
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
        Label(self.ventana,text="DNI").place(x=100,y=180)
        self.usuario_login = Entry(self.ventana)
        self.usuario_login.place(x=100,y=200)

        Label(self.ventana, text="Contraseña").place(x=100, y=220)
        self.password_login = Entry(self.ventana)
        self.password_login.place(x=100, y=240)
        # Botones
        iniciar_sesion_boton = Button(self.ventana,text="Iniciar Sesion",justify="center",command=self.pasar_pagina)
        iniciar_sesion_boton.place(x=120, y=280)
        iniciar_sesion_boton["activebackground"] = "#000"
        iniciar_sesion_boton["activeforeground"] = "#fff"
        iniciar_sesion_boton["bg"] = "#A2E62E"


        registro_boton = Button(self.ventana, text="Registrarse", justify="center",command=self.registro_ventana)
        registro_boton.place(x=270, y=310)
        registro_boton["activebackground"] = "#000"
        registro_boton["activeforeground"] = "#fff"
        registro_boton["bg"] = "#D98C27"
        self.ventana.mainloop()

    def registro_ventana(self):
        self.ventana.destroy()
        self.ventana_registro = Tk()
        self.ventana_registro.geometry("350x350")
        self.ventana_registro.resizable(False, False)
        self.ventana_registro.title("Supermark")
        self.imagen = Image.open("./imagenes/carrito_logo.png")
        self.imagen = self.imagen.resize((50, 50))
        self.imagen_inicio = ImageTk.PhotoImage(self.imagen)
        Label(self.ventana_registro, image=self.imagen_inicio).place(x=40, y=20)
        self.ventana_registro.mainloop()
    def pasar_pagina(self):
        nombre = self.usuario_login.get()
        password = self.password_login.get()
        base= BaseDatos()
        base.crear_base_usuarios()
        self.conexion = sqlite3.connect("./base_datos/usuarios.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"SELECT * FROM USUARIOS WHERE DNI = ? AND CONTRA = ? ",[nombre,password])
        if self.cursor.fetchall():
            messagebox.showinfo("Aviso","Logueo exitoso")
            self.cursor.execute(f"SELECT * FROM USUARIOS WHERE ROL = 1")
            if self.cursor.fetchall():

            else:
                pass
        else:
            messagebox.showerror("Aviso","DNI y/o Contraseña incorrecto/os")

VentanaLogin()