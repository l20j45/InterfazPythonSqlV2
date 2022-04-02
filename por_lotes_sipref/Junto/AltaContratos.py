#!/usr/bin/python

file = open('contratossql.txt','w')
with open('contratos.TXT', 'r') as f:
    for linea in f:
        contador = 0
        parametros=linea.split("|")
        #sql = "INSERT INTO funeraria_contrato_individual SELECT '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',0,'','Sin Archivo','QTNWYX4EFZFMKG','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','0','0000-00-00','*','%s','%s','','%s','','','contratos_registrados/Individual_1.docx','%s','','5','','','15','0','0','0',0,'%s','0','0','%s','0000-00-00','0000-00-00','0000-00-00','PMKYNNXAK0CHX','QWHSMOCYF2AZKT','0','0','PMYP5JXC1W9DEM4',0,0,'00:00:00','%s','0','0','0','0000-00-00','0000-00-00','0000-00-00','PMKYP450K0CHX',0,'PMKYP0DGK0CHX',0,1,1,1;" % ()      

        # sql = "INSERT INTO funeraria_contrato_individual SELECT '%s','%s','%s','%s','%s','%s','%s','%s','%s'8,0,0,'%s','%s',013 limite asignado,'','Sin Archivo','QWYI36BU9KVTQO',017,0,0,020,0,0,0,'%s','%s','%s','%s','0000-00-00 nacimiento cliente 28','*','%s','%s','%s','%s 33','%s','%s','contratos_registrados/Individual_1.docx36','%s','x','1','','','15','0','0','0'45,'%s','%s','0','0','0','%s','%s'52,'0000-00-00','QWVIOS88F2AZKT','QWYI36BU9KVTQO','0','0','colonia58',0,0,'00:00:00horacalle 61','%s','0','0','0','0000-00-00','0000-00-00','0000-00-0068a','QWVIQDFYF2AZKT',0,'QWVIOTBYF2AZKT',0,1,1,1;" % (parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0],parametros[0])       
       
        sql = "INSERT INTO funeraria_contrato_individual SELECT '%s','%s','%s','%s','%s','%s','%s','%s','%s',0,0,'%s','%s',0,'','Sin Archivo','S3MQCJT61W9DEM4',0,0,0,0,0,0,0,'%s','%s','%s','0','0000-00-00','*','%s','%s','%s','%s','%s','%s','contratos_registrados/Individual_1.docx36','%s','x','1','','','15','0','0','0','%s','%s','0','0','0','%s','%s','0000-00-00','PMKYNNXAK0CHX','QWYI36BU9KVTQO','0','0','%s',0,0,'00:00:00','%s','0','0','0','0000-00-00','0000-00-00','0000-00-00','QVHX1JQ2R6W8BM',0,'QVHX12JGR6W8BM',0,1,1,1;" % (parametros[0],parametros[1],parametros[2],parametros[3],parametros[4],parametros[5],parametros[6],parametros[7],parametros[8],parametros[11],parametros[12],parametros[27],parametros[28],parametros[29],parametros[33],parametros[34],parametros[35],parametros[36],parametros[37],parametros[38],parametros[40],parametros[49],parametros[50],parametros[54],parametros[55],parametros[61],parametros[65])     
        
        print(sql)
        
        file.write(sql)
        file.write("\n")