#!/usr/bin/python

""" import mysql.connector
miConexion = mysql.connector.connect( 
                                     host='localhost', 
                                     user= 'daniel', 
                                     passwd='daniel1', 
                                     db='hanbai_fune_pazjocotepec' )

cur = miConexion.cursor() """
file = open('abonosSql.txt','w')
contador = 0
with open('abonos.txt', 'r') as f:
    for linea in f:
        
        parametros=linea.split("|")
        
        print(parametros)
        corte="CorteSnj"+str(contador)
        
        sql ="INSERT INTO funeraria_abonos_individual SELECT '%s','%s','%s','%d','00:00:00','2022-02-01',0,0,0,0,'%s',0,'%s',0,0,0,'%s',0,'S3NV878C9KVTQO','19:13:22','2022-02-01',0,'%s','PMKYNNXAK0CHX','QWYI36BU9KVTQO','0','0','1','1','1','1','1','1','0','0','0','%s',0;" % (parametros[0],parametros[1],parametros[2],float(parametros[3]),parametros[4],parametros[5],parametros[6],parametros[7],corte)
        
        
        contador+=1
        print(parametros)
        file.write(sql)
        file.write("\n")
