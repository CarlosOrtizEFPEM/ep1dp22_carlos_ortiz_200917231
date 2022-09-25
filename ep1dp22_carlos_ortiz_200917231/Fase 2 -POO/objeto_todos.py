import time
import tkinter
from tkinter import *
from tkinter import ttk
from clase_sociedad_anonima import Sociedad_anonima

#{} []
#CREAR Ventana----------
ventana = Tk()
ventana.title = "Parcial 1"
ventana.geometry("1500x710")
#ventana.configure(bg='#49A')

tabla = ttk.Treeview(ventana, columns=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10"))

#instanciar la clase para asignar valores a los atributos y utilizar los métodos

lista=[]
clic = 0
def guardaDatos():   
    registro=Sociedad_anonima()
    #registro= centro_educativo()
    
    #asignar los valores a los atributos
    registro.codigo = txt_codigo.get()
    registro.nombre = txt_nombre.get()
    registro.direccion = txt_direccion.get()
    registro.telefono = txt_telefono.get()
    #registro.director = txt_director.get()
    registro.director = "Carlos Ortiz"
    registro.url = "WWW.ACADEMIA.COM.GT"
    registro.hombres= txt_hombres.get()
    registro.mujeres= txt_mujeres.get()
    registro.sociedad= txt_sociedad.get()
    registro.representante= txt_representante.get()
    registro.correoR= txt_correoR.get()
    
    
    #agregando el estudiante a la lista
    lista.append(registro)
    generarTabla()
    limpiarCajasTexto()

    #limitar el numero de registros a 5    
    global clic
    clic += 1
    if clic >= 6:
        print("BASE DE DATOS LLENA,se cerrara en 3 segundos")
        duracion = 5
        time.sleep(duracion)
        exit()       
            
    
def generarTabla():
    for fila in tabla.get_children():
        tabla.delete(fila)
   
        
    #establecer el tamaño de las columnas
    tabla.column("#0", width=125)
    tabla.column("col1", width=125)
    tabla.column("col2", width=125)
    tabla.column("col3", width=125)
    tabla.column("col4", width=125)
    tabla.column("col5", width=125)
    tabla.column("col6", width=125)
    tabla.column("col7", width=125)
    tabla.column("col8", width=125)
    tabla.column("col9", width=125)
    tabla.column("col10", width=125)
    

    tabla.heading("#0", text="Codigo", anchor=CENTER)
    tabla.heading("col1", text="Nombre", anchor=CENTER)
    tabla.heading("col2", text="Direccion", anchor=CENTER)
    tabla.heading("col3", text="Telefono", anchor=CENTER)
    tabla.heading("col4", text="Director", anchor=CENTER)
    tabla.heading("col5", text="URL", anchor=CENTER)
    tabla.heading("col6", text="Cant.Hombres", anchor=CENTER)
    tabla.heading("col7", text="Cant.Mujeres", anchor=CENTER)
    tabla.heading("col8", text="Nombre Sociedad", anchor=CENTER)
    tabla.heading("col9", text="Nombre Representante", anchor=CENTER)
    tabla.heading("col9", text="Correo Representante", anchor=CENTER)
    
            
    #ciclo para pasar los elementos de lista
    for registro in lista:
        tabla.insert("",END, text=registro.codigo, values=(registro.nombre, registro.direccion, registro.telefono, registro.director, registro.url, registro.hombres, registro.mujeres, registro.sociedad, registro.representante, registro.correoR))
    tabla.pack(fill= tkinter.X)

def limpiarCajasTexto():
    #borrar el contenido de los controles Entry
    txt_codigo.delete(0,"end")
    txt_nombre.delete(0,"end")
    txt_direccion.delete(0,"end")
    txt_telefono.delete(0,"end")
    txt_hombres.delete(0,"end")
    txt_mujeres.delete(0,"end")
    #txt_director.delete(0,"end")
    #txt_url.delete(0,"end")
    txt_sociedad.delete(0,"end")
    txt_representante.delete(0,"end")
    txt_correoR.delete(0,"end")
    

    #pone el foco a este elemento
    txt_codigo.focus_set()

#fondo       letras
#bg="red", ,fg="blue"


#bloque de creacion cajas de texto en ventana - INGRESO DE DATOS
fuente = ("Arial", 14) 
 
lbl_titulo = Label(ventana, text="PARCIAL No.1 - Carlos Ortiz\nUSAC-EFPEM", font=("Arial","14"),fg="RED")

lbl_codigo = Label(ventana, text="Codigo:", font = fuente,fg="blue") 
txt_codigo = Entry(ventana, font= fuente)

lbl_nombre = Label(ventana, text="Nombre:", font = fuente,fg="blue")
txt_nombre = Entry(ventana, font= fuente)

lbl_direccion = Label(ventana, text="Direccion:", font = fuente,fg="blue")
txt_direccion = Entry(ventana, font= fuente)

lbl_telefono = Label(ventana, text="Telefono:", font = fuente,fg="blue")
txt_telefono = Entry(ventana, font= fuente)

#lbl_director = Label(ventana, text="Director:", font = fuente,fg="blue")
#txt_director = Entry(ventana, font= fuente)

#lbl_url = Label(ventana, text="Pagina URL:", font = fuente,fg="blue")
#txt_url = Entry(ventana, font= fuente)

lbl_hombres = Label(ventana, text="Cant.Hombres:", font = fuente,fg="blue")
txt_hombres = Entry(ventana, font= fuente)

lbl_mujeres = Label(ventana, text="Cant.Mujeres:", font = fuente,fg="blue")
txt_mujeres = Entry(ventana, font= fuente)

lbl_sociedad = Label(ventana, text="Sociedad Anonima:", font = fuente,fg="blue")
txt_sociedad = Entry(ventana, font= fuente)

lbl_representante = Label(ventana, text="Nombre Representante:", font = fuente,fg="blue")
txt_representante = Entry(ventana, font= fuente)

lbl_correoR = Label(ventana, text="Correo Representante:", font = fuente,fg="blue")
txt_correoR = Entry(ventana, font= fuente)


btn_guardar = tkinter.Button(ventana, text="Guardar  -solo 5 Registros-", command=guardaDatos, font=fuente, bg="#FFF", activebackground="yellow")

#asignar modulo a bloque de creacion fill de labely textos
lbl_titulo.pack()

lbl_codigo.pack(anchor = tkinter.W)  
txt_codigo.pack(fill = tkinter.X)

lbl_nombre.pack(anchor = tkinter.W)
txt_nombre.pack(fill = tkinter.X)

lbl_direccion.pack(anchor = tkinter.W)
txt_direccion.pack(fill = tkinter.X)

lbl_telefono.pack(anchor = tkinter.W)
txt_telefono.pack(fill = tkinter.X)


#lbl_director.pack(anchor = tkinter.W)
#txt_director.pack(fill = tkinter.X)

#lbl_url.pack(anchor = tkinter.W)
#txt_url.pack(fill = tkinter.X)

lbl_hombres.pack(anchor = tkinter.W)
txt_hombres.pack(fill = tkinter.X)

lbl_mujeres.pack(anchor = tkinter.W)
txt_mujeres.pack(fill = tkinter.X)

lbl_sociedad.pack(anchor = tkinter.W)
txt_sociedad.pack(fill = tkinter.X)

lbl_representante.pack(anchor = tkinter.W)
txt_representante.pack(fill = tkinter.X)

lbl_correoR.pack(anchor = tkinter.W)
txt_correoR.pack(fill = tkinter.X)


#mandar a llamar a accion del boton
btn_guardar.pack(fill = tkinter.X)

#inicio de modulo ventana
ventana.mainloop()
