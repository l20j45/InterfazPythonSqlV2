import conexionlocal as connect
import menus as menu
import consultas as consulta


import sys

opciones = {"permisos":1,"usuarioSys":2,"verModulos":3,"cruzado":3,"modificar":5,"modificarfolio":6}

def run():
    busqueda=opciones[sys.argv[2]]
    parametro=sys.argv[1]
    menu.MenuFunes()
    baseDeDatos =int(input("ingresa tu base de datos: "))
    cnx = connect.conexion(baseDeDatos).conexioncompleta()
    interfazSql = cnx.cursor()
    if busqueda == 1:
        consulta.verPermisos(interfazSql,parametro,baseDeDatos) 
    elif busqueda == 2:
        consulta.verUsuarioSistema(interfazSql,parametro,baseDeDatos)
    elif busqueda == 3:
        consulta.verModulosPersonas(interfazSql,parametro,baseDeDatos) 

     
    cnx.close()
if __name__ == '__main__':
    run()