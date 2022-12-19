from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import math,random
from datetime import datetime
import os,sys
import time
import tkinter as tk
import sys # Paquete usado para invocar a funciones y clases creadas en carpetas diferentes.
sys.path.append(r'F:/Visual Studio Code/Scripts_Selim/Scripts') # Dirección usada por defecto al escribir el código.
from Back_End.Conector import *
from Back_End.CRUD_Base_de_Datos import *

direccion_carpeta = "F:/Visual Studio Code/Scripts_Selim/Scripts/Front_End/Imagenes"
direccion_facturas = "F:/Visual Studio Code/Scripts_Selim/Scripts/Kwik_E_Mart/Facturas"

mi_conexion = conectar_database()
cursor_1 = mi_conexion.cursor()
cursor_2 = mi_conexion.cursor()
cursor_productos = mi_conexion.cursor()
crear_base_datos()
# Ventana inicial:
def ventana_inicial():
    global fondo_ventana,cuadro_1,cuadro_admin,cuadro_cliente,Boton_Admin,Boton_Cliente
    try:
        cuadro_admin.destroy()
    except:
        pass
    try:
        cuadro_cliente.destroy()
    except:
        pass
    cuadro_1 = Frame(root,width=1300,height=800)
    cuadro_1.pack()
    fondo_ventana = ImageTk.PhotoImage(file=direccion_carpeta+"/login.png")
    
    Label(cuadro_1,image = fondo_ventana).pack()

    Boton_Admin = PhotoImage(file=direccion_carpeta+"/Botones/admin.png")
    Boton_Cliente = PhotoImage(file=direccion_carpeta+"/Botones/cliente.png")

    Boton_0 = Button(cuadro_1,image=Boton_Admin,borderwidth=0,bg="white",command=ventana_iniciar_admin)
    Boton_0.place(x=600,y=480)

    Boton_1 = Button(cuadro_1,image=Boton_Cliente,borderwidth=0,bg="white",command=ventana_iniciar_cliente)
    Boton_1.place(x=600,y=600)
# Ventana iniciar sesión como administrador:
def ventana_iniciar_admin():
    global fondo_ventana,cuadro_1,cuadro_admin,cuadro_3,regresar,Boton_login,texto_admin_1,texto_admin_2,admin_entrada_1,admin_entrada_2

    try:
        cuadro_3.destroy()
    except:
        pass

    cuadro_1.destroy()
    cuadro_admin = Frame(root,width=1300,height=800)
    cuadro_admin.pack()

    fondo_ventana = ImageTk.PhotoImage(file=direccion_carpeta+"/login.png")
    Label(cuadro_admin,image=fondo_ventana).pack()

    Label(cuadro_admin,text="Usuario",font=("verdana",21),bg="white").place(x=515,y=500)

    Label(cuadro_admin,text="Clave",font=("verdana",21),bg="white").place(x=515,y=600)

    texto_admin_1 = StringVar()
    texto_admin_2 = StringVar()
    
    admin_entrada_1 = Entry(cuadro_admin,width=15,bg="white",fg="#020202",bd=2,font=("verdana",15),relief=GROOVE,textvariable=texto_admin_1)
    admin_entrada_1.place(x=678,y=504)

    admin_entrada_2 = Entry(cuadro_admin,width=15,bg="white",fg="#020202",bd=2,font=("verdana",15),relief=GROOVE,show="*",textvariable=texto_admin_2)
    admin_entrada_2.place(x=678,y=604)

    Boton_login = PhotoImage(file=direccion_carpeta+"/Botones/login_boton.png")
    Boton_0 = Button(cuadro_admin,image=Boton_login,borderwidth=0,bg="white",command=consultar_admin)
    Boton_0.place(x=610,y=650)

    regresar = PhotoImage(file=direccion_carpeta+"/Botones/volver.png")
    Boton_Regresar = Button(cuadro_admin,image=regresar,borderwidth=0,bg="white",command=ventana_inicial)
    Boton_Regresar.place(x=1100,y=40)
# Ventana iniciar sesión como cliente:
def ventana_iniciar_cliente():
    global fondo_ventana,cuadro_1,cuadro_cliente,cuadro_4,goback,login_btn,texto_cliente_1,texto_cliente_2,cliente_entrada_1,cliente_entrada_2

    try:
        cuadro_4.destroy()
    except:
        pass

    cuadro_1.destroy()
    cuadro_cliente = Frame(root,width=1300,height=800)
    cuadro_cliente.pack()

    fondo_ventana = ImageTk.PhotoImage(file=direccion_carpeta+"/login.png")
    Label(cuadro_cliente,image=fondo_ventana).pack()

    Label(cuadro_cliente,text="Usuario",font=("verdana",21),bg="white").place(x=515,y=500)

    Label(cuadro_cliente,text="Clave",font=("verdana",21),bg="white").place(x=515,y=600)

    texto_cliente_1 = StringVar()
    texto_cliente_2 = StringVar()
    
    cliente_entrada_1 = Entry(cuadro_cliente,width=15,bg="white",fg="#020202",bd=2,font=("verdana",15),relief=GROOVE,textvariable=texto_cliente_1)
    cliente_entrada_1.place(x=678,y=504)

    cliente_entrada_2 = Entry(cuadro_cliente,width=15,bg="white",fg="#020202",bd=2,font=("verdana",15),relief=GROOVE,show="*",textvariable=texto_cliente_2)
    cliente_entrada_2.place(x=678,y=604)

    login_btn = PhotoImage(file=direccion_carpeta+"/Botones/login_boton.png")
    bt0 = Button(cuadro_cliente,image=login_btn,borderwidth=0,bg="white",command = consultar_cliente)
    bt0.place(x=610,y=650)

    goback = PhotoImage(file=direccion_carpeta+"/Botones/volver.png")
    goback_btn = Button(cuadro_cliente,image=goback,borderwidth=0,bg="white",command=ventana_inicial)
    goback_btn.place(x=1100,y=40)
# Consulta de inicio de sesión para administrador:
def consultar_admin():
    global texto_admin_1,texto_admin_2,admin_entrada_1,admin_entrada_2

    conexion = conectar_database()
    conexion.reconnect()
    cursor_1 = conexion.cursor()
    cursor_1.execute('select usuario,clave from administradores')
    fetch_result_1 = cursor_1.fetchall()

    adm_usuario = texto_admin_1.get()
    adm_clave = texto_admin_2.get()

    if adm_usuario == '' or adm_clave == '':
        messagebox.showwarning("¡Cuidado!","¡Complete todos los campos!")
        admin_entrada_1.delete(0,END)
        admin_entrada_2.delete(0,END)
    else:
        for i in fetch_result_1:
            if adm_usuario == i[0] and adm_clave == i[1]:
                messagebox.showinfo("Info","¡Bienvenido al KWIK E MART!")
                return ventana_admin()
        else:
            messagebox.showerror("¡Error!","Usuario o clave incorrecta")
            admin_entrada_1.delete(0,END)
            admin_entrada_2.delete(0,END)
# Consulta de inicio de sesión para clientes:
def consultar_cliente():
    global texto_cliente_1,texto_cliente_2,cliente_entrada_1,cliente_entrada_2
    
    conexion = conectar_database()
    conexion.reconnect()
    cursor_2 = conexion.cursor()
    cursor_2.execute('select usuario,clave from clientes')
    fetch_result_2 = cursor_2.fetchall()
    conexion.commit()
    conexion.close()

    cliente_usuario = texto_cliente_1.get()
    cliente_clave = texto_cliente_2.get()

    if cliente_usuario == '' or cliente_clave == '':
        messagebox.showwarning("¡Cuidado!","¡Complete todos los campos!")
        cliente_entrada_1.delete(0,END)
        cliente_entrada_2.delete(0,END)
    else:
        for i in fetch_result_2:
            if cliente_usuario == i[0] and cliente_clave == i[1]:
                messagebox.showinfo("Info","¡Bienvenido al KWIK E MART!")
                return ventana_clientes()
        else:
            messagebox.showerror("¡Error!","Usuario o clave incorrecta")
            cliente_entrada_1.delete(0,END)
            cliente_entrada_2.delete(0,END)
# Ventana de administrador:
def ventana_admin():
    global cuadro_admin,cuadro_3,pastel,Boton_logout,Boton_inventario,Boton_Cliente2,Boton_factura,Boton_info,cuadro_inventario,bandera_borrar_cursor,cuadro_cliente
    global cuadro_factura
    
    bandera_borrar_cursor = 1

    try:
        cuadro_factura.destroy()
    except:
        pass
    try:
        cuadro_admin.destroy()
    except:
        pass
    try:     
        cuadro_inventario.destroy()
    except:
        pass
    try:
        cuadro_cliente.destroy()
    except:
        pass

    cuadro_3 = Frame(root,width=1300,height=800)
    cuadro_3.pack()

    pastel = ImageTk.PhotoImage(file=direccion_carpeta+"/pastel_gradient.jpg")
    Label(cuadro_3,image=pastel).pack()
 
    Boton_logout = PhotoImage(file=direccion_carpeta+"/Botones/logout_boton_1.png")
    Button(cuadro_3,image=Boton_logout,bd=0,borderwidth=0,bg="#f2f7fa",command=ventana_iniciar_admin).place(x=1100,y=45)

    Label(cuadro_3,text="Modo Administrador",font=("Verdana",45,"bold"),fg="#3d3d3d",bg="#f0f8fa").place(x=380,y=30)

    Boton_inventario = PhotoImage(file=direccion_carpeta+"/Botones/inventario.png")
    Button(cuadro_3,image=Boton_inventario,bd=0,borderwidth=0,bg="#d5eff5",command=ventana_administracion_productos).place(x=110,y=300)

    Boton_Cliente2 = PhotoImage(file=direccion_carpeta+"/Botones/clientes.png")
    Button(cuadro_3,image=Boton_Cliente2,bd=0,borderwidth=0,bg="#d5eff5",command=ventana_administracion_clientes).place(x=395,y=300)

    Boton_factura = PhotoImage(file=direccion_carpeta+"/Botones/facturas.png")
    Button(cuadro_3,image=Boton_factura,bd=0,borderwidth=0,bg="#d5eff5",command=ventana_administracion_facturas).place(x=680,y=300)

    Boton_info = PhotoImage(file=direccion_carpeta+"/Botones/creditos.png")
    Button(cuadro_3,image=Boton_info,bd=0,borderwidth=0,bg="#d5eff5",command=ventana_creditos).place(x=965,y=300)
# Ventana de información del proyecto Supermark:
def ventana_creditos():
    root1 = tk.Tk()
    root1.title("Créditos")
    text1 = tk.Text(root1, height=6, width=85)
    text1.insert(tk.INSERT,"\n\tIntegrantes: Molina, Milgaro y Dahan Selim. Idea original: Matt Groening\n\n\n\t\t\t      Proyecto: Supermark CM4")
    text1.pack()
    root1.mainloop()
    root1.mainloop()
# Agregar productos:
def agregar_productos():
    global boton_agregar,cuadro_inventario,boton_borrar_1,boton_salir_1,ventana_agregar_productos

    try:
        global bandera_borrar_cursor
        bandera_borrar_cursor = 1
    except:
        pass

    cuadro_inventario.destroy()

    ventana_agregar_productos = Frame(root,height=800,width=1300,bg="#ADD8E6")
    ventana_agregar_productos.pack()
    
    cuadro_productoss = Frame(ventana_agregar_productos,width=1200,height=750,bg="white",bd=0,relief=RIDGE)
    cuadro_productoss.place(x=50,y=25)
    
    Label(cuadro_productoss,text="Agregar Productos",font=("Verdana",35,"bold"),fg="#3d3d3d",bg="white").place(x=400,y=20)
    
    producto_dentro_de_cuadro = Frame(cuadro_productoss,height=560,width=550,bg="white",bd=7,relief=RIDGE)
    producto_dentro_de_cuadro.place(x=320,y=120)

    def funcion_boton_agregar():
        try:
            if(agregar_prod_id_texto_1.get() == 0):
                messagebox.showerror("Error","Ingrese un ID para el producto")
            elif(agregar_prod_nombre_texto_1.get() == " " or len(agregar_prod_nombre_texto_1.get()) == 0):
                messagebox.showerror("Error","Ingrese un nombre para el producto")
            elif(agregar_prod_clase_texto_1.get() == " " or len(agregar_prod_clase_texto_1.get()) == 0):
                messagebox.showerror("Error","Especifique una clase")
            elif(agregar_prod_subclase_texto_1.get() == " " or len(agregar_prod_subclase_texto_1.get()) == 0):
                messagebox.showerror("Error","Especifique una marca")
            elif(agregar_prod_stock_texto_1.get() == 0):
                messagebox.showerror("Error","Ingrese una cantidad correcta")
            elif(agregar_prod_precio_texto_1.get() == 0):
                messagebox.showerror("Error","Ingrese un precio unitario")
            else:
                op = messagebox.askyesno("Agregar producto","¿Agregar el producto?")
                if op > 0:
                    mi_conexion_1 = conectar_database()
                    mi_conexion_1.reconnect()
                    cursor_3 = mi_conexion_1.cursor()
                    cursor_3.execute("insert into productos(producto_id,clase,marca,nombre_producto,stock,precio_unitario) VALUES(%s,%s,%s,%s,%s,%s)",
                    (agregar_prod_id_texto_1.get(),agregar_prod_clase_texto_1.get(),agregar_prod_subclase_texto_1.get(),agregar_prod_nombre_texto_1.get(),agregar_prod_stock_texto_1.get(),agregar_prod_precio_texto_1.get())
                    )
                    mi_conexion_1.commit()
                    mi_conexion_1.close()
                    messagebox.showinfo("Agregar producto","¡Producto agregado exitosamente!")
        except:
            pass

    def funcion_boton_borrar():
        agregar_entrada_1.delete(0,END) # ID
        agregar_entrada_2.delete(0,END) # Nombre
        agregar_entrada_3.delete(0,END) # Clase
        agregar_entrada_4.delete(0,END) # Subclase
        agregar_entrada_5.delete(0,END) # Stock
        agregar_entrada_6.delete(0,END) # Precio
        agregar_prod_stock_texto_1.set(0)
        agregar_prod_precio_texto_1.set(0.0)

    # Variables de producto:
    agregar_prod_id_texto_1 = IntVar()
    agregar_prod_nombre_texto_1 = StringVar()
    agregar_prod_clase_texto_1 = StringVar()
    agregar_prod_subclase_texto_1 = StringVar()
    agregar_prod_stock_texto_1 = IntVar()
    agregar_prod_precio_texto_1 = DoubleVar()

    Label(producto_dentro_de_cuadro,text="ID:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=35)
    agregar_entrada_1 = Entry(producto_dentro_de_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=agregar_prod_id_texto_1)
    agregar_entrada_1.place(x=200,y=39)

    Label(producto_dentro_de_cuadro,text="Nombre:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=105)
    agregar_entrada_2 = Entry(producto_dentro_de_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=agregar_prod_nombre_texto_1)
    agregar_entrada_2.place(x=200,y=109)

    Label(producto_dentro_de_cuadro,text="Clase:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=175)
    agregar_entrada_3 = Entry(producto_dentro_de_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=agregar_prod_clase_texto_1)
    agregar_entrada_3.place(x=200,y=179)

    Label(producto_dentro_de_cuadro,text="Marca:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=245)
    agregar_entrada_4 = Entry(producto_dentro_de_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=agregar_prod_subclase_texto_1)
    agregar_entrada_4.place(x=200,y=249)

    Label(producto_dentro_de_cuadro,text="Stock:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=315)
    agregar_entrada_5 = Entry(producto_dentro_de_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=agregar_prod_stock_texto_1)
    agregar_entrada_5.place(x=200,y=319)

    Label(producto_dentro_de_cuadro,text="Precio unitario:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=385)
    agregar_entrada_6 = Entry(producto_dentro_de_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=agregar_prod_precio_texto_1)
    agregar_entrada_6.place(x=200,y=389)

    boton_agregar = PhotoImage(file=direccion_carpeta+"/Botones/agregar_boton.png")
    Button(producto_dentro_de_cuadro,image=boton_agregar,bg="white",bd=0,borderwidth=0,command=funcion_boton_agregar).place(x=80,y=450)

    boton_borrar_1 = PhotoImage(file=direccion_carpeta+"/Botones/borrar_boton_1.png")
    Button(producto_dentro_de_cuadro,image=boton_borrar_1,bg="white",bd=0,borderwidth=0,command=funcion_boton_borrar).place(x=285,y=450)

    boton_salir_1 = PhotoImage(file=direccion_carpeta+"/Botones/producto_salir_1.png")
    Button(cuadro_productoss,image=boton_salir_1,bg="white",bd=0,borderwidth=0,command=ventana_administracion_productos).place(x=1020,y=35)
#  Actualizar productos:
def actualizar_productos():
    global actualizar_boton_1,cuadro_inventario,boton_salir_2,boton_borrar_1,ventana_actualizar_prod,boton_buscar
    
    try:
        global bandera_borrar_cursor
        bandera_borrar_cursor = 1
    except:
        pass
    
    cuadro_inventario.destroy()

    ventana_actualizar_prod = Frame(root,height=800,width=1300,bg="#ADD8E6")
    ventana_actualizar_prod.pack()
    
    cuadro_productoss = Frame(ventana_actualizar_prod,width=1200,height=750,bg="white",bd=0,relief=RIDGE)
    cuadro_productoss.place(x=50,y=25)
        
    Label(cuadro_productoss,text="Actualizar Productos",font=("Verdana",35,"bold"),fg="#3d3d3d",bg="white").place(x=350,y=20)
        
    productos_dentro_cuadro = Frame(cuadro_productoss,height=560,width=550,bg="white",bd=7,relief=RIDGE)
    productos_dentro_cuadro.place(x=320,y=120)  

    def funcion_buscar_id_prod():
        global bandera_buscar_id_prod
        mi_conexion1 = conectar_database()
        mi_conexion1.reconnect()
        cursor_3 = mi_conexion1.cursor()
        cursor_3.execute("select producto_id from productos")
        item = cursor_3.fetchall()

        bandera_buscar_id_prod = 0
        try:
            for i in item:
                if actualizar_prod_id_t1.get() == int(i[0]):
                    bandera_buscar_id_prod = 1
                    cursor_3.execute("select clase,marca,nombre_producto,stock,precio_unitario from productos where producto_id = %s",(actualizar_prod_id_t1.get(),))
                    res = cursor_3.fetchall()
                    temp1 = str(res[0][0]) # Clase
                    temp2 = str(res[0][1]) # Subclase
                    temp3 = str(res[0][2]) # Nombre
                    temp4 = int(res[0][3]) # Stock
                    temp5 = float(res[0][4]) # Precio unitario

                    actualizar_prod_clase_texto_1.set(temp1)
                    actualizar_prod_subclase_texto_1.set(temp2)
                    actualizar_prod_nombre_texto_1.set(temp3)
                    actualizar_prod_stock_texto_1.set(temp4)
                    actualizar_prod_precio_texto_1.set(temp5)
            else:
                if(bandera_buscar_id_prod == 0):
                    messagebox.showerror("Error","Ingresar un ID válido")
                    actualizar_prod_clase_texto_1.set("")
                    actualizar_prod_subclase_texto_1.set("")
                    actualizar_prod_nombre_texto_1.set("")
                    actualizar_prod_stock_texto_1.set(0)
                    actualizar_prod_precio_texto_1.set(0.0)
            mi_conexion1.commit()
            mi_conexion1.close()
        except:
            pass
    
    def funcion_boton_actualizar():
        try:
            global bandera_buscar_id_prod
            if bandera_buscar_id_prod == 1:

                op = messagebox.askyesno("Actualizar producto","¿Actualizar producto?")

                if op > 0:
                    mi_conexion1 = conectar_database()
                    mi_conexion1.reconnect()
                    cursor_3 = mi_conexion1.cursor()
                    cursor_3.execute("update productos set clase=%s,marca=%s,nombre_producto=%s,stock=%s,precio_unitario=%s where producto_id = %s",(actualizar_prod_clase_texto_1.get(),
                    actualizar_prod_subclase_texto_1.get(),actualizar_prod_nombre_texto_1.get(),actualizar_prod_stock_texto_1.get(),actualizar_prod_precio_texto_1.get(),actualizar_prod_id_t1.get()))
                    mi_conexion1.commit()
                    mi_conexion1.close()
                    messagebox.showinfo("Actualizar producto","Producto actualizado exitosamente")
                    actualizar_prod_clase_texto_1.set("")
                    actualizar_prod_subclase_texto_1.set("")
                    actualizar_prod_nombre_texto_1.set("")
                    actualizar_prod_stock_texto_1.set(0)
                    actualizar_prod_precio_texto_1.set(0.0)
        except:
            pass
    
    def funcion_boton_borrar():
        actualizar_prod_clase_texto_1.set("")
        actualizar_prod_subclase_texto_1.set("")
        actualizar_prod_nombre_texto_1.set("")
        actualizar_prod_stock_texto_1.set(0)
        actualizar_prod_precio_texto_1.set(0.0)
        act_entrada1.delete(0,END)

    # Variables:
    actualizar_prod_id_t1 = IntVar()
    actualizar_prod_nombre_texto_1 = StringVar()
    actualizar_prod_clase_texto_1 = StringVar()
    actualizar_prod_subclase_texto_1 = StringVar()
    actualizar_prod_stock_texto_1 = IntVar()
    actualizar_prod_precio_texto_1 = DoubleVar()

    Label(productos_dentro_cuadro,text="ID:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=35)
    act_entrada1= Entry(productos_dentro_cuadro,font=("Verdana",11),width=17,bd=2,relief=GROOVE,textvariable=actualizar_prod_id_t1)
    act_entrada1.place(x=200,y=39)

    Label(productos_dentro_cuadro,text="Nombre:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=105)
    act_entrada2= Entry(productos_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=actualizar_prod_nombre_texto_1)
    act_entrada2.place(x=200,y=109)

    Label(productos_dentro_cuadro,text="Clase:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=175)
    act_entrada3= Entry(productos_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=actualizar_prod_clase_texto_1)
    act_entrada3.place(x=200,y=179)

    Label(productos_dentro_cuadro,text="Marca:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=245)
    act_entrada4= Entry(productos_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=actualizar_prod_subclase_texto_1)
    act_entrada4.place(x=200,y=249)

    Label(productos_dentro_cuadro,text="Stock:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=315)
    act_entrada5= Entry(productos_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=actualizar_prod_stock_texto_1)
    act_entrada5.place(x=200,y=319)

    Label(productos_dentro_cuadro,text="Precio unitario:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=385)
    act_entrada6= Entry(productos_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=actualizar_prod_precio_texto_1)
    act_entrada6.place(x=200,y=389)

    actualizar_boton_1 = PhotoImage(file=direccion_carpeta+"/Botones/actualizar_boton.png")
    Button(productos_dentro_cuadro,image=actualizar_boton_1,bg="white",bd=0,borderwidth=0,command=funcion_boton_actualizar).place(x=80,y=460)
    
    boton_borrar_1 = PhotoImage(file=direccion_carpeta+"/Botones/borrar_boton_1.png")
    Button(productos_dentro_cuadro,image=boton_borrar_1,bg="white",bd=0,borderwidth=0,command=funcion_boton_borrar).place(x=285,y=460)

    boton_buscar = PhotoImage(file=direccion_carpeta+"/Botones/buscar.png")
    Button(productos_dentro_cuadro,image=boton_buscar,bg="white",bd=0,borderwidth=0,command=funcion_buscar_id_prod).place(x=400,y=37)

    boton_salir_2 = PhotoImage(file=direccion_carpeta+"/Botones/producto_salir_1.png")
    Button(cuadro_productoss,image=boton_salir_2,bg="white",bd=0,borderwidth=0,command=ventana_administracion_productos).place(x=1020,y=35)
# Agregar clientes:
def agregar_clientes():
    global boton_agregar,cuadro_cliente,boton_borrar_1,boton_salir_1,ventana_agregar_cliente

    try:
        global bandera_borrar_cursor
        bandera_borrar_cursor = 1
    except:
        pass

    cuadro_cliente.destroy()

    ventana_agregar_cliente = Frame(root,height=800,width=1300,bg="#ADD8E6")
    ventana_agregar_cliente.pack()
        
    cuadro_cliente = Frame(ventana_agregar_cliente,width=1200,height=750,bg="white",bd=0,relief=RIDGE)
    cuadro_cliente.place(x=50,y=25)
     
    Label(cuadro_cliente,text="Agregar Cliente",font=("Verdana",35,"bold"),fg="#3d3d3d",bg="white").place(x=420,y=20)
        
    cliente_dentro_cuadro = Frame(cuadro_cliente,height=560,width=550,bg="white",bd=7,relief=RIDGE)
    cliente_dentro_cuadro.place(x=320,y=120)

    def funcion_boton_agregar():
        try:
            if(agregar_id_cliente_t1.get() == 0):
                messagebox.showerror("Error","ID del cliente necesaria")
            elif(agregar_nombre_cliente_t1.get() == " " or len(agregar_nombre_cliente_t1.get()) == 0):
                messagebox.showerror("Error","Nombre del cliente necesario")
            elif(agregar_celular_cliente_t1.get() == 0):
                messagebox.showerror("Error","Se requiere un número de contacto")
            elif(agregar_direccion_cliente_t1.get() == " " or len(agregar_direccion_cliente_t1.get()) == 0):
                messagebox.showerror("Error","Especifique la dirección")
            elif(agregar_dni_cliente_t1.get() == 0):
                messagebox.showerror("Error","DNI necesario")
            elif(agregar_usuario_cliente_t1.get() == " " or len(agregar_usuario_cliente_t1.get()) == 0):
                messagebox.showerror("Error","Usuario requerido")
            elif(agregar_clave_cliente_t1.get() == " " or len(agregar_clave_cliente_t1.get()) == 0):
                messagebox.showerror("Error","Clave requerida")
            else:
                op = messagebox.askyesno("Agregar cliente","¿Agregar cliente?")
                if op > 0:
                    mi_conexion1 = conectar_database()
                    mi_conexion1.reconnect()
                    cur3 = mi_conexion1.cursor()
                    cur3.execute("insert into clientes(cliente_id,nombre_cliente,celular,domicilio,DNI,usuario,clave) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                    (agregar_id_cliente_t1.get(),agregar_nombre_cliente_t1.get(),agregar_celular_cliente_t1.get(),agregar_direccion_cliente_t1.get(),agregar_dni_cliente_t1.get(),agregar_usuario_cliente_t1.get(),agregar_clave_cliente_t1.get(),)
                    )
                    mi_conexion1.commit()
                    mi_conexion1.close()
                    messagebox.showinfo("Registrar cliente","¡Cliente registrado exitosamente!")
        except:
            pass

    def funcion_boton_borrar():
        agregar_entrada_1.delete(0,END)
        agregar_entrada_2.delete(0,END)
        agregar_entrada_3.delete(0,END)
        agregar_entrada_4.delete(0,END)
        agregar_entrada_5.delete(0,END)
        agregar_entrada_6.delete(0,END)

    # Variables de clientes: 
    agregar_id_cliente_t1 = IntVar()
    agregar_nombre_cliente_t1 = StringVar()
    agregar_celular_cliente_t1 = IntVar()
    agregar_direccion_cliente_t1 = StringVar()
    agregar_dni_cliente_t1 = IntVar()
    agregar_usuario_cliente_t1 = StringVar()
    agregar_clave_cliente_t1 = StringVar()

    Label(cliente_dentro_cuadro,text="ID cliente:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=35)
    agregar_entrada_1 = Entry(cliente_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=agregar_id_cliente_t1)
    agregar_entrada_1.place(x=200,y=39)

    Label(cliente_dentro_cuadro,text="Nombre:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=105)
    agregar_entrada_2 = Entry(cliente_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=agregar_nombre_cliente_t1)
    agregar_entrada_2.place(x=200,y=109)

    Label(cliente_dentro_cuadro,text="Celular:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=175)
    agregar_entrada_3 = Entry(cliente_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=agregar_celular_cliente_t1)
    agregar_entrada_3.place(x=200,y=179)

    Label(cliente_dentro_cuadro,text="Domicilio:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=245)
    agregar_entrada_4 = Entry(cliente_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=agregar_direccion_cliente_t1)
    agregar_entrada_4.place(x=200,y=249)

    Label(cliente_dentro_cuadro,text="DNI:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=315)
    agregar_entrada_5 = Entry(cliente_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=agregar_dni_cliente_t1)
    agregar_entrada_5.place(x=200,y=319)

    Label(cliente_dentro_cuadro,text="Usuario:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=385)
    agregar_entrada_6 = Entry(cliente_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=agregar_usuario_cliente_t1)
    agregar_entrada_6.place(x=200,y=389)

    Label(cliente_dentro_cuadro,text="Clave:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=455)
    agregar_entrada_7 = Entry(cliente_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=agregar_clave_cliente_t1)
    agregar_entrada_7.place(x=200,y=459)

    boton_agregar = PhotoImage(file=direccion_carpeta+"/Botones/agregar_boton.png")
    Button(cliente_dentro_cuadro,image=boton_agregar,bg="white",bd=0,borderwidth=0,command=funcion_boton_agregar).place(x=80,y=500)

    boton_borrar_1 = PhotoImage(file=direccion_carpeta+"/Botones/borrar_boton_1.png")
    Button(cliente_dentro_cuadro,image=boton_borrar_1,bg="white",bd=0,borderwidth=0,command=funcion_boton_borrar).place(x=285,y=500)

    boton_salir_1 = PhotoImage(file=direccion_carpeta+"/Botones/producto_salir_1.png")
    Button(ventana_agregar_cliente,image=boton_salir_1,bg="white",bd=0,borderwidth=0,command=ventana_administracion_clientes).place(x=1060,y=62)
# Actualizar clientes:
def actualizar_clientes():
    global actualizar_boton_2,cuadro_cliente,boton_salir_3,boton_borrar_2,ventana_actualizar_cliente,boton_buscar_2
    
    try:
        global bandera_borrar_cursor
        bandera_borrar_cursor = 1
    except:
        pass
    
    cuadro_cliente.destroy()

    ventana_actualizar_cliente = Frame(root,height=800,width=1300,bg="#ADD8E6")
    ventana_actualizar_cliente.pack()
        
    cuadro_cliente = Frame(ventana_actualizar_cliente,width=1200,height=750,bg="white",bd=0,relief=RIDGE)
    cuadro_cliente.place(x=50,y=25)
        
    Label(cuadro_cliente,text="Actualizar Cliente",font=("Verdana",35,"bold"),fg="#3d3d3d",bg="white").place(x=368,y=20)
    
    cliente_dentro_cuadro = Frame(cuadro_cliente,height=600,width=550,bg="white",bd=7,relief=RIDGE)
    cliente_dentro_cuadro.place(x=320,y=120)  

    def funcion_buscar_id_cliente():
        global bandera_buscar_id_cliente
        mi_conexion_1 = conectar_database()
        mi_conexion_1.reconnect()
        cur3 = mi_conexion_1.cursor()
        cur3.execute("select cliente_id from clientes")
        item = cur3.fetchall()

        bandera_buscar_id_cliente = 0
        try:
            for i in item:
                if actualizar_id_cliente_t1.get() == int(i[0]):
                    bandera_buscar_id_cliente = 1
                    cur3.execute("select nombre_cliente,celular,domicilio,DNI,usuario,clave from clientes where cliente_id = %s",(actualizar_id_cliente_t1.get(),))
                    res = cur3.fetchall()

                    actualizar_nombre_cliente_t1.set(res[0][0])
                    actualizar_celular_cliente_t1.set(res[0][1])
                    actualizar_domicilio_cliente_t1.set(res[0][2])
                    actualizar_dni_cliente_t1.set(res[0][3])
                    actualizar_usuario_cliente_t1.set(res[0][4])
                    actualizar_clave_cliente_t1.set(res[0][5])
            else:
                if(bandera_buscar_id_cliente == 0):
                    messagebox.showerror("Error","Ingresar un ID válido")
                    funcion_boton_borrar()
            mi_conexion_1.commit()
            mi_conexion_1.close()
        except:
            pass
    
    def funcion_boton_actualizar():
        try:
            global bandera_buscar_id_cliente
            if bandera_buscar_id_cliente == 1:

                op = messagebox.askyesno("Actualizar cliente","¿Actualizar datos del cliente?")

                if op > 0:
                    mi_conexion_1 = conectar_database()
                    mi_conexion_1.reconnect()
                    cur3 = mi_conexion_1.cursor()
                    cur3.execute("update clientes set nombre_cliente=%s,celular=%s,domicilio=%s,DNI=%s,usuario=%s,clave=%s where cliente_id = %s",(actualizar_nombre_cliente_t1.get(),
                    actualizar_celular_cliente_t1.get(),actualizar_domicilio_cliente_t1.get(),actualizar_dni_cliente_t1.get(),actualizar_usuario_cliente_t1.get(),actualizar_clave_cliente_t1.get(),actualizar_id_cliente_t1.get(),))
                    mi_conexion_1.commit()
                    mi_conexion_1.close()
                    messagebox.showinfo("Actualizar cliente","¡Datos del cliente actualizados exitosamente!")
                    funcion_boton_borrar()
        except:
            pass
    
    def funcion_boton_borrar():
        global bandera_buscar_id_cliente

        bandera_buscar_id_cliente = 0
        act_entr1.delete(0,END)
        actualizar_nombre_cliente_t1.set("")
        actualizar_celular_cliente_t1.set(0)
        actualizar_domicilio_cliente_t1.set("")
        actualizar_dni_cliente_t1.set(0)
        actualizar_usuario_cliente_t1.set("")
        actualizar_clave_cliente_t1.set("")

    # Variables de cliente:
    actualizar_id_cliente_t1 = IntVar()
    actualizar_nombre_cliente_t1 = StringVar()
    actualizar_celular_cliente_t1 = IntVar()
    actualizar_domicilio_cliente_t1 = StringVar()
    actualizar_dni_cliente_t1 = IntVar()
    actualizar_usuario_cliente_t1 = StringVar()
    actualizar_clave_cliente_t1 = StringVar()

    Label(cliente_dentro_cuadro,text="ID:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=35)
    act_entr1= Entry(cliente_dentro_cuadro,font=("Verdana",11),width=17,bd=2,relief=GROOVE,textvariable=actualizar_id_cliente_t1)
    act_entr1.place(x=200,y=39)

    Label(cliente_dentro_cuadro,text="Nombre:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=105)
    act_entr2= Entry(cliente_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=actualizar_nombre_cliente_t1)
    act_entr2.place(x=200,y=109)

    Label(cliente_dentro_cuadro,text="Celular:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=175)
    act_entr3= Entry(cliente_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=actualizar_celular_cliente_t1)
    act_entr3.place(x=200,y=179)

    Label(cliente_dentro_cuadro,text="Domicilio:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=245)
    act_entr4= Entry(cliente_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=actualizar_domicilio_cliente_t1)
    act_entr4.place(x=200,y=249)

    Label(cliente_dentro_cuadro,text="DNI:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=315)
    act_entr5= Entry(cliente_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=actualizar_dni_cliente_t1)
    act_entr5.place(x=200,y=319)

    Label(cliente_dentro_cuadro,text="Usuario:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=385)
    act_entr6= Entry(cliente_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=actualizar_usuario_cliente_t1)
    act_entr6.place(x=200,y=389)

    Label(cliente_dentro_cuadro,text="Clave:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=455)
    act_entr7= Entry(cliente_dentro_cuadro,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=actualizar_clave_cliente_t1)
    act_entr7.place(x=200,y=459)

    actualizar_boton_2 = PhotoImage(file=direccion_carpeta+"/Botones/actualizar_boton.png")
    Button(cliente_dentro_cuadro,image=actualizar_boton_2,bg="white",bd=0,borderwidth=0,command=funcion_boton_actualizar).place(x=80,y=520)
    
    boton_borrar_2 = PhotoImage(file=direccion_carpeta+"/Botones/borrar_boton_1.png")
    Button(cliente_dentro_cuadro,image=boton_borrar_2,bg="white",bd=0,borderwidth=0,command=funcion_boton_borrar).place(x=285,y=520)

    boton_buscar_2 = PhotoImage(file=direccion_carpeta+"/Botones/cliente_buscar.png")
    Button(cliente_dentro_cuadro,image=boton_buscar_2,bg="white",bd=0,borderwidth=0,command=funcion_buscar_id_cliente).place(x=400,y=37)

    boton_salir_3 = PhotoImage(file=direccion_carpeta+"/Botones/producto_salir_1.png")
    Button(cuadro_cliente,image=boton_salir_3,bg="white",bd=0,borderwidth=0,command=ventana_administracion_clientes).place(x=1020,y=35)
# Evento del cursor 1:
def get_cursor_1(event):
    try:
        global tabla_productos,bandera_borrar_cursor,borrar_valor

        bandera_borrar_cursor = 0

        cursor_fila = tabla_productos.focus()
        contenido = tabla_productos.item(cursor_fila)
        cursor_item = contenido['values']
        borrar_valor = cursor_item[0]
    except:
        pass
# Evento del cursor 2:
def get_cursor_2(event):
    try:
        global tabla_clientes,bandera_borrar_cursor,borrar_valor

        bandera_borrar_cursor = 0

        cursor_fila = tabla_clientes.focus()
        contenido = tabla_clientes.item(cursor_fila)
        cursor_item = contenido['values']
        borrar_valor = cursor_item[0]
    except:
        pass
# Ventana administración de productos:
def ventana_administracion_productos():
    global cuadro_3,cuadro_inventario,pastel,texto_admin_1,boton_adm_imag,boton_buscar_prod,boton_agregar_prod,boton_actualizar_prod,boton_eliminar_prod,boton_salir_prod,ventana_agregar_productos
    global ventana_actualizar_prod,tabla_productos,borrar_valor,bandera_borrar_cursor

    try:
        cuadro_3.destroy()
    except:
        pass

    try:
        ventana_agregar_productos.destroy()
    except:
        pass

    try:
        ventana_actualizar_prod.destroy()
    except:
        pass

    def borrar_productos():
        try:
            global bandera_borrar_cursor,borrar_valor

            if bandera_borrar_cursor == 1:
                messagebox.showerror("Error","Por favor seleccione un producto")
            else:
                op = messagebox.askyesno("Borrar producto","¿Seguro que desea eliminar el producto?")
                if op > 0:
                    messagebox.showinfo("Info","Los registros fueron borrados")
                    mi_conexion_1 = conectar_database()
                    mi_conexion_1.reconnect()
                    cur3 = mi_conexion_1.cursor()
                    cur3.execute("delete from productos where producto_id = %s",(borrar_valor,))
                    mi_conexion_1.commit()
                    mi_conexion_1.close()
                    eliminar_todo()
                    bandera_borrar_cursor = 1
                    buscar_datos_agregados()
        except:
            pass
    
    def eliminar_todo():
        global tabla_productos

        x = tabla_productos.get_children()
        if x != '()':
            for child in x:
                tabla_productos.delete(child)

    def funcion_buscar_prod():
        global tabla_productos
        try:
            mi_conexion_1 = conectar_database()
            mi_conexion_1.reconnect()
            cur4 = mi_conexion_1.cursor()
            cur4.execute("select producto_id from productos")
            res = cur4.fetchall()
            flag = 1
            for i in res:
                if prodent_t1.get() == i[0]:
                    messagebox.showinfo("info","¡Producto encontrado!")
                    flag = 0
                    eliminar_todo()
                    cur4.execute("select producto_id,nombre_producto,clase,marca,stock,precio_unitario from productos where producto_id=%s",(prodent_t1.get(),))
                    items = cur4.fetchall()
                    if len(items) != 0:
                        for i in items:
                            tabla_productos.insert('',END,values=i)
                        mi_conexion_1.commit()
                    mi_conexion_1.close()
                    break
            if flag == 1:
                messagebox.showerror("Error","¡Producto no encontrado!")
                eliminar_todo()
                buscar_datos_agregados()
        except:
            eliminar_todo()
            buscar_datos_agregados()
    
    def buscar_datos_agregados():
        global tabla_productos
        mi_conexion_1 = conectar_database()
        mi_conexion_1.reconnect()
        cur3 = mi_conexion_1.cursor()
        cur3.execute("select producto_id,nombre_producto,clase,marca,stock,precio_unitario from productos")
        items = cur3.fetchall()

        if len(items) != 0:
            for i in items:
                tabla_productos.insert('',END,values=i)
            mi_conexion_1.commit()
        mi_conexion_1.close()   
    
    usuario = texto_admin_1.get()
    usuario = usuario.upper()
    
    cuadro_inventario = Frame(root,width=1300,height=800)
    cuadro_inventario.pack()

    Label(cuadro_inventario,image=pastel).pack()

    cuadro_interior_2 = Frame(cuadro_inventario,width=1250,height=760,bg="white")
    cuadro_interior_2.place(x=25,y=20)

    boton_adm_imag = PhotoImage(file=direccion_carpeta+"/Botones/adm_icon.png")
    Label(cuadro_interior_2,image=boton_adm_imag,bd=0).place(x=5,y=28)

    Label(cuadro_interior_2,text="Inventario",font=("Verdana",35,"bold"),bg="white",fg="#3d3d3d").place(x=487,y=5)
    Label(cuadro_interior_2,text=usuario,font=("Verdana",14,"bold"),bg="white",fg="#3d3d3d").place(x=50,y=25)

    cuadro_menu = LabelFrame(cuadro_interior_2,text=" Menu ",font=("Verdana",13,"bold"),fg="#3d3d3d",bg="white")
    cuadro_menu.place(x=20,y=130,width=435,height=610)
    
    prodent_t1 = IntVar()

    lbl0 = Label(cuadro_menu,text="ID de Producto",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl0.place(x=5,y=10)

    product_ent = Entry(cuadro_menu,font=("Verdana",11),width=25,bd=2,relief=GROOVE,textvariable=prodent_t1)
    product_ent.place(x=25,y=60)

    lbl1 = Label(cuadro_menu,text="Elegir opción",font=("Verdana",11,"bold"),bg="white",fg="#291d29",padx=18,pady=15)
    lbl1.place(x=5,y=100)

    boton_agregar_prod = PhotoImage(file=direccion_carpeta+"/Botones/agregar_producto.png")
    Button(cuadro_menu,image=boton_agregar_prod,bg="white",bd=0,borderwidth=0,command=agregar_productos).place(x=80,y=180)

    boton_actualizar_prod = PhotoImage(file=direccion_carpeta+"/Botones/actualizar_producto.png")
    Button(cuadro_menu,image=boton_actualizar_prod,bg="white",bd=0,borderwidth=0,command=actualizar_productos).place(x=80,y=250)

    boton_eliminar_prod = PhotoImage(file=direccion_carpeta+"/Botones/eliminar_producto.png")
    Button(cuadro_menu,image=boton_eliminar_prod,bg="white",bd=0,borderwidth=0,command=borrar_productos).place(x=80,y=320)

    boton_salir_prod = PhotoImage(file=direccion_carpeta+"/Botones/producto_salir.png")
    Button(cuadro_menu,image=boton_salir_prod,bg="white",bd=0,borderwidth=0,command=ventana_admin).place(x=140,y=500)

    boton_buscar_prod = PhotoImage(file=direccion_carpeta+"/Botones/buscar.png")
    Button(cuadro_menu,image=boton_buscar_prod,bd=0,bg="white",borderwidth=0,command=funcion_buscar_prod).place(x=310,y=58)

    cuadro_prod_2 = Frame(cuadro_interior_2,bg="white",bd=2,relief=RIDGE)
    cuadro_prod_2.place(x=470,y=140,height=600,width=750)

    scroll_x = Scrollbar(cuadro_prod_2,orient=HORIZONTAL)
    scroll_y = Scrollbar(cuadro_prod_2,orient=VERTICAL)
    tabla_productos = ttk.Treeview(cuadro_prod_2,columns=("ID Producto","Nombre","Clase","Marca","Stock","Precio Unitario"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=tabla_productos.xview)
    scroll_y.config(command=tabla_productos.yview)

    tabla_productos.heading("ID Producto",text="ID")
    tabla_productos.heading("Nombre",text="Nombre")
    tabla_productos.heading("Clase",text="Clase")
    tabla_productos.heading("Marca",text="Marca")
    tabla_productos.heading("Stock",text="Cantidad")
    tabla_productos.heading("Precio Unitario",text="Precio")
    
    tabla_productos['show'] = 'headings'

    tabla_productos.column("ID Producto",width=100,anchor=CENTER)
    tabla_productos.column("Nombre",width=120,anchor=CENTER)
    tabla_productos.column("Clase",width=120,anchor=CENTER)
    tabla_productos.column("Marca",width=120,anchor=CENTER)
    tabla_productos.column("Stock",width=120,anchor=CENTER)
    tabla_productos.column("Precio Unitario",width=120,anchor=CENTER)

    tabla_productos.pack(fill=BOTH,expand=1)
    buscar_datos_agregados()

    tabla_productos.bind("<ButtonRelease-1>",get_cursor_1) 
# Ventana administración de clientes:
def ventana_administracion_clientes():
    global cuadro_3,cuadro_cliente,pastel,texto_admin_1,boton_adm_imag,boton_buscar_cliente,boton_agregar_cliente,boton_actualizar_cliente,boton_borrar_cliente,boton_salir_cliente,ventana_agregar_cliente
    global ventana_actualizar_cliente,tabla_clientes,borrar_valor,bandera_borrar_cursor

    try:
        cuadro_3.destroy()
    except:
        pass

    try:
        ventana_agregar_cliente.destroy()
    except:
        pass

    try:
        ventana_actualizar_cliente.destroy()
    except:
        pass

    def eliminar_cliente():
        try:
            global bandera_borrar_cursor,borrar_valor

            if bandera_borrar_cursor == 1:
                messagebox.showerror("Error","¡Por favor seleccione un cliente!")
            else:
                op = messagebox.askyesno("Borrar registros","¿Está seguro?")
                if op > 0:
                    messagebox.showinfo("Info","Registros eliminados")
                    mi_conexion1 = conectar_database()
                    mi_conexion1.reconnect()
                    cur3 = mi_conexion1.cursor()
                    cur3.execute("delete from clientes where cliente_id = %s",(borrar_valor,))
                    mi_conexion1.commit()
                    mi_conexion1.close()
                    eliminar_todos()
                    bandera_borrar_cursor = 1
                    buscar_datos_agregados()
        except:
            pass
    
    def eliminar_todos():
        global tabla_clientes

        x = tabla_clientes.get_children()
        if x != '()':
            for child in x:
                tabla_clientes.delete(child)

    def funcion_buscar_cliente():
        global tabla_clientes,bandera_borrar_cursor
        bandera_borrar_cursor = 1
        try:
            mi_conexion1 = conectar_database()
            mi_conexion1.reconnect()
            cur4 = mi_conexion1.cursor()
            cur4.execute("select cliente_id from clientes")
            res = cur4.fetchall()
            flag = 1
            for i in res:
                if prodent_t2.get() == i[0]:
                    messagebox.showinfo("info","¡Cliente encontrado!")
                    flag = 0
                    eliminar_todos()
                    cur4.execute("select cliente_id,nombre_cliente,celular,domicilio,DNI,usuario,clave from clientes where cliente_id=%s",(prodent_t2.get(),))
                    items = cur4.fetchall()
                    if len(items) != 0:
                        for i in items:
                            tabla_clientes.insert('',END,values=i)
                        mi_conexion1.commit()
                    mi_conexion1.close()
                    break
            if flag == 1:
                messagebox.showerror("Error","¡Cliente no encontrado!")
                eliminar_todos()
                buscar_datos_agregados()
        except:
            eliminar_todos()
            buscar_datos_agregados()
    
    def buscar_datos_agregados():
        global tabla_clientes
        mi_conexion1 = conectar_database()
        mi_conexion1.reconnect()
        cur3 = mi_conexion1.cursor()
        cur3.execute("select cliente_id,nombre_cliente,celular,domicilio,DNI,usuario,clave from clientes")
        items = cur3.fetchall()

        if len(items) != 0:
            for i in items:
                tabla_clientes.insert('',END,values=i)
            mi_conexion1.commit()
        mi_conexion1.close()   
     
    usuario = texto_admin_1.get()
    usuario = usuario.upper()
    
    cuadro_cliente = Frame(root,width=1300,height=800)
    cuadro_cliente.pack()

    Label(cuadro_cliente,image=pastel).pack()

    cuadro_interior_2 = Frame(cuadro_cliente,width=1250,height=760,bg="white")
    cuadro_interior_2.place(x=25,y=20)

    boton_adm_imag = PhotoImage(file=direccion_carpeta+"/Botones/adm_icon.png")
    Label(cuadro_interior_2,image=boton_adm_imag,bd=0).place(x=5,y=28)

    Label(cuadro_interior_2,text="Administrar Clientes",font=("Verdana",35,"bold"),bg="white",fg="#3d3d3d").place(x=390,y=5)
    Label(cuadro_interior_2,text=usuario,font=("Verdana",14,"bold"),bg="white",fg="#3d3d3d").place(x=50,y=25)

    cuadro_menu = LabelFrame(cuadro_interior_2,text=" Menu ",font=("Verdana",13,"bold"),fg="#3d3d3d",bg="white")
    cuadro_menu.place(x=20,y=130,width=435,height=610)
    
    prodent_t2 = IntVar()

    lbl0 = Label(cuadro_menu,text="ID cliente",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl0.place(x=5,y=10)

    cliente_ent = Entry(cuadro_menu,font=("Verdana",11),width=25,bd=2,relief=GROOVE,textvariable=prodent_t2)
    cliente_ent.place(x=25,y=60)

    lbl1 = Label(cuadro_menu,text="Elegir opción",font=("Verdana",11,"bold"),bg="white",fg="#291d29",padx=18,pady=15)
    lbl1.place(x=5,y=100)

    boton_agregar_cliente = PhotoImage(file=direccion_carpeta+"/Botones/agregar_cliente.png")
    Button(cuadro_menu,image=boton_agregar_cliente,bg="white",bd=0,borderwidth=0,command=agregar_clientes).place(x=80,y=180)

    boton_actualizar_cliente = PhotoImage(file=direccion_carpeta+"/Botones/actualizar_cliente.png")
    Button(cuadro_menu,image=boton_actualizar_cliente,bg="white",bd=0,borderwidth=0,command=actualizar_clientes).place(x=80,y=250)

    boton_borrar_cliente = PhotoImage(file=direccion_carpeta+"/Botones/eliminar_cliente.png")
    Button(cuadro_menu,image=boton_borrar_cliente,bg="white",bd=0,borderwidth=0,command=eliminar_cliente).place(x=80,y=320)

    boton_salir_cliente = PhotoImage(file=direccion_carpeta+"/Botones/cliente_salir.png")
    Button(cuadro_menu,image=boton_salir_cliente,bg="white",bd=0,borderwidth=0,command=ventana_admin).place(x=140,y=500)

    boton_buscar_cliente = PhotoImage(file=direccion_carpeta+"/Botones/cliente_buscar.png")
    Button(cuadro_menu,image=boton_buscar_cliente,bd=0,bg="white",borderwidth=0,command=funcion_buscar_cliente).place(x=310,y=58)

    cuadro_cliente_2 = Frame(cuadro_interior_2,bg="white",bd=2,relief=RIDGE)
    cuadro_cliente_2.place(x=470,y=140,height=600,width=750)

    scroll_x = Scrollbar(cuadro_cliente_2,orient=HORIZONTAL)
    scroll_y = Scrollbar(cuadro_cliente_2,orient=VERTICAL)
    tabla_clientes = ttk.Treeview(cuadro_cliente_2,columns=("Id cliente","Nombre","Celular","Domicilio","DNI","Usuario","Clave"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=tabla_clientes.xview)
    scroll_y.config(command=tabla_clientes.yview)

    tabla_clientes.heading("Id cliente",text="ID")
    tabla_clientes.heading("Nombre",text="Nombre")
    tabla_clientes.heading("Celular",text="Celular")
    tabla_clientes.heading("Domicilio",text="Domicilio")
    tabla_clientes.heading("DNI",text="DNI")
    tabla_clientes.heading("Usuario",text="Usuario")
    tabla_clientes.heading("Clave",text="Clave")
    
    tabla_clientes['show'] = 'headings'

    tabla_clientes.column("Id cliente",width=50,anchor=CENTER)
    tabla_clientes.column("Nombre",width=50,anchor=CENTER)
    tabla_clientes.column("Celular",width=50,anchor=CENTER)
    tabla_clientes.column("Domicilio",width=50,anchor=CENTER)
    tabla_clientes.column("DNI",width=50,anchor=CENTER)
    tabla_clientes.column("Usuario",width=50,anchor=CENTER)
    tabla_clientes.column("Clave",width=50,anchor=CENTER)

    tabla_clientes.pack(fill=BOTH,expand=1)
    buscar_datos_agregados()

    tabla_clientes.bind("<ButtonRelease-1>",get_cursor_2)
# Ventana administración de facturas:
def ventana_administracion_facturas():
    global cuadro_3,pastel,cuadro_factura,texto_admin_1,boton_adm_imag,boton_salir_factura,boton_borrar_factura,boton_buscar_factura,tabla_facturas,bandera_borrar_factura,factura_t1
    global borrar_valor_factura
    
    try:
        cuadro_3.destroy()
    except:
        pass
    
    factura_t1 = IntVar()
    bandera_borrar_factura = 1
    usuario = texto_admin_1.get()
    usuario = usuario.upper()

    def buscar_datos_agregados():
        global tabla_facturas

        mi_conexion1 = conectar_database()
        mi_conexion1.reconnect()
        curs = mi_conexion1.cursor()
        curs.execute("select num_factura,fecha,nombre_cliente,celular_cliente from facturas")
        items = curs.fetchall()

        if len(items) != 0:
            for i in items:
                tabla_facturas.insert('',END,values=i)
            mi_conexion1.commit()
        mi_conexion1.close()
    
    def ventana_limpiar_facturas():
        global tabla_facturas

        x = tabla_facturas.get_children()
        if x != '()':
            for i in x:
                tabla_facturas.delete(i)

    def funcion_buscar_facturas():
        global factura_t1,tabla_facturas,bandera_borrar_factura
        bandera_borrar_factura = 1
        try:    
            mi_conexion1 = conectar_database()
            mi_conexion1.reconnect()
            curs = mi_conexion1.cursor()
            curs.execute("select num_factura,fecha,nombre_cliente,celular_cliente from facturas")
            items = curs.fetchall()
            mi_conexion1.commit()
            mi_conexion1.close()
        
            flag = 1
            for i in items:
                if i[0] == factura_t1.get():
                    messagebox.showinfo("Encontrado",f"¡Factura {i[0]} encontrada!")
                    ventana_limpiar_facturas()
                    mi_conexion1 = conectar_database()
                    mi_conexion1.reconnect()
                    curs = mi_conexion1.cursor()
                    curs.execute("select num_factura,fecha,nombre_cliente,celular_cliente from facturas where num_factura=%s",(factura_t1.get(),))
                    res = curs.fetchall()
                    for j in res:
                        tabla_facturas.insert('',END,values=j)
                        mi_conexion1.commit()
                    mi_conexion1.close()     
                    flag = 0
                    break
            if flag == 1:
                messagebox.showerror("No encontrado","Factura no encontrada")
                ventana_limpiar_facturas()
                buscar_datos_agregados()
        except:
            ventana_limpiar_facturas()
            buscar_datos_agregados()
    
    def funcion_borrar_factura():
        try:
            global bandera_borrar_factura,borrar_valor_factura

            if bandera_borrar_factura == 1:
                messagebox.showerror("Error","Por favor elija una factura para borrar")
            else:
                op = messagebox.askyesno("Eliminar registros","¿Está seguro?")
                if op > 0:
                    fil = os.listdir(direccion_facturas)
                    for i in fil:
                        ans = int(i.split('.')[0])
                        if ans == borrar_valor_factura:
                            os.remove(f"F:/Visual Studio Code/Scripts_Selim/Scripts/Kwik_E_Mart/Facturas/{ans}.txt")
                            messagebox.showinfo("Info","¡Registro eliminado!")
                            break
                    mi_conexion1 = conectar_database()
                    mi_conexion1.reconnect()
                    cur3 = mi_conexion1.cursor()
                    cur3.execute("delete from facturas where num_factura = %s",(borrar_valor_factura,))
                    mi_conexion1.commit()
                    mi_conexion1.close()
                    ventana_limpiar_facturas()
                    bandera_borrar_factura = 1
                    buscar_datos_agregados()
        except:
            pass

    cuadro_factura = Frame(root,height=800,width=1300)
    cuadro_factura.pack()

    lbl = Label(cuadro_factura,image=pastel)
    lbl.pack()

    cuadro_factura_interior = Frame(cuadro_factura,width=1250,height=760,bg="white")
    cuadro_factura_interior.place(x=25,y=20)

    boton_adm_imag = PhotoImage(file=direccion_carpeta+"/Botones/adm_icon.png")
    Label(cuadro_factura_interior,image=boton_adm_imag,bd=0).place(x=5,y=28)

    Label(cuadro_factura_interior,text="Administrar Facturas",font=("Verdana",35,"bold"),bg="white",fg="#3d3d3d").place(x=420,y=5)
    Label(cuadro_factura_interior,text=usuario,font=("Verdana",14,"bold"),bg="white",fg="#3d3d3d").place(x=50,y=25)
    
    cuadro_menu = LabelFrame(cuadro_factura_interior,text=" Menu ",font=("Verdana",13,"bold"),fg="#3d3d3d",bg="white")
    cuadro_menu.place(x=20,y=130,width=435,height=610)

    lbl0 = Label(cuadro_menu,text="N° de Factura",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl0.place(x=5,y=10)

    factura_ent = Entry(cuadro_menu,font=("Verdana",11),width=25,bd=2,relief=GROOVE,textvariable=factura_t1)
    factura_ent.place(x=25,y=60)

    boton_buscar_factura = PhotoImage(file=direccion_carpeta+"/Botones/buscar.png")
    Button(cuadro_menu,image=boton_buscar_factura,bd=0,bg="white",borderwidth=0,command=funcion_buscar_facturas).place(x=310,y=58)

    lbl1 = Label(cuadro_menu,text="Elegir opción",font=("Verdana",11,"bold"),bg="white",fg="#291d29",padx=18,pady=15)
    lbl1.place(x=5,y=100)

    boton_borrar_factura = PhotoImage(file=direccion_carpeta+"/Botones/eliminar_factura.png")
    Button(cuadro_menu,image=boton_borrar_factura,bg="white",bd=0,borderwidth=0,command=funcion_borrar_factura).place(x=80,y=180)

    boton_salir_factura = PhotoImage(file=direccion_carpeta+"/Botones/producto_salir.png")
    Button(cuadro_menu,image=boton_salir_factura,bg="white",bd=0,borderwidth=0,command=ventana_admin).place(x=140,y=500)

    cuadro_factura_2 = Frame(cuadro_factura_interior,bg="white",bd=2,relief=RIDGE)
    cuadro_factura_2.place(x=470,y=140,height=600,width=750)

    scroll_x = Scrollbar(cuadro_factura_2,orient=HORIZONTAL)
    scroll_y = Scrollbar(cuadro_factura_2,orient=VERTICAL)
    tabla_facturas = ttk.Treeview(cuadro_factura_2,columns=("Num Fact","Fecha","Nombre de cliente","Contacto cliente"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=tabla_facturas.xview)
    scroll_y.config(command=tabla_facturas.yview)

    tabla_facturas.heading("Num Fact",text="N° Factura")
    tabla_facturas.heading("Fecha",text="Fecha")
    tabla_facturas.heading("Nombre de cliente",text="Nombre de cliente")
    tabla_facturas.heading("Contacto cliente",text="Contacto de cliente")
    
    tabla_facturas['show'] = 'headings'

    tabla_facturas.column("Num Fact",width=90,anchor=CENTER)
    tabla_facturas.column("Fecha",width=90,anchor=CENTER)
    tabla_facturas.column("Nombre de cliente",width=150,anchor=CENTER)
    tabla_facturas.column("Contacto cliente",width=150,anchor=CENTER)

    tabla_facturas.pack(fill=BOTH,expand=1)
    buscar_datos_agregados()
    tabla_facturas.bind("<Double-1>",funcion_ver_factura)
    tabla_facturas.bind("<ButtonRelease-1>",borrar_factura_cursor)
# Función ver factura:
def funcion_ver_factura(event):

    root1 = Tk()
    root1.title("Factura")
    root1.geometry("700x600+550+170")
    root1.config(bg="white")

    cursor_fila = tabla_facturas.focus()
    contenido = tabla_facturas.item(cursor_fila)
    cursor_item = contenido['values']
    borrar_valor_factura_1 = int(cursor_item[0])

    cuadro_factura_1 = Frame(root1)
    cuadro_factura_1.place(x=0,y=0,height=600,width=700)

    scr_y = Scrollbar(cuadro_factura_1,orient=VERTICAL)
    factura_area_texto = Text(cuadro_factura_1,yscrollcommand=scr_y.set,bd=0)
    scr_y.pack(side=RIGHT,fill=Y)
    scr_y.config(command=factura_area_texto.yview)
    factura_area_texto.pack(fill=BOTH,expand=1)

    for i in os.listdir(direccion_facturas):
        if int(i.split('.')[0]) == borrar_valor_factura_1:
            f1 = open(f"F:/Visual Studio Code/Scripts_Selim/Scripts/Kwik_E_Mart/Facturas/{i}","r")
            for j in f1:
                factura_area_texto.insert(END,j)
            f1.close()
            break

    root1.mainloop()
# Borrar factura cursor:
def borrar_factura_cursor(event):
    try:
        global tabla_facturas,bandera_borrar_factura,borrar_valor_factura

        bandera_borrar_factura = 0

        cursor_fila = tabla_facturas.focus()
        contenido = tabla_facturas.item(cursor_fila)
        cursor_item = contenido['values']
        borrar_valor_factura = cursor_item[0]
    except:
        pass
# Ventana cliente:
def ventana_clientes():
    global cuadro_cliente,cuadro_4,pastel,Boton_logout2,boton_buscar,boton_total,boton_generar,boton_borrar,boton_salir,boton_carrito,boton_borrar
    global boton_borrar_prod,txtarea,clientes_nombre,clientes_contacto,numero_factura,cant_t1,cat_t1,subclase_t1,prod_clase_t1,subclase_val,prod_val,stock_val
    global factura_entrada,precio_total,cuenta_total,cliente_entrada,contacto_entrada,cuenta_generada_factura,texto_cliente_1,boton_cliente_imag
   
    cuadro_cliente.destroy()
    
    subclase_val = []
    prod_val = []
    stock_val = []
    precio_total = 0
    cuenta_total = 0
    cuenta_generada_factura = 0
    usuario = texto_cliente_1.get()
    usuario = usuario.upper()


    cuadro_4 = Frame(root,width=1300,height=800)
    cuadro_4.pack()

    pastel = ImageTk.PhotoImage(file=direccion_carpeta+"/pastel_gradient.jpg")
    Label(cuadro_4,image=pastel).pack()

    cuadro_interior_1 = Frame(cuadro_4,width=1250,height=760,bg="white")
    cuadro_interior_1.place(x=25,y=20)
    
    Boton_logout2 = PhotoImage(file=direccion_carpeta+"/Botones/logout_boton_2.png")
    Button(cuadro_interior_1,image=Boton_logout2,bd=0,borderwidth=0,bg="white",command=ventana_iniciar_cliente).place(x=1095,y=17)

    boton_cliente_imag = PhotoImage(file=direccion_carpeta+"/Botones/adm_icon.png")
    Label(cuadro_interior_1,image=boton_cliente_imag,bd=0).place(x=5,y=28)
    Label(cuadro_interior_1,text=usuario,font=("Verdana",14,"bold"),bg="white",fg="#3d3d3d").place(x=50,y=25)

    Label(cuadro_interior_1,text="Compras",font=("Verdana",35,"bold"),fg="#3d3d3d",bg="white").place(x=435,y=5)
    
    def invocar_lista_clases():
        lista_clase["values"] = ["Comida","Bebida","Postre"]

    def llamar_lista_clases(event):
        lista_subclase["values"] = ["Marolio","LaSerenisima","CampoQuijano","Manaos","Grido"]
        lista_clase_prod["values"] = ['Mate', 'Cafe', 'Harina', 'Palmitos', 'Yerba', 'Mermelada', 'Cacao', 'Picadillo', 'Pate', 'Caballa', 'Arroz', 'Arvejas', 'Sardinas', 'Atun', 'Choclo', 'Lentejas', 'Leche', 'Yogurt', 'Soda', 'Helado']
        lista_subclase.current(0)
        lista_clase_prod.current(0)
        cantidad_entrada.delete(0,END)

        Label(cuadro_prod,text="                     ",font=("Verdana",10),bg="white",fg="#291d29").place(x=22,y=290)

        subclase_val = []
        if(lista_clase.get() == "Comida"):
            mi_conexion.reconnect()
            cursor_productos.execute("select marca from productos where clase='Comida' group by marca")
            item = cursor_productos.fetchall()

            for i in item:
                subclase_val.append(i)
            
            lista_subclase["values"] = subclase_val

        elif(lista_clase.get() == "Bebida"):
            mi_conexion.reconnect()
            cursor_productos.execute("select marca from productos where clase='Bebida' group by marca")
            item = cursor_productos.fetchall()

            for i in item:
                subclase_val.append(i)

            lista_subclase["values"] = subclase_val

        elif(lista_clase.get() == "Postre"):
            mi_conexion.reconnect()
            cursor_productos.execute("select marca from productos where clase='Postre' group by marca")
            item = cursor_productos.fetchall()

            for i in item:
                subclase_val.append(i)

            lista_subclase["values"] = subclase_val
        else:
            pass
 
    def llamar_lista_subclase(event):
      
        lista_clase_prod["values"] = [" "]
        lista_clase_prod.current(0)
        prod_val = []
        cantidad_entrada.delete(0,END)

        Label(cuadro_prod,text="                     ",font=("Verdana",10),bg="white",fg="#291d29").place(x=22,y=290)

        if(lista_subclase.get() == "Marolio"):
            mi_conexion.reconnect()
            cursor_productos.execute("select nombre_producto from productos where marca='Marolio'")
            item = cursor_productos.fetchall()

            for i in item:
                prod_val.append(i)
            
            lista_clase_prod["values"] = prod_val

        elif(lista_subclase.get() == "LaSerenisima"):
            mi_conexion.reconnect()
            cursor_productos.execute("select nombre_producto from productos where marca='LaSerenisima'")
            item = cursor_productos.fetchall()

            for i in item:
                prod_val.append(i)
            
            lista_clase_prod["values"] = prod_val

        elif(lista_subclase.get() == "CampoQuijano"):
            mi_conexion.reconnect()
            cursor_productos.execute("select nombre_producto from productos where marca='CampoQuijano'")
            item = cursor_productos.fetchall()

            for i in item:
                prod_val.append(i)
            
            lista_clase_prod["values"] = prod_val

        elif(lista_subclase.get() == "Manaos"):
            mi_conexion.reconnect()
            cursor_productos.execute("select nombre_producto from productos where marca='Manaos'")
            item = cursor_productos.fetchall()

            for i in item:
                prod_val.append(i)
            
            lista_clase_prod["values"] = prod_val

        elif(lista_subclase.get() == "Grido"):
            mi_conexion.reconnect()
            cursor_productos.execute("select nombre_producto from productos where marca='Grido'")
            item = cursor_productos.fetchall()

            for i in item:
                prod_val.append(i)
            
            lista_clase_prod["values"] = prod_val

        else:
            pass

    def llamar_lista_prod_clase(event):
        global stock_val
         
        cantidad_entrada.delete(0,END)
        if(len(stock_val) != 0):
            Label(cuadro_prod,text="En Stock:        ",font=("Verdana",10),bg="white",fg="#291d29").place(x=20,y=290)
        
        mi_conexion.reconnect()
        cursor_productos.execute("select stock from productos where nombre_producto=%s",(lista_clase_prod.get(),))
        stock_val = cursor_productos.fetchall()
        
        if(len(stock_val) != 0):
            stock_lbl = Label(cuadro_prod,text="En Stock: "+str(stock_val[0][0]),font=("Verdana",10),bg="white",fg="red")
            stock_lbl.place(x=22,y=290)

    def factura_inicial():
        txtarea.delete("1.0",END)
        txtarea.insert(END,"\n \t\t\t\t     KWIK E MART ")
        txtarea.insert(END,"\n \t\t\t\t AV EVERGREEN, 742")
        txtarea.insert(END,"\n \t\t\t\t    TARTAGAL-4560 ") 
        txtarea.insert(END,"\n \t\t\t\t CEL: +54-1234567890 \n")
        txtarea.insert(END,"   "+str("=")*78)
        txtarea.insert(END,f"\n    N° de Factura : ")
        txtarea.insert(END,f"\n    Nombre: ")
        txtarea.insert(END,f"\n    Cel: ")
        txtarea.insert(END,"\n    Fecha: \n\n")
        txtarea.insert(END,"   "+str("-")*78)
        txtarea.insert(END,"\n    Producto\t\t\t\tCantidad\t\t\t\tPrecio\n")
        txtarea.insert(END,"   "+str("-")*78)
 
    def agregar_carrito():
        global cant_t1,prod_clase_t1,cuenta_total,precio_total,stock_val
        try:
            if(cuenta_total == 0):
                if(cant_t1.get() > 0 and len(stock_val) != 0):
                    mi_conexion.reconnect()
                    cursor_productos.execute("select stock from productos where nombre_producto = %s",(prod_clase_t1.get(),))
                    cantidad = cursor_productos.fetchall()
                    if(cant_t1.get() > int(cantidad[0][0])):
                        messagebox.showinfo("Info","Por favor seleccione una cantidad correcta")
                    else:
                        mi_conexion.reconnect()
                        cursor_productos.execute("select precio_unitario from productos where nombre_producto=%s",(prod_clase_t1.get(),))
                        item = cursor_productos.fetchall()
                        item = float(item[0][0])
                        txtarea.insert(END,f"\n    {prod_clase_t1.get()}\t\t\t\t{cant_t1.get()}\t\t\t\t{item*cant_t1.get():.2f}")
                        precio_total = precio_total + item*cant_t1.get()
                        cursor_productos.execute("update productos set stock=stock- %s where nombre_producto = %s",(cant_t1.get(),prod_clase_t1.get(),))
        except:
            pass
    
    def ventana_borrar_prod():
        global stock_val
        stock_val = []
        lista_subclase["values"] = [" "]
        lista_clase_prod["values"] = [" "]
        lista_clase["values"] = [" "]
        lista_subclase.current(0)
        lista_clase_prod.current(0)
        lista_clase.current(0)
        cantidad_entrada.delete(0,END)
        Label(cuadro_prod,text="                     ",font=("Verdana",10),bg="white",fg="#291d29").place(x=22,y=290)

    def calcular_total():
        global precio_total,cuenta_total
        if(precio_total != 0):
            if(cuenta_total == 0):
                Msgbox = messagebox.askquestion("Info","¡Calcular total!",icon="warning")
                if Msgbox == 'yes':
                    while cuenta_total == 0:
                        txtarea.insert(END,"\n\n\n   "+str("-")*78)
                        txtarea.insert(END,f"\n    Total\t\t\t\t     \t\t\t\t$ {precio_total:.2f}")
                        txtarea.insert(END,"\n   "+str("-")*78)
                        cuenta_total+=1
                        
    def generar_factura():
        global cuenta_total,cuenta_generada_factura,hoy
        ans = clientes_contacto.get()
        hoy = datetime.now()
        hoy = str(hoy)
        hoy = hoy[:19]

        try:
            if cuenta_generada_factura == 0:
                if cuenta_total != 0:
                    if len(clientes_nombre.get()) == 0 or clientes_nombre.get() == " ":
                        messagebox.showwarning("¡Cuidado!","Requiere nombre del cliente")
                    elif(clientes_contacto.get() == "" or ans.isdigit() == False or len(ans) != 10):
                        messagebox.showwarning("¡Cuidado!","Requiere el contacto del cliente")
                    else:
                        while cuenta_generada_factura == 0:
                            x = random.randint(100000,999999)
                            numero_factura.set(str(x))
                            messagebox.showinfo("Info","Factura generada exitosamente")
                            txtarea.delete("7.19","7.80")
                            txtarea.insert("7.20",f"{numero_factura.get()}")
                            txtarea.delete("8.19","8.80")
                            txtarea.insert("8.20",f"{clientes_nombre.get()}")
                            txtarea.delete("9.19","9.80")
                            txtarea.insert("9.20",f"{clientes_contacto.get()}")
                            txtarea.delete("10.19","10.80")
                            txtarea.insert("10.20",f"{hoy}")
                            guardar_factura()
                            cuenta_generada_factura+=1
                            mi_conexion.commit()

        except:
            pass
    
    def ventana_borrar_factura():
        global precio_total,cuenta_total,cliente_entrada,contacto_entrada,factura_entrada,cuenta_generada_factura

        op = messagebox.askyesno("Borrar ventana","¿Quiere borrar la ventana?")

        if op > 0:
            precio_total = 0
            cuenta_total = 0
            cuenta_generada_factura = 0
            txtarea.delete("1.0",END)
            factura_inicial()
            cliente_entrada.delete(0,END)
            contacto_entrada.delete(0,END)
            factura_entrada.delete(0,END)

        else:
            return

    def guardar_factura():
        global hoy
        ans = messagebox.askyesno("Guardar factura","¿Guardar factura generada?")
        if ans > 0:
            messagebox.showinfo("","Factura guardada exitosamente")
            bill_file = txtarea.get("1.0",END)
            op = open(direccion_facturas+"/"+str(numero_factura.get())+".txt","w")
            op.write(bill_file)
            op.close()
            mi_conexion1 = conectar_database()
            mi_conexion1.reconnect()
            curs = mi_conexion1.cursor()
            curs.execute("insert into facturas(num_factura,fecha,nombre_cliente,celular_cliente) VALUES(%s,%s,%s,%s)",
            (numero_factura.get(),hoy,clientes_nombre.get(),clientes_contacto.get())
            )
            mi_conexion1.commit()
            mi_conexion1.close()
        else:
            return
    
    def buscar_factura():    
        flag = 0
        try:
            for i in os.listdir(direccion_facturas):
                if int(i.split('.')[0]) == numero_factura.get():
                    f1 = open(f"F:/Visual Studio Code/Scripts_Selim/Scripts/Kwik_E_Mart/Facturas/{i}","r")
                    txtarea.delete("1.0",END)
                    for j in f1:
                        txtarea.insert(END,j)
                    f1.close()
                    flag = 1
                    break
            if flag == 0:
                messagebox.showerror("Error","Número de factura incorrecto")
        except:
            pass
    
    def ventana_salir():
        global root

        op = messagebox.askyesno("Salir","¿Está seguro que desea salir?")
        
        if op > 0:
            root.destroy()
        else:
            return

    # Variables

    # Clientes
    clientes_nombre = StringVar()
    clientes_contacto = StringVar()
    numero_factura = IntVar()

    # Productos
    cant_t1 = IntVar()
    cat_t1 = StringVar()
    subclase_t1 = StringVar()
    prod_clase_t1 = StringVar()

    # Area Clientes:

    cuadro_clientes = LabelFrame(cuadro_interior_1,text=" Detalle de cliente ",font=("Verdana",13,"bold"),fg="#3d3d3d",bg="white")
    cuadro_clientes.place(x=15,y=88,width=1220)

    lbl0 = Label(cuadro_clientes,text="Nombre de cliente",font=("Verdana",11),bg="white",fg="#291d29",pady=18,padx=15)
    lbl0.grid(row=0,column=0)

    cliente_entrada = Entry(cuadro_clientes,width=27,font=("Verdana",10),bd=2,relief=GROOVE,textvariable=clientes_nombre)
    cliente_entrada.grid(row=0,column=1)

    lbl1 = Label(cuadro_clientes,text="N° de contacto",font=("Verdana",11),bg="white",fg="#291d29",pady=18,padx=15)
    lbl1.grid(row=0,column=2)

    contacto_entrada = Entry(cuadro_clientes,width=27,font=("Verdana",10),bd=2,relief=GROOVE,textvariable=clientes_contacto)
    contacto_entrada.grid(row=0,column=3)

    lbl2 = Label(cuadro_clientes,text="N° de factura",font=("Verdana",11),bg="white",fg="#291d29",pady=18,padx=15)
    lbl2.grid(row=0,column=4)

    factura_entrada = Entry(cuadro_clientes,width=27,font=("Verdana",10),bd=2,relief=GROOVE,textvariable=numero_factura)
    factura_entrada.grid(row=0,column=5)

    Label(cuadro_clientes,text="   ",bg="white").grid(row=0,column=6)

    boton_buscar = PhotoImage(file=direccion_carpeta+"/Botones/buscar.png")
    Button(cuadro_clientes,bg="white",bd=0,borderwidth=0,image=boton_buscar,command=buscar_factura).grid(row=0,column=7)

    # Area de productos

    cuadro_prod = LabelFrame(cuadro_interior_1,text=" Productos ",font=("Verdana",13,"bold"),fg="#3d3d3d",bg="white")
    cuadro_prod.place(x=15,y=180,width=507,height=455)

    lbl3 = Label(cuadro_prod,text="Seleccionar Clase",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl3.place(x=5,y=10)
    
    lista_clase = ttk.Combobox(cuadro_prod,textvariable=cat_t1,font=("Verdana",10),width=50,height=15,state="readonly",postcommand=invocar_lista_clases)
    lista_clase.place(x=25,y=51)
    lista_clase.bind("<<ComboboxSelected>>",llamar_lista_clases)

    lbl4 = Label(cuadro_prod,text="Marca",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl4.place(x=5,y=80)

    lista_subclase = ttk.Combobox(cuadro_prod,textvariable=subclase_t1,font=("Verdana",10),width=50,height=15,state="readonly")
    lista_subclase.place(x=25,y=120)
    lista_subclase.bind("<<ComboboxSelected>>",llamar_lista_subclase)
    
    lbl5 = Label(cuadro_prod,text="Producto",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl5.place(x=5,y=150)

    lista_clase_prod = ttk.Combobox(cuadro_prod,textvariable=prod_clase_t1,font=("Verdana",10),width=50,height=15,state="readonly")
    lista_clase_prod.place(x=25,y=190)
    lista_clase_prod.bind("<<ComboboxSelected>>",llamar_lista_prod_clase)
    
    lbl6 = Label(cuadro_prod,text="Cantidad",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl6.place(x=5,y=220)

    cantidad_entrada = Entry(cuadro_prod,font=("Verdana",10),width=52,bd=2,relief=GROOVE,textvariable=cant_t1)
    cantidad_entrada.place(x=25.5,y=260)

    boton_carrito = PhotoImage(file=direccion_carpeta+"/Botones/carrito_boton.png")
    Button(cuadro_prod,image=boton_carrito,bg="white",bd=0,borderwidth=0,command=agregar_carrito).place(x=80,y=335)

    boton_borrar_prod = PhotoImage(file=direccion_carpeta+"/Botones/borrar_producto.png")
    Button(cuadro_prod,image=boton_borrar_prod,bg="white",bd=0,borderwidth=0,command=ventana_borrar_prod).place(x=260,y=335)
    
    ventana_borrar_prod()
    # Area de confirmar compra

    cuadro_confirm = LabelFrame(cuadro_interior_1,text=" Confirmar ",font=("Verdana",13,"bold"),fg="#3d3d3d",bg="white")
    cuadro_confirm.place(x=15,y=640,width=507,height=100)
 
    boton_total = PhotoImage(file=direccion_carpeta+"/Botones/total.png")
    Button(cuadro_confirm,image=boton_total,bg="white",bd=0,borderwidth=0,command=calcular_total).place(x=10,y=20)

    boton_generar = PhotoImage(file=direccion_carpeta+"/Botones/generar.png")
    Button(cuadro_confirm,image=boton_generar,bg="white",bd=0,borderwidth=0,command=generar_factura).place(x=133,y=20)

    boton_borrar = PhotoImage(file=direccion_carpeta+"/Botones/borrar_factura.png")
    Button(cuadro_confirm,image=boton_borrar,bg="white",bd=0,borderwidth=0,command=ventana_borrar_factura).place(x=262,y=20)

    boton_salir = PhotoImage(file=direccion_carpeta+"/Botones/salir.png")
    Button(cuadro_confirm,image=boton_salir,bg="white",bd=0,borderwidth=0,command=ventana_salir).place(x=388,y=20)

    # Area de facturación:

    cuadro_factura = LabelFrame(cuadro_interior_1,text=" Ventana de factura ",font=("Verdana",13,"bold"),bg="white",fg="#3d3d3d")
    cuadro_factura.place(x=530,y=180,height=560,width=705)

    scroll_y = Scrollbar(cuadro_factura,orient=VERTICAL)
    txtarea = Text(cuadro_factura,yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH,expand=1)

    factura_inicial()
# Comenzar aplicación:
root = Tk()
root.title("KWIK E MART")
root.geometry("1300x750+100+0")

ventana_inicial()

root.mainloop()