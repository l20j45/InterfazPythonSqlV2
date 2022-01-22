#!/usr/bin/python

""" import mysql.connector
miConexion = mysql.connector.connect( 
                                     host='localhost', 
                                     user= 'daniel', 
                                     passwd='daniel1', 
                                     db='hanbai_fune_pazjocotepec' )

cur = miConexion.cursor() """
file = open('statusSep.txt','w')
with open('status.txt', 'r') as f:
    for linea in f:
        parametro=linea.split("|")
       # print (parametro)
        print(parametro[0])
        if parametro[0]=="Cancelado":
            status = 6
        elif parametro[0]=="Firmado":
            status = 1
        elif parametro[0]=="Nuevo":
            status = 0
        elif parametro[0]=="Otorgado":
            status = 8
        elif parametro[0]=="Pagado":
            status = 7
        elif parametro[0]=="Pasivo":
            status = 3    
        file.write(str(status))
        file.write("\n")