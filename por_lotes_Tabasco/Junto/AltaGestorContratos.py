import string
import random
from datetime import datetime
from logger_base import log

file1 = open('contratos.NubeUp','w')
length_of_string = 16
with open('ContratosSqlTratado.sqlZip') as querys:
    for contador,sql in enumerate(querys):
        sqlFinal=sql.replace("'","&#roro;")
        now = datetime.now()
        fechaFormateada = now.strftime('%Y-%m-%d %H:%M:%S')
        finalSql=sql.replace("'","&#roro;")
        reference = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
        nubeQuery = f"INSERT INTO `system_synchronization` (`id_log`, `Serie`, `iduser`, `idmodule`, `register`, `Type`, `Query`, `authorization`) VALUES ('{reference}', '228', '0', '194 ', '{fechaFormateada}', '0 ', '{finalSql}', '');"
        log.info(nubeQuery)
        file1.write(nubeQuery)
print(f'se realizaron {contador} querys')
print("la query quedo en: contratos.NubeUp")    