from tkinter import *
from tkinter import ttk,messagebox
from base_de_datos import BaseDatos
import sqlite3

class ProductosTabs:

    def principal(self,ventana,frame):
        self.registro_datos_entry(frame)
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






    def registro_datos_entry(self,frame):
        Label(frame,text="REGISTRO DE PRODUCTOS",justify="center").place(x=640,y=25)
        Label(frame, text="Codigo").place(x=640, y=60)
        self.codigo_entry = Entry(frame)
        self.codigo_entry.place(x=640,y=85)

        Label(frame, text="Producto").place(x=640, y=110)
        self.producto_entry = Entry(frame)
        self.producto_entry.place(x=640, y=135)


        Label(frame, text="Marca").place(x=640, y=160)
        self.marca_entry = Entry(frame)
        self.marca_entry.place(x=640, y=185)

        Label(frame, text="Seccion").place(x=640, y=210)
        self.seccion_entry = Entry(frame)
        self.seccion_entry.place(x=640, y=235)

        Label(frame, text="Precio").place(x=640, y=260)
        self.precio_entry = Entry(frame)
        self.precio_entry.place(x=640, y=285)

        Label(frame, text="Stock").place(x=640, y=310)
        self.stock_entry = Entry(frame)
        self.stock_entry.place(x=640, y=335)

        Label(frame, text="Descripcion").place(x=640, y=360)
        self.descripcion_entry = Entry(frame)
        self.descripcion_entry.place(x=640, y=385)

        # Botones

        enviar_datos = Button(frame,text="Enviar datos",justify="center",command=self.insertar_datos_tabla)
        enviar_datos.place(x=700,y=425)
        enviar_datos["activebackground"] = "#000"
        enviar_datos["activeforeground"] = "#fff"
        enviar_datos["bg"] = "#C84A2F"
        enviar_datos.config(height=2)



        editar_datos = Button(frame, text="Seleccionar Datos", justify="center",command=self.seleccionar_datos)
        editar_datos.place(x=440, y=370)
        editar_datos["activebackground"] = "#000"
        editar_datos["activeforeground"] = "#fff"
        editar_datos["bg"] = "#C84A2F"
        editar_datos.config(height=2)

        enviar_datos_actualizados = Button(frame, text="Enviar Datos Actualizados", justify="center",command=self.editar_producto)
        enviar_datos_actualizados.place(x=440, y=420)
        enviar_datos_actualizados["activebackground"] = "#000"
        enviar_datos_actualizados["activeforeground"] = "#fff"
        enviar_datos_actualizados["bg"] = "#C84A2F"
        enviar_datos_actualizados.config(height=2)

        eliminar_datos = Button(frame, text="Eliminar datos", justify="center")
        eliminar_datos.place(x=180, y=370)
        eliminar_datos["activebackground"] = "#000"
        eliminar_datos["activeforeground"] = "#fff"
        eliminar_datos["bg"] = "#C84A2F"
        eliminar_datos.config(height=2)

        exportar_csv = Button(frame, text="Exportar Excel", justify="center")
        exportar_csv.place(x=180, y=420)
        exportar_csv["activebackground"] = "#000"
        exportar_csv["activeforeground"] = "#fff"
        exportar_csv["bg"] = "#C84A2F"
        exportar_csv.config(height=2)

    def botones_funciones(self,frame,ventana):
        pass

    def validacion_datos(self):
        return not self.codigo_entry.get() or not self.producto_entry.get() or not self.marca_entry.get() or not self.precio_entry.get() \
        or not self.stock_entry.get() or not self.descripcion_entry.get() or not self.seccion_entry.get()
    def insertar_datos_tabla(self):
        if self.validacion_datos() == True:
            messagebox.showerror("Aviso","Debe completar todos los campos")
        else:
            base = BaseDatos()
            base.insertar_datos_productos(self.codigo_entry.get(),self.producto_entry.get(),self.marca_entry.get(),self.seccion_entry.get(), self.precio_entry.get(),self.stock_entry.get(),self.descripcion_entry.get())
            self.codigo_entry.delete(0,END)
            self.producto_entry.delete(0,END)
            self.marca_entry.delete(0,END)
            self.precio_entry.delete(0,END)
            self.stock_entry.delete(0,END)
            self.descripcion_entry.delete(0,END)
            self.seccion_entry.delete(0,END)
            messagebox.showinfo("Aviso","Envio exitoso")

    def editar_producto(self):
        if self.validacion_datos() == True:
            messagebox.showerror("Aviso","No deben quedar campos vacios")
        else:
            self.base_de_datos.actualizar_datos_productos(self.codigo_entry.get(),
                                                    self.producto_entry.get(),
                                                    self.marca_entry.get(),
                                                    self.seccion_entry.get(),
                                                    self.precio_entry.get(),
                                                    self.stock_entry.get(),
                                                    self.descripcion_entry.get())

            self.producto_entry.delete(0,END)
            self.codigo_entry.delete(0,END)
            self.marca_entry.delete(0,END)
            self.seccion_entry.delete(0,END)
            self.precio_entry.delete(0,END)
            self.stock_entry.delete(0,END)
            self.descripcion_entry.delete(0,END)
            messagebox.showinfo("Aviso","Datos actualizados")

    def seleccionar_datos(self):
        self.seleccion = self.tabla.focus()
        self.detalles = self.tabla.item(self.seleccion)
        self.valor = self.detalles.get("values")[0]
        self.valor2 = self.detalles.get("values")[1]
        self.valor3 = self.detalles.get("values")[2]
        self.valor4 = self.detalles.get("values")[3]
        self.valor5 = self.detalles.get("values")[4]
        self.valor6 = self.detalles.get("values")[5]
        self.valor7 = self.detalles.get("values")[6]
        #self.valor8 = self.detalles.get("values")[7]
        self.codigo_entry.insert(0,self.valor2)
        self.producto_entry.insert(0,self.valor3)
        self.marca_entry.insert(0,self.valor4)
        self.seccion_entry.insert(0,self.valor5)
        self.precio_entry.insert(0,self.valor6)
        self.stock_entry.insert(0,self.valor7)
        #self.descripcion_entry.insert(0,self.valor8)




        # INSERTAR ESTOS DATOS EN EL ENTRY CUANDO SE QUIERA CONSULTAR

    def usuarios(self):
        pass
        # Nos dirige a otra ventana donde podemos ver a los usuarios registrados

    def excel(self):
        pass
        # Funcion que devuelve un excel con todos los productos

    def eliminar_producto(self):
        pass
        # Revisar si hace falta
