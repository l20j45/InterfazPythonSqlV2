import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="katana",
  port="3319"
)

mycursor = mydb.cursor()
file = open('ContratosNuevos.txt','w')
with open('contratos.txt', 'r') as f:
    for linea in f:
        
        parametros=linea.split("|")
        
        print(parametros)
        contratosinEspacios=parametros[1].replace(" ","")
        file.write("codigo|"+parametros[0] +"|contrato sin tratar|"+parametros[1] +"|contrato tratado|"+contratosinEspacios+"|latitud|"+parametros[2]+"|longitud|"+parametros[3])
        file.write("\n")

