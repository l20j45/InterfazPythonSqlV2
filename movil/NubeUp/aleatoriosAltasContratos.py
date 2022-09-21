import string
import random
from datetime import datetime
from logger_base import log

listaValores=[]
listaMensajes=[]

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
print("0.-Tabasco: Matriz")
print("1.-Tabasco: TEAPA")
print("2.-Tabasco: PARAISO")
print("3.-Tabasco: VILLAHERMOSA")
print("4.-Tabasco: COMALCALCO")
print("5.-La paz: La paz")
print("6.-Sipref: ARANDAS")
print("7.-Sipref: AYOTLAN")
print("8.-Sipref: LA BARCA")
print("9.-Sipref: SAHUAYO")
print("10.-Sipref: TONALA")
print("11.-Sipref: LA PIEDAD MICHOACAN")
print("11.-Sipref: SAN JULIAN")
print("12.-Sipref: JACONA")
print("13.-Tequila: TEQUILA SEFI")
print("14.-Tequila: MAGDALENA")
print("15.-Tequila: TEQUILA BODEGA")
print("16.-Tequila: ETZATLAN")
print("17.-Ixtlan: IXTLAN")
print("18.-san jorge: SAN JORGE MATRIZ")
print("19.-Tequila: ETZATLAN")

'PMKYOY2EK0CHX','PMKYOYRYK0CHX','PMKYOZ3MK0CHX','PMKYOZRIK0CHX','PMKYP0DGK0CHX','QTR814B494X5AD','QVHX12JGR6W8BM','QVI2EIXSR6W8BM','QVI2PFY4R6W8BM','QVIQ9EBU1W9DEM4','1','2','3','4','PJRLAXBO1S07ZH6','PNUSFFYA1BUKEB9'

listaValores = IngresarValores()

file1 = open('AleatoriosAltasContratos.txt','w')
listaSucursalPrefijo=['CAR','VHS-T-','PAR','VHS','COM','Modif']
listaSucursalCodigo=['QWVIOTBYF2AZKT','S3OVUKO09KVTQO','S3OVUL3U9KVTQO','S3OVUL8K9KVTQO','S3OVUM349KVTQO','PM2S1QMO1WW8SPU','PMKYOY2EK0CHX','PMKYOYRYK0CHX','PMKYOZ3MK0CHX','PMKYOZRIK0CHX','PMKYP0DGK0CHX','QTR814B494X5AD','QVHX12JGR6W8BM','QVI2EIXSR6W8BM','QVI2PFY4R6W8BM','QVIQ9EBU1W9DEM4','1','2','3','4','PJRLAXBO1S07ZH6','PNUSFFYA1BUKEB9']
for x in range(listaValores[1]):
    status1 = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
    sucursal=listaSucursalCodigo[listaValores[0]]
    prefijo=listaSucursalPrefijo[listaValores[0]]
    prefijo=prefijo+str(listaValores[2]+x)
    if(listaValores[0]>4):
        mensaje=f"('{status1}', '{prefijo}', 0, 'limpio', 'limpio', 'limpio', 'limpio', '2022-03-01', 10.0000000000000, 0.0000000000000, 0.0000000000000, 100.0000000000000, 0, 0.0000000000000, '', 'Sin Archivo', 'S35UTKT61PMBXBH', 0.0000000000000, 0.0000000000000, 0.0000000000000, 0.0000000000000, '0', 0.0000000000000, '0', 'x', 'x', 'x', 0, '0000-00-00', 'XX', 'x', 'x', 'x', 'x', 'x', 'x', 'contratos_registrados/Individual_38412.docx', 'x', 'x', '1,6', '', '', 15, '', '', 0, 0.0000000000000, 10.0000000000000, 0, 0, 0, '0000-00-00', '0000-00-00', '0000-00-00', '{sucursal} ', 'S3LEH7M8XB1RSV', 'PM3LSDTY1WW8SPU', 'PM3LLTNGNZLFN5', 'QTNLH7G6NZLFN5', 10, 2, '00:00:00', 10.0000000000000, '0', '0', '0', '0000-00-00', '0000-00-00', '0000-00-00', 'PM2S85AK1WW8SPU', 0, '{sucursal}', 0, 1, 1, 1)"
    else:
        mensaje=f"('{status1} ','MODIF{prefijo} ','3','MODIF','MODIF','MODIF','MODIF','2022-01-01','1',0,0,'0','0',0,'','Sin Archivo','QWYI36BU9KVTQO',0,0,0,0,0,0,0,'x','x','x','0','0000-00-00','*','x','x','x','x','x','x','contratos_registrados/Individual_1.docx36','x','x','1','','','15','0','0','0','0','1','0','0','0','2022-2-10','2022-02-23','0000-00-00','{sucursal} ','QWYI36BU9KVTQO','0','0','QWYNRBIY9KVTQO',0,0,'00:00:00','1','0','0','0','0000-00-00','0000-00-00','0000-00-00','QWVIQDFYF2AZKT',0,'{sucursal} ',0,1,1,1)"     
    
    if x +1 == listaValores[1]:
        mensaje += ';'
    else :
        mensaje += ','
    listaMensajes.append(mensaje)
sqlPrefix=f'INSERT INTO `funeraria_contrato_individual` (`idcontrato_individual`, `Folio`, `Estatus`, `Paquete`, `Estado`, `Municipio`, `Localidad`, `Fecha`, `precio`, `promocion`, `pago_inicial`, `Abonos_de`, `Plan_de_Pago`, `limite_asignado`, `Funeraria_Procedencia`, `archivo_adjunto`, `idusuario`, `Comision_Vendedor`, `Comision_Lider`, `Comision_Gerente`, `Bono`, `Bono_Asignado`, `Inscripcion`, `Inscripcion_Asignado`, `Apellido_Paterno`, `Apellido_Materno`, `Nombre`, `Estado_Civil`, `Nacimiento`, `IFE`, `Domicilio`, `Colonia`, `Entre_Calles`, `Telefono`, `Beneficiario`, `Observaciones`, `archivo_contrato`, `Domicilio2`, `Correo`, `dia_cobro`, `firma1`, `firma2`, `plazo_entrega`, `latitud`, `longitud`, `Tipo_Cobranza`, `Monto_Liquidado`, `Saldo_Deudor`, `horario_cobro`, `Estado_Cobro`, `Retrasos`, `ultimo_pago`, `pago_programado`, `fecha_entrega`, `idgrupo`, `idvendedor`, `idlider`, `idgerente`, `idcolonia`, `edad`, `genero`, `hora_calle`, `precio_paquete`, `NumeroServicio`, `NumeroFactura`, `NumeroTitulo`, `Fecha_Cancelacion`, `Fecha_Pagado`, `Fecha_Utilizado`, `idpaquete_kit`, `deleted`, `idsucursal`, `pagos`, `tipo_comision_vendedor`, `tipo_comision_lider`, `tipo_comision_gerente`) VALUES '
finalSql=sqlPrefix+''.join(listaMensajes)
log.info(finalSql)

now = datetime.now()
fechaFormateada = now.strftime('%Y-%m-%d %H:%M:%S')
finalSqlFinal= finalSql.replace("'","&#roro;")
reference = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
sql3 = f"INSERT INTO `system_synchronization` (`id_log`, `Serie`, `iduser`, `idmodule`, `register`, `Type`, `Query`, `authorization`) VALUES ('{reference}', '22870050', '0', '196', '{fechaFormateada}', 'INSERT', '{finalSqlFinal}', '');"
log.info(sql3)
file1.write(sql3)