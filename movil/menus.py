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
    cprint("1 p.py (numero del folio) folio", 'red')
    print("busca el folio y devuelve los datos de idagente_folio\n")
    cprint("2 p.py (nombre del personal) personal", 'red')
    print("busca el nombre del personal y devuelve los datos de nombre,idpersonal,usuario, clave\n")
    cprint("3 p.py (nombre del personal) cruzado", 'red')
    print("busca el folio  y devuelve los datos de nombre,idpersonal,usuario, clave y folios asigandos que tenga para venta\n")
    cprint("4 p.py (numero del contrato) contrato", 'red')
    print("busca el folio y devuelve los datos de idcontrato_individual,folio\n")
    cprint("5 p.py (numero del contrato) modificar", 'red')
    print("busca el folio y permite modificar el folio en agentes de folio y contratos\n")
    cprint("6 p.py (numero del contrato) modificarfolio", 'red')
    print("busca el folio y permite modificar el folio en agentes folio y lo borra del count\n")



def MenuArchivoMovil():
    print("archivo m o movil")
    print("")
    cprint("1 m.py 1 mod", 'red')
    print("permite cambiar mis apps de base de datos\n")
    cprint("2 m.py (nombre del personal) rutas", 'red')
    print("busca las rutas o lugares que el personal tiene asignadas en\n")
    cprint("3 m.py (folio del contrato) contrato", 'red')
    print("busca el contrato y devuelve a que colonia esta asignada y que cobrador lo tiene asignado\n")
    cprint("4 m.py (folio del contrato) vista", 'red')
    print("devuelve todos los contratos que tiene en vista un cobrador\n")
    cprint("5 m.py (folio del contrato) contratov", 'red')
    print("busca el contrato y devuelve a que colonia esta asignada y que cobrador lo tiene asignado en la tabla de vistas\n")
    cprint("6 m.py (folio del contrato) abonos", 'red')
    print("devuelve los abonos que tiene un contrato\n")
    cprint("7 m.py (folio del contrato) abonosrecibidos", 'red')
    print("devuelve los abonos que haya dado un cobrador en una fecha predeterminada\n")
    cprint("8 m.py 1 alta", 'red')
    print("te pide los datos como nombre, imei, empresa para poder darlos de alta en la tabla de imeis\n")

def MenuArchivoExtra():
    print("archivo e o extra")
    print("")
    cprint("1 e.py (nombre del personal) permisos", 'red')
    print("muestra los permisos que tiene cada persona\n")
    cprint("2 e.py (nombre del personal) usuarioSys", 'red')
    print("muestra el usuario del sistema con contraseña\n")
    cprint("3 e.py (nombre del personal) verModulos", 'red')
    print("ves los modulos que tiene dado de alta cada usuario\n")



def menuFunesBusqueda(baseDeDatos):
    datos = ["", ""]
    if baseDeDatos == 1:
        datos = ["1.- local", "prueba2","local"]
    elif baseDeDatos == 2:
        datos = ["2.- Remoto Developer", "DVL","local"]         
    elif baseDeDatos == 3:
        datos = ["3.- sipref", "SIP","PMKYNNXAK0CHX","hanbai_sipref"]         
    elif baseDeDatos == 4:
        datos = ["4.- vallarta", "prueba2","local","hanbai_fune_socorro"]         
    elif baseDeDatos == 5:
        datos = ["5.- san jorge", "SJG","PNUSFF361BUKEB9","hanbai_fune_sanjorge"]
    elif baseDeDatos == 6:
        datos = ["6.- zacatecas", "prueba2","local"]        
    elif baseDeDatos == 7:
        datos = ["7.- san gaspar", "SGP","PL6J4E10K0CHX","hanbai_fune_sangaspar"]
    elif baseDeDatos == 8:
        datos = ["8.- la paz", "PAZ","PM2S1LLK1WW8SPU","hanbai_fune_pazjocotepec"]
    elif baseDeDatos == 9:
        datos = ["9.- ixtlan", "IXT","PJRLAMD81S07ZH6","hanbai_funeixtlan"]
    elif baseDeDatos == 10:
        datos = ["10.- tequila", "TEQ","1","hanbai_sefi"]
    elif baseDeDatos == 11:
        datos = ["11.- juchipila", "prueba2","local"]
    elif baseDeDatos == 12:
        datos = ["12.- tabasco", "TAB","QWVIOS88F2AZKT","hanbai_fune_angelessureste"]
    elif baseDeDatos == 13:
        datos = ["13.- DEMO", "DEM123","DEMO","distributor_solutionsoft_demo"]
    elif baseDeDatos == 14:
        datos = ["14.- Developer 1", "DEV123","DEVELOPER 1","distributor_solutionsoft_developer"]
    elif baseDeDatos == 15:
        datos = ["15.- Developer 2", "DVL123","DEVELOPER","distributor_solutionsoft_developer2"]
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
    fileCsv = open(nombre+".csv", 'w',encoding="utf-8")
    myFile = csv.writer(fileCsv)
    myFile.writerow(encabezado)
    myFile.writerows(registros)
    fileCsv.close()

def guardarCsvAppend(nombre,encabezado: list,registros):
    fileCsv = open(nombre+".csv", 'a',encoding="utf-8")
    myFile = csv.writer(fileCsv)
    myFile.writerow(encabezado)
    myFile.writerows(registros)
    fileCsv.close()

def guardarCsvAppendContenido(nombre,registros):
    fileCsv = open(nombre+".csv", 'a',encoding="utf-8")
    myFile = csv.writer(fileCsv)
    myFile.writerows(registros)
    fileCsv.close()

def guardarCsvAppendColumna(nombre,contenido:list):
    fileCsv = open(nombre+".csv", 'a',encoding="utf-8")
    myFile = csv.writer(fileCsv)
    myFile.writerows(contenido)
    fileCsv.close()
    
def guardarCsvEncabezado(nombre,encabezado: list):
    fileCsv = open(nombre+".csv", 'w',encoding="utf-8")
    myFile = csv.writer(fileCsv)
    myFile.writerow(encabezado)
    fileCsv.close()