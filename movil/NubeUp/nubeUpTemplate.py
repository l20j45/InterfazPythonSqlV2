import string
import random
from datetime import datetime
from logger_base import log

file1 = open('template.txt','w')
length_of_string = 16

listaAcciones={"0":"INSERT", "1":"DELETE", "2":"UPDATE"}

print("menu".center(60,'=')+"""
191.- Administracion de Personal
192.- Localidades y Paquetes
193.- Administracion de Paquetes
194.- Agentes de Venta
195.- Personal de Cobranza
196.- Lista de Contratos
197.- Gerentes y Lideres
198.- Ventas y Comisiones
199.- Pago de Comisiones
200.- Control de Ganado
201.- Comisiones
202.- Administración de Acciones
203.- Reportes Personalizados
204.- Lista Cremaciones
205.- Administracion Doctores
206.- Administracion Funerarias
207.- Administracion Certificado Funerarias
208.- Servicios Funerarios
209.- Vehiculos Funerarios
210.- Cafeteria Funeraria
211.- Lugares Predeterminados
212.- Laboratorios Funeraria
213.- Mobiliario Funeraria
214.- Logistica Servicios Venta
215.- Logistica Administracion de Acciones
216.- Definicion de articulos
219.- Permisos Web """)
module=input("En donde haras las modificacion?: ")
log.debug(module)
print("Que accion realizaras".center(60,'=')+"""
0.-Insert
1.-Delete
2.-Update""")
opcion=input("Ingresa la opcion: ")
action=listaAcciones[opcion]
log.debug(action)
sql=input("Ingresa la query en una linea: ")
now = datetime.now()
fechaFormateada = now.strftime('%Y-%m-%d %H:%M:%S')
reference = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
nubeQuery = f"INSERT INTO `system_synchronization` (`id_log`, `Serie`, `iduser`, `idmodule`, `register`, `Type`, `Query`, `authorization`) VALUES ('{reference}', '22870050', '0', '{module} ', '{fechaFormateada}', '{action} ', '{sql}', '');"
log.info(nubeQuery)
file1.write(nubeQuery)