import csv

with open('plantillaContratos.csv') as csv_file:
    file = open('contratossqlTratado.Tratado','w')
    csv_reader = csv.reader(csv_file, delimiter=',')
    for contador,parametros in enumerate(csv_reader):

        if contador > 9:
            listaDeParametros={
            'idcontrato_individual' :  parametros[0],
            'Folio' :  parametros[1],
            'Estatus' :  parametros[2],
            'Paquete' :  parametros[3],
            'Estado' :  parametros[4],
            'Municipio' :  parametros[5],
            'Localidad' :  parametros[6],
            'Fecha' :  parametros[7],
            'precio' :  parametros[8],
            'promocion' :  parametros[9],
            'pago_inicial' :  parametros[10],
            'Abonos_de' :  parametros[11],
            'Plan_de_Pago' :  parametros[12],
            'limite_asignado' :  parametros[13],
            'Funeraria_Procedencia' :  parametros[14],
            'archivo_adjunto' :  parametros[15],
            'idusuario' :  parametros[16],
            'Comision_Vendedor' :  parametros[17],
            'comision_pagada_vendedor' :  parametros[18],
            'Comision_Lider' :  parametros[19],
            'comision_pagada_lider' :  parametros[20],
            'Comision_Gerente' :  parametros[21],
            'comision_pagada_gerente' :  parametros[22],
            'Bono' :  parametros[23],
            'Bono_Asignado' :  parametros[24],
            'Inscripcion' :  parametros[25],
            'Inscripcion_Asignado' :  parametros[26],
            'Apellido_Paterno' :  parametros[27],
            'Apellido_Materno' :  parametros[28],
            'Nombre' :  parametros[29],
            'Estado_Civil' :  parametros[30],
            'Nacimiento' :  parametros[31],
            'IFE' :  parametros[32],
            'Domicilio' :  parametros[33],
            'Colonia' :  parametros[34],
            'Entre_Calles' :  parametros[35],
            'Telefono' :  parametros[36],
            'Beneficiario' :  parametros[37],
            'Observaciones' :  parametros[38],
            'archivo_contrato' :  parametros[39],
            'Domicilio2' :  parametros[40],
            'Correo' :  parametros[41],
            'dia_cobro' :  parametros[42],
            'firma1' :  parametros[43],
            'firma2' :  parametros[44],
            'plazo_entrega' :  parametros[45],
            'latitud' :  parametros[46],
            'longitud' :  parametros[47],
            'Tipo_Cobranza' :  parametros[48],
            'Monto_Liquidado' :  parametros[49],
            'Saldo_Deudor' :  parametros[50],
            'horario_cobro' :  parametros[51],
            'Estado_Cobro' :  parametros[52],
            'Retrasos' :  parametros[53],
            'ultimo_pago' :  parametros[54],
            'pago_programado' :  parametros[55],
            'fecha_entrega' :  parametros[56],
            'idgrupo' :  parametros[57],
            'idvendedor' :  parametros[58],
            'idlider' :  parametros[59],
            'idgerente' :  parametros[60],
            'idcolonia' :  parametros[61],
            'edad' :  parametros[62],
            'genero' :  parametros[63],
            'hora_calle' :  parametros[64],
            'precio_paquete' :  parametros[65],
            'NumeroServicio' :  parametros[66],
            'NumeroFactura' :  parametros[67],
            'NumeroTitulo' :  parametros[68],
            'Fecha_Cancelacion' :  parametros[69],
            'Fecha_Pagado' :  parametros[70],
            'Fecha_Utilizado' :  parametros[71],
            'idpaquete_kit' :  parametros[72],
            'deleted' :  parametros[73],
            'idsucursal' :  parametros[74],
            'pagos' :  parametros[75],
            'tipo_comision_vendedor' :  parametros[76],
            'tipo_comision_lider' :  parametros[77],
            'tipo_comision_gerente' :  parametros[78],
            'final' :  parametros[79]}
            
            sql = f"""INSERT IGNORE INTO funeraria_contrato_individual SELECT '{listaDeParametros['idcontrato_individual']}','{listaDeParametros['Folio']}','{listaDeParametros['Estatus']}','{listaDeParametros['Paquete']}','{listaDeParametros['Estado']}','{listaDeParametros['Municipio']}','{listaDeParametros['Localidad']}','{listaDeParametros['Fecha']}','{listaDeParametros['precio']}','0','{listaDeParametros['pago_inicial']}','{listaDeParametros['Abonos_de']}','{listaDeParametros['Plan_de_Pago']}','0','','Sin Archivo','{listaDeParametros['idusuario']}','{listaDeParametros['Comision_Vendedor']}','{listaDeParametros['Comision_Lider']}','{listaDeParametros['Comision_Gerente']}','0','0','0','0','{listaDeParametros['Apellido_Paterno']}','{listaDeParametros['Apellido_Materno']}','{listaDeParametros['Nombre']}','0','2000-01-01','{listaDeParametros['IFE']}','{listaDeParametros['Domicilio']}','{listaDeParametros['Colonia']}','{listaDeParametros['Entre_Calles']}','{listaDeParametros['Telefono']}','{listaDeParametros['Beneficiario']}','{listaDeParametros['Observaciones']}','contratos_registrados/Individual_1.docx','{listaDeParametros['Domicilio2']}','{listaDeParametros['Correo']}','1,2','','','3','{listaDeParametros['latitud']}','{listaDeParametros['longitud']}','0','{listaDeParametros['Monto_Liquidado']}','{listaDeParametros['Saldo_Deudor']}','0','0','{listaDeParametros['Retrasos']}','{listaDeParametros['ultimo_pago']}','{listaDeParametros['pago_programado']}','0000-00-00','{listaDeParametros['idgrupo']}','{listaDeParametros['idvendedor']}','0','0','{listaDeParametros['idcolonia']}',0,0,'00:00:00','{listaDeParametros['precio_paquete']}','0','0','0','0000-00-00','0000-00-00','0000-00-00','{listaDeParametros['idpaquete_kit']}',0,'{listaDeParametros['idsucursal']}',0,1,1,1;"""

#            sql = f"""INSERT IGNORE INTO funeraria_contrato_individual SELECT '{listaDeParametros['idcontrato_individual']}','{listaDeParametros['Folio']}','{listaDeParametros['Estatus']}','{listaDeParametros['Paquete']}','{listaDeParametros['Estado']}','{listaDeParametros['Municipio']}','{listaDeParametros['Localidad']}','{listaDeParametros['Fecha']}','{listaDeParametros['precio']}','0','{listaDeParametros['pago_inicial']}','{listaDeParametros['Abonos_de']}','{listaDeParametros['Plan_de_Pago']}','0','','Sin Archivo','{listaDeParametros['idusuario']}','{listaDeParametros['Comision_Vendedor']}','{listaDeParametros['Comision_Lider']}','{listaDeParametros['Comision_Gerente']}','0','0','0','0','{listaDeParametros['Apellido_Paterno']}','{listaDeParametros['Apellido_Materno']}','{listaDeParametros['Nombre']}','0','2000-01-01','{listaDeParametros['IFE']}','{listaDeParametros['Domicilio']}','{listaDeParametros['Colonia']}','{listaDeParametros['Entre_Calles']}','{listaDeParametros['Telefono']}','{listaDeParametros['Beneficiario']}','{listaDeParametros['Observaciones']}','contratos_registrados/Individual_1.docx','{listaDeParametros['Domicilio2']}','{listaDeParametros['Correo']}','1,2','','','3','{listaDeParametros['latitud']}','{listaDeParametros['longitud']}','0','{listaDeParametros['Monto_Liquidado']}','{listaDeParametros['Saldo_Deudor']}','0','0','{listaDeParametros['Retrasos']}','{listaDeParametros['ultimo_pago']}','{listaDeParametros['pago_programado']}','0000-00-00','{listaDeParametros['idgrupo']}','{listaDeParametros['idvendedor']}','0','0','{listaDeParametros['idcolonia']}',0,0,'00:00:00','{listaDeParametros['precio_paquete']}','0','0','0','0000-00-00','0000-00-00','0000-00-00','{listaDeParametros['idpaquete_kit']}',0,'{listaDeParametros['idsucursal']}',0,1,1,1;"""
            print(sql)
            file.write(sql)
            file.write("\n")
            
print("numero de contratos",contador)
