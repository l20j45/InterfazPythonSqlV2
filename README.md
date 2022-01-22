# InterfazPythonSql

Este es el readme del programa que uso para casi todo en la funeraria.

apartir de ahora voy a tratar de poner mejores practicas en mi programacion esta es una de ellas, estoy generando dos versiones, una para movil y otra para computadora, basicamennte es la misma pero sin el complemento de pyperclip

hasta ahora hace 4 funciones dividadas en argumentos que van a ser cambiados

**funciones**

- Funcion 1
  
  - Busqueda de folios, esto puede ser 
    - Folio unico ejemplo: 1
    - Folio por rango: 1-10

- Funcion 2
  
  - Busqueda de contratos por id
    - Actualemente solo se trae la cadena especial y el id, pero voy a hacer un cambio
    - [ x ] va a traerme tambien el estatus, la latitud y longitud, la ruta a la que pertenece

- Funcion 3
  
  - Aqui busca al persona por nombre, hice un cambio que metio un concat en el nombre pero voy a hacer otro cambio

- Funcion 4
  
  - Aqui lo que hace es buscar en el persona todos los folios que tenga activos, esto quiere decir folios que puedan ser utilizados y si los tiene muestra el folio y la cadena especial

- Funcion 5
  
  - Me cambia de base de datos la aplicacion, aunque este movimiento va a ser movido hacia otro archivo que seria la que solo maneje archivos referentes a la aplicacion, tales como las rutas, altas y modificacion de la base de datos

## RESTRUCTURACION

actualmente todo esta como argumentos lo cual hace comodo pero dificil para cualquier usarlo, lo hare solo con dos argumentos especiales para darle mas rapidos al entendimiento.

argumentos actuales\
`python principal.py 1`\
muestra por folio unico\
`python principal.py 1-10`\
muestra por serie de folios\
`python principal.py lpa 2`\
muestra el contrato por serie de contrato\
`python principal.py nombre apellido apellido`\
Busca por nombre de usuario\
`python principal.py nombre apellido apellido 3`\
muestra la busqueda cruzada por usuario\
`python principal.py mod`\
entra a modificar la base de datos de las aplicaciones moviles\

el plan es cambiar esto para que solo sea con dos argumentos y se especifique el ultimo argumenot lo que va a realizarse

## Estructura del codigo

Actualemente hay 4 archivos y se debe de leer de esta forma

- conexion.py
  
  - conexionlocal.py
    - este archivo contiene esta variante y se referia a la clase de donde se realiza la conexion con mysql, vienen varios argumentos de conexion, como nombre del host, puerto, usuario, contraseña y base de datos este seria el primero que se tiene que modificar

- menus.py
  
  - este archivo contiene los menus que se muestra en la aplicacion, tales como el menu inicial, los argumentos que se mandan segun las opciones, y como se imprimen los mensajes en los archivos

- p.py o principal.py
  
  - Este es el el archivo que ejecuta todo, con ello damos inicio al programa, es el unico que tiene punto de entrada, posteriormente tendra otro archivo llamado m.py - movil.py

- consultas.py
  
  - en este archivo se encuentran todas las consultas que se realizan en el programa, esto con el fin de darle una mejor forma y claridad al todo el codigo
