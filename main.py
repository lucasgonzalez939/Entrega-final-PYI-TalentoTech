#ATENCION
#Falta implementar un par de cosas como la verificacion y alertas de stock, pero no tengo mucho más tiempo ahora mismo

import sqlite3 #Importamos la libreria sqlite3 para almacenar en la base de datos local
import cargar_datos_ejemplo  #Importamos la funcion para cargar datos de ejemplo
import crud  #Importamos las funciones CRUD para la base de datos
from crud import create, read, update, delete  #Importamos las funciones CRUD específicas

#Conectamos o creamos la base de datos inventario.db
db = sqlite3.connect("inventario.db")

#Creamos el cursor para ejecutar comandos SQL
cursor = db.cursor()

#Creamos la tabla inventario si no existe aún
cursor.execute('''CREATE TABLE IF NOT EXISTS inventario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT,
    fecha_ingreso DATE NOT NULL,
    fecha_actualizacion DATE,
    alerta_stock INTEGER DEFAULT 0)''')

#Confirmamos si la tabla inventario existe llamando a sqlite_master
res = cursor.execute('''SELECT name FROM sqlite_master''')

#Si la tabla no se creó, reportamos y salimos del programa
if res.fetchone()[0] != 'inventario':
    print("La tabla no existe, vuelva a intentar. Saliendo...")
    exit()
else:
    print("Base de datos cargada correctamente")

if len(read(db)) == 0:
    cargar_datos_ejemplo.cargar_datos_ejemplo(db) #Cargamos datos de ejemplo si la tabla está vacía



#Variable global para controlar el bucle principal
global corriendo
corriendo = True



#Saludo de bienvenida
print("Sistema de gestión de productos")

#Implementar aqui el llamado a la funcion de reporte de alertas de stock y mostrarlas al iniciar






#Mostrar el menu principal.
def menu_principal():
    print("\n Ingrese el número de la opción deseada:")
    print("1 - Registrar nuevo producto")
    print("2 - Ver productos registrados")
    print("3 - Actualizar producto")
    print("4 - Buscar producto")
    print("5 - Eliminar producto")
    print("6 - Alertas de stock")
    print("7 - Salir")
    seleccionar_opcion()



#Función de selección principal.
def seleccionar_opcion():
    try:
        opcion = int(input("Opción: "))
        if opcion > 0 and opcion <= 7:
            print("Seleccionada opción",opcion)
            match opcion:
                case 1:
                    opcion_nuevo_producto()
            
                case 2:
                    opcion_ver_productos()

                case 3:
                    opcion_actualizar_producto()

                case 4:
                    opcion_buscar_productos()

                case 5:
                    opcion_eliminar_producto()

                case 6:
                    print("Funcionalidad de alertas de stock no implementada aún")

                case 7:
                    opcion_salir()

                case _:
                    print("Ingrese una opción...")
        else:
            print("Opcion invalida, ingrese una opción \n")
                
    except:
        print("Entrada vacia, ingrese una opción \n")

#Función para añadir un nuevo producto.
def opcion_nuevo_producto():
    nombre = input("Ingresa el nombre del nuevo producto: ")
    descripcion = input("Ingresa la descripción del nuevo producto: ")
    cantidad = input("Ingresa la cantidad del nuevo producto: ")
    precio = input("Ingresa el precio del nuevo producto: ")
    categoria = input("Ingresa la categoría del producto: ")
    alerta_stock = input("Ingresa el numero de alerta de stock del nuevo producto: ")
    create(db, nombre, descripcion, cantidad, precio, categoria, alerta_stock)
    print("Nuevo producto registrado: ", nombre)




#FUNCIONES DE INTERFAZ DE USUARIO

#Funcion para buscar productos almacenados en la lista por nombre o letra.
def opcion_buscar_productos():
    resultados = []
    busqueda = input("Ingrese el nombre de un producto o categoria para buscarlo: ")
    if busqueda != "":
        print("Buscando ", busqueda)
        resultados = buscar_nombre_categoria(busqueda)
        if len(resultados) != 0:
            print("Se encontraron ", len(resultados), " resultados")
            for r in resultados:
                print("Index:", r[0], "|",
                "Nombre:", r[1], "|",
                "Descripcion:", r[2], "|",
                "Categoría:", r[5], "|",
                "Precio: $", r[4],
                "Cantidad:", r[3], "\n")

        else:
            print("No se encontraron resultados \n")

    else:
        print("Debe ingresar un producto para buscar \n")



#Funcion para buscar productos por indice
def opcion_buscar_producto_por_id(id):
    if id != None:
        resultado = buscar_id(id)
    else:
        print("Error buscando por indice")
    return resultado



#Funcion para eliminar productos 
def opcion_eliminar_producto():
    paraEliminar = input("Ingrese el numero de id del producto que desea eliminar: ")
    if paraEliminar != "":
        identificador = int(paraEliminar)
        entrada = buscar_id(identificador)
        print(entrada["nombre"])
        delete(db, identificador)
    else:
        print("Nada para eliminar, ingrese un ID de producto")

def buscar_id(id):
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM inventario WHERE id = ?''', (id,))
    producto = cursor.fetchone()
    if producto:
        producto_dict = {
            "id": producto[0],
            "nombre": producto[1],
            "descripcion": producto[2],
            "cantidad": producto[3],
            "precio": producto[4],
            "categoria": producto[5],
            "fecha_ingreso": producto[6],
            "fecha_actualizacion": producto[7],
            "alerta_stock": producto[8]
        }
        return producto_dict
    else:
        print(f"No se encontró ningún producto con ID {id}")
        return None


#Funcion para buscar productos por nombre o categoria
def buscar_nombre_categoria(busqueda):
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM inventario WHERE nombre LIKE ? OR categoria LIKE ?''', (f'%{busqueda}%', f'%{busqueda}%'))
    productos = cursor.fetchall()
    if productos:
        return productos
    else:
        print(f"No se encontraron productos con el nombre o categoría '{busqueda}'")


def opcion_ver_productos():
    productos = read(db)
    if productos:
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Categoría: {producto[5]}, Precio: {producto[4]}")
    else:
        print("No hay productos registrados en la base de datos.")


def opcion_actualizar_producto():
    id_actualizar = input("Ingrese el ID del producto que desea actualizar: ")
    if id_actualizar != "":
        identificador = int(id_actualizar)
        producto = buscar_id(identificador)
        if producto:
            print(f"Actualizando producto: {producto['nombre']}")
            nombre = input(f"Nuevo nombre (actual: {producto['nombre']}): ") or producto['nombre']
            descripcion = input(f"Nueva descripción (actual: {producto['descripcion']}): ") or producto['descripcion']
            cantidad = input(f"Nueva cantidad (actual: {producto['cantidad']}): ") or producto['cantidad']
            precio = input(f"Nuevo precio (actual: {producto['precio']}): ") or producto['precio']
            categoria = input(f"Nueva categoría (actual: {producto['categoria']}): ") or producto['categoria']
            alerta_stock = input(f"Nuevo alerta de stock (actual: {producto['alerta_stock']}): ") or producto['alerta_stock']
            update(db, identificador, nombre, descripcion, cantidad, precio, categoria, alerta_stock)
        else:
            print("Producto no encontrado.")
    else:
        print("Debe ingresar un ID de producto para actualizar.")

#Función para cerrar el programa.
def opcion_salir():
    print("Gracias por utilizar nuestro sistema. Saliendo...")
    global corriendo
    corriendo = False


#Bucle principal, se detiene cuando se selecciona la opción 5 y la variable corriendo se vuelve False
while corriendo == True:
    menu_principal()
    if corriendo == False:
        break

