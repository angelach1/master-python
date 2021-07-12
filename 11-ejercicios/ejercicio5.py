"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla:

ACCION              AVENTURA            DEPORTES
GTA                 ASSASINSS           FIFA 21
CALL OF DUTY        CRASH BAND.         PRO 21
PUGB                PRINCE OF PERSIA    MOTO GP 21

Mostrar esta información ordenada por categorías.
"""

tabla = [
    {
        "categoría": "ACCIÓN",
        "juegos": ["GTA", "CALL OF DUTY", "PUGB"]
    },
    {
        "categoría": "AVENTURA",
        "juegos": ["ASSASINSS", "CRASH BAND.", "PRINCE OF PERSIA"]
    },
    {
        "categoría": "DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for categoria in tabla:
    print(f"--------------{categoria['categoría']}----------------")
    for juego in categoria['juegos']:
        print(juego)