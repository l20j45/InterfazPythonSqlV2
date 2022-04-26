#!/usr/bin/python

import mysql.connector

miConexion = mysql.connector.connect( 
                                     host='www.kitaokatechdb.online', 
                                     user= 'fune_angelessur', 
                                     passwd='fune_angelessur123', 
                                     db='hanbai_fune_angelessureste',
                                     port=3306)

cur = miConexion.cursor()
file = open('selectMasivoEncontrado.txt','w')
with open('selectMasivo.txt', 'r') as f:
    for linea in f:                
        parametro=linea.split("|")
        sql= "SELECT idcontrato_individual,Folio,idcolonia,idsucursal FROM funeraria_contrato_individual WHERE Folio ='"+parametro[0]+"';"
        cur.execute(sql)    
        registros = cur.fetchall()
        if len(registros) != 0:
            for row in registros:
                mensaje ="contrato: |"+ str(parametro[0]) + "| id_id_: |" + str(row[0])+ "| id_folio_: |" + str(row[1])+ "| id_colonia_: |" + str(row[2])+ "| id_sucursal_: |" + str(row[3])
                print(mensaje)
                file.write(mensaje)
                file.write("\n")
        else:
            mensaje ="0|" +parametro[0] + " |registros no encontrados"
            print(mensaje)
            file.write(mensaje)
            file.write("\n")
miConexion.close()
