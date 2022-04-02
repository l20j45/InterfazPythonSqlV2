from termcolor import colored, cprint

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
    print("busca el contrato y devuelve a que colonia esta asignada y que cobrador lo tiene asignado")

def menuFunesBusqueda(baseDeDatos):
    datos = ["", ""]
    if baseDeDatos == 1:
        datos = ["1.- local", "prueba2","local"]
        return datos
    elif baseDeDatos == 2:
        datos = ["2.- Remoto Developer", "DVL","local"]
        return datos
    elif baseDeDatos == 3:
        datos = ["3.- sipref", "SIP","PMKYNNXAK0CHX"]
        return datos
    elif baseDeDatos == 4:
        datos = ["4.- vallarta", "prueba2","local"]
        return datos
    elif baseDeDatos == 5:
        datos = ["5.- san jorge", "SJG","PNUSFF361BUKEB9"]
        return datos
    elif baseDeDatos == 6:
        datos = ["6.- zacatecas", "prueba2","local"]
        return datos
    elif baseDeDatos == 7:
        datos = ["7.- san gaspar", "SGP","PL6J4E10K0CHX"]
        return datos
    elif baseDeDatos == 8:
        datos = ["8.- la paz", "PAZ","PM2S1LLK1WW8SPU"]
        return datos
    elif baseDeDatos == 9:
        datos = ["9.- ixtlan", "IXT","PJRLAMD81S07ZH6"]
        return datos
    elif baseDeDatos == 10:
        datos = ["10.- tequila", "TEQ","1"]
        return datos
    elif baseDeDatos == 11:
        datos = ["11.- juchipila", "prueba2","local"]
        return datos
    elif baseDeDatos == 12:
        datos = ["12.- tabasco", "TAB","QWVIOS88F2AZKT"]
        return datos
    elif baseDeDatos == 13:
        datos = ["13.- DEMO", "DEM","DEMO"]
        return datos
    
def imprimir(mensaje1, mensaje2,file):
    print(mensaje1)
    print(mensaje2)
    print("-------------------------------------------------------")
    file.write(mensaje1)
    file.write("\n")    
    file.write(mensaje2)
    file.write("\n-------------------------------------------------------\n")

def imprimirRojo(mensaje1, mensaje2,file):
    cprint(mensaje1,'red')
    cprint(mensaje2,'red')
    cprint("-------------------------------------------------------",'red')
    file.write(mensaje1)
    file.write("\n")    
    file.write(mensaje2)
    file.write("\n-------------------------------------------------------\n")  

def imprimirUnaLinea(mensaje1,file):
    print(mensaje1)
    file.write(mensaje1)