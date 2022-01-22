#!/usr/bin/python

""" import mysql.connector
miConexion = mysql.connector.connect( 
                                     host='localhost', 
                                     user= 'daniel', 
                                     passwd='daniel1', 
                                     db='hanbai_fune_pazjocotepec' )

cur = miConexion.cursor() """
nombre =""
apellidoPat =""
apellidomat =""
file = open('nombresSeparados.txt','w')
contador=0
with open('nombres.txt', 'r') as f:
    for linea in f:
        parametro=linea.split(" ")
       # print (parametro)
        nombre=""
        apellidoPat=""
        apellidomat=""
        if len(parametro)==3:
            nombre = parametro[0]
            apellidoPat=parametro[1]
            apellidomat=parametro[2]
        elif len(parametro)==4:
            nombre = parametro[0] + " " +parametro[1] 
            apellidoPat=parametro[2]
            apellidomat=parametro[3]
        elif len(parametro)==5:
            nombre = parametro[0] + " " +parametro[1]+ " " +parametro[2] 
            apellidoPat=parametro[3]
            apellidomat=parametro[4]
        elif len(parametro)==6:
            nombre = parametro[0] + " " +parametro[1] + " " +parametro[2]+ " " +parametro[3] 
            apellidoPat=parametro[4]
            apellidomat=parametro[5]
        elif len(parametro)==7:
            nombre = parametro[0] + " " +parametro[1] + " " +parametro[2]+ " " +parametro[3] + " " +parametro[4] 
            apellidoPat=parametro[5]
            apellidomat=parametro[6]
        elif len(parametro)==8:
            nombre = parametro[0] + " " +parametro[1] + " " +parametro[2]+ " " +parametro[3] + " " +parametro[4] 
            apellidoPat=parametro[5]
            apellidomat=parametro[6]
        print("nombre "+str(contador))
        print(parametro)
        print(nombre + apellidoPat)
        file.write("nombre :|"+nombre)
        file.write("|apellidoPat :|"+apellidoPat)
        file.write("|apellidoMat :|"+apellidomat)
        contador+=1
           
        
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