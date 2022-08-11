#!/usr/bin/python

import mysql.connector

miConexion = mysql.connector.connect( 
                                     host='www.kitaokatechdb.online', 
                                     user= 'fune_angelessur', 
                                     passwd='fune_angelessur123', 
                                     db='hanbai_fune_angelessureste',
                                     port=3306)

cur = miConexion.cursor()
file = open('selectMasivoEncontrado.txt','w')
file2 = open('selectMasivoNOEncontrado.txt','w')
contador = 0
contador2 = 0
with open('selectMasivo.txt', 'r') as f:
    for linea in f:                
        parametro=linea.split("|")
        sql= f"""SELECT idabono,Abono,Fecha_Android
        from funeraria_abonos_individual fai
        where
            abonos_idcontrato_individual = (select idcontrato_individual from funeraria_contrato_individual where folio='{parametro[0]}') 
        and  Fecha_Oficina >= "{parametro[1]}" LIMIT 1;"""
        cur.execute(sql)    
        registros = cur.fetchall()
        if len(registros) != 0:
            for row in registros:
                mensaje =f'contrato {parametro[0]} fecha {parametro[1]} abono {parametro[2]} \n idabono {row[0]} abono = {row[1]} fecha {row[2]}'
                print(mensaje)
                file.write(mensaje)
                file.write("\n")
                contador +=1
        else:
            mensaje ="0|" +parametro[0] + " |registros no encontrados"
            print(mensaje)
            file2.write(mensaje)
            file2.write("\n")
            contador2 +=1
print(f'contrados con abonos : {contador} ')
print(f'contrados sin abonos : {contador2} ')
miConexion.close()
