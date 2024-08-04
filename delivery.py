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
from funciones import *

#-----------------------------------------------
# Programa principal
#-----------------------------------------------

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

seleccion_menu() # Realiza la selección del menu según el nivel de usuario