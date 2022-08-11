import conexionlocal as connect
import menus as menu
import consultas as consulta
import sys

opciones = {"mod":1,"rutas":2,"contrato":3,"vista":4,"contratov":5,"abonos":6,"abonosrecibidos":7,"alta":8,"generarAbono":9}

def run():
    busqueda=opciones[sys.argv[2]]
    parametro=sys.argv[1]
    if busqueda!=8:
        menu.MenuFunes()
        baseDeDatos =int(input("ingresa tu base de datos: "))
    if busqueda == 1 or busqueda == 8:
        cnx = connect.conexion(13).conexioncompleta()
    else :
        cnx = connect.conexion(baseDeDatos).conexioncompleta()
    interfazSql = cnx.cursor()
    if busqueda == 1:
        consulta.modAplicacion(interfazSql,baseDeDatos) 
    elif busqueda == 2:
        consulta.busquedaRutas(interfazSql,parametro,baseDeDatos)
    elif busqueda == 3:
        consulta.busquedaContratoApp(interfazSql,parametro,baseDeDatos)
    elif busqueda == 4:
        consulta.buscarEnVista(interfazSql,parametro,baseDeDatos)
    elif busqueda == 5:
        consulta.busquedaContratoVista(interfazSql,parametro,baseDeDatos)
    elif busqueda == 6:
        consulta.busquedaAbonos(interfazSql,parametro,baseDeDatos)
    elif busqueda == 7:
        consulta.busquedaAbonosCobrador(interfazSql,parametro,baseDeDatos)
    elif busqueda == 8:
        consulta.agregarPersona(interfazSql,cnx)
    elif busqueda == 9:
        consulta.generadorDeAbonos(interfazSql,parametro,baseDeDatos)
    cnx.close()
if __name__ == '__main__':
    run()