#!/usr/bin/python

file = open('contratossql.txt','w')
with open('contratos.TXT', 'r') as f:
    for linea in f:
        contador = 0
        parametros=linea.split("|")
        sql = "INSERT INTO funeraria_contrato_individual SELECT '%s','%s','%s','%s','%s','%s','%s','%s','%s','0','%s','%s','%s','0','','Sin Archivo','%s','%s','0','0','0','0','0','0','%s','%s','%s','0','0000-00-00','*','%s','%s','','%s','','','contratos_registrados/Individual_1.docx','*','','1','','','15','0','0','0','%s','%s','0','0','0','0000-00-00','0000-00-00','0000-00-00','QWVIOS88F2AZKT','%s','0','0','%s',0,0,'00:00:00','%s','0','0','0','0000-00-00','0000-00-00','0000-00-00','QWVIQDFYF2AZKT',0,'QWVIOTBYF2AZKT','%s',1,1,1;" % (parametros[0].upper(),parametros[1],parametros[2],parametros[3],parametros[4],parametros[5],parametros[6],parametros[7],parametros[8],parametros[10],parametros[11],parametros[12],parametros[16],parametros[17],parametros[24],parametros[25],parametros[26],parametros[30],parametros[31],parametros[33],parametros[46],parametros[47],parametros[55],parametros[58],parametros[62],parametros[72]) 

        print(sql)
        
        file.write(sql)
        file.write("\n")