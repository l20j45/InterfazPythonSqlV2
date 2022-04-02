file = open('abonosSql.txt','w')
contador = 0
with open('abonos.txt', 'r') as f:
    for linea in f:
        parametros=linea.split("|")
        codigoCorte="migDiez6"+ str(contador)
        print(parametros)
        sql ="INSERT INTO funeraria_abonos_individual SELECT '%s','%s','%s','%d','00:00:00','2021-11-01',0,0,0,0,'%s',0,0,0,0,0,'%s',0,'QWVIOWCUF2AZKT','19:13:22','2022-02-05',0,'%s','QWVIOS88F2AZKT','QWYI36BU9KVTQO','0','0','1','1','1','1','1','1','0','0','0','%s',0;" % (parametros[0],parametros[1],parametros[2],float(parametros[3]),parametros[4],parametros[5],parametros[6],codigoCorte)
        contador+=1
        file.write(sql)
        file.write("\n")
print("abonos dados de alta",contador)
