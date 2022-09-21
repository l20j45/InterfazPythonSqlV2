file = open('abonosSql.txt','w')
contador = 0
with open('abonos.txt', 'r') as f:
    for linea in f:
        parametros=linea.split("|")
        corte=parametros[7]+str(contador)
        listaDeParametros={
        'idabono' :parametros[0],	
        'abonos_idcontrato_individual' :parametros[1],	
        'idcobrador' :parametros[2], 
        'Abono' :parametros[3],	
        'Hora_Android':'00:00:00',	
        'Fecha_Android':'2022-07-01',	
        'incripcion':'0',	
        'inscripcion_cobrador':'0',	
        'Pago_Bono':'0',	
        'comision_cobrador_bono':'0',	
        'comision_vendedor':parametros[4],	
        'comision_cobrador_vendedor':'0',	
        'comision_lider':'0',	
        'comiscion_cobrador_lider':'0',	
        'comision_gerente':'0',	
        'comision_cobrador_gerente':'0',	
        'comision_oficina':parametros[5],	
        'comision_cobrador_oficina':'0',	
        'idusuario':parametros[2],	
        'Hora_Oficina':'14:01:00',	
        'Fecha_Oficina':'2022-07-01',	
        'pagado':'1',	
        'bonificacion':parametros[6],	
        'idgrupo':'PMKYNNXAK0CHX',	
        'idvendedor':parametros[2],	
        'idlider':'0',	
        'idgerente':'0',	
        'idcorte_inscripcion':'1',	
        'idcorte_bono':'0',	
        'idcorte_vendedor':'1',	
        'idcorte_lider':'0',	
        'idcorte_gerente':'0',	
        'idcorte_cobrador':'0',	
        'Bono_Asignado':'1',	
        'Inscripcion_Asignado':'1',	
        'id_abono_dividido':'1',	
        'idcorte_cobros':corte,	
        'deleted':'0'}
        #print(parametros)
        print(listaDeParametros['idcorte_cobros'])
        sql =f"""INSERT INTO funeraria_abonos_individual SELECT '{listaDeParametros['idabono']}','{listaDeParametros['abonos_idcontrato_individual']}','{listaDeParametros['idcobrador']}',{listaDeParametros['Abono']},'00:00:00','{listaDeParametros['Fecha_Android']}',0,0,0,0,{listaDeParametros['comision_vendedor']},0,0,0,0,0,{listaDeParametros['comision_oficina']},0,'{listaDeParametros['idusuario']}','{listaDeParametros['Hora_Oficina']}','{listaDeParametros['Fecha_Oficina']}',{listaDeParametros['pagado']},{listaDeParametros['bonificacion']},'{listaDeParametros['idgrupo']}','{listaDeParametros['idvendedor']}','0','0','1','1','1','1','1','1','1','1','1','{listaDeParametros['idcorte_cobros']}',0;"""
        print(sql)
        contador+=1
        file.write(sql)
        file.write("\n")
print("abonos dados de alta",contador)
