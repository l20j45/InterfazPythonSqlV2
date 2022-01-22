#!/usr/bin/python
from termcolor import colored, cprint
import string
import random
import mysql.connector
miConexion = mysql.connector.connect( 
                                     host='localhost', 
                                     user= 'root', 
                                     passwd='root', 
                                     db='katana',
                                     port=3319)
grupo = "PMKYNNXAK0CHX"
sucursal = "QVIQ9EBU1W9DEM4"

cur = miConexion.cursor()
file = open('municipíosExistentes.txt','w')
file2 = open('municipiossql.txt','w')
file3 = open('municipiosbusquedas.txt','w')
with open('MUNICIPIOS.txt', 'r') as f:
    for linea in f:
        parametro=linea.split("|")
        status = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(15))
        sql = f"SELECT * FROM funeraria_municipios WHERE Municipio LIKE '{parametro[0]}%' AND idsucursal = '{sucursal}' AND idestado ='{parametro[1]}' ;"
        file3.write(sql)
        file3.write("\n")
        #print(sql)
        cur.execute(sql)    
        registros = cur.fetchall()
        if len(registros) != 0:
            for row in registros:
                mensaje ="municipio:"+ str(parametro[0])+ ": nombre :" + str(row[2]) + ": clave :" + str(row[0])
                if str(parametro[0])!=str(row[2]) :
                    cprint('estos son diferentes '+parametro[0]+': '+str(row[2]), 'red', attrs=['blink'])
                print(mensaje)
                file.write(mensaje)
                file.write("\n")       
        else:
            sql = "INSERT INTO funeraria_municipios (idmunicipio,idestado,Municipio,google_map,idgrupo,idsucursal) VALUES('%s','%s','%s','','%s','%s');"%(status.upper(),str(parametro[1]),str(parametro[0]),grupo,sucursal)
            print(sql)
            #cur.execute(sql)    
            #registros = cur.fetchall() 
            file2.write(sql)
            file2.write("\n")
            #miConexion.commit()
miConexion.close()