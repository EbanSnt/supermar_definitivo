from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
from base_de_datos import BaseDatos
from datetime import date
from datetime import datetime

class ProductosTabUsers:
    def principal(self, ventana, frame):
        base = BaseDatos()
        base.crear_base_ventas()
        self.contenedor_tabla = Frame(ventana, height=350, width=400)
        self.tabla = ttk.Treeview(frame, height=16,
                                  columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7"))
        self.tabla.place(relx=0.01, rely=0.02)

        self.tabla.column("#1", width=80, anchor=CENTER)
        self.tabla.column("#2", width=80, anchor=CENTER)
        self.tabla.column("#3", width=80, anchor=CENTER)
        self.tabla.column("#4", width=80, anchor=CENTER)
        self.tabla.column("#5", width=80, anchor=CENTER)
        self.tabla.column("#6", width=80, anchor=CENTER)
        self.tabla.column("#7", width=140, anchor=CENTER)

        self.tabla["show"] = "headings"
        self.tabla.heading("#1", text="CODIGO", anchor=CENTER)
        self.tabla.heading("#2", text="PRODUCTO", anchor=CENTER)
        self.tabla.heading("#3", text="MARCA", anchor=CENTER)
        self.tabla.heading("#4", text="SECCION", anchor=CENTER)
        self.tabla.heading("#5", text="PRECIO", anchor=CENTER)
        self.tabla.heading("#6", text="STOCK", anchor=CENTER)
        self.tabla.heading("#7", text="DESCRIPCION", anchor=CENTER)
        # Insertar datos en la tabla
        self.base_de_datos = BaseDatos()
        self.base_de_datos.crear_base_productos()
        self.conexion = sqlite3.connect("./base_datos/productos.db")
        self.cursor = self.conexion.cursor()
        self.insertar = self.cursor.execute("SELECT * FROM PRODUCTOS")
        for dato in self.insertar:
            self.tabla.insert('', 0, values=(dato[1], dato[2], dato[3], dato[4], dato[5],
                                             dato[6], dato[7]))
        self.conexion.commit()
        self.conexion.close()
        # Boton Agregar Producto
        agregar_producto_boton = Button(frame,text="Agregar",command=self.agregar_producto)
        agregar_producto_boton.place(x=650,y=280)
        agregar_producto_boton["activebackground"] = "#000"
        agregar_producto_boton["activeforeground"] = "#fff"
        agregar_producto_boton["bg"] = "lightblue"
        agregar_producto_boton.config(height=2)

        eliminar_producto_boton = Button(frame, text="Eliminar", command=self.eliminar_producto)
        eliminar_producto_boton.place(x=750, y=280)
        eliminar_producto_boton["activebackground"] = "#000"
        eliminar_producto_boton["activeforeground"] = "#fff"
        eliminar_producto_boton["bg"] = "lightblue"
        eliminar_producto_boton.config(height=2)

        enviar_compra = Button(frame, text="Enviar Compra", command=self.confirmar_compra)
        enviar_compra.place(x=650, y=350)
        enviar_compra["activebackground"] = "#000"
        enviar_compra["activeforeground"] = "#fff"
        enviar_compra["bg"] = "lightblue"
        enviar_compra.config(height=2)
        Label(frame,text="Productos Seleccionados").place(x=640,y=10)
        # productos_seleccionados = Text(frame, height=20,width=18,state=DISABLED)
        # productos_seleccionados.place(x=640,y=40)
        self.productos_seleccionados = ttk.Treeview(frame)

        self.productos_seleccionados.place(x=640,y=40)
        self.compra = []
        self.valor_compra = 0
        self.productos_maximo = 30
        self.stock = 0
        # self.arbol_tree = self.productos_seleccionados.insert("",END,text="Menu")

    def agregar_producto(self):
        try:
                if self.productos_maximo > 0:
                    self.seleccion = self.tabla.focus()
                    self.detalles = self.tabla.item(self.seleccion)
                    self.valor0 = self.detalles.get("values")[0]
                    self.valor1 = self.detalles.get("values")[1]
                    self.valor2 = self.detalles.get("values")[2]
                    self.valor3 = self.detalles.get("values")[3]
                    self.valor4 = self.detalles.get("values")[4]
                    self.valor5 = self.detalles.get("values")[5]
                    self.valor6 = self.detalles.get("values")[6]
                    if int(self.valor5) > 0:
                        self.productos_seleccionados.insert("",END,text = f"{self.valor1} {self.valor2} ${self.valor4}")
                        self.compra.append(f"{self.valor1} {self.valor2} ${self.valor4}")
                        self.valor_compra += float(self.valor4)
                        print(self.compra)
                        print(self.valor_compra)
                        print(self.valor5)
                        base = BaseDatos()
                        base.actualizar_datos_productos_usuarios_menos(self.valor0)
                        self.tabla.delete(*self.tabla.get_children())
                        self.conexion = sqlite3.connect("./base_datos/productos.db")
                        self.cursor = self.conexion.cursor()
                        self.insertar = self.cursor.execute("SELECT * FROM PRODUCTOS")
                        for dato in self.insertar:
                            self.tabla.insert('', 0, values=(dato[1], dato[2], dato[3], dato[4], dato[5],
                                                             dato[6], dato[7]))
                        self.conexion.commit()
                        self.conexion.close()
                        self.productos_maximo-=1
                    else:
                        messagebox.showerror("Aviso","Stock insuficiente")
                else:
                    messagebox.showerror("Aviso","Excede los 30 productos")
        except:
            messagebox.showerror("Aviso","Debe seleccionar un producto")
    def eliminar_producto(self):
        try:
            seleccion = self.productos_seleccionados.selection()[0]
            self.productos_seleccionados.delete(seleccion)
            self.compra.remove(f"{self.valor1} {self.valor2} ${self.valor4}")
            self.valor_compra -= float(self.valor4)
            print(self.compra)
            base = BaseDatos()
            base.actualizar_datos_productos_usuarios_mas(self.valor0)
            self.tabla.delete(*self.tabla.get_children())
            self.conexion = sqlite3.connect("./base_datos/productos.db")
            self.cursor = self.conexion.cursor()
            self.insertar = self.cursor.execute("SELECT * FROM PRODUCTOS")
            for dato in self.insertar:
                self.tabla.insert('', 0, values=(dato[1], dato[2], dato[3], dato[4], dato[5],
                                                 dato[6], dato[7]))
            self.conexion.commit()
            self.conexion.close()
            self.productos_maximo+=1
        except:
            messagebox.showerror("Aviso", "Debe Seleccionar un producto")

    def confirmar_compra(self):
        self.ventana_compra = Tk()
        self.ventana_compra.title("Confirmar Compra")
        self.ventana_compra.geometry("400x400")
        self.ventana_compra.config(background="black")
        self.ventana_compra.resizable(False,False)

        Label(self.ventana_compra,text="Confirmar Compra - Complete los datos",bg="black",foreground="white").place(x=100,y=20)
        self.detalles_compra = Text(self.ventana_compra,state=DISABLED,height=15,width=25)
        self.detalles_compra.place(x=10,y=50)

        Label(self.ventana_compra,text="Nombre",bg="black",foreground="white").place(x=230,y=50)
        self.nombre = Entry(self.ventana_compra)
        self.nombre.place(x=230,y=70)

        Label(self.ventana_compra, text="Apellido",bg="black",foreground="white").place(x=230, y=90)
        self.apellido = Entry(self.ventana_compra)
        self.apellido.place(x=230, y=110)

        Label(self.ventana_compra, text="DNI",bg="black",foreground="white").place(x=230, y=130)
        self.dni = Entry(self.ventana_compra)
        self.dni.place(x=230, y=150)
        now = datetime.now()
        self.fecha = now.strftime('%d/%m/%Y  %H:%M:%S')
        self.ticket = now.strftime('0001-%Y%H%M%S')
        Label(self.ventana_compra,text=f"Fecha:{self.fecha}",bg="black",foreground="white").place(x=230,y=180)
        Label(self.ventana_compra, text=f"Total compra: ${self.valor_compra}",bg="black",foreground="white").place(x=230, y=210)
        Label(self.ventana_compra,text=f"Ticket: {self.ticket}",bg="black",foreground="white").place(x=230,y=240)
        boton_enviar = Button(self.ventana_compra,text="Confirmar Compra",command=self.enviar_compra)
        boton_enviar.place(x=230,y=270)
        boton_enviar["activebackground"] = "#000"
        boton_enviar["activeforeground"] = "#fff"
        boton_enviar["bg"] = "lightblue"
        boton_enviar.config(height=2)
        self.detalles = "\n".join(self.compra)
        self.detalles_compra.config(state=NORMAL)
        self.detalles_compra.insert("0.0",self.detalles)
        self.detalles_compra.config(state=DISABLED)
        self.ventana_compra.mainloop()


    def enviar_compra(self):

        self.detalles2 = ",".join(self.compra)
        base = BaseDatos()
        base.insertar_datos_ventas(self.nombre.get(),self.apellido.get(),self.dni.get(),self.valor_compra,self.ticket,self.fecha,self.detalles2)
        messagebox.showinfo("Aviso","Compra realizada con exito")

