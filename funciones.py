#------------------------------------------------------------------
# Programa de control de stock y entrega de productos
#------------------------------------------------------------------
#------------------------------------------------------------------
# Importar las Librerías que usamos:
#------------------------------------------------------------------
from colorama import init, Fore, Style #Librería para colorear 
init(autoreset=True)

import json # Librería para usar archivos con extension JSON
import sys # Librería utilizada para salir del proceso con el metodo exit
from getpass_asterisk.getpass_asterisk  import  getpass_asterisk # Librería utilizada para ocultar usuario y contraseña de ingreso con "*"

#-----------------------------------------------
# Función limpiar
#-----------------------------------------------
def limpiar():# Limpieza de pantalla
    print(); print(); print(); print()

#-----------------------------------------------
# Función de Usuarios 
#-----------------------------------------------
def crear_usuario():# Función que crea usuarios y los graba en el archivo usuario.json
    limpiar()
    usuarios = {}
    usuario = input(Fore.YELLOW + Style.BRIGHT + "Ingrese el nombre de usuario: ")
    contraseña = input(Fore.YELLOW + Style.BRIGHT + "Ingrese la contraseña: ")
    band = True
    while band:
        try:
            nivel = int(input(Fore.YELLOW + Style.BRIGHT + "Ingrese el nivel de acceso: " ))
            if nivel == 1 or nivel == 2 or nivel == 3:
                print(Fore.CYAN + Style.BRIGHT + "Usuario creado exitosamente.")
                nivel = str(nivel)
                band = False
                break
            else:
                print(Fore.RED + "El nivel de usuario debe ser entre 1 y 3")
                print(Fore.RED + "Ingrese el nivel correcto")
                    
        except:
            print(Fore.RED + Style.BRIGHT + "Debe ser un número entero entre 1 y 3...")
            print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")
        
# Creo el diccionario de los usuarios:

    usuarios = {
        "usuario"   : usuario,
        "password"  : contraseña,
        "nivel"     : nivel
    }

# Guardo los usuarios en una lista:

    listaDeUsuarios.append(usuarios)

# Guardo los datos en un archivo:

    lista = open("usuarios.json", "w") 
    json.dump(listaDeUsuarios, lista, indent=4)  
    lista.close()     

#-----------------------------------------------
# Función Ingreso al programa 
#-----------------------------------------------
def usuario():#Función dedicada a comparar y chequear si el usuario y contraseña ingresados es un usuario habilitado
    intentos = 3  # Número de intentos permitidos

    while intentos > 0:
# Solicitar nombre de usuario y contraseña
        usuario_i = getpass_asterisk(Fore.BLUE + Style.BRIGHT + "Ingrese el nombre de usuario: ")
        password_i = getpass_asterisk(Fore.BLUE + Style.BRIGHT + "Ingrese la contraseña: ")
        
# Buscar el usuario en el archivo JSON
        
        usuario_correcto = False
        for usuario in listaDeUsuarios:
            if usuario["usuario"] == usuario_i  and usuario["password"] == password_i:
                nivel = int(usuario["nivel"])
                print(Fore.CYAN + Style.BRIGHT + "Credenciales correctas. ¡Bienvenido!")
                usuario_correcto = True
                return nivel
        if usuario_correcto:
            break
        else:
            intentos = intentos - 1
            if intentos > 0:
                print(Fore.RED + f"Usuario o contraseña incorrectos. Le quedan {intentos} intentos.")
            else:
                print(Fore.RED + "Usuario o contraseña incorrectos. No le quedan más intentos.")
                sys.exit()

#-----------------------------------------------
# Función listar de productos
#-----------------------------------------------
def listar():# Función que tiene como finalidad realizar una lista de productos y caracteristias dados de alta
    limpiar()
    print(Fore.GREEN + Style.BRIGHT + "Lista de Productos.")
    print(Fore.GREEN + "="*55)
    print(Fore.GREEN + "| Código | Nombre del Producto  |  Talle   | Cantidad |")
    print(Fore.GREEN + "="*55)
    for producto in listaDeProductos:
        print(f"| {producto ['codigo']:6} ", end="")       
        print(f"| {producto ['nombre'][:20]:20} ", end="")  
        print(f"| {producto ['talle']:8} ", end="")
        print(f"| {producto ['cantidad']:8} |")
    print(Fore.GREEN + "="*55)

#-----------------------------------------------
# Chequeo si el código se repite 
#-----------------------------------------------
def validar_codigo(codigo):# Verifica si el código ingresado se repite
    respuesta = False
    for producto in listaDeProductos:
        if producto["codigo"]==codigo:
            respuesta = True
            break
    return respuesta

#-----------------------------------------------
# Función Modificación de Productos
#-----------------------------------------------
def editar():# Función utilizada para realizar cambios en los datos de los productos
# 1) Chequeamos si el código ingresado existe
    limpiar()
    while True:
        bandera = True
        while bandera:
            try:
                codigo = int(input(Fore.CYAN + Style.BRIGHT + "Ingrese el código del producto: "))
                bandera = False
            except:
                print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
                print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")

        if validar_codigo(codigo):
# Buscar los datos del producto
            for producto in listaDeProductos:
                if producto["codigo"] == codigo:
# 2) Mostramos los datos 
                    limpiar()
                    print("Nombre...........", producto["nombre"])
                    print("Talle............", producto["talle"])
                    print("Cantidad.........", producto["cantidad"])
# 3) Guardamos los datos en nuevas variables
                    a_nombre = producto["nombre"]
                    a_talle = producto["talle"]
                    a_cantidad = producto["cantidad"]
# 4) Pedimos ingresar los nuevos datos
                    limpiar()
                    print(Fore.CYAN + "Datos editados ( Presinar Enter si no se realizan cambios)")
                    nombre     = input("Nombre:............ ")
                    talle      = input("Talle:............. ")
                    cantidad   = input("Cantidad:.......... ")
# 5) Armamos un nuevo diccionario con los datos editados
                                
                    if len(nombre) == 0:
                        n_nombre = a_nombre
                    else:
                        n_nombre = nombre

                    if len(talle) == 0:
                        n_talle = a_talle
                    else:
                        n_talle = int(talle)

                    if len(cantidad) == 0:
                        n_cantidad = a_cantidad
                    else:
                        n_cantidad = int(cantidad)

# Creamos el diccionario con los datos del prducto editado:
                    producto = {
                        "codigo"   : codigo,
                        "nombre"   : n_nombre,
                        "talle"    : n_talle,
                        "cantidad" : n_cantidad
                        }

                    for id, editado in enumerate(listaDeProductos):  
                        if editado["codigo"] == codigo:
                            del listaDeProductos[id]
                                    
# Agregar el diccionario con cambios editados
                    listaDeProductos.append(producto)

# Actualizamos el archivo JSON
                    archivo = open("producto.json", "w") 
                    json.dump(listaDeProductos, archivo, indent=4) 
                    archivo.close()                     

                    return
        else:
            print(Fore.RED + "El código ingresado no existe.")
            opción = input(Fore.RED + "¿Desea probar con otro código? [s/n]")
            if opción.lower() == "n":
                return

#-----------------------------------------------
# Función Eliminar Productos
#-----------------------------------------------
def eliminar():# Función que elimina por completo un producto específico con todos sus campos
# 1) Chequeamos si el código ingresado existe
    limpiar()
    while True:
        flag = True
        while flag:
            try:
                codigo = int(input(Fore.CYAN + Style.BRIGHT + "Ingrese el código del producto: "))
                flag = False
            except:
                print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
                print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")
        if validar_codigo(codigo):
# Buscar los datos del producto
            for producto in listaDeProductos:
                if producto["codigo"] == codigo:
# 2) Mostramos los datos 
                    limpiar()
                    print("Nombre............", producto["nombre"])
                    print("Talle.............", producto["talle"])
                    print("Cantidad..........", producto["cantidad"])
                    limpiar()
                    opción = input(Fore.RED + "¿Estas seguro de eliminar el registro? [s/n]: ")
                    if opción.lower() == "s":
                        for id, editado in enumerate(listaDeProductos):  
                            if editado["codigo"] == codigo:
                                del listaDeProductos[id]
# Actualizamos el archivo JSON
                    archivo = open("producto.json", "w") 
                    json.dump(listaDeProductos, archivo, indent=4) 
                    archivo.close()                     
                    return
        else:
            print(Fore.RED + "El código ingresado no existe.")
            opcion = input(Fore.RED + "¿Desea probar con otro código? [s/n]")
            if opcion.lower() == "n":
                return
#-------------------------------------------------
# Función  Control de Stock (Entrega de Productos)
#------------------------------------------------- 
def stock():# Función que realiza el descuento del producto del stock entregando mercadería a empleados
    limpiar()
    while True:
        aux = True
        while aux:
            try:
                codigo = int(input(Fore.CYAN + Style.BRIGHT + "Ingrese el código del producto: "))
                aux = False
            except:
                print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
                print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")
        if validar_codigo(codigo):
            for producto in listaDeProductos:
                if producto["codigo"] == codigo:
                    print()
                    print("Nombre:  ", producto["nombre"])
                    print("Talle:   ", producto["talle"])
                    print("Cantidad disponible:", producto["cantidad"])
                    print()
                    aux_1 = True
                    while aux_1:
                        try:
                            cantidad_e = int(input(Fore.CYAN + Style.BRIGHT + "Cantidad del Producto a entregar: "))
                            aux_1 = False
                        except:
                            print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
                            print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")
                    if cantidad_e > producto["cantidad"]:
                        print(Fore.RED + "La cantidad a entregar es mayor que la cantidad disponible.")
                        continue

                    empleado_e = input(Fore.CYAN + Style.BRIGHT + "Nombre del empleado que se le entrega el producto: ")

# Crear el registro de entrega
                    reporte = {
                        "codigo"     : codigo,
                        "nombre"     : producto["nombre"],
                        "talle"      : producto["talle"],
                        "cantidad"   : cantidad_e,
                        "empleado_e" : empleado_e
                    }

# Guardar el registro de entrega en la lista de empleados
                    listaDeEmpleados.append(reporte)

# Actualizar la cantidad de stock en el producto
                    producto["cantidad"] -= cantidad_e

# Actualizar el archivo JSON de productos con la nueva cantidad
                    archivo = open("producto.json", "w") 
                    json.dump(listaDeProductos, archivo, indent=4)

# Guardar los datos en un archivo JSON de entregas
                    reporte =  open("entrega.json", "w") 
                    json.dump(listaDeEmpleados, reporte, indent=4)

                    print(Fore.GREEN + "Producto entregado exitosamente.")
                    return
        else:
            print(Fore.RED + "El código ingresado no existe.")
            eleccion = input(Fore.RED + "¿Desea intentar con otro código? [s/n]: ")
            if eleccion.lower() == "n":
                return
#-------------------------------------------------------
# Función Reporte de Control de Stock (Listar entregas)
#-------------------------------------------------------            
def reportes():# Realiza un listado detallando el producto y a que empleado fue entregado, quedando registrado en un archivo 
    limpiar()
    print(Fore.GREEN + Style.BRIGHT + "Lista de Productos Entregados.")
    print(Fore.GREEN + "="*78)
    print(Fore.GREEN + "| Código | Nombre del Producto  |  Talle   | Cantidad |  Nombre del Empleado |")
    print(Fore.GREEN + "="*78)
    for reporte in listaDeEmpleados:
        print(f"| {reporte ['codigo']:6} ", end="")       
        print(f"| {reporte ['nombre'][:20]:20} ", end="")  
        print(f"| {reporte ['talle']:8} ", end="")
        print(f"| {reporte ['cantidad']:8} ", end="")
        print(f"| {reporte ['empleado_e'][:20]:20} | ")
    print(Fore.GREEN + "="*78)

#-----------------------------------------------
# Función Alta de Productos
#-----------------------------------------------
def alta():# Función encargada de dar de alta a los productos que ingresan al stock
    limpiar()
    while True:
        auxiliar = True
        while auxiliar:
            try:
                codigo = int(input(Fore.CYAN + Style.BRIGHT + "Ingrese el código de producto: "))
                auxiliar = False
            except:
                print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
                print(Fore.RED + Style.BRIGHT + "Intente nuevamente!!!!!!!!!!")
        validar = validar_codigo(codigo)
        if validar == False:
            break
        else:
            print(Fore.YELLOW + "Ese código ya esta registrado. Ingrese el correcto....")

    nombre   = input(Fore.CYAN + Style.BRIGHT + "Nombre del Producto: ")
    auxiliar_2 = True
    while auxiliar_2:
        try:
            talle    = int(input(Fore.CYAN + Style.BRIGHT + "Talle del Producto: "))
            auxiliar_2 = False
        except:
            print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
            print(Fore.RED + Style.BRIGHT + "Intente nuevamente!!!!!!!!!!")
    auxiliar_3 = True
    while auxiliar_3:
        try:
            cantidad = int(input(Fore.CYAN + Style.BRIGHT + "Cantidad del Producto: "))
            auxiliar_3 = False
        except:
            print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
            print(Fore.RED + Style.BRIGHT + "Intente nuevamente!!!!!!!!!!")
        

# Creo el diccionario de los productos:

    producto = {
        "codigo"   : codigo,
        "nombre"   : nombre,
        "talle"    : talle,
        "cantidad" : cantidad
        }

# Guardo los productos en una lista:

    listaDeProductos.append(producto)

# Guardo los datos en un archivo:

    archivo = open("producto.json", "w") 
    json.dump(listaDeProductos, archivo, indent=4)  
    archivo.close()

#-----------------------------------------------
# Función para editar usuarios 
#-----------------------------------------------
def editar_usuario():# Se pueden realizar cambios a los datos del usuario, clave y nivel de acceso
# 1) Chequeamos si el usuario ingresado existe
    limpiar()
    while True:
        cambio_password = input(Fore.YELLOW + Style.BRIGHT + "Ingrese el usuario a editar: ")
# Buscar los datos del usuario
        for usuarios in listaDeUsuarios:
            if usuarios["usuario"] == cambio_password:
# 2) Mostramos los datos 
                limpiar()
                print("Usuario:................", usuarios["usuario"])
                print("Contraseña:.............", usuarios["password"])
                print("Nivel:..................", usuarios["nivel"])
# 3) Guardamos los datos en nuevas variables
                a_usuario  = usuarios["usuario"]
                a_password = usuarios["password"]
                a_nivel    = usuarios["nivel"]
# 4) Pedimos ingresar los nuevos datos
                limpiar()
                print(Fore.CYAN + "Datos editados ( Presinar Enter si no se realizan cambios)")
                usuario   = input("Usuario:............ ")
                password  = input("Contraseña:......... ")
                
                flags = True
                while flags:
                    try:
                        nivel = int(input("Nivel:.............. "))
                        if nivel == 1 or nivel == 2 or nivel == 3:
                            print(Fore.CYAN + Style.BRIGHT + "Usuario editado exitosamente.")
                            nivel = str(nivel)
                            flags = False
                            break
                        else:
                            print(Fore.RED + "El nivel de usuario debe ser entre 1 y 3")
                            print(Fore.RED + "Ingrese el nivel correcto")
                                
                    except:
                        print(Fore.RED + Style.BRIGHT + "Debe ser un número entero entre 1 y 3...")
                        print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")
        
# 5) Armamos un nuevo diccionario con los datos editados
                    
                if len(usuario) == 0:
                    n_usuario = a_usuario
                else:
                    n_usuario = usuario

                if len(password) == 0:
                    n_password = a_password
                else:
                    n_password = password

                if len(nivel) == 0:
                    n_nivel = a_nivel
                else:
                    n_nivel = nivel

# Creamos el diccionario con los datos del prducto editado:
                usuarios = {
                    "usuario"  : n_usuario,
                    "password" : n_password,
                    "nivel"    : n_nivel
                    }

                for ident, editados in enumerate(listaDeUsuarios):  
                    if editados["usuario"] == cambio_password:
                        del listaDeUsuarios[ident]
                                
# Agregar el diccionario con cambios editados
                listaDeUsuarios.append(usuarios)

# Actualizamos el archivo JSON
                a = open("usuarios.json", "w") 
                json.dump(listaDeUsuarios, a, indent=4) 
                a.close()                     
                return
        else:
            print(Fore.RED + "El usuario ingresado no existe.")
            seleccion = input(Fore.RED + "¿Desea probar con otro usuario? [s/n]")
            if seleccion.lower() == "n":
                return

#-----------------------------------------------
# Función Eliminar Usuario
#-----------------------------------------------
def eliminar_usuario():# Elimina del registro al usuario completo
# 1) Chequeamos si el usuario ingresado existe
    limpiar()
    while True:
        cambio_password = input(Fore.CYAN + Style.BRIGHT + "Usuario a eliminar: ")
# Buscar los datos del producto
        for usuarios in listaDeUsuarios:
            if usuarios["usuario"] == cambio_password:
# 2) Mostramos los datos 
                limpiar()
                print("Usuario................", usuarios["usuario"])
                print("Contraseña.............", usuarios["password"])
                print("Nivel..................", usuarios["nivel"])
                opción = input(Fore.RED + Style.BRIGHT + "¿Estas seguro de eliminar el usuario? [s/n]: ")
                if opción.lower() == "s":
                    for ident, editados in enumerate(listaDeUsuarios):  
                        if editados["usuario"] == cambio_password:
                            del listaDeUsuarios[ident]
                            
# Actualizamos el archivo JSON
                a = open("usuarios.json", "w") 
                json.dump(listaDeUsuarios, a, indent=4) 
                a.close()                     
                return
        else:
            print(Fore.RED + "El usuario ingresado no existe.")
            seleccion = input(Fore.RED + "¿Desea probar con otro usuario? [s/n]")
            if seleccion.lower() == "n":
                return

#-----------------------------------------------
# Función para detectar el nivel de usuario 
#-----------------------------------------------
def nivel_acceso_usuario():# Realiza una comparación para determinar el nivel de control del usuario
    nivel_i = usuario()# Compara con la devolución del usuario y contraseña correctos ingresados
    for elemento in listaDeUsuarios:
        if int(elemento["nivel"] == "1") and nivel_i == 1 :
            nivel_usuario = 1
        elif int(elemento["nivel"] == "2") and nivel_i == 2 :
            nivel_usuario = 2
        elif int(elemento["nivel"] == "3") and nivel_i == 3 :
            nivel_usuario = 3
    return nivel_usuario
#------------------------------------------------------------
# Función para seleccionar el menu según el nivel de usuario
#------------------------------------------------------------

def seleccion_menu():# Dependiendo del nivel de usuario muestra el menu correspondiente
    nivel_usuario = nivel_acceso_usuario()
    if nivel_usuario == 3:
        print(Fore.CYAN + Style.BRIGHT + "Ud. posee nivel de acceso 3")
        menu()
    elif nivel_usuario == 2:
        print(Fore.CYAN + Style.BRIGHT + "Ud. posee nivel de acceso 2")
        menu_2()
    elif nivel_usuario == 1:
        print(Fore.CYAN + Style.BRIGHT + "Ud. posee nivel de acceso 1")
        menu_1()

#-----------------------------------------------
# Función encabezado
#-----------------------------------------------
def encabezado(): # Imprime el encabezado del programa
    print(Fore.BLUE + Style.BRIGHT + "="*55)
    titulo = "Bienvenido al Programa de Stock!!!!"
    print(Fore.CYAN + Style.BRIGHT + titulo.center(55))
    print(Fore.BLUE + Style.BRIGHT + "="*55)

#-----------------------------------------------
# Menu Nivel 1 
#-----------------------------------------------
def menu_1():# Menu de usuario nivel 1
    encabezado()
    while True:
        print(Fore.BLUE+Style.BRIGHT + "="*55)
        print(Fore.BLUE + "1) Listar productos")
        print(Fore.BLUE + "2) Entregar productos")
        print(Fore.BLUE + "3) Listar entregas")
        print(Fore.BLUE + "4) Salir")
        print(Fore.BLUE + Style.BRIGHT + "="*55)
        opción = input (Fore.CYAN + "Seleccione una opción del 1..4: ")

# Analizar la respuesta del usuario

        match opción:
            case "1"  : # Listar
                listar()
            case "2"  : # Entrega productos por Empleados (Control Stock)
                stock()
            case "3"  : # Listar productos por Empleados
                reportes()
            case "4"  : # Salir
                print("Salió del programa!!!!")
                sys.exit()

#-----------------------------------------------
# Menu Nivel 2
#-----------------------------------------------
def menu_2():# Menu de usuario nivel 2
    encabezado()
    while True:
        print(Fore.BLUE + Style.BRIGHT + "="*55)
        print(Fore.BLUE + "1) Alta productos")
        print(Fore.BLUE + "2) Editar productos")
        print(Fore.BLUE + "3) Listar productos")
        print(Fore.BLUE + "4) Entregar productos")
        print(Fore.BLUE + "5) Listar entregas")
        print(Fore.BLUE + "6) Salir")
        print(Fore.BLUE + Style.BRIGHT + "="*55)
        opción = input (Fore.CYAN + "Seleccione una opción del 1..6: ")

# Analizar la respuesta del usuario

        match opción:
            case "1"  : # Alta
                alta()
            case "2"  : # Editar
                editar()
            case "3"  : # Listar
                listar()
            case "4"  : # Entrega productos por Empleados (Control Stock)
                stock()
            case "5"  :# Listar productos por Empleados (Reporte 2)
                reportes()
            case "6"  :# Salir
                print("Salió del programa!!!!")
                sys.exit()                        
#-----------------------------------------------
# Menu Nivel 3
#-----------------------------------------------
def menu():# Menu de usuario nivel 3
    encabezado()
    while True:
        print(Fore.BLUE + Style.BRIGHT + "="*55)
        print(Fore.BLUE + "1) Alta productos")
        print(Fore.BLUE + "2) Editar productos")
        print(Fore.BLUE + "3) Listar productos")
        print(Fore.BLUE + "4) Eliminar productos")
        print(Fore.BLUE + "5) Entregar productos")
        print(Fore.BLUE + "6) Listar entregas")
        print(Fore.BLUE + "7) Crear Usuarios")
        print(Fore.BLUE + "8) Editar Usuarios")
        print(Fore.BLUE + "9) Eliminar Usuarios")
        print(Fore.BLUE +"10) Salir")
        print(Fore.BLUE + Style.BRIGHT + "="*55)
        opción = input (Fore.CYAN + "Seleccione una opción del 1..10: ")

# Analizar la respuesta del usuario

        match opción:
            case "1"  : # Alta
                alta()
            case "2"  : # Editar
                editar()
            case "3"  : # Listar
                listar()
            case "4"  : # Eliminar
                eliminar()
            case "5"  : # Entrega productos por Empleados (Control Stock)
                stock()
            case "6"  : # Listar productos por Empleados (Reporte 2)
                reportes()
            case "7"  : # Crea usuarios nuevos
                crear_usuario()
            case "8"  : # Edición de usuarios existentes
                editar_usuario()
            case "9"  : # Eliminar usuarios del registro
                eliminar_usuario()
            case "10"  : # Salir
                print("Salió del programa!!!!")
                sys.exit()

try: 
    archivo = open("producto.json", "r")
    listaDeProductos = json.load(archivo)
    archivo.close()
    reporte = open("entrega.json", "r")
    listaDeEmpleados = json.load(reporte)
    reporte.close()
    lista = open("usuarios.json", "r") 
    listaDeUsuarios = json.load(lista)  
    lista.close()
except:
    listaDeProductos = []
    listaDeEmpleados = []
    listaDeUsuarios  = []
    codigo = 1