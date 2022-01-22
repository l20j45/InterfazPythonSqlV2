#!/usr/bin/python
"""
tipo: lista
parametros: {0,Nuevo}{1,Firma}{2,Entregado}{3,Activo}{4,Suspendido}{5,Domicilio}{6,Cancelado}{7,Pagado}{8,Utilizado}
ancho_celda:90
"""
statusDiccionario = {
  "NUEVO": 0,
  "FIRMA": 1,
  "ENTREGADO": 2,
  "ACTIVO": 3,
  "SUSPENDIDO": 4,
  "DOMICILIO": 5,
  "CANCELADO": 6,
  "PAGADO": 7,
  "UTILIZADO": 8
}

status = 0
file = open('statusSep.txt','w')
with open('status.txt', 'r') as f:
    for linea in f:
        parametro=linea.split("|")
        aConvertir = parametro[0].replace(" ","")
        status = statusDiccionario[aConvertir.upper()]
        print(status)
        file.write("status :|"+str(status))
        file.write("\n")