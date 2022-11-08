import csv
sql="INSERT INTO funeraria_abonos_individual VALUES "


with open('Abonos.csv') as csv_file:
    file = open('abonosSqlTratado.sqlZip','w')
    csv_reader = csv.reader(csv_file, delimiter=',')
    for contador,parametros in enumerate(csv_reader):
        if contador > 4:
            parametros[4]="0" if float(parametros[4])<0 else parametros[4]
            parametros[3]="0" if float(parametros[3])<0 else parametros[3]
            parametros[5]="0" if float(parametros[5])<0 else parametros[5]
            parametros[6]="0" if float(parametros[6])<0 else parametros[6]
            listaDeParametros={
            'idabono' :parametros[0],	
            'abonos_idcontrato_individual' :parametros[1],	
            'idcobrador' :parametros[2], 
            'Abono' :parametros[3],	
            'Hora_Android':'00:00:00',	
            'Fecha_Android':'2022-10-24',	
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
            'Fecha_Oficina':'2022-10-24',	
            'pagado':'1',	
            'bonificacion':parametros[6],	
            'idgrupo':parametros[8],	
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
            'idcorte_cobros':parametros[7],	
            'deleted':'0'}
            #print(parametros)
            if  contador %59==0:
                sql += f""" ('{listaDeParametros['idabono']}','{listaDeParametros['abonos_idcontrato_individual']}','{listaDeParametros['idcobrador']}',{listaDeParametros['Abono']},'00:00:00','{listaDeParametros['Fecha_Android']}',0,0,0,0,{listaDeParametros['comision_vendedor']},0,0,0,0,0,{listaDeParametros['comision_oficina']},0,'{listaDeParametros['idusuario']}','{listaDeParametros['Hora_Oficina']}','{listaDeParametros['Fecha_Oficina']}',{listaDeParametros['pagado']},{listaDeParametros['bonificacion']},'{listaDeParametros['idgrupo']}','{listaDeParametros['idvendedor']}','0','0','1','1','1','1','1','1','1','1','1','{listaDeParametros['idcorte_cobros']}',0);"""
                print(sql)
                file.write(sql)
                file.write("\n")
                sql ="INSERT INTO funeraria_abonos_individual VALUES "
            else:
                sql += f""" ('{listaDeParametros['idabono']}','{listaDeParametros['abonos_idcontrato_individual']}','{listaDeParametros['idcobrador']}',{listaDeParametros['Abono']},'00:00:00','{listaDeParametros['Fecha_Android']}',0,0,0,0,{listaDeParametros['comision_vendedor']},0,0,0,0,0,{listaDeParametros['comision_oficina']},0,'{listaDeParametros['idusuario']}','{listaDeParametros['Hora_Oficina']}','{listaDeParametros['Fecha_Oficina']}',{listaDeParametros['pagado']},{listaDeParametros['bonificacion']},'{listaDeParametros['idgrupo']}','{listaDeParametros['idvendedor']}','0','0','1','1','1','1','1','1','1','1','1','{listaDeParametros['idcorte_cobros']}',0),"""
    #        sql =f"""INSERT INTO funeraria_abonos_individual SELECT '{listaDeParametros['idabono']}','{listaDeParametros['abonos_idcontrato_individual']}','{listaDeParametros['idcobrador']}',{listaDeParametros['Abono']},'00:00:00','{listaDeParametros['Fecha_Android']}',0,0,0,0,{listaDeParametros['comision_vendedor']},0,0,0,0,0,{listaDeParametros['comision_oficina']},0,'{listaDeParametros['idusuario']}','{listaDeParametros['Hora_Oficina']}','{listaDeParametros['Fecha_Oficina']}',{listaDeParametros['pagado']},{listaDeParametros['bonificacion']},'{listaDeParametros['idgrupo']}','{listaDeParametros['idvendedor']}','0','0','1','1','1','1','1','1','1','1','1','{listaDeParametros['idcorte_cobros']}',0;"""
    sqlFinal=sql.rstrip(sql[-1])
    sqlFinal+=";"
    print(sqlFinal)
    file.write(sqlFinal)
    file.write("\n")
print("numero de contratos",contador)
