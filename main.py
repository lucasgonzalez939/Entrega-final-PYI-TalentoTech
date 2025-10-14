#Requerimientos del proyecto
# Ingreso de datos de productos: 
# El sistema debe permitir ingresar datos básicos de los productos: 
# nombre, categoría, y precio (sin centavos). 
# Estos datos deben almacenarse en una lista, 
# donde cada producto sea representado/a 
# como una sublista de tres elementos (nombre, categoría, y precio).

# Visualización de productos registrados: 
# El programa debe incluir una funcionalidad 
# para mostrar en pantalla todos los productos ingresados. 
# La información debe presentarse de manera ordenada y legible, 
# con cada producto numerado.

# Búsqueda de productos: 
# El sistema debe permitir buscar productos por su nombre. 
# Si encuentra coincidencias, 
# debe mostrar la información completa de los productos que coincidan. Si
# no hay coincidencias, debe informar que no se encontraron resultados.

# Eliminación de productos: 
# El sistema debe permitir eliminar un producto de la lista, 
# identificándolo por su posición (número) en la lista.


# Requisitos:
# Usar listas para almacenar y gestionar los datos. 

# Incorporar bucles while y for según corresponda. 

# Validar entradas del usuario o usuaria, 
# asegurándote de que no se ingresen datos vacíos o incorrectos.

# Utilizar condicionales para gestionar las opciones del menú 
# y las validaciones necesarias.

# Presentar un menú que permita elegir 
# entre las funcionalidades disponibles: 
# agregar productos, visualizar productos, 
# buscar productos y eliminar productos.

# El programa debe continuar funcionando 
# hasta que se elija una opción para salir.

global corriendo
corriendo = True

print("Sistema de gestión de productos")

productos = []

#Mostrar el menu principal.
def menu_principal():
    print("Ingrese el número de la opción deseada:")
    print("1 - Ingresar nuevo producto")
    print("2 - Ver productos")
    print("3 - Buscar producto")
    print("4 - Eliminar producto")
    print("5 - Salir")
    seleccionar_opcion()


#Función de selección principal.
def seleccionar_opcion():
    opcion = int(input("Opción: "))
    print("Seleccionada opción",opcion)
    match opcion:
        case 1:
            opcion_nuevo_producto()
            
        case 2:
            opcion_ver_productos()

        case 3:
            opcion_buscar_productos()

        case 4:
            opcion_eliminar_producto()

        case 5:
            opcion_salir()




#Función para cerrar el programa.
def opcion_salir():
    print("Gracias por utilizar nuestro sistema. Saliendo...")
    global corriendo
    corriendo = False


#Función para añadir un nuevo producto.
def opcion_nuevo_producto():
    nombreProducto = input("Ingresa el nombre del nuevo producto: ")
    categoriaProducto = input("Ingresa la categoría del producto: ")
    precioProducto = input("Ingresa el precio del nuevo producto: ")
    guardar(nombreProducto, categoriaProducto, precioProducto)
    

#Función para ver todos los productos en la lista.
def opcion_ver_productos():
    print("Productos guardados: ")
    


#Funcion para buscar productos almacenados en la lista por nombre o letra.
def opcion_buscar_productos(busqueda):
    print("Buscando {busqueda}")


#Funcion para eliminar productos 
def opcion_eliminar_producto(idProducto):
    print("Eliminando {idProducto}")


#Función para guardar el nuevo producto al final de la lista.
def guardar(nombre, categoria, precio):
    nuevaEntrada = {
        "nombre":nombre,
        "categoria":categoria,
        "precio":precio          
    }
    productos.append(nuevaEntrada)


#Bucle principal, se detiene cuando se selecciona la opción 5 y la variable corriendo se vuelve False
while corriendo == True:
    menu_principal()
    if corriendo == False:
        break

