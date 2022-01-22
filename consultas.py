from menus import *
import os
from urllib.parse import quote
import mysql.connector
import pyperclip as pc

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
                            mensaje1 = f"Folio: {folioBuscar} \ncadena especial: {row[0]}"
                            imprimirUnaLinea(mensaje1,file)
                            pc.copy(row[0])
                                                        
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
    file = open('contratos.txt','w')
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
                mensaje1 = f"Contrato: {row[1]} \ncadena especial: {row[0]}"
                imprimirUnaLinea(mensaje1,file)
                pc.copy(row[0])
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)  

def busquedaPersonal(interfazSql,nombre,baseDeDatos):
    os.system ("clear") 
    sql="""SELECT  concat_ws(" ",Nombre, Paterno, Materno) as nombre,idpersonal,usuario, clave
        FROM funeraria_personal
        WHERE concat_ws(" ",Nombre, Paterno, Materno) like "%%%s%%"; """ % (nombre)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        if len(registros) != 0:
            print (f"\npersona buscada:{nombre}")
            print("=====================================================\n")
            file = open('personas.txt','w')
            file.write(f"{datos[0]}\npersona buscada: {nombre}\n")            
            file.write("=====================================================\n")
            for row in registros:
                mensaje1=f"persona encontrada: {row[0]}"  
                mensaje2=f"id personal: {row[1]} \nusuario: {row[2]} password: {row[3]}"
                imprimir(mensaje1,mensaje2,file)
                pc.copy(row[1])
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)
        
def busquedaCruzada(interfazSql,nombre,baseDeDatos):
    os.system ("clear")
    sql="""SELECT fp.idpersonal, concat_ws(" ",fp.Nombre, fp.Paterno, fp.Materno) as nombreCompleto ,a.idagente_folio, a.folio, a.status_folio
    from funeraria_personal fp
    inner join funeraria_agente_folios a on a.idpersonal = fp.idpersonal
    where concat_ws(" ",fp.Nombre, fp.Paterno, fp.Materno) like "%%%s%%" and a.status_folio=0; """ % (nombre)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        if len(registros) != 0:
            print (f"\npersona buscada: {nombre}")
            file = open('Cruzada.txt','w')
            file.write(f"{datos[0]} \npersona buscada: {nombre}\n")
            file.write("=====================================================\n")
            print("=====================================================\n")
            for row in registros:
                mensaje1=f"codigo personal: {row[0]} persona encontrada: {row[1]}"
                mensaje2=f"Cadena especial: {row[2]} Folio: {row[3]} estatus {row[4]}"
                imprimir(mensaje1,mensaje2,file)
                pc.copy(row[2])    
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
    
def busquedaRutas(interfazSql,nombre,baseDeDatos):
    os.system ("clear") 
    sql="""select FP.idpersonal, FP.nombre_completo,FP.usuario,FP.clave, FCCC.idcolonia,FC.Colonia,fl.Localidad,fm.Municipio,fe.Estado
from funeraria_personal FP
left join funeraria_comisiones_cobrador_colonia FCCC on FCCC.idpersonal = FP.idpersonal
left join funeraria_colonia FC on  FC.idcolonia = FCCC.idcolonia
inner join funeraria_localidad fl on FC.idlocalidad = fl.idlocalidad
inner join funeraria_municipios fm on fl.idmunicipio = fm.idmunicipio
inner join funeraria_estado fe on fe.idestado = fm.idestado
where FP.nombre_completo like "%%%s%%" OR FP.usuario like "%%%s%%";
 """ % (nombre,nombre)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        if len(registros) != 0:
            print (f"\npersona buscada:{nombre}")
            print("=====================================================\n")
            file = open('LocalidadesApp.txt','w')
            file.write(f"{datos[0]}\npersona buscada: {nombre}\n")            
            file.write("=====================================================\n")
            for row in registros:
                mensaje1=f"Persona encontrada: {row[1]} \nCodigo: {row[0]} Usuario: {row[2]} Contraseña: {row[3]}"  
                mensaje2=f"Id_colonia: {row[4]} Colonia: {row[5]} \nLocalidad: {row[6]} Municipio: {row[7]} Estado: {row[8]}"
                imprimir(mensaje1,mensaje2,file)
                pc.copy(row[0])
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)

def busquedaContratoApp(interfazSql,folio,baseDeDatos):
    os.system ("clear") 
    sql="""SELECT
	FCI.idcontrato_individual,FCI.Folio,FCI.Estatus,FCI.Nombre,FCI.Apellido_Paterno,FCI.Apellido_Materno,
    FCI.latitud,FCI.longitud,FCI.idcolonia,FC.Colonia, FCCC.idpersonal, FP.nombre_completo,FP.usuario,FP.clave
from funeraria_contrato_individual FCI
	left join funeraria_colonia FC
		on  FCI.idcolonia = FC.idcolonia
	LEFT join funeraria_comisiones_cobrador_colonia FCCC
		on FC.idcolonia = FCCC.idcolonia
	left join funeraria_personal FP
		on FCCC.idpersonal = FP.idpersonal
	where FCI.FOLIO LIKE "%%%s%%";
 """ % (folio)
    print(sql)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        if len(registros) != 0:
            print (f"\nContrato Buscado:{folio}")
            print("=====================================================")
            file = open('ContratosApp.txt','w')
            file.write(f"{datos[0]}\nContrato Buscado: {folio}")            
            file.write("=====================================================")
            for row in registros:
                mensaje1=f"Folio encontrado: {row[1]} \nCodigo contrato: {row[0]} Estatus: {row[2]} \nNombre del Cliente: {row[3]} {row[4]} {row[5]}"  
                mensaje2=f"Latitud {row[6]} Longitud {row[7]} \n\nId_colonia: {row[8]} Colonia: {row[9]} \nidPersonal: {row[10]} Nombre personal: {row[11]} Usuario: {row[12]} clave: {row[13]}"
                imprimir(mensaje1,mensaje2,file)
                pc.copy(row[0])
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)
        
def modificarContrato(interfazSql,folio,baseDeDatos,cnx):
    os.system ("clear") 
    sql="""SELECT idcontrato_individual , Folio, concat_ws(" ",Nombre, Apellido_Paterno, Apellido_Materno) as nombre
    from funeraria_contrato_individual
    where Folio like "%%%s%%"; """ % (folio)
    print(sql)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaContratos=[]
        if len(registros) != 0:
            print (f"\nContrato Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: {row[0]}:{row[1]} nombre: {row[2]}")
                contador+=1
                listaContratos.append(row[0])
            idContrato=listaContratos[int(input("Que contrato deseas modificar?: "))]
            print(idContrato)
            nuevoFolio=input("Cual es el nuevo folio que vas a ponerle?: ")
            print(nuevoFolio) 
            sql1=f"UPDATE funeraria_contrato_individual SET Folio='{nuevoFolio}'  where idcontrato_individual='{idContrato}';"
            sql2=f"UPDATE funeraria_agente_folios SET folio_contrato='{nuevoFolio}' where idcontrato ='{idContrato}';"
            print(sql1)
            print(sql2)
            interfazSql.execute(sql1) ##ejecutamos el sql
            interfazSql.execute(sql2) ##ejecutamos el sql
            cnx.commit()
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)