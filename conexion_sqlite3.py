import sqlite3
"""
try:
    mi_conexion = sqlite3.connect("database/miprimeradb.sqlite3")
    cursor = mi_conexion.cursor()

        cursor.execute("INSERT INTO puntuacion VALUES "\
            "(3,'25.08','75.25','50','100.17')")
        mi_conexion.commit()

    cursor.execute("SELECT max(ID) FROM puntuacion")
    N_PARTIDA = cursor.fetchall()
    N_PARTIDA = list(N_PARTIDA[0])
    print(N_PARTIDA[0]+1)


        mi_conexion.close()

except Exception as ex:
    print(ex)
"""

mi_conexion = sqlite3.connect("database/miprimeradb.sqlite3")
cursor = mi_conexion.cursor()
"""
        cursor.execute("INSERT INTO puntuacion VALUES "\
            "(3,'25.08','75.25','50','100.17')")
        mi_conexion.commit()
"""
cursor.execute("SELECT max(ID) FROM puntuacion")
N_PARTIDA = cursor.fetchall()
N_PARTIDA = list(N_PARTIDA[0])
print(N_PARTIDA[0]+1)

"""
        mi_conexion.close()
"""
