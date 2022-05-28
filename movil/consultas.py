from datetime import date, datetime, timedelta
from menus import *
import os
from urllib.parse import quote
import mysql.connector
import re

listaEstatus={0:'Nuevo',1:'Firma',2:'Entregado',3:'Activo',4:'Suspendido',5:'Domicilio',6:'Cancelado',7:'Pagado',8:'Utilizado'}
listaTipoDeCobranza={ 0 : 'Domicilio', 1 : 'Oficina'}
funPruebas={13 : "DEM", 14 : "DEV", 15 : "DVL"}
listaFunerariasdb={0:'TEQ',1:'IXT',2:'SGP',3:'PAZ',4:'SIP',5:'SJG',6:'TAB',7:'SOC'}
listaFunerariasidEmpresa={0:'1',1:'PJRLAMD81S07ZH6',2:'SGP',3:'PM2S1LLK1WW8SPU',4:'PMKYNNXAK0CHX',5:'PNUSFF361BUKEB9',6:'QWVIOS88F2AZKT',7:'SOC'}


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
            print(sql)
            try:
                interfazSql.execute(sql)
                registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
                if len(registros) != 0:
                    
                    print("=====================================================")
                    for row in registros:
                            mensaje1 = f"Folio: {folioBuscar} \ncadena especial: {row[0]}"
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
    file = open('contratos.txt','w')
    sql="""SELECT idcontrato_individual,folio
        FROM funeraria_contrato_individual
        WHERE folio like "%%%s%%"; """ % quote(str(folio), safe='')
    print(sql)
    try:
        interfazSql.execute(sql)
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        if len(registros) != 0:
            for row in registros:
                mensaje1 = f"Contrato: {row[1]} \ncadena especial: {row[0]}"
                imprimirUnaLinea(mensaje1,file)
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)  

def busquedaPersonal(interfazSql,nombre,baseDeDatos):
    os.system ("clear") 
    sql="""SELECT  concat_ws(" ",FP.Nombre, FP.Paterno, FP.Materno) as nombre,FP.idpersonal,FP.usuario, FP.clave,ss.station
        FROM funeraria_personal FP
        LEFT join system_station ss on ss.idstation=FP.idsucursal
        WHERE concat_ws(" ",Nombre, Paterno, Materno) like "%%%s%%"; """ % (nombre)
    print(sql)
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
                mensaje2=f"id personal: {row[1]} Sucursal: {row[4]} \nusuario: {row[2]} password: {row[3]}"
                imprimir(mensaje1,mensaje2,file)
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
    where concat_ws(" ",fp.Nombre, fp.Paterno, fp.Materno) like "%%%s%%" and a.status_folio=0 ORDER BY a.fecha , a.folio; """ % (nombre)
    print(sql)
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
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)
        
     
def modAplicacion(interfazSql,baseDeDatos):
    os.system ("clear") 
    datos = menuFunesBusqueda(baseDeDatos)
    print("Se a cambiado tu aplicacion a "+datos[0])
    listasid=[78,93,121,135,254,298,299,306,307,308]
    for id in listasid:
        if(baseDeDatos not in [13,14,15]):
            sql="""UPDATE `gruposefi`.`apps_imei` SET `idempresa`='%s', `imei_iddb`='%s'
         WHERE  `idseries`='%d';"""% (datos[2], datos[1],id) 
        else :
            acceso=funPruebas[baseDeDatos]
            sql="""UPDATE `gruposefi`.`apps_imei` SET `imei_iddb`='%s'
         WHERE  `idseries`='%d';"""% (acceso,id)
        try:
            interfazSql.execute(sql)
        except mysql.connector.Error as err:
                print(err)
                print("Message", err.msg)     
    
def busquedaContratoApp(interfazSql,folio,baseDeDatos):
    os.system ("clear") 
    sql="""SELECT
	FCI.idcontrato_individual,FCI.Folio,FCI.Estatus,FCI.Nombre,FCI.Apellido_Paterno,FCI.Apellido_Materno,
    FCI.latitud,FCI.longitud,FCI.idcolonia,FC.Colonia, FCCC.idpersonal, FP.nombre_completo,FP.usuario,FP.clave,FCI.Fecha,FCI.Monto_Liquidado,FCI.Saldo_Deudor,FCI.Tipo_Cobranza,FCI.pago_programado
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
                
                mensaje1=f"Folio encontrado: {row[1]} \nFecha contrato: {row[14]} fecha del proximo pago: {row[18]} \nCodigo contrato: {row[0]} Estatus: {listaEstatus[row[2]]}\nTipo de cobranza: {listaTipoDeCobranza[row[17]]}  Monto liquidado: {round(row[15],2)} Saldo deudo: {round(row[16],2)} \nNombre del Cliente: {row[3]} {row[4]} {row[5]}"  
                mensaje2=f"Latitud {row[6]} Longitud {row[7]} \nId_colonia: {row[8]} Colonia: {row[9]} \nidPersonal: {row[10]} Nombre personal: {row[11]} Usuario: {row[12]} clave: {row[13]}"
                imprimir(mensaje1,mensaje2,file)
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)
        
def modificarContrato(interfazSql,folio,baseDeDatos,cnx):
    os.system ("clear") 
    sql="""SELECT idcontrato_individual , Folio, concat_ws(" ",Nombre, Apellido_Paterno, Apellido_Materno) as nombre, idsucursal
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
        listaSucursales=[]
        listaFolios=[]
        if len(registros) != 0:
            print (f"\nContrato Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: {row[0]}:{row[1]} nombre: {row[2]}")
                contador+=1
                listaContratos.append(row[0])
                listaSucursales.append(row[3])
                listaFolios.append(row[1])
                
            opcion=int(input("Que contrato deseas modificar?: "))
            idContrato=listaContratos[opcion]
            sucursal=listaSucursales[opcion]
            folio=listaFolios[opcion]
            folioNuevo=re.sub(r"[^0-9]","",folio)
            print(idContrato)
            print(sucursal)
            print(folioNuevo)
            nuevoFolio=input("Cual es el nuevo folio que vas a ponerle?: ")
            print(nuevoFolio)
            sql1=f"UPDATE funeraria_contrato_individual SET Folio='{nuevoFolio}'  where idcontrato_individual='{idContrato}';"
            sql2=f"UPDATE funeraria_agente_folios SET folio_contrato='{nuevoFolio}' where idcontrato ='{idContrato}';"
            sql3=f"DELETE FROM system_folio_count where invoice='{folioNuevo}' and (idstation IN('{sucursal}','{sucursal}-G'));"

            print(sql1)
            print(sql2)
            print(sql3)
            interfazSql.execute(sql1) ##ejecutamos el sql
            interfazSql.execute(sql2) ##ejecutamos el sql
            interfazSql.execute(sql3) ##ejecutamos el sql
            cnx.commit()
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)
        
def modificarFolio(interfazSql,folio,baseDeDatos,cnx):
    os.system ("clear") 
    sql="""SELECT faf.idagente_folio, faf.folio,faf.fecha, fp.nombre_completo,ss.idstation,ss.station
    from funeraria_agente_folios faf
left join funeraria_personal fp on faf.idpersonal = fp.idpersonal
left join system_station ss on ss.idstation = fp.idsucursal
    where Folio like "%%%s%%";; """ % (folio)
    print(sql)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaContratos=[]
        listaSucursales=[]
        if len(registros) != 0:
            print (f"\nContrato Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: {row[0]}:{row[1]} nombre: {row[2]}")
                contador+=1
                listaContratos.append(row[0])
                listaSucursales.append(row[0])
            opcion=int(input("Que folio deseas modificar?: "))
            idFolio=listaContratos[opcion]
            sucursal=listaSucursales[opcion]
            
            sucursal=row[4]
            print(sucursal)
            print(idFolio)
            nuevoFolio=input("Cual es el nuevo folio que vas a ponerle?: ")
            print(nuevoFolio) 
            
            sql1=f"UPDATE funeraria_agente_folios set folio='{nuevoFolio}' where idagente_folio='{idFolio}';"
            sql2=f"DELETE FROM system_folio_count where invoice='{opcion}' and (idstation IN('{sucursal}','{sucursal}-G'));"

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
        
def verPermisos(interfazSql,nombre,baseDeDatos):
    os.system ("clear") 
    sql=f"""SELECT su.full_name,su.username,su.password,faa.modulo,faac.campo,faacu.estatus,ss.station,faacu.idaccion_campo
FROM system_users su
LEFT JOIN funeraria_administracion_acciones_campos_usuarios faacu ON faacu.idusuario = su.iduser
LEFT JOIN funeraria_administracion_acciones_campos faac ON faac.idaccion_campo = faacu.idaccion_campo
LEFT JOIN funeraria_administracion_acciones faa ON faac.idaccion_modulo = faa.idaccion_modulo
LEFT JOIN system_station ss ON ss.idstation = faacu.idsucursal
WHERE full_name like '%{nombre}%'
ORDER BY faacu.idaccion_campo,faacu.estatus DESC;"""
    print(sql)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])

        if len(registros) != 0:
            print (f"\Persona buscada:{nombre}")
            print("=====================================================")
            file = open('Permisos.txt','w')
            file.write(f"{datos[0]}\nPersona buscada:{nombre}")            
            file.write("=====================================================")
            for row in registros:
                mensaje1=f"Persona encontrada: {row[0]} \nUsuario: {row[1]} Contraseña: {row[2]}\nId_accion_campo: {row[7]}"  
                mensaje2=f"Modulo: {row[3]} Campo: {row[4]} \nEstatus: {row[5]} Sucursal: {row[6]}"
                if row[5] == 0:
                   imprimirRojo(mensaje1,mensaje2,file)
                else :
                    imprimir(mensaje1,mensaje2,file)
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)
        
def verUsuarioSistema(interfazSql,nombre,baseDeDatos):
    os.system ("clear") 
    sql=f"""SELECT su.full_name,su.username,su.password,su.iduser
FROM system_users su
WHERE full_name like '%{nombre}%';"""
    print(sql)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])

        if len(registros) != 0:
            print (f"\Persona buscada:{nombre}")
            print("=====================================================")
            file = open('Permisos.txt','w')
            file.write(f"{datos[0]}\nPersona buscada:{nombre}")            
            file.write("=====================================================")
            for row in registros:
                mensaje1=f"Persona encontrada: {row[0]} Codigo: {row[3]} \nUsuario: {row[1]} Contraseña: {row[2]}"  
                imprimirUnaLinea(mensaje1,file)
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)
        
def buscarEnVista(interfazSql,folio,baseDeDatos):
    os.system ("clear") 
    sql=f"""select concat_ws(' ',Nombre,Paterno,Materno) as nombreCompleto, idpersonal
from funeraria_personal where concat_ws(' ',Nombre,Paterno,Materno) like '%{folio}%'"""
    print(sql)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaId=[]
        listaPersona=[]
        if len(registros) != 0:
            print (f"\Persona buscada Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: persona : {row[0]} id : {row[1]}")
                listaId.append(row[1])
                listaPersona.append(row[0])
                contador+=1
            opcion=int(input("Que persona deseas buscar?: "))
            idContrato=listaId[opcion]
            nombreMostrar=listaPersona[opcion]

            print(idContrato)

            sql1=f"""SELECT folio,idcontrato_individual,fc.Colonia,concat_ws(' ',Nombre,Apellido_Paterno,Apellido_Materno) as nombre,latitud,longitud,Ultimo_Pago,APP_Ultimo_Pago,Numero_pagos,APP_Numero_pagos,pagos
                FROM online_view_app_contratos
                left join funeraria_colonia fc on online_view_app_contratos.idcolonia = fc.idcolonia
                WHERE idpersonal='{idContrato}';"""
            print(sql1)

            interfazSql.execute(sql1) ##ejecutamos el sql
            registros2 = interfazSql.fetchall()
            if len(registros2) != 0:
                print (f"\Persona buscada Buscado:{nombreMostrar}")
                print("=====================================================")
                file = open('vistaApp.txt','w')
                file.write(f"{datos[0]}\nPersona buscada: {nombreMostrar}")            
                file.write("\n=====================================================")
                contador = 0
                contadorSinGps = 0
                for row in registros2:
                    mensaje1=f"registro : {contador+1}\nfolio {row[0]}: idcontrato : {row[1]} ruta : {row[2]}\nnombre {row[3]}: latitud : {row[4]} longitud : {row[5]}"
                    mensaje2=f"ultimo dia de pago  {row[6]}: app ultimo dia de pago : {row[7]}\nnumero de pagos  {row[8]}: app numero de pagos : {row[9]} pagos "
                    if row[4] == "0" or row[5] == "0" :
                        contadorSinGps+=1
                    imprimir(mensaje1,mensaje2,file)
                    contador+=1
                print("=====================================================")
                print(f"NUMERO DE CONTRATOS EN LA APP : {contador-1}")
                print(f"NUMERO DE CONTRATOS EN LA APP SIN PUNTOS GPS : {contadorSinGps}")
                print(f"NUMERO DE CONTRATOS EN LA APP CON PUNTOS GPS : {contador-1-contadorSinGps}")
            else:
                print("esta persona no tiene contratos en vistas")
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)
        
def busquedaContratoVista(interfazSql,folio,baseDeDatos):
    os.system ("clear") 
    sql=f"""SELECT ovac.folio,ovac.idcontrato_individual,fc.Colonia,concat_ws(' ',ovac.Nombre,ovac.Apellido_Paterno,ovac.Apellido_Materno) as nombre,
    ovac.latitud,ovac.longitud,ovac.Ultimo_Pago,ovac.APP_Ultimo_Pago,ovac.Numero_pagos,ovac.APP_Numero_pagos,
    ovac.pagos,concat_ws(' ',fp.Nombre,fp.Paterno,fp.Materno) as nombreVendedor,fp.usuario
    FROM online_view_app_contratos ovac
    left join funeraria_colonia fc on ovac.idcolonia = fc.idcolonia
    left join funeraria_personal fp on ovac.idpersonal = fp.idpersonal
    WHERE ovac.Folio like '%{folio}%'"""
    print(sql)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        contador = 0
        print(datos[0])
        if len(registros) != 0:
            print (f"\nContrato Buscado:{folio}")
            print("=====================================================")
            file = open('ContratosAppVista.txt','w')
            file.write(f"{datos[0]}\nContrato Buscado: {folio}")            
            file.write("\n=====================================================")
            for row in registros:
                mensaje1=f"registro : {contador+1}\nfolio {row[0]}: idcontrato : {row[1]} ruta : {row[2]}\nnombre del vendedor: {row[11]} usuario: {row[12]} \nnombre {row[3]}: latitud : {round(float(row[4]),5)} longitud : {round(float(row[5]),5)}"
                mensaje2=f"ultimo dia de pago  {row[6]}: app ultimo dia de pago : {row[7]}\nnumero de pagos  {row[8]}: app numero de pagos : {row[9]} pagos {row[10]}"
                imprimir(mensaje1,mensaje2,file)
                contador+=1
        else:
            print ("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)
        
def busquedaRutas(interfazSql,folio,baseDeDatos):
    os.system ("clear") 
    sql=f"""select concat_ws(' ',Nombre,Paterno,Materno) as nombreCompleto, idpersonal
from funeraria_personal where concat_ws(' ',Nombre,Paterno,Materno) like '%{folio}%' or idpersonal like '%{folio}%'"""
    print(sql)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaId=[]
        listaPersona=[]
        if len(registros) != 0:
            print (f"\Persona buscada Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: persona : {row[0]} id : {row[1]}")
                listaId.append(row[1])
                listaPersona.append(row[0])
                contador+=1
            opcion=int(input("Que persona deseas buscar?: "))
            idpersonal=listaId[opcion]
            nombreMostrar=listaPersona[opcion]
            print(idpersonal)
            sql=f"""SELECT FP.idpersonal, FP.nombre_completo,FP.usuario,FP.clave, FCCC.idcolonia,FC.Colonia,fl.Localidad,fm.Municipio,fe.Estado
        from funeraria_personal FP
        left join funeraria_comisiones_cobrador_colonia FCCC on FCCC.idpersonal = FP.idpersonal
        left join funeraria_colonia FC on  FC.idcolonia = FCCC.idcolonia
        left join funeraria_localidad fl on FC.idlocalidad = fl.idlocalidad
        left join funeraria_municipios fm on fl.idmunicipio = fm.idmunicipio
        left join funeraria_estado fe on fe.idestado = fm.idestado
        where FP.idpersonal = '{idpersonal}';
        """
            print(sql)
            try:
                interfazSql.execute(sql) ##ejecutamos el sql    
                registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
                # print(len(prueba)) imprimimos el numero de registros
                datos=menuFunesBusqueda(baseDeDatos)
                listaColonias = []
                print(datos)
                if len(registros) != 0:
                    print (f"\npersona buscada:{nombreMostrar}")
                    print("=====================================================\n")
                    file = open('LocalidadesApp.txt','w')
                    file.write(f"{datos[0]}\npersona buscada: {nombreMostrar}\n")            
                    file.write("=====================================================\n")
                    for row in registros:
                        mensaje1=f"Persona encontrada: {row[1]} \nCodigo: {row[0]} Usuario: {row[2]} Contraseña: {row[3]}"  
                        mensaje2=f"Id_colonia: {row[4]} Colonia: {row[5]} \nLocalidad: {row[6]} Municipio: {row[7]} Estado: {row[8]}"
                        listaColonias.append(row[4])
                        imprimir(mensaje1,mensaje2,file)
                    totalColonias=len(listaColonias)
                    contadorColonias=0
                    colonias=""
                    if len(listaColonias) >1 :
                        for linea in listaColonias:
                            if contadorColonias == totalColonias-1:
                                colonias+=f"'{linea}'"
                            else :
                                colonias+=f"'{linea}',"
                            contadorColonias+=1
                    else :
                        colonias=f"'{listaColonias[0]}'"
                    sql=f"select count(*) from funeraria_contrato_individual where idcolonia in({colonias});"
                    interfazSql.execute(sql) ##ejecutamos el sql    
                    registros2 = interfazSql.fetchall() ##vemos cuantos registros trae el sql
                    if len(registros2) != 0:
                        for row2 in registros2:
                            mensaje1=f"numero de contratos: {row2[0]} \ntiene : {totalColonias} de colonias"
                            imprimirUnaLinea(mensaje1,file)
                else:
                    print ("registros no encontrados")
            except mysql.connector.Error as err:
                print(err)
                print("Message", err.msg)
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)

def busquedaAbonos(interfazSql,folio,baseDeDatos):
    os.system ("clear") 
    sql=f"""SELECT fci.Folio,fci.idcontrato_individual
    from funeraria_contrato_individual fci
    where fci.Folio like '%{folio}%';"""
    print(sql)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaId=[]
        listaPersona=[]
        if len(registros) != 0:
            print (f"\Folio Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: Folio : {row[0]} id : {row[1]}")
                listaId.append(row[1])
                listaPersona.append(row[0])
                contador+=1
            opcion=int(input("Que folio deseas buscar?: "))
            idContrato=listaId[opcion]
            nombreMostrar=listaPersona[opcion]
            print(idContrato)
            sql=f"""SELECT fci.Folio,fp.nombre_completo,fai.Abono,fai.bonificacion,fai.Fecha_Android,fai.Fecha_Oficina,
            CASE
                when fai.deleted = 0 THEN 'valido'
                when fai.deleted = 1 THEN 'invalido'
            END as Estatus
            FROM funeraria_contrato_individual fci
            LEFT JOIN funeraria_personal fp on fp.idpersonal = fci.idvendedor
            LEFT JOIN funeraria_abonos_individual fai on fai.abonos_idcontrato_individual = fci.idcontrato_individual
            WHERE fci.idcontrato_individual = '{idContrato}'
            ORDER BY fai.Fecha_Android;"""
            listaVendedores=[]
            print(sql)
            try:
                interfazSql.execute(sql) ##ejecutamos el sql    
                registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
                # print(len(prueba)) imprimimos el numero de registros
                datos=menuFunesBusqueda(baseDeDatos)
                print(datos)
                if len(registros) != 0:
                    print (f"\Folio buscada:{nombreMostrar}")
                    print("=====================================================\n")
                    file = open('LocalidadesApp.txt','w')
                    file.write(f"{datos[0]}\Folio buscada: {nombreMostrar}\n")            
                    file.write("=====================================================\n")
                    for row in registros:
                        listaVendedores.append(row[1])
                        mensaje1=f"Abono: {float(row[2])} Bonificacion: {float(row[3])}"  
                        mensaje2=f" fecha cobro: {row[4]} Fecha Recepcion: {row[5]} Estatus: {row[6]}"
                        mensajeImp= mensaje1+mensaje2
                        print(mensajeImp)
                        soloArchivo(mensaje1,mensaje2,file)  
                    print("\nVendedores: \n" , listaVendedores)
                    sql2=f"""SELECT fci.idcontrato_individual,fci.Folio, sum(fai.Abono+fai.bonificacion) as total, sum(fai.Abono) as Abonos,sum(fai.bonificacion) as Bonificacion, fci.limite_asignado as Funeraria, fci.pago_inicial, count(fai.Abono) 
                    from funeraria_contrato_individual fci
                    LEFT JOIN funeraria_abonos_individual fai on fai.abonos_idcontrato_individual = fci.idcontrato_individual
                    where fci.idcontrato_individual = '{idContrato}';"""
                    print("\n\n"+sql2+"\n\n")
                    interfazSql.execute(sql2) ##ejecutamos el sql    
                    registros2 = interfazSql.fetchall() ##vemos cuantos registros trae el sql
                    if len(registros2) != 0:
                        for row in registros2:
                            mensaje1=f"idContrato: {row[0]} \nFolio: {row[1]} Total: {float(row[2])} Abonos: {float(row[3])} Bonificacion: {float(row[4])}"
                            mensaje2=f"Funeraria: {float(row[5])} Pago Inicial: {float(row[6])} Total de abonos : {row[7]}"
                            imprimir(mensaje1,mensaje2,file)
                else:
                    print ("registros no encontrados")
            except mysql.connector.Error as err:
                print(err)
                print("Message", err.msg)
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)

def busquedaAbonosCobrador(interfazSql,folio,baseDeDatos):
    os.system ("clear") 
    sql=f"""select concat_ws(' ',Nombre,Paterno,Materno) as nombreCompleto, idpersonal
from funeraria_personal where concat_ws(' ',Nombre,Paterno,Materno) like '%{folio}%' or idpersonal like '%{folio}%'"""
    print(sql)
    try:
        interfazSql.execute(sql) ##ejecutamos el sql    
        registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos=menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaId=[]
        listaPersona=[]
        if len(registros) != 0:
            print (f"\Persona buscada Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: persona : {row[0]} id : {row[1]}")
                listaId.append(row[1])
                listaPersona.append(row[0])
                contador+=1
            opcion=int(input("Que persona deseas buscar?: "))
            idpersonal=listaId[opcion]
            nombreMostrar=listaPersona[opcion]
            fecha =input("Ingresa la fecha que deseas buscar: ")
            if fecha=="1":
                fechaFormateada=date.today()
            else :
                fechaFormateada=datetime.strptime(fecha, '%Y-%m-%d')
            diasAtras= int( input("cuantos dias antes: "))
            FechaAnterior = fechaFormateada - timedelta(days=diasAtras)
            print(idpersonal)
            sql=f"""SELECT fp.idpersonal,fp.nombre_completo,oaai.idabono_individual,oaai.Folio,oaai.Abono,oaai.Fecha_pago,oaai.cobrado_oficina
            from funeraria_personal fp
            left join online_android_abonos_individual oaai on oaai.idcobrador = fp.idpersonal
            where idpersonal = "{idpersonal}" and oaai.Fecha_pago between '{FechaAnterior.strftime("%Y-%m-%d")} '  and '{fechaFormateada.strftime("%Y-%m-%d")} '
            order by Fecha_pago desc;"""
            print(sql)
            try:
                interfazSql.execute(sql) ##ejecutamos el sql    
                registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
                # print(len(prueba)) imprimimos el numero de registros
                datos=menuFunesBusqueda(baseDeDatos)
                listaColonias = []
                print(datos)
                if len(registros) != 0:
                    print (f"\npersona buscada:{nombreMostrar}")
                    print("=====================================================\n")
                    file = open('AbonosDados.txt','w')
                    file.write(f"{datos[0]}\npersona buscada: {nombreMostrar}\n")            
                    file.write("=====================================================\n")
                    contador=0
                    total = 0
                    for row in registros:
                        if row[6] == 0:
                            status="no cobrado"
                        else :
                            status = "Cobrado" 
                        mensaje1=f"IdAbono: {row[2][-10:]} Folio: {row[3]} Abono: {row[4]:,.2f} Fecha: {row[5]} CobradorOficina: {status}"  
                        imprimirUnaLinea(mensaje1,file)
                        contador+=1
                        total+=row[4]
                    print(f"\nhubo {contador} abonos en android online con un total de {total:,.2f} ") 
                else:
                    print ("registros no encontrados")
            except mysql.connector.Error as err:
                print(err)
                print("Message", err.msg)
            sql=f"""SELECT fp.idpersonal,fp.nombre_completo,fci.idabono,fci.abonos_idcontrato_individual,fci.Fecha_Android,fci.Abono,fci.bonificacion,fci.idcorte_cobros
            from funeraria_personal fp
            left join funeraria_abonos_individual fci on fci.idcobrador = fp.idpersonal
            where idpersonal = "{idpersonal}" and fci.Fecha_Android between '{FechaAnterior.strftime("%Y-%m-%d")}'  and '{fechaFormateada.strftime("%Y-%m-%d")}'
            order by Fecha_Android desc;"""
            print(sql)
            try:
                interfazSql.execute(sql) ##ejecutamos el sql    
                registros = interfazSql.fetchall() ##vemos cuantos registros trae el sql
                # print(len(prueba)) imprimimos el numero de registros
                datos=menuFunesBusqueda(baseDeDatos)
                listaColonias = []
                print(datos)
                if len(registros) != 0:
                    print (f"\npersona buscada:{nombreMostrar}")
                    print("=====================================================\n")
                    file = open('AbonosDados.txt','a')
                    file.write(f"{datos[0]}\npersona buscada: {nombreMostrar}\n")            
                    file.write("=====================================================\n")
                    contador=0
                    totalAbonos = 0
                    totalBonificacion = 0
                    for row in registros:
                        mensaje1=f"IdAbono: {row[2][-10:]} Folio: {row[3][-5:]} Fecha: {row[4]} Abono: {row[5]:,.2f} Bonificacion: {row[6]:,.2f} idcorte : {row[7]}"  
                        imprimirUnaLinea(mensaje1,file)
                        contador+=1
                        totalAbonos+=row[5]
                        totalBonificacion+=row[6]
                    print(f"\nhubo {contador} abonos en recibidos con un total de {totalAbonos:,.2f} y una bonificacion total de total de {totalBonificacion:,.2f} ") 
                else:
                    print ("registros no encontrados")
            except mysql.connector.Error as err:
                print(err)
                print("Message", err.msg)
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)
        
def agregarPersona(interfazSql,cnx):
    os.system ("clear") 
    listaFunerariasdb={0:'TEQ',1:'IXT',2:'SGP',3:'PAZ',4:'SIP',5:'SJG',6:'TAB',7:'SOC'}
    print("0.- Tequila")
    print("1.- Ixtlan")
    print("2.- San gaspar")
    print("3.- La paz")
    print("4.- Sipref")
    print("5.- San jorge")
    print("6.- Tabasco")
    print("7.- Socorro")
    opcion=int(input("cual es la funeraria a la que deseas dar de alta?: "))
    nombrePersona=input("a quien daras de alta?: ")
    imei=input("cual es su imei?: ")
    app=input("en que app necesitas? 0 0 cobranza 1 = ventas 2 = logistica: ")
    db=listaFunerariasdb[opcion]
    empresa=listaFunerariasidEmpresa[opcion]
    fechaFormateada=date.today()
    sql=f"""INSERT INTO `gruposefi`.`apps_imei` (`idempresa`, `Serie`, `Descripcion`, `Fecha_Inicio`, `Fecha_Vigencia`, `imei_iddb`, `id_app`) 
    VALUES ('{empresa}', '{imei}', '{nombrePersona}', '{fechaFormateada}', '2030-12-31', '{db}', '{app}');"""
    try:
        interfazSql.execute(sql)
        cnx.commit()
        print("dado de alta")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)
        