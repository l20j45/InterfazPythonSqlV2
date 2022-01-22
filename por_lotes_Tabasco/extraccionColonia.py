#!/usr/bin/python

import mysql.connector

miConexion = mysql.connector.connect( 
                                     host='localhost', 
                                     user= 'root', 
                                     passwd='root', 
                                     db='katana',
                                     port=3319)

cur = miConexion.cursor()
file = open('coloniasinsert.txt','w')
with open('colonias.txt', 'r') as f:
    for linea in f:                
        parametro=linea.split("|")
        sql= parametro[1]
        cur.execute(sql)    
        registros = cur.fetchall()
        if len(registros) != 0:
            for row in registros:
                mensaje ="1 | contrato: |"+ str(parametro[0]) + "| id_colonia_: |" + str(row[0])
                print(mensaje)
                file.write(mensaje)
                file.write("\n")
        else:
            mensaje ="0|" +parametro[0] + " |registros no encontrados"
            print(mensaje)
            file.write(mensaje)
            file.write("\n")
            print ()
miConexion.close()