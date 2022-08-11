import menus as menu

mensaje="Menu archivo principal.py o p.y"
print(mensaje.center(len(mensaje)+30,"="))
menu.MenuArchivoPrincipal()
mensaje="Menu archivo movil.py o m.y"
print(mensaje.center(len(mensaje)+30,"="))
menu.MenuArchivoMovil()
mensaje="Menu archivo e.y"
print(mensaje.center(len(mensaje)+60,"="))
menu.MenuArchivoExtra()