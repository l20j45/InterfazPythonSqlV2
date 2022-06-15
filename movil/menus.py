from termcolor import colored, cprint
import csv

def MenuFunes():
    print("1.- local")
    print("2.- Remoto Developer")
    print("3.- sipref")
    print("4.- vallarta")
    print("5.- san jorge")
    print("6.- zacatecas")
    print("7.- san gaspar")
    print("8.- la paz")
    print("9.- ixtlan")
    print("10.- tequila")
    print("11.- juchipila")
    print("12.- tabasco")
    print("13.- DEMO")
    print("14.- Developer 1")
    print("15.- Developer 2")
    
def MenuArchivoPrincipal():
    print("archivo p o principal")
    print("")
    cprint("1 principal (numero del folio) folio", 'red')
    print("busca el folio y devuelve los datos de idagente_folio\n")
    cprint("2 principal (nombre del personal) personal", 'red')
    print("busca el nombre del personal y devuelve los datos de nombre,idpersonal,usuario, clave\n")
    cprint("3 principal (nombre del personal) cruzado", 'red')
    print("busca el folio  y devuelve los datos de nombre,idpersonal,usuario, clave y folios asigandos que tenga para venta\n")
    cprint("4 principal (numero del contrato) contrato", 'red')
    print("busca el folio y devuelve los datos de idcontrato_individual,folio\n")
    cprint("5 principal (numero del contrato) modificar", 'red')
    print("busca el folio y permite modificar el folio en agentes de folio y contratos\n")
    cprint("6 principal (numero del contrato) modificarfolio", 'red')
    print("busca el folio y permite modificar el folio en agentes folio y lo borra del count\n")



def MenuArchivoMovil():
    print("archivo m o movil")
    print("")
    cprint("1 movil 1 mod", 'red')
    print("permite cambiar mis apps de base de datos\n")
    cprint("2 movil (nombre del personal) rutas", 'red')
    print("busca las rutas o lugares que el personal tiene asignadas en\n")
    cprint("3 movil (folio del contrato) contrato", 'red')
    print("busca el contrato y devuelve a que colonia esta asignada y que cobrador lo tiene asignado\n")
    cprint("4 movil (folio del contrato) vista", 'red')
    print("devuelve todos los contratos que tiene en vista un cobrador\n")
    cprint("5 movil (folio del contrato) contratov", 'red')
    print("busca el contrato y devuelve a que colonia esta asignada y que cobrador lo tiene asignado en la tabla de vistas\n")
    cprint("6 movil (folio del contrato) abonos", 'red')
    print("devuelve los abonos que tiene un contrato\n")
    cprint("7 movil (folio del contrato) abonosrecibidos", 'red')
    print("devuelve los abonos que haya dado un cobrador en una fecha predeterminada\n")
    cprint("8 movil 1 alta", 'red')
    print("te pide los datos como nombre, imei, empresa para poder darlos de alta en la tabla de imeis\n")



def menuFunesBusqueda(baseDeDatos):
    datos = ["", ""]
    if baseDeDatos == 1:
        datos = ["1.- local", "prueba2","local"]
    elif baseDeDatos == 2:
        datos = ["2.- Remoto Developer", "DVL","local"]         
    elif baseDeDatos == 3:
        datos = ["3.- sipref", "SIP","PMKYNNXAK0CHX"]         
    elif baseDeDatos == 4:
        datos = ["4.- vallarta", "prueba2","local"]         
    elif baseDeDatos == 5:
        datos = ["5.- san jorge", "SJG","PNUSFF361BUKEB9"]
    elif baseDeDatos == 6:
        datos = ["6.- zacatecas", "prueba2","local"]        
    elif baseDeDatos == 7:
        datos = ["7.- san gaspar", "SGP","PL6J4E10K0CHX"]
    elif baseDeDatos == 8:
        datos = ["8.- la paz", "PAZ","PM2S1LLK1WW8SPU"]
    elif baseDeDatos == 9:
        datos = ["9.- ixtlan", "IXT","PJRLAMD81S07ZH6"]
    elif baseDeDatos == 10:
        datos = ["10.- tequila", "TEQ","1"]
    elif baseDeDatos == 11:
        datos = ["11.- juchipila", "prueba2","local"]
    elif baseDeDatos == 12:
        datos = ["12.- tabasco", "TAB","QWVIOS88F2AZKT"]
    elif baseDeDatos == 13:
        datos = ["13.- DEMO", "DEM123","DEMO"]
    elif baseDeDatos == 14:
        datos = ["14.- Developer 1", "DEV123","DEVELOPER 1"]
    elif baseDeDatos == 15:
        datos = ["15.- Developer 2", "DVL123","DEVELOPER"]
    return datos
    
def imprimir(mensaje1, mensaje2,file):
    print(mensaje1)
    print(mensaje2)
    print("--------------------------------------------------------------------")
    file.write(mensaje1)
    file.write("\n")    
    file.write(mensaje2)
    file.write("\n-------------------------------------------------------\n")

def soloArchivo(mensaje1, mensaje2,file):
    file.write(mensaje1)
    file.write("\n")    
    file.write(mensaje2)
    file.write("\n-------------------------------------------------------\n")

def imprimirRojo(mensaje1, mensaje2,file):
    cprint(mensaje1,'red')
    cprint(mensaje2,'red')
    cprint("-----------------------------------------------------------------",'red')
    file.write(mensaje1)
    file.write("\n")    
    file.write(mensaje2)
    file.write("\n-------------------------------------------------------\n")  

def imprimirUnaLinea(mensaje1,file):
    print(mensaje1)
    file.write(mensaje1)
    
def guardarCsv(nombre,encabezado: list,registros):
    fileCsv = open(nombre+".csv", 'w')
    myFile = csv.writer(fileCsv)
    myFile.writerow(encabezado)
    myFile.writerows(registros)
    fileCsv.close()

def guardarCsvAppend(nombre,encabezado: list,registros):
    fileCsv = open(nombre+".csv", 'a')
    myFile = csv.writer(fileCsv)
    myFile.writerow(encabezado)
    myFile.writerows(registros)
    fileCsv.close()

def guardarCsvAppendContenido(nombre,registros):
    fileCsv = open(nombre+".csv", 'a')
    myFile = csv.writer(fileCsv)
    myFile.writerows(registros)
    fileCsv.close()

def guardarCsvAppendColumna(nombre,contenido:list):
    fileCsv = open(nombre+".csv", 'a')
    myFile = csv.writer(fileCsv)
    myFile.writerows(contenido)
    fileCsv.close()
    
def guardarCsvEncabezado(nombre,encabezado: list):
    fileCsv = open(nombre+".csv", 'w')
    myFile = csv.writer(fileCsv)
    myFile.writerow(encabezado)
    fileCsv.close()