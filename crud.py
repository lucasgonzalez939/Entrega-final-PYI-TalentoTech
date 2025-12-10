#FUNCIONES CRUD PARA LA BASE DE DATOS

#Función para crear un nuevo producto en la base de datos.
def create(db, nombre, descripcion, cantidad, precio, categoria, alerta_stock):
    cursor = db.cursor()
    cursor.execute('''INSERT INTO inventario (nombre, descripcion, cantidad, precio, categoria, fecha_ingreso, alerta_stock)
                      VALUES (?, ?, ?, ?, ?, DATE('now'), ?)''',
                   (nombre, descripcion, cantidad, precio, categoria, alerta_stock))
    db.commit()
    print(f"Producto '{nombre}' agregado a la base de datos.")


#Funcion para leer todos los productos de la base de datos.
def read(db):
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM inventario''')
    productos = cursor.fetchall()
    return productos


#Funcion para actualizar un producto en la base de datos.
def update(db, id, nombre, descripcion, cantidad, precio, categoria, alerta_stock):
    cursor = db.cursor()
    cursor.execute('''UPDATE inventario
                      SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?, fecha_actualizacion = DATE('now'), alerta_stock = ?
                      WHERE id = ?''',
                   (nombre, descripcion, cantidad, precio, categoria, alerta_stock, id))
    db.commit()
    print(f"Producto con ID {id} actualizado.")

#Funcion para eliminar un producto de la base de datos.
def delete(db, id):
    cursor = db.cursor()
    cursor.execute('''DELETE FROM inventario WHERE id = ?''', (id,))
    confirmacion =input("Confirma que desea eliminar el producto? S/N \n")
    if confirmacion == "s" or confirmacion == "S":
        db.commit()
        print(f"Producto con ID {id} eliminado de la base de datos.")
    else:
        print("Eliminación cancelada \n")