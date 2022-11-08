import string
import random
import csv

nombreArchivoSalida="altasColonias.sql"
length_of_string = 16
archivoSalida = open(nombreArchivoSalida,'w')


with open('colonias.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        codigo = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
        sql =f"INSERT INTO funeraria_colonia VALUES('{codigo}','{row['idlocalidad']}','{row['colonia']}','','{row['idgrupo']}');"
        print(sql)
        archivoSalida.write(sql+"\n")
    print("\n\n")
    print("Archivo de salida".center(60,'='))
    print(nombreArchivoSalida)