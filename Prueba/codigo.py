import re
import sys
from pprint import pprint

def quitar_tildes(texto):
    texto = texto.lower()
    # Se crea una tabla para reemplazar manualmente las tildes
    tildes = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
    texto = texto.translate(tildes)
    
    #Quita todo lo que no sean letras y espacios
    texto = re.sub(r'[^a-zñ\s]', '', texto)
    
    return texto



def procesar_texto(parrafo):
    lista = list()
    parrafo_limpio = quitar_tildes(parrafo)
    separa_texto = parrafo_limpio.split(" ")
    num_palabras = len(separa_texto)
    
    # Lista de palabras sin repetir
    lista_palabras = list(set(separa_texto))
    
    # Obtiene la palabra más larga del texto, ordenandolas por longitud
    separa_texto.sort(key = len)
    mas_larga = separa_texto[-1]
    
    # Cuenta apariciones por palabra usando un conjunto para evitar repeticiones
    for palabra in set(separa_texto):
        cuenta = separa_texto.count(palabra)
        lista.append([palabra, cuenta])
    
    
    diccionario = {
        'Numero total de palabras': num_palabras,
        'Lista de palabras': lista_palabras,
        'Palabra mas larga': mas_larga,
        'Numero de apariciones': lista
    }
    
    return diccionario


def archivoTXT(nombre_archivo):
    with open(nombre_archivo, encoding="UTF-8") as archivo:
        convierte_parrafo = archivo.read()
        eliminar_salto = convierte_parrafo.replace("\n", " ")
        print(f"Texto leído:\n{eliminar_salto}\n")
        resultado = procesar_texto(eliminar_salto)
        print("-----------------------------------------------------------------")
        pprint(resultado)
        print("-----------------------------------------------------------------")

if __name__ == "__main__":
    if len(sys.argv) > 1: # Verifica que se haya recibido un archivo como argumento
        archivoTXT(sys.argv[1])
    else:
        print("Falta el archivo .txt como argumento.")