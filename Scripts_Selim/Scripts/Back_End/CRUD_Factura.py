import sys # Paquete usado para invocar a funciones y clases creadas en carpetas diferentes.
sys.path.append(r'F:\Visual Studio Code\Scripts_Selim\Scripts') # Dirección usada por defecto al escribir el código.
from Back_End.CRUD_Carrito import ver_listado, total_acum, descuento_acum, ver_prod_comprados, vaciar_carrito
from Back_End.CRUD_Producto import consultar_stock, actualizar_stock
# CRUD Factura:
# Total a pagar:
def total_pago(conexion, id_usuario):
    total_bruto = total_acum(conexion, id_usuario)
    descuento = descuento_acum(conexion, id_usuario)
    total_neto = total_bruto*(1-descuento)
    return total_neto
# Modificar stock:
def actualizar_stock_compra(conexion, id_usuario):
    prod_comp = ver_prod_comprados(conexion, id_usuario)
    id_prod = []
    cant_carrito = []
    cant_disp = []
    stock_actual = []
    for id in range(len(prod_comp)):
        id_prod.append((prod_comp[id][0]))
        cant_carrito.append((prod_comp[id][1]))
    for i in range(len(prod_comp)):
        cant_disp.append(consultar_stock(conexion,id_prod[i]))
    for j in range(len(prod_comp)):
        stock_actual.append(cant_disp[j] - cant_carrito[j])
    for k in range(len(prod_comp)):
        actualizar_stock(conexion, id_prod[k], stock_actual[k])
# Confirmar compra y emitir factura:
def emitir_factura(conexion, id_usuario, confirmar):
    ver_listado(conexion, id_usuario)
    total_pago(conexion, id_usuario)
    if (confirmar == True):
        actualizar_stock_compra(conexion, id_usuario)
        vaciar_carrito(conexion, id_usuario)
        print("Compra realizada")
    else:
        print("No se confirmó la compra")