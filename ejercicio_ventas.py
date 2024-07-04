from funciones_ventas import *

while True:
    opc = menu()
    if opc == 1:
        nueva_venta()
    elif opc == 2:
        pass
    elif opc == 3:
        pass
    elif opc == 4:
        pass
    else:
        os.system("cls")
        print("Ha salido.")
        break