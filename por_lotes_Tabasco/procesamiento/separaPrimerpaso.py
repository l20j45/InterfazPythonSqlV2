#!/usr/bin/python

""" import mysql.connector
miConexion = mysql.connector.connect( 
                                     host='localhost', 
                                     user= 'daniel', 
                                     passwd='daniel1', 
                                     db='hanbai_fune_pazjocotepec' )

cur = miConexion.cursor() """
with open('DATOS.TXT', 'r') as f:
    for linea in f:
        parametro=linea.split("|")
       # print (parametro)


"""         sql= parametro[1]
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

miConexion.close() """
