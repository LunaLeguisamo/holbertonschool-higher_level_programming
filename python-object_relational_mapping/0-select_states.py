#!/usr/bin/python3
import MySQLdb
import sys

def main():
    #obtener argumentos de la linea de comandos
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    #conectar a la base de datos
    db = MySQLdb.connect(
        host="localhost", 
        port =3306, user=username, 
        password=password,
        db=database
        )
    
    cursor = db.cursor()
    
    #Ejecutar la consulta para obtener los states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    #Obtener todos los resultados
    states = cursor.fetchall()
    
    #Mostrar resultados
    for state in states:
        print(state)
        
    #Cerrar el cursor y la conexion
    cursor.close()
    db.close()
    
if __name__ == "__main__":
    main()