#!/usr/bin/python

""" import mysql.connector
miConexion = mysql.connector.connect( 
                                     host='localhost', 
                                     user= 'daniel', 
                                     passwd='daniel1', 
                                     db='hanbai_fune_pazjocotepec' )

cur = miConexion.cursor() """
file = open('localidadesSql.txt','w')
contador = 0
with open('localidades.txt', 'r') as f:
    for linea in f:
        
        parametros=linea.split("|")
        
        print(parametros)
              
        sql ="INSERT INTO funeraria_colonia VALUES('%s','%s','%s','','QWVIOS88F2AZKT');" % (parametros[0],parametros[1],parametros[2])
        

        

        print(parametros)
        file.write(sql)
        file.write("\n")
        