from menus import *
import os
from urllib.parse import quote
import mysql.connector

def busquedaFolio(interfazSql,folios,baseDeDatos):
    rango = False
    for letra in folios:
        if letra in "-":
            rango=True
    if(rango):
        minyMax = folios.split("-")
        rango = range(int(minyMax[0]),int(minyMax[1]),)
    else:
        rango = folios.split(".")
    os.system ("clear")
    datos=menuFunesBusqueda(baseDeDatos)
    print(datos[0])
    if len(rango)!=0:
        file = open('folios.txt','w')
        file.write(datos[0])
        print ("\nfolios buscados: ")
        print(rango)
        for folioBuscar in rango: 
            file.write("\n")
            file.write("=====================================================\n")       
        
            sql="""SELECT idagente_folio 
                    FROM funeraria_agente_folios 
                    WHERE folio = %s """ % quote(str(folioBuscar), safe='')
            try:
                interfazSql.execute(sql)
                registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
                if len(registros) != 0:
                    
                    print("=====================================================")
                    for row in registros:
                            mensaje1 = "Folio: "+ str(folioBuscar)+ " \ncadena especial: "+ row[0] 
                            imprimirUnaLinea(mensaje1,file)
                                                        
                else:
                    print ("registros no encontrados")
            except mysql.connector.Error as err:
                print(err)
                print("Message", err.msg)        
    else:
        print("error en los folios")
    print("=====================================================")
    file.write("\n=====================================================")
        
def busquedaFolioContrato(interfazSql,folio,baseDeDatos):
    os.system ("clear")
    sql="""SELECT idcontrato_individual,folio
        FROM funeraria_contrato_individual
        WHERE folio like "%%%s%%"; """ % quote(str(folio), safe='')

    try:
        interfazSql.execute(sql)
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        if len(registros) != 0:
            for row in registros:
                print("Contrato: "+ row[1]+ " \ncadena especial: "+ row[0])
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)  

def busquedaPersonal(interfazSql,nombre, apeidoPaterno, apeidoMaterno,baseDeDatos):
    os.system ("clear") 
    nombreCompleto = nombre+" "+apeidoPaterno+" "+apeidoMaterno; 
    sql="""SELECT  concat_ws(" ",Nombre, Paterno, Materno) as nombre,idpersonal,usuario, clave
        FROM funeraria_personal
        WHERE concat_ws(" ",Nombre, Paterno, Materno) like "%%%s%%"; """ % (nombreCompleto)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        if len(registros) != 0:
            print ("\npersona buscada:", nombre, apeidoPaterno, apeidoMaterno )
            print("=====================================================\n")
            file = open('personas.txt','w')
            file.write(datos[0])
            file.write("\npersona buscada: "+ nombre +" "+ apeidoPaterno +" "+ apeidoMaterno)            
            file.write("\n")
            file.write("=====================================================\n")
            for row in registros:
                mensaje1="persona encontrada: " + row[0]+ " " +row[1]+" "+row[2]
                mensaje2="id personal: "+row[3]+"\nusuario: "+ row[4]+" password: "+row[5]
                imprimir(mensaje1,mensaje2,file)
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)
        
def busquedaCruzada(interfazSql,nombre, apeidoPaterno, apeidoMaterno,baseDeDatos):
    os.system ("clear")
    nombreCompleto = nombre+" "+apeidoPaterno+" "+apeidoMaterno; 
    sql="""SELECT fp.idpersonal, concat_ws(" ",fp.Nombre, fp.Paterno, fp.Materno) as nombreCompleto ,a.idagente_folio, a.folio, a.status_folio
    from funeraria_personal fp
    inner join funeraria_agente_folios a on a.idpersonal = fp.idpersonal
    where concat_ws(" ",fp.Nombre, fp.Paterno, fp.Materno) like "%%%s%%" and a.status_folio=0; """ % (nombreCompleto)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        if len(registros) != 0:
            print ("\npersona buscada:", nombre, apeidoPaterno, apeidoMaterno)
            file = open('Cruzada.txt','w')
            file.write(datos[0])
            file.write("\npersona buscada: "+ nombre +" "+ apeidoPaterno +" "+ apeidoMaterno)
            file.write("\n")
            file.write("=====================================================\n")
            
            print("=====================================================\n")
            for row in registros:
                mensaje1 = "codigo personal: "+row[0]+" persona encontrada: "+ str(row[1])+" "+ str(row[2])+" "+ (row[3])
                mensaje2 = "Cadena especial: "+ str(row[4]) +" Folio: "+str(row[5])
                imprimir(mensaje1,mensaje2,file)    
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)
        
     
def modAplicacion(interfazSql,baseDeDatos):
    os.system ("clear") 
    datos = menuFunesBusqueda(baseDeDatos)
    print("Se a cambiado tu aplicacion a "+datos[0])
    listasid=[78,93,121,135]
    for id in listasid:
        sql="""UPDATE `gruposefi`.`apps_imei` SET `idempresa`='%s', `imei_iddb`='%s'
         WHERE  `idseries`='%d';"""% (datos[2], datos[1],id) 
        try:
            interfazSql.execute(sql)
        except mysql.connector.Error as err:
                print(err)
                print("Message", err.msg)     
    
