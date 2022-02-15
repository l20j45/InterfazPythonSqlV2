#!/usr/bin/python

import mysql.connector

miConexion = mysql.connector.connect( 
                                     host='localhost', 
                                     user= 'root', 
                                     passwd='root', 
                                     db='katana',
                                     port=3319)

cur = miConexion.cursor()
sql= "TRUNCATE `funeraria_abonos_individual`;"
sql2= "TRUNCATE `funeraria_contrato_individual`;"
cur.execute(sql)    
cur.execute(sql2)    
miConexion.commit()        