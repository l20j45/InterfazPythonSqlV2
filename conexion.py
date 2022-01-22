import mysql.connector
from mysql.connector import errorcode
from urllib.parse import quote


class conexion:
    def __init__(self,opcion):
        folio = 1
        servidor = ""
        usuario = ""
        password = ""
        bd = ""
        puerto = ""
        cnx = ""
        
        if opcion == 1: #local
            servidor=""
            usuario=""
            password=""
            bd=""
            puerto=""

        else:
            print("no existe la funeraria")
            exit()          
        try:    
            self.cnx = mysql.connector.connect(
                host=servidor,
                user=usuario,
                passwd=password,
                database=bd,
                port=puerto)
    
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)          
    def conexioncompleta(self):
        return self.cnx