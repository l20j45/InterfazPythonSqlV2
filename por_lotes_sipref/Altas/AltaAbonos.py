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

        codigoCorte="migJacona"+ str(contador)
        
        print(parametros)
              
        #sql ="INSERT INTO funeraria_abonos_individual SELECT '%s','%s','0',%d,'00:00:00','2020-00-00',0,0,0,0,%d,0,0,0,0,0,0,0,'QTNWYX4EFZFMKG','00:00:00','2021-00-00',0,0,'PMKYNNXAK0CHX','QWHSMOCYF2AZKT','0','0','1','1','1','1','1','1','1','1','1','0',0;" % (codigo,parametros[0],cantidadAbono,comisionPagada)
        
        sql ="INSERT INTO funeraria_abonos_individual SELECT '%s','%s','%s','%d','00:00:00','2021-11-01',0,0,0,0,'%s',0,0,0,0,0,'%s',0,'QTNWYX4EFZFMKG','19:13:22','2021-12-05',0,'%s','PMKYNNXAK0CHX','QXFV6IEW1W9DEM4','0','0','1','1','1','1','1','1','0','0','0','%s',0;" % (parametros[0],parametros[1],parametros[2],float(parametros[3]),parametros[4],parametros[5],parametros[6],codigoCorte)
        
        
        contador+=1
        print(parametros)
        file.write(sql)
        file.write("\n")
        



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
