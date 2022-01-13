import mysql.connector

# Conexión
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

# ¿La conexión ha sido correcta?
# print(database)

# Cursor
cursor = database.cursor(buffered = True)

# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

"""
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""


# Crear tablas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos(
        id int(10) auto_increment not null,
        marca varchar(40) not null,
        modelo varchar(40) not null,
        precio float(10, 2) not null,
        CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    )
""")

"""
cursor.execute("SHOW TABLES")

for tabla in cursor:
    print(tabla)
"""

# INSERTAR REGISTROS
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000),
]

#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)

database.commit()

# LISTAR REGISTROS
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")

result =  cursor.fetchall()

print("----------------TODOS MIS COCHES---------------------")
for coche in result:
    #print(coche)
    print(coche[0], coche[1], coche[2], coche[3])

print("----------------PRIMER COCHE DE LA TABLA---------------------")

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)

# BORRAR REGISTROS
cursor.execute("DELETE FROM vehiculos WHERE marca = 'renault'")
database.commit()

print(cursor.rowcount, "borrados.")

# ACTUALIZAR REGISTROS
cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca = 'Seat'")
database.commit()

print(cursor.rowcount, "actualizados.")





