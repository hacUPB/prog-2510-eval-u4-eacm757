#Funcion para que el usuario ingrese una ruta o la ruta actual
import os    #Para aceder a archivos y directorios del sistema operativo 
import csv   # Lee archivos csv (archivos separados por coma)
import matplotlib.pyplot as plt   #Para los grficos 

#----------------------------Funciones para texto------------------------
#Funcion para que el usuario ingrese una ruta o la ruta actual
def listar_archivos():
    ruta = input("Ingrese la ruta")
    if not ruta:           #si la ruta esta vacia o presiona enter, lo evalua como booleano 
        ruta = os.getcwd() #Toma la ruta actual
    try:
        archivos = os.listdir(ruta)   #Lista los archivos encontrados en esa carpeta 
        print("Archivos encontrados:")
        for archivo in archivos:
            print(archivo)
    except FileNotFoundError:         #Si la ruta no existe no marca el error 
        print("Ruta no válida.")

#Funcion para contar el numero de palabras y caracteres
def contar_palabras_y_caracteres(nombre_archivo):
    with open(nombre_archivo, "r", encoding= "utf-8") as archivo:  #with para que el archivo se cierre al final #uft-8 caracteres especiales(chat gpt)
        contenido = archivo.read()  #Lee todo el contenido del archivo 
       
        todos_caracteres = len(contenido) #incluye todo, espacios en blanco puntos
       
        palabras = contenido.split() #split divide por espacios en blanco los guarda el una lista
        palabritas = len(palabras) #cuenta las palabras de esa lista
        
        contenido = contenido.replace(" ", "")
        contenido = contenido.replace("\n", "")  #reeplaza los espacios en blanco y saltos, por nada
        sin_espacio = len(contenido)
        
        print(f"Numero de palabras: {palabritas}")
        print(f"Numero de caracteres con espcaio: {todos_caracteres}")
        print(f"Numero de caracteres sin espcaio: {sin_espacio}")

#Funcion para reemplazar palabras
def reemplazar_palabra(nombre_archivo): 
    palabra_areeplazar = input("Ingrese la palabra que quiere reemplazar:")
    palabra_nueva = input("Ingrese la nueva palabra:")  
    
    with open(nombre_archivo, "r", encoding= "utf-8") as archivo: # abrimos el archivo en modo lectura #with para que el archivo se cierre al final #uft-8 caracteres especiales(chat gpt)
        contenido = archivo.read()  #Lee todo el contenido del archivo y archivo se asigna como una variable
    contenido = contenido.replace(palabra_areeplazar, palabra_nueva) #reeplaza la palabra anterior por una nueva y actualiza el contenido, pero no lo guarda
    
    with open(nombre_archivo, "w", encoding= "utf-8") as archivo:
        archivo.write(contenido) #abrimos el archivo en modo escritura y le pasamos el contenido actualizado y lo guarda


#Funcion para contar las vocales
def histograma_vocales(nombre_archivo):
    with open(nombre_archivo, "r", encoding= "utf-8") as archivo:
        contenido = archivo.read()  #leemos el archivo y lo guardamos en un avariable 
        contenido = contenido.lower() #se pone todo el texto en minusculas

        conteo_a = 0 
        conteo_e = 0 
        conteo_i = 0    #contadores para cada vocal
        conteo_o = 0 
        conteo_u = 0 

        for vocal in contenido:  # Recorremos todo el contenido y cada que encuentre una vocal, suma al contador correspondiente
            if vocal == 'a':
                conteo_a += 1 
            elif vocal == 'e':
                conteo_e += 1 
            elif vocal == 'i':
                conteo_i += 1 
            elif vocal == 'o':
                conteo_o += 1 
            elif vocal == 'u':
                conteo_u += 1 

    vocales = ['A', 'E', 'I', 'O', 'U']
    cantidades = [conteo_a, conteo_e, conteo_i, conteo_o, conteo_u]  # asignamos los Ejes de la tabla
    
    plt.bar(vocales, cantidades, color='skyblue')
    plt.title('Conteo de Vocales')  #Agrege plt bar con chat gpt pq no se graficaba la tabla
    plt.xlabel('Vocal')   #eje x y y
    plt.ylabel('Cantidad')  
    plt.show()  #muestra la tabla
#--------------------------Fin funciones texto---------------------------

#-------------------------Funciones csv----------------------------------
#Funcion de csv para mostras las 15 primeras filas 
def mostrar_filas(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)   #lee cada linea del archivo separada por algun delimitador y crea una lista  
        cont = 0
        for fila in lector: #Cada linea del archivo, seria cada lista del lector
            if cont == 15:
                break
            print(fila)
            cont +=1    #correccion de logica con chat gpt  # sin return ya que las mostramos ahi mismo con print

#Funcion para calcular estadisticas, datos, promedio, mediana etc ######
def calcular_estadisticas(nombre_archivo, indice):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)  #lo combierte en listas para poder acceder a los indices el  ####signo menos al indice

#Funcion para graficar una columna con datos
def grafica(nombre_archivo):
    indice = input("Ingrese el indice de la columna a graficar:")
    indice -=1
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        
        datos = []  #Una lista donde se guardaran los datos
        for fila in lector:
            valor = float(fila[indice])  #serie de datos #accede al indice indicado por el usuario #convertimos el valor a flotante para  estadisticas
            datos.append(valor)  
    plt.plot(datos)      #Agrege plot con chat gpt #genera el grafico de lineas 
    plt.title("Gráfico de la columna")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.show() 
#-----------------------Fin funciones csv--------------------------------


#----------------------submenu para texto--------------------------------
def submenu_texto():
    archivo = input("Ingrese el nombre del archivo:")      #Se asigna el nombre al archivo
    if not archivo.endswith(".txt"):     #Con ayuda de chat gpt agregre la verficacion 
        archivo += ".txt"

    while True:  
        print("Submenu para archivos de .txt\n1. Contar numero de palabras y caracteres.\n2. Reemplazar una palabra por otra\n3. Histograma ocurrencia de vocales\n4. Salir")
       
        opcion = input("Seleccione la opcion a realizar:") 
        if opcion == "1":
            contar_palabras_y_caracteres(archivo)    #Se llama a la funcion y se la pasa el nombre del archivo "archivo"
        elif opcion == "2":
            reemplazar_palabra(archivo)
        elif opcion == "3":                            
            histograma_vocales(archivo)
        elif opcion == "4":
            print("Saliendo del programa")          
            break
        else:
            print("Opcion no valida, Intente de nuevo")
#----------------------Fin submenu para texto----------------------------

#----------------------Submenu para csv----------------------------------
def submenu_csv():
    archivo = input("Ingrese el nombre del archivo:")
    if not archivo.endswith(".csv"):    
        archivo += ".csv"
    
    while True:
        print("Submenu para archivos .csv\n1. Mostrar las primeras 15 filas del texto\n2. Calcular estadisticas\n3. Graficar una columna completa con datos\n4. Salir")
       
        opcion = input("Seleccione la opcion a realizar:") 
        if opcion == "1":
            mostrar_filas(archivo)
        elif opcion == "2":
            indice = input("Ingrese el indice de la columna a calcular:")
            indice -= 1  #Pq el indice cominenza en 0 
            calcular_estadisticas(archivo, indice)
        elif opcion == "3":                            
            grafica(archivo)
        elif opcion == "4":
            print("Saliendo del programa")        
            break
        else:
            print("Opcion no valida, Intente de nuevo")
#----------------------Fin submenu para csv------------------------------

#----------------------incio del programa--------------------------------
def main():
    while True:
        print("Menú Principal")
        print("1. Listar archivos en la ruta actual o ingresar uns ruta")
        print("2. Procesar archivo de texto .txt")
        print("3. Procesar archivo CSV .csv")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")    
          
        if opcion == "1" :
            listar_archivos() 
        elif opcion == "2":
            submenu_texto()
        elif opcion == "3":
            submenu_csv()
        elif opcion == "4":
            print("Programa finalizado.")
            break  
        else:
            print("Opción no valida. Intente de nuevo.")
#----------------------Fin del programa----------------------------------

if __name__ == "__main__":
    main()