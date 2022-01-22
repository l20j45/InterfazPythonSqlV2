#!/usr/bin/python
''' tipo: lista
parametros: {0,SEMANAL}{1,QUINCENAL}{2,MENSUAL}{3,CADA 2 MESES}{4,CADA 3 MESES}{5,CADA 4 MESES}{6,CADA 5 MESES}{7,CADA 6 MESES}{8,CADA 7 MESES}{9,CADA 8 MESES}{10,CADA 9 MESES}{11,CADA 10 MESES}{12,CADA 11 MESES}{13,CADA AÃƒâ€˜O}
ancho_celda:100 '''

periodicidadDiccionario = {
  "SEMANAL": 0,
  "QUINSENALES": 1,
  "QUINCENAL": 1,
  "QUINSENAL": 1,
  "QUINCENALES": 1,
  "QUINSENALES": 1,
  "CATORCENAL": 1,
  "MENSUAL": 2,
  "NA": 2,
  "MENSUALES": 2,
  "BIMESTRAL": 3,
  "CADA 3 MESES": 4,
  "CADA 4 MESES": 5,
  "CADA 5 MESES": 6,
  "CADA 6 MESES": 7,
  "CADA 7 MESES": 8,
  "CADA 8 MESES": 9,
  "CADA 9 MESES": 10,
  "CADA 10 MESES": 11,
  "CADA 11 MESES": 12,
  "CADA ANIO": 13
}

status = 0
file = open('diadepagoSep.txt','w')
with open('diasdepago.txt', 'r') as f:
    for linea in f:
        parametro=linea.split("|")
        aConvertir = parametro[0].replace(" ","")
        status = periodicidadDiccionario[aConvertir.upper()]
        print(status)
        file.write(str(status))
        file.write("\n")