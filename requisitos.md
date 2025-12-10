* Proyecto PreEntrega

Ingreso de datos de productos: 
El sistema debe permitir ingresar datos básicos de los productos: 
nombre, categoría, y precio (sin centavos). 
Estos datos deben almacenarse en una lista, 
donde cada producto sea representado/a 
como una sublista de tres elementos (nombre, categoría, y precio).

Visualización de productos registrados: 
El programa debe incluir una funcionalidad 
para mostrar en pantalla todos los productos ingresados. 
La información debe presentarse de manera ordenada y legible, 
con cada producto numerado.

Búsqueda de productos: 
El sistema debe permitir buscar productos por su nombre. 
Si encuentra coincidencias, 
debe mostrar la información completa de los productos que coincidan. Si
no hay coincidencias, debe informar que no se encontraron resultados.

Eliminación de productos: 
El sistema debe permitir eliminar un producto de la lista, 
identificándolo por su posición (número) en la lista.

Requisitos:
Usar listas para almacenar y gestionar los datos. 

Incorporar bucles while y for según corresponda. 

Validar entradas del usuario o usuaria, 
asegurándote de que no se ingresen datos vacíos o incorrectos.

Utilizar condicionales para gestionar las opciones del menú 
y las validaciones necesarias.

Presentar un menú que permita elegir 
entre las funcionalidades disponibles: 
agregar productos, visualizar productos, 
buscar productos y eliminar productos.

El programa debe continuar funcionando 
hasta que se elija una opción para salir.







* Entrega de Proyecto Final

Requerimientos

Base de datos: Crear una base de datos llamada 'inventario.db' para almacenar los datos de los productos. La tabla 'productos' debe contener las siguientes columnas:

'id': Identificador único del producto (clave primaria, autoincremental).

'nombre': Nombre del producto (texto, no nulo).

'descripcion': Breve descripción del producto (texto).

'cantidad': Cantidad disponible del producto (entero, no nulo).

'precio': Precio del producto (real, no nulo).

'categoria': Categoría a la que pertenece el producto (texto).

  
Funcionalidades de la aplicación

La aplicación debe permitir:

Registrar nuevos productos.

Visualizar datos de los productos registrados.

Actualizar datos de productos, mediante su ID.

Eliminación de productos, mediante su ID.

Búsqueda de productos, mediante su ID. De manera opcional, se puede implementar la búsqueda por los campos nombre o categoría.

Reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario o usuaria.

Entrega de Proyecto

Obligatorio

Interfaz de usuario

Implementar una interfaz de usuario básica, para interactuar con la base de datos a través de la terminal. La interfaz debe incluir un menú principal con las opciones necesarias para acceder a cada funcionalidad descrita anteriormente.

Opcional: Utilizar el módulo 'colorama' para mejorar la legibilidad y experiencia de usuario en la terminal, añadiendo colores a los mensajes y opciones

Entrega de Proyecto

Obligatorio

Requisitos técnicos

El código debe estar bien estructurado, utilizando funciones para modularizar la lógica de la aplicación.

Los comentarios deben estar presentes en el código, explicando las partes clave del mismo.