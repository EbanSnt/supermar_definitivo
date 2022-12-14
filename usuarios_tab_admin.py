from tkinter import *
from tkinter import ttk,messagebox
from base_de_datos import BaseDatos
import sqlite3

class UsuariosTab:
    def principal(self,ventana,frame):
        self.contenedor_tabla = Frame(ventana, height=350, width=400)
        self.tabla = ttk.Treeview(frame, height=16,
                                  columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7","#8","#9"))
        self.tabla.place(relx=0.01, rely=0.02)

        self.tabla.column("#1", width=40, anchor=CENTER)
        self.tabla.column("#2", width=70, anchor=CENTER)
        self.tabla.column("#3", width=70, anchor=CENTER)
        self.tabla.column("#4", width=70, anchor=CENTER)
        self.tabla.column("#5", width=70, anchor=CENTER)
        self.tabla.column("#6", width=70, anchor=CENTER)
        self.tabla.column("#7", width=70, anchor=CENTER)
        self.tabla.column("#8", width=70, anchor=CENTER)
        self.tabla.column("#9", width=70, anchor=CENTER)

        self.tabla["show"] = "headings"
        self.tabla.heading("#1", text="ID", anchor=CENTER)
        self.tabla.heading("#2", text="NOMBRE", anchor=CENTER)
        self.tabla.heading("#3", text="APELLIDO", anchor=CENTER)
        self.tabla.heading("#4", text="DNI", anchor=CENTER)
        self.tabla.heading("#5", text="TELEFONO", anchor=CENTER)
        self.tabla.heading("#6", text="DIRECCION", anchor=CENTER)
        self.tabla.heading("#7", text="CORREO", anchor=CENTER)
        self.tabla.heading("#8", text="ROL", anchor=CENTER)
        self.tabla.heading("#9", text="CONTRASEÑA", anchor=CENTER)
        # Insertar datos en la tabla
        self.base_de_datos = BaseDatos()
        self.base_de_datos.crear_base_productos()
        self.conexion = sqlite3.connect("./base_datos/usuarios.db")
        self.cursor = self.conexion.cursor()
        self.insertar = self.cursor.execute("SELECT * FROM USUARIOS")
        for dato in self.insertar:
            self.tabla.insert('', 0, values=(dato[0],dato[1], dato[2], dato[3], dato[4], dato[5],
                                             dato[6], dato[7],dato[8]))
        self.conexion.commit()
        self.conexion.close()
        self.registro_datos_entry(frame)

    def registro_datos_entry(self, frame):
        Label(frame, text="ACTUALIZAR DATOS", justify="center").place(x=640, y=25)
        Label(frame, text="Contraseña").place(x=640, y=60)
        self.password_entry = Entry(frame)
        self.password_entry.place(x=640, y=85)

        Label(frame, text="Nombre").place(x=640, y=110)
        self.nombre_entry = Entry(frame)
        self.nombre_entry.place(x=640, y=135)

        Label(frame, text="Apellido").place(x=640, y=160)
        self.apellido_entry = Entry(frame)
        self.apellido_entry.place(x=640, y=185)

        Label(frame, text="DNI").place(x=640, y=210)
        self.dni_entry = Entry(frame)
        self.dni_entry.place(x=640, y=235)

        Label(frame, text="Telefono").place(x=640, y=260)
        self.telefono_entry = Entry(frame)
        self.telefono_entry.place(x=640, y=285)

        Label(frame, text="Direccion").place(x=640, y=310)
        self.direccion_entry = Entry(frame)
        self.direccion_entry.place(x=640, y=335)

        Label(frame, text="Email").place(x=640, y=360)
        self.email_entry= Entry(frame)
        self.email_entry.place(x=640, y=385)

        Label(frame, text="Rol").place(x=640, y=410)
        self.rol_entry = Entry(frame)
        self.rol_entry.place(x=640, y=435)

        # Botones

        enviar_datos = Button(frame, text="Enviar datos", justify="center", command=self.enviar_datos)
        enviar_datos.place(x=700, y=460)
        enviar_datos["activebackground"] = "#000"
        enviar_datos["activeforeground"] = "#fff"
        enviar_datos["bg"] = "lightblue"

        enviar_datos.config(height=2)

        editar_datos = Button(frame, text="Seleccionar Datos", justify="center", command=self.introduccir_datos_entry)
        editar_datos.place(x=470, y=370)
        editar_datos["activebackground"] = "#000"
        editar_datos["activeforeground"] = "#fff"
        editar_datos["bg"] = "lightblue"
        editar_datos.config(height=2)

        enviar_datos_actualizados = Button(frame, text="Enviar Datos Actualizados", justify="center",
                                           command=self.actializar_datos_tabla)
        enviar_datos_actualizados.place(x=470, y=420)
        enviar_datos_actualizados["activebackground"] = "#000"
        enviar_datos_actualizados["activeforeground"] = "#fff"
        enviar_datos_actualizados["bg"] = "lightblue"
        enviar_datos_actualizados.config(height=2)

        exportar_csv = Button(frame, text="Exportar Excel", justify="center")
        exportar_csv.place(x=320, y=420)
        exportar_csv["activebackground"] = "#000"
        exportar_csv["activeforeground"] = "#fff"
        exportar_csv["bg"] = "lightblue"
        exportar_csv.config(height=2)

    # Para introducir los datos que se encuentren seleccionados en la tabla
    # Primero borra los entry para asegurarse de que no haya datos previos
    def introduccir_datos_entry(self):
        try:
            self.password_entry.delete(0,END)
            self.nombre_entry.delete(0,END)
            self.apellido_entry.delete(0,END)
            self.dni_entry.delete(0,END)
            self.telefono_entry.delete(0,END)
            self.direccion_entry.delete(0,END)
            self.email_entry.delete(0,END)
            self.rol_entry.delete(0,END)
            self.seleccion = self.tabla.focus()
            self.detalles = self.tabla.item(self.seleccion)
            self.valor = self.detalles.get("values")[0]
            self.valor2 = self.detalles.get("values")[1]
            self.valor3 = self.detalles.get("values")[2]
            self.valor4 = self.detalles.get("values")[3]
            self.valor5 = self.detalles.get("values")[4]
            self.valor6 = self.detalles.get("values")[5]
            self.valor7 = self.detalles.get("values")[6]
            self.valor8 = self.detalles.get("values")[7]
            self.valor9 = self.detalles.get("values")[8]

            self.password_entry.insert(0,self.valor9)
            self.nombre_entry.insert(0,self.valor2)
            self.apellido_entry.insert(0,self.valor3)
            self.dni_entry.insert(0,self.valor4)
            self.telefono_entry.insert(0,self.valor5)
            self.direccion_entry.insert(0,self.valor6)
            self.email_entry.insert(0,self.valor7)
            self.rol_entry.insert(0,self.valor8)
        except:
            messagebox.showerror("Aviso","Debe Seleccionar un registro")
    # Para validad que no haya campos vacios al momento de enviar los datos
    def validacion_de_datos(self):
        return not self.nombre_entry.get() or not self.apellido_entry.get() or not self.dni_entry.get() \
        or not self.telefono_entry.get() or not self.direccion_entry.get() or not self.rol_entry.get() \
        or not self.password_entry.get()
    def actializar_datos_tabla(self):
        #  def actualizar_datos_usuarios(self,nombre,apellido,dni,telefono,direccion,correo,rol,password):
        #         self.conexion = sqlite3.connect("./base_datos/usuarios.db")
        #         self.cursor = self.conexion.cursor()
        #         self.cursor.execute("SELECT * FROM USUARIOS")
        #         consulta = """UPDATE USUARIOS SET NOMBRE = ?, APELLIDO = ?, TELEFONO = ?, DIRECCION = ?, CORREO = ?, ROL = ?, CONTRA = ? WHERE DNI = ?"""
        #         parametros = (nombre,apellido,telefono,direccion,correo,rol,password,dni)
        #         self.cursor.execute(consulta,parametros)
        #         self.conexion.commit()
        #         self.conexion.close()

        if self.validacion_de_datos() == True:
            messagebox.showerror("Aviso","No debe haber campos vacios")
        else:
            base = BaseDatos()
            base.actualizar_datos_usuarios(self.nombre_entry.get(),self.apellido_entry.get(),self.dni_entry.get(),
                                           self.telefono_entry.get(),self.direccion_entry.get(),self.email_entry.get(),
                                           self.rol_entry.get(),self.password_entry.get())

            self.nombre_entry.delete(0,END)
            self.apellido_entry.delete(0,END)
            self.dni_entry.delete(0,END)
            self.telefono_entry.delete(0,END)
            self.direccion_entry.delete(0,END)
            self.email_entry.delete(0,END)
            self.rol_entry.delete(0,END)
            self.password_entry.delete(0,END)
            messagebox.showinfo("Aviso","Datos Actualizados")

    def enviar_datos(self):
        if self.validacion_de_datos() == True:
            messagebox.showerror("Aviso","No debe haber campos vacios")
        else:
            base = BaseDatos()
            base.insertar_datos_usuarios(self.nombre_entry.get(),self.apellido_entry.get(),
                                           self.dni_entry.get(),self.telefono_entry.get(),
                                           self.direccion_entry.get(),self.email_entry.get(),self.rol_entry.get(),
                                           self.password_entry.get())

            self.nombre_entry.delete(0, END)
            self.apellido_entry.delete(0, END)
            self.dni_entry.delete(0, END)
            self.telefono_entry.delete(0, END)
            self.direccion_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.rol_entry.delete(0, END)
            self.password_entry.delete(0, END)
            messagebox.showinfo("Aviso","Datos enviados exitosamente")


