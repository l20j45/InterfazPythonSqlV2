import conexionlocal as connect
import menus as menu
import consultas as consulta


import sys

opciones = {"Comparar":1,}

def run():
    busqueda=opciones[sys.argv[2]]
    parametro=sys.argv[1]
    menu.MenuFunes()
    baseDeDatos =int(input("ingresa tu base de datos: "))
    cnx = connect.conexion(baseDeDatos).conexioncompleta()
    interfazSql = cnx.cursor()
    if busqueda == 1:
        consulta.comparar(interfazSql,parametro,baseDeDatos) 


     
    cnx.close()
if __name__ == '__main__':
    run()