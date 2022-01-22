import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="katana",
  port="3319"
)

mycursor = mydb.cursor()
file = open('Consulta.txt','w')
with open('lectura.txt', 'r') as f:
    for linea in f:
        
        parametros=linea.split("|")
        
        print(parametros)
              
        sql ="SELECT * FROM funeraria_abonos_individual WHERE abonos_idcontrato_individual ='%s';" % (parametros[0])
        print(sql)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            file.write("codigo:|"+x[0]+"|contrato:|"+x[1]+"|cobrador:|"+x[2]+"|abono:|"+str(x[3]))
            file.write("\n")

