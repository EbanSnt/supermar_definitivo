from tkinter import *
from tkinter import ttk,messagebox
from base_de_datos import BaseDatos
import sqlite3

class ComprasTabUsers:
    def principal(self,ventana,frame):
            self.contenedor_tabla = Frame(ventana, height=350, width=600)
            self.tabla = ttk.Treeview(frame, height=16,
                                      columns=("#1", "#2", "#3", "#4","#5","#6","#7","#8"))
            self.tabla.place(relx=0.01, rely=0.02)

            self.tabla.column("#1", width=40, anchor=CENTER)
            self.tabla.column("#2", width=90, anchor=CENTER)
            self.tabla.column("#3", width=90, anchor=CENTER)
            self.tabla.column("#4", width=90, anchor=CENTER)
            self.tabla.column("#5", width=80, anchor=CENTER)
            self.tabla.column("#6", width=80, anchor=CENTER)
            self.tabla.column("#7", width=100, anchor=CENTER)
            self.tabla.column("#8", width=200, anchor=CENTER)



            self.tabla["show"] = "headings"
            self.tabla.heading("#1", text="ID", anchor=CENTER)
            self.tabla.heading("#2", text="NOMBRE", anchor=CENTER)
            self.tabla.heading("#3", text="APELLIDO", anchor=CENTER)
            self.tabla.heading("#4", text="DNI", anchor=CENTER)
            self.tabla.heading("#5", text="MONTO COMPRA", anchor=CENTER)
            self.tabla.heading("#6", text="COMPROBANTE", anchor=CENTER)
            self.tabla.heading("#7", text="FECHA", anchor=CENTER)
            self.tabla.heading("#8", text="DESCRIPCION", anchor=CENTER)


            #Insertar datos en la tabla
            self.base_de_datos = BaseDatos()
            self.base_de_datos.crear_base_productos()
            self.conexion = sqlite3.connect("./base_datos/ventas.db")
            self.cursor = self.conexion.cursor()
            self.insertar = self.cursor.execute("SELECT * FROM VENTAS")
            for dato in self.insertar:
                self.tabla.insert('', 0, values=(dato[0], dato[1], dato[2], dato[3],
                                                 dato[4],dato[5],dato[6],dato[7]))
            self.conexion.commit()
            self.conexion.close()

