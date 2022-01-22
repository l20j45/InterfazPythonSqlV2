#!/usr/bin/python

""" import mysql.connector
miConexion = mysql.connector.connect( 
                                     host='localhost', 
                                     user= 'daniel', 
                                     passwd='daniel1', 
                                     db='hanbai_fune_pazjocotepec' )

cur = miConexion.cursor() """
file = open('inserts.txt','w')
with open('updateVendedor.txt', 'r') as f:
    for linea in f:
        contador = 0
        parametros=linea.split("|")
        sql = "INSERT INTO funeraria_contrato_individual SELECT '%s','%s','%s','%s','%s','%s','%s','2020-01-01','%s','%s','%s','%s','%s',0,'','Sin Archivo','QTNWYX4EFZFMKG','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','0','0000-00-00','*','%s','%s','','%s','','','contratos_registrados/Individual_1.docx','%s','','5','','','15','0','0','0',0,'%s','0','0','%s','0000-00-00','0000-00-00','0000-00-00','PMKYNNXAK0CHX','QWHSMOCYF2AZKT','0','0','PMYP5JXC1W9DEM4',0,0,'00:00:00','%s','0','0','0','0000-00-00','0000-00-00','0000-00-00','PMKYP450K0CHX',0,'PMKYP0DGK0CHX',0,1,1,1;" % (parametros[0],parametros[1],parametros[37],parametros[2],parametros[3],parametros[4],parametros[5],parametros[7],parametros[8],parametros[9],parametros[10],parametros[11],parametros[13],parametros[14],parametros[15],parametros[16],parametros[17],parametros[18],parametros[19],parametros[20],parametros[21],parametros[22],parametros[23],parametros[24],parametros[25],parametros[26],parametros[28],parametros[29],parametros[32])    
        file.write("insert :|" + sql)
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
