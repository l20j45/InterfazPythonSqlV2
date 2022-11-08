import string
import random
import csv

nombreArchivoSalida="altasMunicipios.sql"
length_of_string = 16
archivoSalida = open(nombreArchivoSalida,'w')


with open('municipios.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        codigo = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
        sql =f"INSERT INTO funeraria_municipios VALUES('{codigo}','{row['idestado']}','{row['municipio']}','','{row['idgrupo']}','{row['idsucursal']}');"
        print(sql)
        archivoSalida.write(sql+"\n")
    print("\n\n")
    print("Archivo de salida".center(60,'='))
    print(nombreArchivoSalida)