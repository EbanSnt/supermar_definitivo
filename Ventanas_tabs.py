from tkinter import ttk
from tkinter import *
from productos_tab_admin import ProductosTabs
from usuarios_tab_admin import UsuariosTab
from base_de_datos import BaseDatos

class Ventana:
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
        contenedor_logo = Frame(self.ventana,background="red")
        contenedor_logo.place(width=800,height=70,x=0,y=0)
        contenedor_tabs = Frame(self.ventana,background="blue")
        contenedor_tabs.place(x=0,y=75,width=800,height=510)
        # Pestañas (Configuracion)
        tabs = ttk.Notebook(self.ventana)
        tabs.place(x=0,y=70,height=510,width=800)
        usuarios = Frame(tabs,background="yellow")
        productos = Frame(tabs,background="green")
        ventas = Frame(tabs)
        tabs.add(productos,text="  Productos  ")
        tabs.add(usuarios,text="  Usuarios  ")
        tabs.add(ventas,text="  Ventas realizadas  ")
        # Se inicializan las pestañas
        productos_tab = ProductosTabs()
        productos_tab.principal(self.ventana,productos)
        usuarios_tab = UsuariosTab()
        usuarios_tab.principal(self.ventana,usuarios)
        # Boton refrescar pagina
        refrescar_datos = Button(productos, text="Refrescar Pagina", justify="center", command=self.destruir_ventana)
        refrescar_datos.place(x=40, y=420)
        refrescar_datos["activebackground"] = "#000"
        refrescar_datos["activeforeground"] = "#fff"
        refrescar_datos["bg"] = "#C84A2F"
        refrescar_datos.config(height=2)

        self.ventana.mainloop()
    def destruir_ventana(self):
        self.ventana.destroy()
        Ventana()

Ventana()