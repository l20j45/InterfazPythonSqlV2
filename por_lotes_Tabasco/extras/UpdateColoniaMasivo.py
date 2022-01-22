#!/usr/bin/python

import mysql.connector

miConexion = mysql.connector.connect( 
                                     host='localhost', 
                                     user= 'root', 
                                     passwd='root', 
                                     db='katana',
                                     port=3319)

cur = miConexion.cursor()
file = open('UpdateMasivoEncontrado.txt','w')
with open('UpdateMasivo.txt', 'r') as f:
    for linea in f:                
        parametro=linea.split("|")
        sql= "UPDATE `hanbai_fune_angelessureste`.`funeraria_contrato_individual` SET `Fecha`='2021-11-01' WHERE  `idcontrato_individual`='"+parametro[0]+"';"
        file.write(sql)
        file.write("\n")
            
miConexion.close()