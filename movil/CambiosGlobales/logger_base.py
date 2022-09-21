import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('logs.log', mode ="w"),
                    log.FileHandler('logSinBorrar.log'),
                    log.StreamHandler()
                ]) #muestra todos
#log.basicConfig(level=log.INFO) #solo muestra de info abajo
#log.basicConfig(level=log.WARNING) #muestra de warning abajo
#log.basicConfig(level=log.ERROR) #muestra de error abajo


if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')