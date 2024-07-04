import csv
import os
import msvcrt

#Dicciorios

# Listas
F_pago = ["Efectivo","Tarjeta de débito","Tarjeta de crédito","Transferencia electrónica"]
ventas = []

# Utilidad
def limpiar():
    os.system("cls")
def esperar_tecla():
    print("<<Presione una tecla para continuar>>")
    msvcrt.getch()
def mostrar_lista():
        print(f"Lista de ventas:\n{ventas}")
        esperar_tecla()

# Menú
def menu():
    limpiar()
    print("""
Menú Almecén
=============
1. Registrar nueva venta
2. Reporte de ventas histórico
3. Reporte de ventas por producto
4. Reporte por formas de pago
5. Salir""")
    while True:
        try:
            opc = int(input("> Opción: "))
            if opc in(1,2,3,4,5):
                break
            else:
                print(">>> Opción inválida! Debe ingresar un número de la lista! <<<")
        except:
            print(">>> Error! Debe ingresar un número! <<<")
    return opc
def menu_f_pago():
        print("__Métodos de pago__")
        for i,pago in enumerate(F_pago):
            print(f"\t{i+1}) {pago}")    
# Leer
def nombre_producto():
    while True:
        nom_producto = input("__Ingrese nombre del producto__\n> ")
        if len(nom_producto) <= 2:
            print(">>> Error! Nombre demasiado corto! <<<")
        else:
            break
    return nom_producto

def cantidad_producto():
    print("__Cantidad de unidades__")
    cant_producto = validar_opc()
    return cant_producto

def valor_producto():
    print("__Valor unitario__ ")
    val_producto = validar_opc()
    return val_producto

def forma_pago():
    while True:
        menu_f_pago()
        opc = input("> Seleccione: ")
        #Opciones:
        if opc == '1':
            print(">> Ha elegido:",F_pago[0])
            f_pago = F_pago[0]
            break
        elif opc == '2':
            print(">> Ha elegido:",F_pago[1])
            f_pago = F_pago[1]
            break
        elif opc == '3':
            print(">> Ha elegido:",F_pago[2])
            f_pago = F_pago[2]
            break
        elif opc == '4':
            print(">> Ha elegido:",F_pago[3])
            f_pago = F_pago[3]
            break
        else:
            print("\t>>> Opción Inválida! Ingrese un número de la lista... <<<")
    return f_pago

# Opc 1 _ Nueva venta
def nueva_venta():
    limpiar()
    print("Registrando una nueva venta")
    print("============================")
    nom_producto = nombre_producto()
    cant_producto = cantidad_producto()
    val_producto = valor_producto()
    form_pago = forma_pago()
    total = cant_producto * val_producto
    ventas.append([nom_producto,cant_producto,val_producto,form_pago,total])
    archivo_csv()
    print(f"\n>> Venta registrada con éxito...\n>> Total compra: ${total}")
    esperar_tecla()

# Archivo CSV
def archivo_csv():
    with open ("ventas.csv","w",newline="") as csv_ventas:
        writer = csv.writer(csv_ventas)
        writer.writerow(['PRODUCTO','CANTIDAD','VALOR UNITARIO','FORMA DE PAGO','TOTAL'])
        writer.writerows(ventas)
    
# Validaciones 2
def validar_opc():
    while True:
        try:
            u_producto = int(input("> "))
            if u_producto <= 0:
                print(">>> Número inválido! Ingrese número mayor a 0 <<<")
            else:
                break
        except:
            print("Error! Debe ingresar un número!")
    return u_producto