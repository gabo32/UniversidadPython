from logger_base import log
from usuario import Usuario
from usuario_dao import UsuarioDAO

opcion = None
while opcion != 5:
    print('Opciones: ')
    print('1 listar usuarios')
    print('2 agregar usuario')
    print('3 modificar usuario')
    print('4 eliminar usuario')
    print('5 salir')

    opcion = int(input('Escribe tu opcion(1-5)'))

    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('EScribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info(f'Usuarios insertados {usuarios_insertados}')
    elif opcion == 3:
        id_usuario_var = int(input('Escribe el id del usuario a modficar: '))
        username_var = input('EScribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Escribe el id del usuario a modficar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')
    else:
        log.info('Salimnos de la aplicacion')
