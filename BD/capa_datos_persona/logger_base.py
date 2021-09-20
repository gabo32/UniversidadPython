import logging

# nombre mas corto
log = logging

# warning por defecto
log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje de info')
    log.warning('Mensaje de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje critito')
