import string
import random

listaValores=[]

def IngresarValores():
    opcion=int(input("ingresa la sucursal: "))
    numerodeContratos=int(input("cuantos contratos quieres: "))
    inicio=int(input("ingresa desde que numero necesitas: "))
    listaValores.append(opcion)
    listaValores.append(numerodeContratos)
    listaValores.append(inicio)
    return listaValores


length_of_string = 16
print("que sucursal necesitas")
print("Tabasco")
print("0.- Matriz")
print("1.- TEAPA")
print("2.- PARAISO")
print("3.- VILLAHERMOSA")
print("4.- COMALCALCO")
print("La paz")
print("5.- La paz")

listaValores = IngresarValores()

file1 = open('AleatoriosAltasContratos.txt','w')
listaSucursalPrefijo=['CAR','VHS-T-','PAR','VHS','COM','Modif']
listaSucursalCodigo=['QWVIOTBYF2AZKT','S3OVUKO09KVTQO','S3OVUL3U9KVTQO','S3OVUL8K9KVTQO','S3OVUM349KVTQO','PM2S1QMO1WW8SPU']
for x in range(listaValores[1]):
    status1 = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
    sucursal=listaSucursalCodigo[listaValores[0]]
    prefijo=listaSucursalPrefijo[listaValores[0]]
    prefijo=prefijo+str(listaValores[2]+x)
    if(listaValores[0]==5):
        sentenciaSql=f"INSERT INTO `funeraria_contrato_individual` (`idcontrato_individual`, `Folio`, `Estatus`, `Paquete`, `Estado`, `Municipio`, `Localidad`, `Fecha`, `precio`, `promocion`, `pago_inicial`, `Abonos_de`, `Plan_de_Pago`, `limite_asignado`, `Funeraria_Procedencia`, `archivo_adjunto`, `idusuario`, `Comision_Vendedor`, `Comision_Lider`, `Comision_Gerente`, `Bono`, `Bono_Asignado`, `Inscripcion`, `Inscripcion_Asignado`, `Apellido_Paterno`, `Apellido_Materno`, `Nombre`, `Estado_Civil`, `Nacimiento`, `IFE`, `Domicilio`, `Colonia`, `Entre_Calles`, `Telefono`, `Beneficiario`, `Observaciones`, `archivo_contrato`, `Domicilio2`, `Correo`, `dia_cobro`, `firma1`, `firma2`, `plazo_entrega`, `latitud`, `longitud`, `Tipo_Cobranza`, `Monto_Liquidado`, `Saldo_Deudor`, `horario_cobro`, `Estado_Cobro`, `Retrasos`, `ultimo_pago`, `pago_programado`, `fecha_entrega`, `idgrupo`, `idvendedor`, `idlider`, `idgerente`, `idcolonia`, `edad`, `genero`, `hora_calle`, `precio_paquete`, `NumeroServicio`, `NumeroFactura`, `NumeroTitulo`, `Fecha_Cancelacion`, `Fecha_Pagado`, `Fecha_Utilizado`, `idpaquete_kit`, `deleted`, `idsucursal`, `pagos`, `tipo_comision_vendedor`, `tipo_comision_lider`, `tipo_comision_gerente`) VALUES ('{status1}', '{prefijo}', 0, 'limpio', 'limpio', 'limpio', 'limpio', '2022-03-01', 10.0000000000000, 0.0000000000000, 0.0000000000000, 100.0000000000000, 0, 0.0000000000000, '', 'Sin Archivo', 'S35UTKT61PMBXBH', 0.0000000000000, 0.0000000000000, 0.0000000000000, 0.0000000000000, '0', 0.0000000000000, '0', 'x', 'x', 'x', 0, '0000-00-00', 'XX', 'x', 'x', 'x', 'x', 'x', 'x', 'contratos_registrados/Individual_38412.docx', 'x', 'x', '1,6', '', '', 15, '', '', 0, 0.0000000000000, 10.0000000000000, 0, 0, 0, '0000-00-00', '0000-00-00', '0000-00-00', 'PM2S1LLK1WW8SPU', 'S3LEH7M8XB1RSV', 'PM3LSDTY1WW8SPU', 'PM3LLTNGNZLFN5', 'QTNLH7G6NZLFN5', 10, 2, '00:00:00', 10.0000000000000, '0', '0', '0', '0000-00-00', '0000-00-00', '0000-00-00', 'PM2S85AK1WW8SPU', 0, '{sucursal}', 0, 1, 1, 1);"
    else:
        sentenciaSql=f"INSERT INTO funeraria_contrato_individual SELECT '{status1} ','MODIF{prefijo} ','3','MODIF','MODIF','MODIF','MODIF','2022-01-01','1',0,0,'0','0',0,'','Sin Archivo','QWYI36BU9KVTQO',0,0,0,0,0,0,0,'x','x','x','0','0000-00-00','*','x','x','x','x','x','x','contratos_registrados/Individual_1.docx36','x','x','1','','','15','0','0','0','0','1','0','0','0','2022-2-10','2022-02-23','0000-00-00','QWVIOS88F2AZKT','QWYI36BU9KVTQO','0','0','QWYNRBIY9KVTQO',0,0,'00:00:00','1','0','0','0','0000-00-00','0000-00-00','0000-00-00','QWVIQDFYF2AZKT',0,'{sucursal} ',0,1,1,1;"     
    print(sentenciaSql)
    file1.write(str(sentenciaSql))
    file1.write("\n")
