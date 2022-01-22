#!/usr/bin/python

print ("Resultados de mysql.connector:")
import mysql.connector
miConexion = mysql.connector.connect( 
                                     host='localhost', 
                                     user= 'root', 
                                     passwd='root', 
                                     db='katana' ,
                                     port=3319)

cur = miConexion.cursor()
file = open('colonias.txt','w')

with open('consultasParaTraerId.txt', 'r') as f:
    for linea in f:
        parametro=linea.split("|")
        sql= parametro[1]
        cur.execute(sql)    
        registros = cur.fetchall()
        if len(registros) != 0:
            for row in registros:
                mensaje ="contrato_: "+ str(parametro[0]) + " id_colonia_: " + str(row[0])
                print(mensaje)
                file.write(mensaje)
                file.write("\n")
        else:
            print ("registros no encontrados")

miConexion.close()