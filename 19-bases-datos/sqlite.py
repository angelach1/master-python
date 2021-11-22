# Importar módulo
import sqlite3

# Conexión
conexion = sqlite3.connect("pruebas.db")

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255), 
    descripcion text, 
    precio int(255)
    );
""")

# Guardar cambios
conexion.commit()

# Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripción de mi producto', 550)")
conexion.commit()

# Borrar registros
cursor.execute("DELETE FROM productos")

conexion.commit()

# Insertar varios registros a la vez
productos = [
    ("Ordenador portátil", "Buen PC", 700),
    ("Teléfono móvil", "Buen Teléfono", 140),
    ("Placa Base", "Buena Placa", 80),
    ("Tablet 15", "Buena Tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES (NULL, ?, ?, ?)", productos)
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio = 678 WHERE precio = 80")
conexion.commit


# Listar datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print(producto)

for producto in productos:
    print("ID:", producto[0])
    print("Título:", producto[1])
    print("Descripción:", producto[2])
    print("Precio:", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone()
print(producto)



# Cerrar la conexión
conexion.close()
