import sqlite3 # Importamos la librería para entre otras cosas crear la tabla con sqlite3
from colorama import init, Fore, Style, Back

init(autoreset=True)

# CONSTANTE ruta_db para disponer facilmente de la ubicacion de la base
ruta_db = "inventario.db"


#/////// FUNCIÓN para CONECTAR a nuestra base de datos, se llamará cada vez que debamos leer o modificar la base //////
def conectar_db():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    return conexion, cursor



#/////// FUNCIÓN para CREAR la tabla con sqlite3 ///////
def db_crear_tabla_productos():
    conexion, cursor = conectar_db()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        categoria TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL
        )"""
        )
    conexion.commit()
    conexion.close()


#/////// FUNCIÓN para INSERTAR registros en la tabla producto de nuestra DB ///////
"""
db_insertar_producto(producto)
1. recibe como argumento un diccionario con las clave/valor de cada campo de la tabla
2. inserta los datos en la tabla productos
"""

def db_insertar_producto(nombre, descripcion, categoria, cantidad, precio):

    try:
        # Rutima que inserta en la Tabla
        conexion, cursor = conectar_db()
        query = "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?, ?, ?, ?, ?)" #guardo la query en una variable
        datos = (nombre, descripcion, categoria, cantidad, precio) #guardo los datos en una variable
        cursor.execute(query, datos) #utilizo las variables query y datos para execute
        conexion.commit()

        state = True #si sale todo bien
    except Exception as error: #captura el error ocurrido y lo guarda en la variable "error"
        print(Back.WHITE + Fore.RED + f"Error: {error}")
        conexion.close()
        state = False #si ocurre un error
        
    finally:
        conexion.close()
        return state



#/////// FUNCIÓN para LISTAR TODOS los productos de la tabla "productos" ///////
"""
db_get_productos()
1. lee todos los datos de la tabla productos
2. retorna una lista de tuplas con los datos de la tabla
"""

def db_get_productos():
    conexion, cursor = conectar_db()
    query = "SELECT * FROM productos"
    cursor.execute(query)
    lista_productos = cursor.fetchall()  # retorna una lista de tuplas de productos
    conexion.close()
    return lista_productos



#/////// FUNCIÓN para MOSTRAR un PRODUCTO determinado por id (busqueda por id) ///////
"""
db_get_producto_by_id(id)
1. busca en la tabla el registro segun el id
2. retorna una tupla con el resultado
"""

def db_get_producto_by_id(id):
    conexion, cursor = conectar_db()
    query = "SELECT * FROM productos WHERE id = ?"
    placeholders = (id,)
    cursor.execute(query, placeholders)
    producto = cursor.fetchone()  # retorna una tupla
    conexion.close()
    return producto




#/////// FUNCIÓN para MODIFICAR info de un producto ya existente ///////
"""
db_actualizar_producto(id, nueva_cantidad)
1. actualiza la cantidad del producto según el id
"""

def db_actualizar_producto(id, nueva_cantidad):
    conexion = sqlite3.connect(ruta_db)
    conexion, cursor = conectar_db()
    query = "UPDATE productos SET cantidad = ? WHERE id = ?"
    placeholders = (nueva_cantidad, id)
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()



#/////// FUNCIÓN para ELIMINAR un producto por id ///////
"""
db_eliminar_producto(id)
1. elimina de la tabla el producto con el id que recibe como argumento
"""

def db_eliminar_producto(id):
    conexion, cursor = conectar_db()
    query = "DELETE FROM productos WHERE id = ?"
    placeholders = (id,)
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()



#/////// FUNCIÓN para MINIMO STOCK ///////
"""
db_get_productos_by_condicion(minimo_stock)
1. retornar una lista_producto con aquellos registros cuya cantidad < minimo_stock
"""

def db_get_productos_by_condicion(minimo_stock):
    conexion, cursor = conectar_db()
    query = "SELECT * FROM productos WHERE cantidad < ?"
    placeholders = (minimo_stock,)
    cursor.execute(query, placeholders)
    lista_productos = cursor.fetchall()  # retorna una lista de tuplas
    conexion.close()
    return lista_productos

