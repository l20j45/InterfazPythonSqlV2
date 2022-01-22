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
idgrupo = "PMKYNNXAK0CHX"

cur = miConexion.cursor()
file = open('localidadesExistentes.txt','w')
file2 = open('localidadesSql.txt','w')
file3 = open('localidadesBusqueda.txt','w')
with open('LOCALIDADES.txt', 'r') as f:
    for linea in f:
        parametro=linea.split("|")
        status = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(15))
        sql = "SELECT * FROM funeraria_localidad WHERE Localidad LIKE '"+parametro[0] +"%' AND idmunicipio ='"+parametro[1]+"';"
        #print(sql)
        file3.write(sql)
        file3.write("\n")
        cur.execute(sql)    
        registros = cur.fetchall()
        if len(registros) != 0:
            for row in registros:
                mensaje ="municipio:"+ str(parametro[0])+ ": nombre : " + str(row[3]) + " clave: " + str(row[0])
                print(mensaje)
                if str(parametro[0])!=str(row[2]) :
                    cprint('estos son diferentes '+parametro[0]+': '+str(row[2]), 'red', attrs=['blink'])
                file.write(mensaje)
                file.write("\n")       
        else:
            sql = "INSERT INTO funeraria_localidad (idlocalidad,idmunicipio,Localidad,google_map,idgrupo) VALUES('%s','%s','%s','','%s');" %(status.upper(),str(parametro[1]),str(parametro[0]),idgrupo)
            print(sql)
            #cur.execute(sql)    
            #registros = cur.fetchall() 
            file2.write(sql)
            file2.write("\n")
            #miConexion.commit()
miConexion.close()