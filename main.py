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


#Saludo de bienvenida
print("Sistema de gestión de productos")


#Variable global que almacena los productos (hardcodeada con ejemplos)
global productos
productos = [{"nombre":"SSD 256GB", "categoria":"Almacenamiento", "precio":"16580"},
             {"nombre":"SSD 480GB", "categoria":"Almacenamiento", "precio":"20450"},
             {"nombre":"Procesador i7-11570F", "categoria":"Procesadores", "precio":"170580"},
             {"nombre":"Procesador i3-10400H", "categoria":"Procesadores", "precio":"110500"},
             {"nombre":"Memoria DDR4 8GB", "categoria":"Memorias", "precio":"21000"},
             {"nombre":"Memoria DDR4 16GB", "categoria":"Memorias", "precio":"32000"},
             {"nombre":"Memoria DDR4 32GB", "categoria":"Memorias", "precio":"48000"},
            ] #Lista para almacenar los productos.



#Mostrar el menu principal.
def menu_principal():
    print("\n Ingrese el número de la opción deseada:")
    print("1 - Ingresar nuevo producto")
    print("2 - Ver productos")
    print("3 - Buscar producto")
    print("4 - Eliminar producto")
    print("5 - Salir")
    seleccionar_opcion()



#Función de selección principal.
def seleccionar_opcion():
    try:
        opcion = int(input("Opción: "))
        if opcion > 0 and opcion <= 5:
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

                case _:
                    print("Ingrese una opción...")
        else:
            print("Opcion invalida, ingrese una opción \n")
                
    except:
        print("Entrada vacia, ingrese una opción \n")



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
    
    if len(productos) != 0:
        print("Productos guardados: \n")
        for p in productos:
            print("Index:", productos.index(p), "|",
                "Nombre:", p["nombre"], "|",
                "Categoría:", p["categoria"], "|",
                "Precio: $", p["precio"])
    else:
        print("Aún no hay productos guardados... \n")



#Funcion para buscar productos almacenados en la lista por nombre o letra.
def opcion_buscar_productos():
    resultados = []
    busqueda = input("Ingrese el nombre de un producto o categoria para buscarlo: ")
    if busqueda != "":
        print("Buscando ", busqueda)
        for p in productos:
            if  busqueda in p["nombre"] or busqueda in p["categoria"]:
                resultados.append(p)
                
        if len(resultados) != 0:
            print("Se encontraron ", len(resultados), " resultados")
            for r in resultados:
                print("Index:", productos.index(r), "|",
                "Nombre:", r["nombre"], "|",
                "Categoría:", r["categoria"], "|",
                "Precio: $", r["precio"])
        else:
            print("No se encontraron resultados \n")

    else:
        print("Debe ingresar un producto para buscar \n")



#Funcion para buscar productos por indice
def opcion_buscar_producto_por_index(indice):
    if indice != 0:
        resultado = productos[indice]
    else:
        print("Error buscando por indice")
    return resultado



#Funcion para eliminar productos 
def opcion_eliminar_producto():
    paraEliminar = input("Ingrese el numero de Index del producto que desea eliminar: ")
    if paraEliminar != "":
        indice = int(paraEliminar)
        entrada = opcion_buscar_producto_por_index(indice)
        print(entrada["nombre"])
        confirmacion = input("¿Confirmar eliminación? S/N \n")
        if confirmacion == "s" or confirmacion == "S":
            productos.pop(indice)
            print("Eliminando ", entrada["nombre"])
        else:
            print("Nada se eliminará \n")
    else:
        print("Nada para eliminar, ingrese un Index")



#Función para guardar el nuevo producto al final de la lista.
def guardar(nombre, categoria, precio):
    if nombre != "" and categoria != "" and precio != "":
        nuevaEntrada = {
            "nombre":nombre,
            "categoria":categoria,
            "precio":precio
        }
        productos.append(nuevaEntrada)
        print(nombre, " guardado")

    else:
        print("Faltan datos... \n")



#Bucle principal, se detiene cuando se selecciona la opción 5 y la variable corriendo se vuelve False
while corriendo == True:
    menu_principal()
    if corriendo == False:
        break

