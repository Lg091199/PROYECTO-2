#Luis Fernández, Alejandro Guevara
import json
from mypackages.crud import create,read,delete,update_precio,update_cantidad,read_all
path="inventario.json"
while True:
    opcion_menu_principal=input("\nPor favor seleccione una de las opciones dadas:\n\n(1) Agregar producto\n(2) Buscar producto\n(3) Eliminar producto\n(4) Actualizar producto\n(5) Mostrar inventario\n(6) Salir\n\n")
    #AGREGAR PRODUCTO
    if opcion_menu_principal=="1":
        producto={}
        nombre=input("Ingrese el nombre del nuevo producto: ").upper()
        while True:
            try:
                precio=float(input("Ingrese el precio del nuevo producto: "))
                break
            except:
                print("Ingrese un valor numerico, intente nuevamente: ")
        while True:
            try:
                stock=int(input("Ingrese la cantidad que posee actualmente: "))
                break
            except:
                print("Ingrese un valor numerico, intente nuevamente: ")
        producto["nombre"]=nombre
        producto["precio"]=precio
        producto["cantidad"]=stock
        create(nombre,producto,path)
    #BUSCAR PRODUCTO
    elif opcion_menu_principal=="2":
        producto=input("Ingrese el nombre del producto que desea buscar: ").upper()
        read(producto,path)
    #ELIMINAR PRODUCTO
    elif opcion_menu_principal=="3":
        producto=input("Ingrese el nombre del producto que desea eliminar: ").upper()
        delete(producto,path)
    #ACTUALIZAR PRODUCTO
    elif opcion_menu_principal=="4":
        opcion_4=input("Ingrese una opción:\n(a) Actualizar precio\n(b) Actualizar cantidad\n")
        if opcion_4=="a":
            producto=input("Ingrese el nombre del producto que desea actualizar: ").upper()
            while True:
                try:
                    nuevo_precio=float(input("Ingrese el nuevo precio del producto:"))
                    break
                except:
                    print("Ingrese un valor numerico, intente nuevamente: ")
            update_precio(nuevo_precio,producto,path)
        elif opcion_4=="b":
            añadir_retirar=input("Ingrese una opción:\n(a) Añadir\n(b) Retirar\n")
            if añadir_retirar=="a":
                up="añadir"
                producto=input("Ingrese el nombre del producto\n").upper()
                while True:
                    try:
                        cantidad=int(input("Ingrese la cantidad que desea añadir: "))
                        break
                    except:
                        print("Ingrese un valor numerico, intente nuevamente: ")
                update_cantidad(up,cantidad,producto,path)
            elif añadir_retirar=="b":
                up="retirar"
                producto=input("Ingrese el nombre del producto\n").upper()
                while True:
                    try:
                        cantidad=int(input("Ingrese la cantidad que desea añadir: "))
                        break
                    except:
                        print("Ingrese un valor numerico, intente nuevamente: ")
                update_cantidad(up,cantidad,producto,path)
    #MOSTRAR INVENTARIO 
    elif opcion_menu_principal=="5":
        read_all(path)
    #SALIR
    elif opcion_menu_principal=="6":
        print("¡Gracias por utilizar nuestro programa!")    
        break
        
        
        
        
        
        