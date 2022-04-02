#!/usr/bin/python

import mysql.connector

miConexion = mysql.connector.connect( 
                                     host='www.kitaokatechdb.online', 
                                     user= 'fune_angelessur', 
                                     passwd='fune_angelessur123', 
                                     db='hanbai_fune_angelessureste',
                                     port=3306)

listaEncontrados=[]
cur = miConexion.cursor()
file = open('contratosEncontrados.txt','w')
with open('foliosBuscados.txt', 'r') as f:
    for linea in f:                
        parametro=linea.split("|")
        sql= "SELECT idcontrato_individual,Folio FROM funeraria_contrato_individual WHERE Folio ='"+parametro[0]+"';"
        cur.execute(sql)    
        registros = cur.fetchall()
        if len(registros) != 0:
            for row in registros:
                mensaje =f'se encontro el folio {parametro[0]} en este registro {row[0]}:{row[1]}'
                listaEncontrados.append(parametro[0])
                print(mensaje)
        else:
            mensaje ="0|" +linea + " |registros no encontrados"
            print(mensaje)
miConexion.close()
cadenasEncontradas="|".join(listaEncontrados)
eliminarEncontrados=f"grep -Ev '{cadenasEncontradas}'"
SepararEncontrados=f"grep -E '{cadenasEncontradas}'"
print("____________________________________________")
print("Encontrados \n\n"+eliminarEncontrados+" juntosUsar.csv > DarDeAlta.csv")

print("Nuevos \n\n"+SepararEncontrados+" juntosUsar.csv > repetidos.csv")
