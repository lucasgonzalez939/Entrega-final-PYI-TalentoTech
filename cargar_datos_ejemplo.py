#Cargar datos de ejemplo en la base de datos
#Datos de ejemplo para cargar en la base de datos
def cargar_datos_ejemplo(db):
    cursor = db.cursor()
    productos_ejemplo = [
        ("SSD 256GB", "Unidad de estado sólido de 256GB", 15, 16580, "Almacenamiento", 5),
        ("SSD 480GB", "Unidad de estado sólido de 480GB", 10, 20450, "Almacenamiento", 5),
        ("Procesador i7-11570F", "Procesador Intel Core i7 de 11va generación", 8, 170580, "Procesadores", 3),
        ("Procesador i3-10400H", "Procesador Intel Core i3 de 10ma generación", 12, 110500, "Procesadores", 3),
        ("Memoria DDR4 8GB", "Módulo de memoria RAM DDR4 de 8GB", 25, 21000, "Memorias", 10),
        ("Memoria DDR4 16GB", "Módulo de memoria RAM DDR4 de 16GB", 20, 32000, "Memorias", 10),
        ("Memoria DDR4 32GB", "Módulo de memoria RAM DDR4 de 32GB", 10, 48000, "Memorias", 5),
    ]
    
    for producto in productos_ejemplo:
        cursor.execute('''INSERT INTO inventario (nombre, descripcion, cantidad, precio, categoria, fecha_ingreso, alerta_stock)
                          VALUES (?, ?, ?, ?, ?, DATE('now'), ?)''', producto)
    
    db.commit()
    print("Datos de ejemplo cargados correctamente.")
