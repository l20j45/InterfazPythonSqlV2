import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

def menu():
    ###Database Server 1
    print("que sucursal necesitas")
    print("0.-Tabasco: Matriz")
    print("1.-Tabasco: TEAPA")
    print("2.-Tabasco: PARAISO")
    print("3.-Tabasco: VILLAHERMOSA")
    print("4.-Tabasco: COMALCALCO")
    print("5.-La paz: La paz")

def credentialDirectory(option):
    if option == 0:
        credential = os.getenv('DatabaseServer1')
    elif option == 1:
        credential = os.getenv('DatabaseServer2')
    elif option == 2:
        credential = os.getenv('DatabaseServer3')
    elif option == 3:
        credential = os.getenv('DatabaseServer4')
    elif option == 4:
        credential = os.getenv('DatabaseServer5')
    elif option == 5:
        credential = os.getenv('DatabaseServer6')
    elif option == 6:
        credential = os.getenv('DatabaseServer7')
    return credential

def treatment(credential):
    myarray = credential.split("-")
    name = myarray[5]
    parameters = {
        'host': myarray[1],
        'user': myarray[2],
        'passwd': myarray[3],
        'database': myarray[0],
        'port': myarray[4]
    }
    return parameters, name
