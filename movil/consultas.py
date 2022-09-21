from datetime import date, datetime, timedelta
from menus import *
import os
from urllib.parse import quote
import mysql.connector
import re
import string
import random



listaEstatus = {0: 'Nuevo', 1: 'Firma', 2: 'Entregado', 3: 'Activo',
                4: 'Suspendido', 5: 'Domicilio', 6: 'Cancelado', 7: 'Pagado', 8: 'Utilizado'}
listaTipoDeCobranza = {0: 'Domicilio', 1: 'Oficina'}
funPruebas = {13: "DEM", 14: "DEV", 15: "DVL"}
listaFunerariasdb = {0: 'TEQ', 1: 'IXT', 2: 'SGP',
                     3: 'PAZ', 4: 'SIP', 5: 'SJG', 6: 'TAB', 7: 'SOC'}
listaFunerariasidEmpresa = {0: '1', 1: 'PJRLAMD81S07ZH6', 2: 'SGP', 3: 'PM2S1LLK1WW8SPU',
                            4: 'PMKYNNXAK0CHX', 5: 'PNUSFF361BUKEB9', 6: 'QWVIOS88F2AZKT', 7: 'SOC'}


def busquedaFolio(interfazSql, folios, baseDeDatos):
    rango = False
    for letra in folios:
        if letra in "-":
            rango = True
    if(rango):
        minyMax = folios.split("-")
        rango = range(int(minyMax[0]), int(minyMax[1]),)
    else:
        rango = folios.split(".")
    os.system("clear")
    datos = menuFunesBusqueda(baseDeDatos)
    print(datos[0])
    if len(rango) != 0:
        file = open('folios.txt', 'w')
        file.write(datos[0])
        print("\nfolios buscados: ")
        print(rango)
        encabezado = ['idFolio','folio', 'Estatus', 'Nombre Completo',
                                  'Sucursal']
        guardarCsvEncabezado("folios", encabezado)
        for folioBuscar in rango:
            file.write("\n")
            file.write(
                "=====================================================\n")
            sql = f"""SELECT faf.idagente_folio,faf.folio,
     case faf.status_folio
         WHEN '0' THEN "Nuevo"
					WHEN  1 THEN "Firma"
					WHEN  2 THEN "Entregado"
					WHEN  3 THEN "Activo"
					WHEN  4 THEN "Suspendido"
					WHEN  5 THEN "Domicilio"
					WHEN  6 THEN "Cancelado"
					WHEN  7 THEN "Pagado"
					WHEN  8 THEN "Utilizado"
					END AS Estatus , fp.nombre_completo,ss.station
        FROM funeraria_agente_folios faf
        left join funeraria_personal fp on faf.idpersonal = fp.idpersonal
        left join system_station ss on fp.idsucursal = ss.idstation
        WHERE folio = {folioBuscar};"""
            try:
                interfazSql.execute(sql)
                registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
                if len(registros) != 0:
                    guardarCsvAppendContenido("folios",registros)
                    print("=====================================================")
                    for row in registros:
                        mensaje1 = f"Folio: {folioBuscar} \ncadena especial: {row[0]}, folio:{row[1]} estatus: {row[2]}  nombre:{row[3]}  sucursal:{row[4]}"
                        imprimirUnaLinea(mensaje1, file)
                else:
                    print("registros no encontrados")
            except mysql.connector.Error as err:
                print(err)
                print("Message", err.msg)
    else:
        print("error en los folios")
    print("=====================================================")
    file.write("\n=====================================================")


def busquedaFolioContrato(interfazSql, folio, baseDeDatos):
    os.system("clear")
    file = open('contratos.txt', 'w')
    sql = """SELECT idcontrato_individual,folio
        FROM funeraria_contrato_individual
        WHERE folio like "%%%s%%"; """ % quote(str(folio), safe='')
    print(sql)
    try:
        interfazSql.execute(sql)
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        if len(registros) != 0:
            for row in registros:
                mensaje1 = f"Contrato: {row[1]} \ncadena especial: {row[0]}"
                imprimirUnaLinea(mensaje1, file)
        else:
            print("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def busquedaPersonal(interfazSql, nombre, baseDeDatos):
    os.system("clear")
    sql = f"""SELECT concat_ws(" ",FP.Nombre, FP.Paterno, FP.Materno) as nombre,FP.idpersonal,FP.usuario, FP.clave,ss.station
        FROM funeraria_personal FP
        LEFT join system_station ss on ss.idstation=FP.idsucursal
        WHERE concat_ws(" ",Nombre, Paterno, Materno) like "%%{nombre}%%";"""
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        if len(registros) != 0:
            print(f"\npersona buscada:{nombre}")
            print("=====================================================\n")
            file = open('personas.txt', 'w')
            file.write(f"{datos[0]}\npersona buscada: {nombre}\n")
            file.write(
                "=====================================================\n")
            for row in registros:
                mensaje1 = f"persona encontrada: {row[0]}"
                mensaje2 = f"id personal: {row[1]} Sucursal: {row[4]} \nusuario: {row[2]} password: {row[3]}"
                imprimir(mensaje1, mensaje2, file)
        else:
            print("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def busquedaCruzada(interfazSql, nombre, baseDeDatos):
    os.system("clear")
    sql = f"""SELECT fp.idpersonal, concat_ws(" ",fp.Nombre, fp.Paterno, fp.Materno) as nombreCompleto ,a.idagente_folio, a.folio, 
    case a.status_folio
         WHEN '0' THEN "Nuevo"
					WHEN  1 THEN "Recepcionado"
					WHEN  2 THEN "Contrato Hecho"
					WHEN  3 THEN "Activo"
					WHEN  4 THEN "Cancelado"
					WHEN  5 THEN "Domicilio"
					WHEN  6 THEN "Cancelado"
					WHEN  7 THEN "Pagado"
					WHEN  8 THEN "Utilizado"
					END AS Estatus,
       ss.station as SucursalPersonal,ss2.station as SucursalFolio,fp.usuario,fp.clave
    from funeraria_personal fp
    left join funeraria_agente_folios a on a.idpersonal = fp.idpersonal
    left join system_station ss on fp.idsucursal = ss.idstation
    left join system_station ss2 on ss2.idstation = a.sucursal_origen
    where concat_ws(" ",fp.Nombre, fp.Paterno, fp.Materno) like "%%{nombre}%%" or fp.usuario like '%{nombre}%'  and a.status_folio=0 ORDER BY a.fecha , a.folio; """
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        if len(registros) != 0:
            print(f"\npersona buscada: {nombre}\nUsuario: {registros[0][7]} Clave: {registros[0][8]} \nSucursal de la persona {registros[0][5]}")
            file = open('Cruzada.txt', 'w')
            file.write(f"\npersona buscada: {nombre}\n Usuario:{registros[0][7]} Clave:{registros[0][8]} \nSucursal de la persona {registros[0][5]}")
            file.write(
                "=====================================================\n")
            print("=====================================================\n")
            encabezado = ['idpersonal', 'nombre_completo', 'Cadena especial',
                                  'Folio', 'Estatus','SucursalDelVendedor','SucursalDelFolio','Usario','Clave']
            guardarCsv("Cruzada", encabezado, registros)
            for row in registros:
                mensaje1 = f"Codigo personal: {row[0]} persona encontrada: {row[1]}"
                mensaje2 = f"Cadena especial: {row[2]} Folio: {row[3]} Estatus: {row[4]} Sucursal: {row[6]}"
                imprimir(mensaje1, mensaje2, file)
        else:
            print("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def modAplicacion(interfazSql, baseDeDatos):
    os.system("clear")
    datos = menuFunesBusqueda(baseDeDatos)
    print("Se a cambiado tu aplicacion a "+datos[0])
    listasid = [78, 93, 121, 135, 254, 298, 299, 306, 307, 308]
    for id in listasid:
        if(baseDeDatos not in [13, 14, 15]):
            sql = """UPDATE `gruposefi`.`apps_imei` SET `idempresa`='%s', `imei_iddb`='%s'
         WHERE  `idseries`='%d';""" % (datos[2], datos[1], id)
        else:
            acceso = funPruebas[baseDeDatos]
            sql = """UPDATE `gruposefi`.`apps_imei` SET `imei_iddb`='%s'
         WHERE  `idseries`='%d';""" % (acceso, id)
        try:
            interfazSql.execute(sql)
        except mysql.connector.Error as err:
            print(err)
            print("Message", err.msg)
    sql = f"SELECT password_company FROM apps_db WHERE basedatos_db='{datos[3]} '";
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        if len(registros) != 0:
            for row in registros:
                print("Contraseña de la app :", row[0])
        else:
            print("No registros")
    except mysql.connector.Error as err:
            print(err)
            print("Message", err.msg)
    


def busquedaContratoApp(interfazSql, folio, baseDeDatos):
    os.system("clear")
    sql = f"""SELECT FCI.idcontrato_individual,FCI.Folio,
       case FCI.Estatus
         WHEN '0' THEN "Nuevo"
                                        WHEN  1 THEN "Firma"
                                        WHEN  2 THEN "Entregado"
                                        WHEN  3 THEN "Activo"
                                        WHEN  4 THEN "Suspendido"
                                        WHEN  5 THEN "Esperando devolucion"
                                        WHEN  6 THEN "Cancelado"
                                        WHEN  7 THEN "Pagado"
                                        WHEN  8 THEN "Utilizado"
                                        END AS Estatus,
       FCI.Nombre, FCI.Apellido_Paterno, FCI.Apellido_Materno, FCI.latitud,FCI.longitud, FCI.idcolonia,FC.Colonia, FCCC.idpersonal,FP.nombre_completo, FP.usuario, FP.clave, FCI.Fecha, FCI.Monto_Liquidado, FCI.Saldo_Deudor,
       case FCI.Tipo_Cobranza
         WHEN '0' THEN "Domicilio"
                                        WHEN  1 THEN "Oficina"
                                        END AS tipo_cobranza,
       FCI.pago_programado,
		 case FCI.Plan_de_Pago
                                        WHEN  0 THEN "Semanal"
                                        WHEN  1 THEN "Quincenal"
                                        WHEN  2 THEN "Mensual"
                                        WHEN  3 THEN "CADA 2 MESES"
                                        WHEN  4 THEN "CADA 3 MESES"
                                        WHEN  5 THEN "CADA 4 MESES"
                                        WHEN  6 THEN "CADA 5 MESES"
                                        WHEN  7 THEN "CADA 6 MESES"
                                        WHEN  8 THEN "CADA 7 MESES"
                                        WHEN  9 THEN "CADA 8 MESES"
                                        WHEN  10 THEN "CADA 9 MESES"
                                        WHEN  11 THEN "CADA 10 MESES"
                                        WHEN  12 THEN "CADA 11 MESES"
                                        WHEN  13 THEN "anual"
                                        END AS Plan_de_pago, FCI.dia_cobro
from funeraria_contrato_individual FCI
         left join funeraria_colonia FC
                   on FCI.idcolonia = FC.idcolonia
         LEFT join funeraria_comisiones_cobrador_colonia FCCC
                   on FC.idcolonia = FCCC.idcolonia
         left join funeraria_personal FP
                   on FCCC.idpersonal = FP.idpersonal
where FCI.FOLIO LIKE "%{folio}%";"""
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        if len(registros) != 0:
            print(f"\nContrato Buscado:{folio}")
            print("=====================================================")
            file = open('ContratosApp.txt', 'w')
            file.write(f"{datos[0]}\nContrato Buscado: {folio}")
            file.write("=====================================================")
            encabezado = ['idcontrato_individual','Folio','etatus',
       'Nombre','Apellido_Paterno', 'Apellido_Materno', 'latitud','longitud','idcolonia','Colonia','idpersonal','nombre_completo','usuario','clave', 'Fecha','Monto_Liquidado','Saldo_Deudor',
       'Tipo_Cobranza', 'pago_programado', 'dia de cobranza', 'dias de cobro']
            guardarCsv("ContratosApp", encabezado, registros)
            for row in registros:

                mensaje1 = f"Folio encontrado: {row[1]}\nPeriodicidad de cobranza: {row[19]} Dias de cobranza: {row[20]} \nFecha contrato: {row[14]} fecha del proximo pago: {row[18]} \nCodigo contrato: {row[0]} Estatus: {row[2]}\nTipo de cobranza: {row[17]}  Monto liquidado: {round(row[15],2)} Saldo deudo: {round(row[16],2)} \nNombre del Cliente: {row[3]} {row[4]} {row[5]}"
                mensaje2 = f"Latitud {row[6]} Longitud {row[7]} \nId_colonia: {row[8]} Colonia: {row[9]} \nidPersonal: {row[10]} Nombre personal: {row[11]} \nUsuario: {row[12]} clave: {row[13]}"
                imprimir(mensaje1, mensaje2, file)
        else:
            print("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def modificarContrato(interfazSql, folio, baseDeDatos, cnx):
    os.system("clear")
    sql = """SELECT idcontrato_individual , Folio, concat_ws(" ",Nombre, Apellido_Paterno, Apellido_Materno) as nombre, idsucursal
    from funeraria_contrato_individual
    where Folio like "%%%s%%"; """ % (folio)
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaContratos = []
        listaSucursales = []
        listaFolios = []
        if len(registros) != 0:
            print(f"\nContrato Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: {row[0]}:{row[1]} nombre: {row[2]}")
                contador += 1
                listaContratos.append(row[0])
                listaSucursales.append(row[3])
                listaFolios.append(row[1])

            opcion = int(input("Que contrato deseas modificar?: "))
            idContrato = listaContratos[opcion]
            sucursal = listaSucursales[opcion]
            folio = listaFolios[opcion]
            folioNuevo = re.sub(r"[^0-9]", "", folio)
            print(idContrato)
            print(sucursal)
            print(folioNuevo)
            nuevoFolio = input("Cual es el nuevo folio que vas a ponerle?: ")
            print(nuevoFolio)
            sql1 = f"UPDATE funeraria_contrato_individual SET Folio='{nuevoFolio}'  where idcontrato_individual='{idContrato}';"
            sql2 = f"UPDATE funeraria_agente_folios SET folio_contrato='{nuevoFolio}' where idcontrato ='{idContrato}';"
            sql3 = f"DELETE FROM system_folio_count where invoice='{folioNuevo}' and (idstation IN('{sucursal}','{sucursal}-G'));"

            print(sql1)
            print(sql2)
            print(sql3)
            interfazSql.execute(sql1)  # ejecutamos el sql
            interfazSql.execute(sql2)  # ejecutamos el sql
            interfazSql.execute(sql3)  # ejecutamos el sql
            cnx.commit()
        else:
            print("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def modificarFolio(interfazSql, folio, baseDeDatos, cnx):
    os.system("clear")
    sql = """SELECT faf.idagente_folio, faf.folio,faf.fecha, fp.nombre_completo,ss.idstation,ss.station
    from funeraria_agente_folios faf
left join funeraria_personal fp on faf.idpersonal = fp.idpersonal
left join system_station ss on ss.idstation = fp.idsucursal
    where Folio like "%%%s%%";; """ % (folio)
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaContratos = []
        listaSucursales = []
        if len(registros) != 0:
            print(f"\nContrato Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: {row[0]}:{row[1]} nombre: {row[2]}")
                contador += 1
                listaContratos.append(row[0])
                listaSucursales.append(row[0])
            opcion = int(input("Que folio deseas modificar?: "))
            idFolio = listaContratos[opcion]
            sucursal = listaSucursales[opcion]

            sucursal = row[4]
            print(sucursal)
            print(idFolio)
            nuevoFolio = input("Cual es el nuevo folio que vas a ponerle?: ")
            print(nuevoFolio)

            sql1 = f"UPDATE funeraria_agente_folios set folio='{nuevoFolio}' where idagente_folio='{idFolio}';"
            sql2 = f"DELETE FROM system_folio_count where invoice='{opcion}' and (idstation IN('{sucursal}','{sucursal}-G'));"

            print(sql1)
            print(sql2)
            interfazSql.execute(sql1)  # ejecutamos el sql
            interfazSql.execute(sql2)  # ejecutamos el sql
            cnx.commit()
        else:
            print("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def verPermisos(interfazSql, nombre, baseDeDatos):
    os.system("clear")
    sql = f"""SELECT su.full_name,su.username,su.password,faa.modulo,faac.campo,faacu.estatus,ss.station,faacu.idaccion_campo
FROM system_users su
LEFT JOIN funeraria_administracion_acciones_campos_usuarios faacu ON faacu.idusuario = su.iduser
LEFT JOIN funeraria_administracion_acciones_campos faac ON faac.idaccion_campo = faacu.idaccion_campo
LEFT JOIN funeraria_administracion_acciones faa ON faac.idaccion_modulo = faa.idaccion_modulo
LEFT JOIN system_station ss ON ss.idstation = faacu.idsucursal
WHERE full_name like '%{nombre}%'
ORDER BY ss.station,faacu.idaccion_campo,faacu.estatus DESC;"""
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])

        if len(registros) != 0:
            print(f"\Persona buscada:{nombre}")
            print("=====================================================")
            file = open('Permisos.txt', 'w')
            file.write(f"{datos[0]}\nPersona buscada:{nombre}")
            file.write("=====================================================")
            encabezado = ['full_name','username','password','modulo','campo','estatus','station','idaccion_campo']
            guardarCsv("Permisos", encabezado, registros)
            for row in registros:
                mensaje1 = f"Persona encontrada: {row[0]} \nUsuario: {row[1]} Contraseña: {row[2]}\nId_accion_campo: {row[7]}"
                mensaje2 = f"Modulo: {row[3]} Campo: {row[4]} \nEstatus: {row[5]} Sucursal: {row[6]}"
                if row[5] == 0:
                    imprimirRojo(mensaje1, mensaje2, file)
                else:
                    imprimir(mensaje1, mensaje2, file)
        else:
            print("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def verUsuarioSistema(interfazSql, nombre, baseDeDatos):
    os.system("clear")
    sql = f"""SELECT su.full_name,su.username,su.password,su.iduser
FROM system_users su
WHERE full_name like '%{nombre}%';"""
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])

        if len(registros) != 0:
            print(f"\Persona buscada:{nombre}")
            print("=====================================================")
            file = open('Permisos.txt', 'w')
            file.write(f"{datos[0]}\nPersona buscada:{nombre}")
            file.write("=====================================================")
            for row in registros:
                mensaje1 = f"Persona encontrada: {row[0]} Codigo: {row[3]} \nUsuario: {row[1]} Contraseña: {row[2]}"
                imprimirUnaLinea(mensaje1, file)
        else:
            print("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def buscarEnVista(interfazSql, folio, baseDeDatos):
    os.system("clear")
    sql = f"""select concat_ws(' ',Nombre,Paterno,Materno) as nombreCompleto, idpersonal
from funeraria_personal where concat_ws(' ',Nombre,Paterno,Materno) like '%{folio}%'"""
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaId = []
        listaPersona = []
        if len(registros) != 0:
            print(f"\Persona buscada Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: persona : {row[0]} id : {row[1]}")
                listaId.append(row[1])
                listaPersona.append(row[0])
                contador += 1
            opcion = int(input("Que persona deseas buscar?: "))
            idContrato = listaId[opcion]
            nombreMostrar = listaPersona[opcion]

            print(idContrato)

            sql1 = f"""SELECT folio,idcontrato_individual,fc.Colonia,concat_ws(' ',Nombre,Apellido_Paterno,Apellido_Materno) as nombre,latitud,longitud,Ultimo_Pago,APP_Ultimo_Pago,Numero_pagos,APP_Numero_pagos,pagos
                FROM online_view_app_contratos
                left join funeraria_colonia fc on online_view_app_contratos.idcolonia = fc.idcolonia
                WHERE idpersonal='{idContrato}';"""
            print(sql1)

            interfazSql.execute(sql1)  # ejecutamos el sql
            registros2 = interfazSql.fetchall()
            if len(registros2) != 0:

                print(f"\Persona buscada Buscado:{nombreMostrar}")
                print("=====================================================")
                file = open('vistaApp.txt', 'w')
                file.write(f"{datos[0]}\nPersona buscada: {nombreMostrar}")
                file.write(
                    "\n=====================================================")
                encabezado = ['folio','idcontrato_individual','Colonia', 'nombre','latitud','longitud','Ultimo_Pago','APP_Ultimo_Pago','Numero_pagos','APP_Numero_pagos','pagos']
                guardarCsv("vistaApp", encabezado, registros2)
                contador = 0
                contadorSinGps = 0
                print(registros2)
                for row in registros2:
                    mensaje1 = f"registro : {contador+1}\nfolio {row[0]}: idcontrato : {row[1]} ruta : {row[2]}\nnombre {row[3]}: latitud : {row[4]} longitud : {row[5]}"
                    mensaje2 = f"ultimo dia de pago  {row[6]}: app ultimo dia de pago : {row[7]}\nnumero de pagos  {row[8]}: app numero de pagos : {row[9]} pagos "
                    if row[4] == "0" or row[5] == "0":
                        contadorSinGps += 1
                    imprimir(mensaje1, mensaje2, file)
                    contador += 1
                print("=====================================================")
                print(f"NUMERO DE CONTRATOS EN LA APP : {contador-1}")
                print(f"NUMERO DE CONTRATOS EN LA APP SIN PUNTOS GPS : {contadorSinGps}")
                print(f"NUMERO DE CONTRATOS EN LA APP CON PUNTOS GPS : {contador-1-contadorSinGps}")
                contenidoExtra=[(f"NUMERO DE CONTRATOS EN LA APP : {contador-1}",""),(f"NUMERO DE CONTRATOS EN LA APP SIN PUNTOS GPS : {contadorSinGps}",""),(f"NUMERO DE CONTRATOS EN LA APP CON PUNTOS GPS : {contador-1-contadorSinGps}","")]
                guardarCsvAppendColumna("vistaApp",contenidoExtra)
            else:
                print("esta persona no tiene contratos en vistas")
        else:
            print("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def busquedaContratoVista(interfazSql, folio, baseDeDatos):
    os.system("clear")
    sql = f"""SELECT ovac.folio,ovac.idcontrato_individual,fc.Colonia,concat_ws(' ',ovac.Nombre,ovac.Apellido_Paterno,ovac.Apellido_Materno) as nombre,
    ovac.latitud,ovac.longitud,ovac.Ultimo_Pago,ovac.APP_Ultimo_Pago,ovac.Numero_pagos,ovac.APP_Numero_pagos,
    ovac.pagos,concat_ws(' ',fp.Nombre,fp.Paterno,fp.Materno) as nombreVendedor,fp.usuario
    FROM online_view_app_contratos ovac
    left join funeraria_colonia fc on ovac.idcolonia = fc.idcolonia
    left join funeraria_personal fp on ovac.idpersonal = fp.idpersonal
    WHERE ovac.Folio like '%{folio}%'"""
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        contador = 0
        print(datos[0])
        if len(registros) != 0:
            print(f"\nContrato Buscado:{folio}")
            print("=====================================================")
            file = open('ContratosAppVista.txt', 'w')
            file.write(f"{datos[0]}\nContrato Buscado: {folio}")
            file.write(
                "\n=====================================================")
            encabezado = ['folio','idcontrato_individual','Colonia','nombre','latitud','longitud','Ultimo_Pago','APP_Ultimo_Pago','Numero_pagos','APP_Numero_pagos','pagos','nombreVendedor','usuario']
            guardarCsv("ContratosAppVista", encabezado, registros)
            for row in registros:
                mensaje1 = f"registro : {contador+1}\nfolio {row[0]}: idcontrato : {row[1]} ruta : {row[2]}\nnombre del vendedor: {row[11]} usuario: {row[12]} \nnombre {row[3]}: latitud : {round(float(row[4]),5)} longitud : {round(float(row[5]),5)}"
                mensaje2 = f"ultimo dia de pago  {row[6]}: app ultimo dia de pago : {row[7]}\nnumero de pagos  {row[8]}: app numero de pagos : {row[9]} pagos {row[10]}"
                imprimir(mensaje1, mensaje2, file)
                contador += 1
        else:
            print("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def busquedaRutas(interfazSql, folio, baseDeDatos):
    os.system("clear")
    sql = f"""select concat_ws(' ',Nombre,Paterno,Materno) as nombreCompleto, idpersonal
from funeraria_personal where concat_ws(' ',Nombre,Paterno,Materno) like '%{folio}%' or idpersonal like '%{folio}%' or usuario like '%{folio}%';"""
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaId = []
        listaPersona = []
        if len(registros) != 0:
            print(f"\Persona buscada Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: persona : {row[0]} id : {row[1]}")
                listaId.append(row[1])
                listaPersona.append(row[0])
                contador += 1
            opcion = int(input("Que persona deseas buscar?: "))
            idpersonal = listaId[opcion]
            nombreMostrar = listaPersona[opcion]
            print(idpersonal)
            sql = f"""SELECT FP.idpersonal, FP.nombre_completo,FP.usuario,FP.clave, FCCC.idcolonia,FC.Colonia,fl.Localidad,fm.Municipio,fe.Estado
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
                interfazSql.execute(sql)  # ejecutamos el sql
                registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
                # print(len(prueba)) imprimimos el numero de registros
                datos = menuFunesBusqueda(baseDeDatos)
                listaColonias = []
                print(datos)
                if len(registros) != 0:
                    print(f"\npersona buscada:{nombreMostrar}")
                    print("=====================================================\n")
                    file = open('LocalidadesApp.txt', 'w')
                    file.write(
                        f"{datos[0]}\npersona buscada: {nombreMostrar}\n")
                    file.write(
                        "=====================================================\n")
                    encabezado = ['idpersonal','nombre_completo','usuario','clave','idcolonia','Colonia','Localidad','Municipio','Estado']
                    guardarCsv("LocalidadesApp", encabezado, registros)
                    for row in registros:
                        mensaje1 = f"Persona encontrada: {row[1]} \nCodigo: {row[0]} Usuario: {row[2]} Contraseña: {row[3]}"
                        mensaje2 = f"Id_colonia: {row[4]} Colonia: {row[5]} \nLocalidad: {row[6]} Municipio: {row[7]} Estado: {row[8]}"
                        listaColonias.append(row[4])
                        imprimir(mensaje1, mensaje2, file)
                    totalColonias = len(listaColonias)
                    contadorColonias = 0
                    colonias = ""
                    if len(listaColonias) > 1:
                        for linea in listaColonias:
                            if contadorColonias == totalColonias-1:
                                colonias += f"'{linea}'"
                            else:
                                colonias += f"'{linea}',"
                            contadorColonias += 1
                    else:
                        colonias = f"'{listaColonias[0]}'"
                    sql = f"select count(*) from funeraria_contrato_individual where idcolonia in({colonias});"
                    interfazSql.execute(sql)  # ejecutamos el sql
                    registros2 = interfazSql.fetchall()  # vemos cuantos registros trae el sql
                    if len(registros2) != 0:
                        contenidoExtra=[(f"numero de contratos: {registros2[0][0]}",""),(f"tiene : {totalColonias} de colonias","")]
                        guardarCsvAppendColumna("LocalidadesApp",contenidoExtra)
                        for row2 in registros2:
                            mensaje1 = f"numero de contratos: {row2[0]} \ntiene : {totalColonias} de colonias"
                            imprimirUnaLinea(mensaje1, file)
                else:
                    print("registros no encontrados")
            except mysql.connector.Error as err:
                print(err)
                print("Message", err.msg)
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def busquedaAbonos(interfazSql, folio, baseDeDatos):
    os.system("clear")
    sql = f"""SELECT fci.Folio,fci.idcontrato_individual
    from funeraria_contrato_individual fci
    where fci.Folio like '%{folio}%';"""
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaId = []
        listaPersona = []
        if len(registros) != 0:
            print(f"\Folio Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: Folio : {row[0]} id : {row[1]}")
                listaId.append(row[1])
                listaPersona.append(row[0])
                contador += 1
            opcion = int(input("Que folio deseas buscar?: "))
            idContrato = listaId[opcion]
            nombreMostrar = listaPersona[opcion]
            print(idContrato)
            sql = f"""SELECT fci.Folio,fp.nombre_completo,fai.Abono,fai.bonificacion,fai.Fecha_Android,fai.Fecha_Oficina,
            CASE
                when fai.deleted = 0 THEN 'valido'
                when fai.deleted = 1 THEN 'invalido'
            END as Estatus
            FROM funeraria_contrato_individual fci
            LEFT JOIN funeraria_personal fp on fp.idpersonal = fci.idvendedor
            LEFT JOIN funeraria_abonos_individual fai on fai.abonos_idcontrato_individual = fci.idcontrato_individual
            WHERE fci.idcontrato_individual = '{idContrato}'
            ORDER BY fai.Fecha_Android;"""
            listaVendedores = []
            print(sql)
            try:
                interfazSql.execute(sql)  # ejecutamos el sql
                registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
                # print(len(prueba)) imprimimos el numero de registros
                datos = menuFunesBusqueda(baseDeDatos)
                print(datos)
                if len(registros) != 0:
                    print(f"\Folio buscada:{nombreMostrar}")
                    print("=====================================================\n")
                    file = open('abonosContratos.txt', 'w')
                    file.write(f"{datos[0]}\Folio buscada: {nombreMostrar}\n")
                    file.write(
                        "=====================================================\n")
                    encabezado = ['Folio','nombre_completo','Abono','bonificacion','Fecha_Android','Fecha_Oficina','estatus']
                    guardarCsv("abonosContratos", encabezado, registros)
                    for row in registros:
                        listaVendedores.append(row[1])
                        mensaje1 = f"Abono: {float(row[2])} Bonificacion: {float(row[3])}"
                        mensaje2 = f" fecha cobro: {row[4]} Fecha Recepcion: {row[5]} Estatus: {row[6]}"
                        mensajeImp = mensaje1+mensaje2
                        print(mensajeImp)
                        soloArchivo(mensaje1, mensaje2, file)
                    print("\nVendedores: \n", listaVendedores)
                    sql2 = f"""SELECT fci.idcontrato_individual,fci.Folio, sum(fai.Abono+fai.bonificacion) as total, sum(fai.Abono) as Abonos,sum(fai.bonificacion) as Bonificacion, fci.limite_asignado as Funeraria, fci.pago_inicial, count(fai.Abono),fci.precio_paquete
                    from funeraria_contrato_individual fci
                    LEFT JOIN funeraria_abonos_individual fai on fai.abonos_idcontrato_individual = fci.idcontrato_individual
                    where fci.idcontrato_individual = '{idContrato}';"""
                    print("\n\n"+sql2+"\n\n")
                    interfazSql.execute(sql2)  # ejecutamos el sql
                    registros2 = interfazSql.fetchall()  # vemos cuantos registros trae el sql
                    if len(registros2) != 0:
                        encabezado = ['idcontrato_individual','Folio','total','Abonos','Bonificacion','Funeraria','pago_inicial', 'numero de abonos','precio_paquete']
                        guardarCsvAppend("abonosContratos", encabezado, registros2)
                        for row in registros2:
                            mensaje1 = f"idContrato: {row[0]} \nFolio: {row[1]} Costo paquete : {float(row[8])} restante : {float(row[8])-float(row[2])-float(row[6])}\nTotal: {float(row[2])} Abonos: {float(row[3])} Bonificacion: {float(row[4])} "
                            mensaje2 = f"Funeraria: {float(row[5])} Pago Inicial: {float(row[6])} Total de abonos : {row[7]}"
                            imprimir(mensaje1, mensaje2, file)
                else:
                    print("registros no encontrados")
            except mysql.connector.Error as err:
                print(err)
                print("Message", err.msg)
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def busquedaAbonosCobrador(interfazSql, folio, baseDeDatos):
    os.system("clear")
    sql = f"""select concat_ws(' ',Nombre,Paterno,Materno) as nombreCompleto, idpersonal
from funeraria_personal where concat_ws(' ',Nombre,Paterno,Materno) like '%{folio}%' or idpersonal like '%{folio}%' or usuario like '%{folio}%'"""
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaId = []
        listaPersona = []
        if len(registros) != 0:
            print(f"\Persona buscada Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: persona : {row[0]} id : {row[1]}")
                listaId.append(row[1])
                listaPersona.append(row[0])
                contador += 1
            opcion = int(input("Que persona deseas buscar?: "))
            idpersonal = listaId[opcion]
            nombreMostrar = listaPersona[opcion]
            fecha = input("Ingresa la fecha que deseas buscar: ")
            if fecha == "1":
                fechaFormateada = date.today()
            else:
                fechaFormateada = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
            diasAtras = int(input("cuantos dias antes: "))
            FechaAnterior = fechaFormateada - timedelta(days=diasAtras)
            print(idpersonal)
            sql = f"""SELECT fp.idpersonal,fp.nombre_completo,oaai.idabono_individual,oaai.Folio,oaai.Abono,oaai.Fecha_pago,case oaai.cobrado_oficina
           when 0 then 'no recepcionado'
               when 1 then 'recepcionado'
     end as cobrado_oficina
     ,oaai.Hora_pago
            from funeraria_personal fp
            left join online_android_abonos_individual oaai on oaai.idcobrador = fp.idpersonal
            where idpersonal = "{idpersonal}" and oaai.Fecha_pago between '{FechaAnterior.strftime("%Y-%m-%d")} '  and '{fechaFormateada.strftime("%Y-%m-%d")} '
            order by Fecha_pago desc ,oaai.Hora_pago;"""
            print(sql)
            try:
                interfazSql.execute(sql)  # ejecutamos el sql
                registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
                # print(len(prueba)) imprimimos el numero de registros
                datos = menuFunesBusqueda(baseDeDatos)
                listaColonias = []
                print(datos)
                if len(registros) != 0:
                    print(f"\npersona buscada:{nombreMostrar}")
                    print("=====================================================\n")
                    file = open('AbonosDados.txt', 'w')
                    file.write(
                        f"{datos[0]}\npersona buscada: {nombreMostrar}\n")
                    file.write(
                        "=====================================================\n")
                    contador = 0
                    total = 0
                    encabezado = ['idpersonal', 'nombre_completo', 'idabono_individual',
                                  'Folio', 'Abono', 'Fecha_pago', 'cobrado_oficina', 'Hora_pago']
                    guardarCsv("AbonosDados", encabezado, registros)

                    for row in registros:
                        mensaje1 = f"IdAbono: {row[2][-10:]} Folio: {row[3]} Abono: {row[4]:,.2f} Fecha: {row[5]} Hora registrado: {row[7]} {row[6]}"
                        imprimirUnaLinea(mensaje1, file)
                        contador += 1
                        total += row[4]
                    contenidoExtra=[(f"hubo {contador} abonos en android online con un total de {total:,.2f} ","")]
                    guardarCsvAppendColumna("AbonosDados",contenidoExtra)    
                    print(
                        f"\nhubo {contador} abonos en android online con un total de {total:,.2f} ")
                else:
                    print("registros no encontrados")
            except mysql.connector.Error as err:
                print(err)
                print("Message", err.msg)
            sql = f"""SELECT fp.idpersonal,fp.nombre_completo,fci.idabono,fci.abonos_idcontrato_individual,fci.Fecha_Android,fci.Abono,fci.bonificacion,fci.idcorte_cobros
            from funeraria_personal fp
            left join funeraria_abonos_individual fci on fci.idcobrador = fp.idpersonal
            where idpersonal = "{idpersonal}" and fci.Fecha_Android between '{FechaAnterior.strftime("%Y-%m-%d")}'  and '{fechaFormateada.strftime("%Y-%m-%d")}'
            order by Fecha_Android desc;"""
            print(sql)
            try:
                interfazSql.execute(sql)  # ejecutamos el sql
                registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
                # print(len(prueba)) imprimimos el numero de registros
                datos = menuFunesBusqueda(baseDeDatos)
                print(datos)
                if len(registros) != 0:
                    print(f"\npersona buscada:{nombreMostrar}")
                    print("=====================================================\n")
                    file = open('AbonosDados.txt', 'a')
                    file.write(
                        f"{datos[0]}\npersona buscada: {nombreMostrar}\n")
                    file.write(
                        "=====================================================\n")
                    encabezado = ['idpersonal', 'nombre_completo', 'idabono', 'abonos_idcontrato_individual',
                                  'Fecha_Android', 'Abono', 'bonificacion', 'idcorte_cobros']
                    guardarCsvAppend("AbonosDados", encabezado, registros)
                    contador = 0
                    totalAbonos = 0
                    totalBonificacion = 0
                    for row in registros:
                        mensaje1 = f"IdAbono: {row[2][-10:]} Folio: {row[3][-5:]} Fecha: {row[4]} Abono: {row[5]:,.2f} Bonificacion: {row[6]:,.2f} idcorte : {row[7]}"
                        imprimirUnaLinea(mensaje1, file)
                        contador += 1
                        totalAbonos += row[5]
                        totalBonificacion += row[6]
                    contenidoExtra=[(f"hubo {contador} abonos en recibidos con un total de {totalAbonos:,.2f} y una bonificacion total de total de {totalBonificacion:,.2f} ","")]
                    guardarCsvAppendColumna("AbonosDados",contenidoExtra)  
                    print(
                        f"\nhubo {contador} abonos en recibidos con un total de {totalAbonos:,.2f} y una bonificacion total de total de {totalBonificacion:,.2f} ")
                else:
                    print("registros no encontrados")
            except mysql.connector.Error as err:
                print(err)
                print("Message", err.msg)
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def agregarPersona(interfazSql, cnx):
    os.system("clear")

    listaFunerarias = {0: 'Tequila', 1: 'Ixtlan', 2: 'San gaspar',
                       3: 'La paz', 4: 'Sipref', 5: 'San jorge', 6: 'Tabasco', 7: 'Socorro'}
    for element in listaFunerarias:
        print(f"{element}.- {listaFunerarias[element]}")
    opcion = int(input("cual es la funeraria a la que deseas dar de alta?: "))
    print(f"seleccionaste esta funeraria {listaFunerarias[opcion]} ")
    nombrePersona = input("a quien daras de alta?: ")
    imei = input("cual es su imei?: ")
    app = input("en que app necesitas? 0 = cobranza 1 = ventas 2 = logistica: ")
    db = listaFunerariasdb[opcion]
    empresa = listaFunerariasidEmpresa[opcion]
    fechaFormateada = date.today()
    fechaFormateada = fechaFormateada - timedelta(days=1)
    sql = f"""INSERT INTO `gruposefi`.`apps_imei` (`idempresa`, `Serie`, `Descripcion`, `Fecha_Inicio`, `Fecha_Vigencia`, `imei_iddb`, `id_app`) 
    VALUES ('{empresa}', '{imei}', '{nombrePersona}', '{fechaFormateada}', '2030-12-31', '{db}', '{app}');"""
    print(sql)
    try:
        interfazSql.execute(sql)
        cnx.commit()
        print("dado de alta")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def verModulosPersonas(interfazSql, folio, baseDeDatos):
    os.system("clear")
    sql = f"""select full_name,iduser 
from system_users
where full_name like '%{folio}%' or iduser like '%{folio}%';"""
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaId = []
        listaPersona = []
        if len(registros) != 0:
            print(f"\Persona buscada Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: persona : {row[0]} id : {row[1]}")
                listaId.append(row[1])
                listaPersona.append(row[0])
                contador += 1
            opcion = int(input("Que persona deseas buscar?: "))
            idpersonal = listaId[opcion]
            nombreMostrar = listaPersona[opcion]
            print(idpersonal)

            sql = f"""SELECT su.full_name,su.username,su.password,ss.station,sl.title,sm.title,sp.record,sp.remove,sp.edit,sp.list
            from system_users su
            left join system_privileges sp on su.iduser = sp.iduser
            left join system_modules sm on sp.idmodule = sm.idmodule
            left join system_station ss on ss.idstation = sp.idstation
            left join system_layer_module slm on sm.idmodule = slm.idmodule
            left join system_layer sl on slm.idlayer = sl.idlayer
            WHERE su.iduser="{idpersonal}"
            order by ss.station,sl.title;"""
            print(sql)
            try:
                interfazSql.execute(sql)  # ejecutamos el sql
                registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
                # print(len(prueba)) imprimimos el numero de registros
                datos = menuFunesBusqueda(baseDeDatos)
                listaColonias = []
                print(datos)
                if len(registros) != 0:
                    print(f"\npersona buscada:{nombreMostrar}")
                    print("=====================================================\n")
                    file = open('modulosPersona.txt', 'w')
                    file.write(
                        f"{datos[0]}\npersona buscada: {nombreMostrar}\n")
                    file.write(
                        "=====================================================\n")
                    contador = 0
                    encabezado = ["nombre completo", "usuario", "password", "sucursal",
                                  "agrupador", "modulo", "guardar", "borrar", "editar", "ver"]
                    guardarCsv("modulosPersona", encabezado, registros)
                    for row in registros:
                        permisoAgregar = "agregar" if row[6] == "1" else ""
                        permisoBorrar = "Borrar" if row[7] == "1" else ""
                        permisoEditar = "Editar" if row[8] == "1" else ""
                        permisoVer = "Ver" if row[9] == "1" else ""

                        mensaje1 = f"Persona encontrada: {row[0]} \nUsuario: {row[1]} Contraseña: {row[2]} sucursal: {row[3]}"
                        mensaje2 = f"Agrupador: {row[4]} modulo: *{row[5]}* \nPermisos: {permisoAgregar} {permisoBorrar} {permisoEditar} {permisoVer}"
                        imprimir(mensaje1, mensaje2, file)
                    file.close()

                else:
                    print("registros no encontrados")
            except mysql.connector.Error as err:
                print(err)
                print("Message", err.msg)
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)


def generadorDeAbonos(interfazSql, folio, baseDeDatos):
    os.system("clear")
    sql = f"""select concat_ws(' ',Nombre,Paterno,Materno) as nombreCompleto, idpersonal, idgrupo
from funeraria_personal where concat_ws(' ',Nombre,Paterno,Materno) like '%{folio}%'"""
    print(sql)
    try:
        interfazSql.execute(sql)  # ejecutamos el sql
        registros = interfazSql.fetchall()  # vemos cuantos registros trae el sql
        # print(len(prueba)) imprimimos el numero de registros
        datos = menuFunesBusqueda(baseDeDatos)
        print(datos[0])
        contador = 0
        listaId = []
        listaPersona = []
        listaGroup = []
        if len(registros) != 0:
            print(f"\Persona buscada Buscado:{folio}")
            print("=====================================================")
            for row in registros:
                print(f"opcion {contador}: persona : {row[0]} id : {row[1]}")
                listaId.append(row[1])
                listaPersona.append(row[0])
                listaGroup.append(row[2])
                contador += 1
            opcion = int(input("Que persona deseas buscar?: "))
            idPersona = listaId[opcion]
            nombreMostrar = listaPersona[opcion]
            grupo = listaGroup[opcion]
            fechaFormateada = date.today()
            length_of_string = 21
            
            print(idPersona)

            sql1 = f"""SELECT folio,latitud,longitud
                FROM online_view_app_contratos
                WHERE idpersonal='{idPersona}';"""
            print(sql1)

            interfazSql.execute(sql1)  # ejecutamos el sql
            registros2 = interfazSql.fetchall()
            if len(registros2) != 0:

                print(f"\Persona buscada Buscado:{nombreMostrar}")
                print("=====================================================")
                file = open('abonosGenerados.txt', 'w')
                contador = 0
                print(registros2)
                for row in registros2:
                    status1 = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
                    sql = f"INSERT INTO `online_android_abonos_individual` (`idabono_individual`, `Folio`, `idcobrador`, `Abono`, `Reimprecion`, `Latitud`, `Longitud`, `Fecha_pago`, `Hora_pago`, `idgrupo`, `cobrado_oficina`) VALUES ('{status1}', '{row[0]}', '{idPersona}', 100, 0, '{row[1]}', '{row[2]}', '{fechaFormateada}', '14:00:0', '1', 0);\n"
                    imprimirUnaLinea(sql, file)
                    contador += 1
            else:
                print("esta persona no tiene contratos en vistas")
        else:
            print("registros no encontrados")
    except mysql.connector.Error as err:
        print(err)
        print("Message", err.msg)