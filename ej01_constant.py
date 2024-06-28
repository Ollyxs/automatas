#MENU
MENU = '''
    |---------------------------------------------------------------|
    |                Bienvenidos, elija una opcion                  |
    |                                                               |
    | 1. Listar todas las sesiones por ID                           |
    | 2. Listar los inicios de session en un periodo de tiempo      |
    | 3. Tiempo total de la sesion de un usuario                    |
    | 4. Mac de un usuario                                          |
    | 5. Listar usuarios conectados a una AP                        |
    | 6. Salir                                                      |
    |---------------------------------------------------------------|

    '''

#REGEX
#DATETIME_REGEX = ('''(0[1-9]|[12][0-9]|3[01])\/([1-9]|1[0-2])\/[12]\d{3} ([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]''')
#DATETIME_REGEX = r'\d{2}/\d{2}/\d{4}'
DATETIME_REGEX = r'^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d{4}$'


#PATHS
PATH_TXT = "usuarios.txt"
FULLPATH_TXT = r"/home/ollyxs/Documentos/GitHub/automatas/usuarios.txt"
PATH_XLSX = "usuarios.xlsx"
FULLPATH_XLSX = r"/home/ollyxs/Documentos/GitHub/automatas/files/usuarios.xlsx"
PATH_XLSX_USER = r"/home/ollyxs/Documentos/GitHub/automatas/files/UserSession.xlsx"
PATH_DATE_USR = r"/home/ollyxs/Documentos/GitHub/automatas/files/DateUser.xlsx"
PATH_MAC_USER = r"/home/ollyxs/Documentos/GitHub/automatas/files/MacUser.xlsx"
PATH_MAC_DT = r"/home/ollyxs/Documentos/GitHub/automatas/files/MacDatetime.xlsx"

#INPUTS
QUESTION_RET = "Volver a menu principal? (Y/N) "
INP_SHOW_DATA = "Ver informacion completa de las conexiones? (Y/N) "
UN_INP = "Nombre de Usuario: "
DATETIME_INPUT = "Ingrese la fecha, con el formato >>> DD/MM/YYYY: "
DATETIME_INPUT_1 = "Ingrese la fecha con este formato >>> DD/MM/YYYY: "
DATETIME_INPUT_2 = "Ingrese la fecha con este formato >>> DD/MM/YYYY: "
DATETIME_RANGE_INPUT = "Quiere usar un rango de tiempo para buscar? (Y/N) "
MAC_USER_INP = "Ingrese la MAC del Usuario para analizar: "
AP_INPUT = "Ingrese la MAC AP para buscar: "
SPECIFIC_DATE_INPUT = "Ingrese una fecha fija con este formato >>> DD/MM/YYYY :  "

#Mensajes
RETURN_MENU = "Menu principal"
SEARCHING_DATA = "Buscando"
LOADING_DATA = "Cargando"
LOAD_DATA = "Carga correcta"
CLIENT_ADDED = "Cliente añadido"
DELETE_DATA = "Datos Borrados"
CLIENT_ATTENDED = "Todos los clientes ya han sido atendidos"
USER_NOT_FOUND = "No existe el usuario"
MAC_NOT_FOUND = "No existe la MAC"
WRONG_DT_1 = "Valores ingresados en formato incorrecto"
WRONG_DT_2 = "Valores ingresados en formato incorrecto"
INSC_FALSE = "No puede inscribirse."
INSC_TRUE = "Inscripcion correcta"
NOT_INT_DNI = "Ingrese el digito entero"
INP_FB = "Opcion elegida: "
INFO_HELP = "Testeo"
VALIDATE_CHECKING = "Validando"
VALIDATE_CORRECT = "Datos validados"
DATETIME_RANGE_MSG = "Ingrese un rango de fechas"
DT_RANGE_MSG = "Setee un rango de fechas"
TO_EXCEL = "Para mas detalles, vea el excel"
CHECK_XLSX = "Para mas detalles, vea el excel 'Usuarios WiFi'"
NO_MATCH = "No hay coincidencias para los datos que esta buscando"
ERR = "Error"

#Operaciones de string
JUMP_LINE = "\n"

#Salida
EXIT = "Saliendo. Hasta Luego"
