from funciones_database import *
from colorama import init, Fore, Style, Back

init(autoreset=True)


# ******************************************************************
# DECLARACION DE FUNCIONES
# ******************************************************************

#/////// FUNCIÓN MENU ///////
def menu_mostrar_opciones():
    print("===================================================================")
    print(Style.BRIGHT + Fore.GREEN + "\n                         MENÚ PRINCIPAL")
    print("\n===================================================================")
    print(Fore.GREEN+
        """
        1. Agregar producto
        2. Mostrar productos
        3. Actualizar cantidad de producto
        4. Eliminar producto
        5. Buscar producto
        6. Reporte de bajo stock
        7. Salir
        """)
    print("===================================================================")
    
    opcion = input(Style.BRIGHT + Fore.BLUE +"Ingrese la opción deseada: ")
    return opcion



#/////// FUNCIÓN REGISTRAR producto ///////
"""
menu_registrar_producto()
1. solicita al usuario el ingreso de los datos
2. valida los valores y tipos de datos ingresados
3. llama a db_insertar_producto(producto) y le pasa como argumento el diccionario producto para que lo inserte en la base de datos
"""
def menu_registrar_producto():
    print(Fore.BLUE + "\nIngrese los siguientes datos del producto: ")
    nombre = input(Fore.BLUE + "Nombre: ")
    descripcion = input(Fore.BLUE + "Descripción: ")
    categoria = input(Fore.BLUE + "Categoría: ")

    # Valido cantidad
    while True:
        try:
            cantidad = int(input(Fore.BLUE + "Cantidad: "))
            break 
        except ValueError:
            print(Back.LIGHTWHITE_EX + Fore.RED + "Error: debe ingresar un número entero...")
            
    # Valido precio
    while True:
        try:
            precio = float(input(Fore.BLUE + "Precio: "))
            break
        except ValueError:
            print(Back.LIGHTWHITE_EX + Fore.RED + "ERROR: debe ingresar un valor numérico...}")

    # ejecuto la función insertar producto en la BD
    resultado = db_insertar_producto(nombre, descripcion, categoria, cantidad, precio)
    if resultado == True: #pruebo si el registro nuevo se incertó correctamente en la BD
        print(Fore.GREEN + "Registro insertado exitosamente...!")
    else:
        print(Back.LIGHTWHITE_EX + Fore.RED + "Algo fallo, el registro no pudo agregarse...")




#/////// FUNCIÓN MOSTRAR producto ///////
"""
menu_mostrar_productos()
1. no recibe ningún argumento
2. llama a db_get_productos() que retorna una lista de tuplas con el contenido de la tabla
3. si hay productos, los muestra en consola usando un bucle for
4. si no hay productos, muestra un mensaje indicando que no hay productos
"""
def menu_mostrar_productos():
    lista_productos = db_get_productos()  # retorna una lista

    if not lista_productos:
        print(Fore.GREEN + "No hay productos que mostrar...")
    else:
        for producto in lista_productos:
            print(producto)




#/////// FUNCIÓN ACTUALIZAR producto ///////
""""
def menu_actualizar_producto()
1. solicita al usuario que ingrese el id del producto a modificar
2. busca el producto en la tabla (si no existe informamos)
3. muestra la cantidad actual y solicita que ingrese la nueva cantidad
4. llama a db_actualizar_registro(id, nueva_cantidad) para que actualice la cantidad
"""
def menu_actualizar_producto():
    id = int(input(Fore.BLUE + "Ingrese el id del producto a actualizar: "))
    producto = db_get_producto_by_id(id)
    if producto:
        print(producto)
        nueva_cantidad = int(input(Fore.BLUE + "Ingrese la nueva cantidad: "))
        db_actualizar_producto(id, nueva_cantidad)
        print(Fore.GREEN + "Cantidad actualizada exitosamente...!")
    else:
        print(Fore.GREEN + "No existe el producto con el id ingresado...!")




#/////// FUNCIÓN ELIMINAR producto ///////
"""
menu_eliminar_producto()
1. solicita al usuario que ingrese el id del producto a eliminar
2. busca el producto por el id en la tabla (si no existe informa)
3. muestra el producto y solicita confirmación
4. llama a db_eliminar_producto(id) para eliminar el registro con el id indicado
"""
def menu_eliminar_producto():
    id = int(input(Back.WHITE + Fore.RED + "Ingrese el id del producto a eliminar: "))
    producto = db_get_producto_by_id(id)
    if producto:
        print(producto)
        db_eliminar_producto(id)
        print(Fore.GREEN + "Producto eliminado exitosamente...!")
    else:
        print(Fore.GREEN + "No existe el producto con el id ingresado...")




#/////// FUNCIÓN BUSCAR producto ///////
"""
menu_buscar_producto()
1. solicita al usuario que ingrese el id del producto a buscar
2. llama a db_get_producto_by_id(id)
3. si el producto existe lo muestra en consola, de lo contrario informa el error
"""
def menu_buscar_producto():
    id = int(input(Fore.BLUE + "Ingrese el id a buscar: "))
    producto = db_get_producto_by_id(id)

    if not producto:
        print(Fore.GREEN + "No se ha encontrado el producto...")
    else:
        print(producto)




#/////// FUNCIÓN BAJO STOCK producto ///////
"""
menu_reporte_bajo_stock()
1. solicita al usuario que ingrese la cantidad mínima de stock 
2. llama a db_get_productos_by_condicion(condicion) que retorna una lista_productos de bajo stock
3. si hay productos, los muestra en consola, de lo contrario informa que no hay productos en bajo stock
"""
def menu_reporte_bajo_stock():
    minimo_stock = int(input(Fore.BLUE + "Ingrese el minimo stock: "))
    lista_productos = db_get_productos_by_condicion(minimo_stock)
    if lista_productos:
        for producto in lista_productos:
            print(Back.WHITE + Fore.RED + f"test {producto}")
    else:
        print(Fore.GREEN + "No hay productos con stock menor a " + str(minimo_stock))
