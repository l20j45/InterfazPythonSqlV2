#!/usr/bin/python

import mysql.connector

miConexion = mysql.connector.connect( 
                                     host='localhost', 
                                     user= 'root', 
                                     passwd='root', 
                                     db='katana',
                                     port=3319)

cur = miConexion.cursor()
file = open('AbonosMasivosEncontrado.txt','w')
with open('AbonosMasivos.txt', 'r') as f:
    for linea in f:                
        parametro=linea.split("|")
        sql= f"select count(*) from funeraria_abonos_individual where abonos_idcontrato_individual='{parametro[0]}'"
        cur.execute(sql)    
        registros = cur.fetchall()
        if len(registros) != 0:
            for row in registros:
                mensaje =f"{row[0]}" 
                print(mensaje)
                file.write(mensaje)
                file.write("\n")
        else:
            mensaje ="0|" +parametro[0] + " |registros no encontrados"
            print(mensaje)
            file.write(mensaje)
            file.write("\n")
miConexion.close()