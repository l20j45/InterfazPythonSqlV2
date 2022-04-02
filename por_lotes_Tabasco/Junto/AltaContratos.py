#!/usr/bin/python

file = open('contratossql.txt','w')
contador=0
with open('contratos.TXT', 'r') as f:
    for linea in f:
        parametros=linea.split("|")
        sql = "INSERT INTO funeraria_contrato_individual SELECT '%s','%s','%s','%s','%s','%s','%s','%s','%s',0,0,'%s','%s',0,'','Sin Archivo','QWYI36BU9KVTQO',0,0,0,0,0,0,0,'%s','%s','%s','0','0000-00-00','*','%s','%s','%s','%s','%s','%s','contratos_registrados/Individual_1.docx36','%s','x','1','','','15','0','0','0','%s','%s','0','0','0','%s','%s','0000-00-00','QWVIOS88F2AZKT','QWYI36BU9KVTQO','0','0','%s',0,0,'00:00:00','%s','0','0','0','0000-00-00','0000-00-00','0000-00-00','QWVIQDFYF2AZKT',0,'QWVIOTBYF2AZKT',0,1,1,1;" % (parametros[0],parametros[1],parametros[2],parametros[3],parametros[4],parametros[5],parametros[6],parametros[7],parametros[8],parametros[11],parametros[12],parametros[27],parametros[28],parametros[29],parametros[33],parametros[34],parametros[35],parametros[36],parametros[37],parametros[38],parametros[40],parametros[49],parametros[50],parametros[54],parametros[55],parametros[61],parametros[65])        
        print(sql)
        file.write(sql)
        file.write("\n")
        contador=contador+1
print("numero de contratos",contador)
