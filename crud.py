#Luis Fernandez, Alejandro Guevara
import json
def create(name,producto,path): #name=nombre del producto, producto=diccionario, path=ruta
    inventario={}
    productos_existentes=[]
    with open(path,"r") as archivo:
        inventario=json.load(archivo)
    for i in inventario["data"]:
        key=i["nombre"]
        productos_existentes.append(key)
    verificar= name in productos_existentes 
    if verificar==True:
        return print("El producto {} ya existe, por favor ingrese otro".format(name))
    else:
        inventario["data"].append(producto)
        with open(path,"w") as archivo:
            json.dump(inventario,archivo,indent=4)
        return print("El producto {} fue agregado con éxito".format(name))
def read(name,path): #name=nombre del producto, path=ruta
    inventario={}
    productos_existentes=[]
    with open(path,"r") as archivo:
        inventario=json.load(archivo)
    for i in inventario["data"]:
        key=i["nombre"]
        productos_existentes.append(key)
    verificar=name in productos_existentes
    if verificar==False:
        return print("El producto {} no existe en el inventario".format(name))
    else:
        for i in inventario["data"]:
            if i["nombre"]==name:
                print("Producto:{}\nPrecio:{}\nCantidad:{}".format(i["nombre"],i["precio"],i["cantidad"]))
    
def delete(name,path): #name=nombre del producto, path=ruta
    inventario={}
    productos_existentes=[]
    with open(path,"r") as archivo:
        inventario=json.load(archivo)
    for i in inventario["data"]:
        key=i["nombre"]
        productos_existentes.append(key)
    verificar=name in productos_existentes
    if verificar==False:
        return print("El producto {} no existe en el inventario".format(name))
    else:
        for i in inventario["data"]:
            if i["nombre"]==name:
                inventario["data"].remove(i)
            with open(path,"w") as archivo:
                json.dump(inventario,archivo,indent=4)
        return print("El producto {} fue eliminado con éxito".format(name))
   
def update_precio(nuevo_valor,name,path): #nuevo_valor=precio nuevo, name=nombre del producto, path=ruta
    inventario={}
    productos_existentes=[]
    with open(path,"r") as archivo:
        inventario=json.load(archivo)
    for i in inventario["data"]:
        key=i["nombre"]
        productos_existentes.append(key)
    verificar=name in productos_existentes
    if verificar==False:
        return print("El producto {} no existe en el inventario".format(name))
    else:
        for i in inventario["data"]:
            if i["nombre"]==name:
                indice=inventario["data"].index(i)
                inventario["data"][indice]["precio"]=nuevo_valor
                with open(path,"w") as archivo:
                        json.dump(inventario,archivo,indent=4)
        return print("El precio del producto {} fue actualizado con éxito".format(name))
def update_cantidad(up,nuevo_valor,name,path): #up=añadir o retirar, name=nombre del producto, path=ruta
    inventario={}
    productos_existentes=[]
    with open(path,"r") as archivo:
        inventario=json.load(archivo)
    for i in inventario["data"]:
        key=i["nombre"]
        productos_existentes.append(key)
    verificar=name in productos_existentes
    if verificar==False:
        return print("El producto {} no existe en el inventario".format(name))
    else:
        for i in inventario["data"]:
            if i["nombre"]==name:
                indice=inventario["data"].index(i)
                if up=="añadir":
                    inventario["data"][indice]["cantidad"]=inventario["data"][indice]["cantidad"]+nuevo_valor
                    with open(path,"w") as archivo:
                        json.dump(inventario,archivo,indent=4)
                    return print("La cantidad del producto {} fue actualizada con éxito".format(name))
                elif up=="retirar":
                    inventario["data"][indice]["cantidad"]=inventario["data"][indice]["cantidad"]-nuevo_valor
                    with open(path,"w") as archivo:
                        json.dump(inventario,archivo,indent=4)
                    return print("La cantidad del producto {} fue actualizada con éxito".format(name))
def read_all(path): #path=ruta
    inventario={}
    with open(path,"r") as archivo:
        inventario=json.load(archivo)
    for i in inventario["data"]:
      print("Producto:{}\nPrecio:{}\nCantidad:{}".format(i["nombre"],i["precio"],i["cantidad"]))
      print("")
    