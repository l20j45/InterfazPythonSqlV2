import conexionlocal as connect
import menus as menu
import consultas as consulta

import mysql.connector
import sys

opciones = {"folio":1,"contrato":4,"personal":2,"cruzado":3,"modificar":5,"modificarfolio":6}

def run():
    busqueda=opciones[sys.argv[2]]
    parametro=sys.argv[1]
    menu.MenuFunes()
    baseDeDatos =int(input("ingresa tu base de datos: "))
    cnx = connect.conexion(baseDeDatos).conexioncompleta()
    interfazSql = cnx.cursor()
    if busqueda == 1:
        consulta.busquedaFolio(interfazSql,parametro,baseDeDatos)
    elif busqueda == 2:
        consulta.busquedaPersonal(interfazSql,parametro,baseDeDatos)
    elif busqueda == 3:
        consulta.busquedaCruzada(interfazSql,parametro,baseDeDatos)
    elif busqueda == 4:
        consulta.busquedaFolioContrato(interfazSql,parametro,baseDeDatos)
    elif busqueda == 5:
        consulta.modificarContrato(interfazSql,parametro,baseDeDatos,cnx)
    elif busqueda == 6:
        consulta.modificarFolio(interfazSql,parametro,baseDeDatos,cnx) 
     
    cnx.close()
if __name__ == '__main__':
    run()