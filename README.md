
# Análisis de texto en python

Este proyecto hace un anáslis de un texto, eliminando tildes, signos y caracteres especiales, y luego procesa el contenido para mostrar información como:

- Numero total de palabras.
- Lista de palabras sin repetir.
- Palabra más larga.
- Frecuencia de aparición de cada palabra.
 


## Requisitos

Este proyecto requiere tener instalado Python 3.6 o superior.

Para verificar la versión, se puede usar el siguiente comando:

```bash
  python --version
```



## Uso desde la consola
Ajustar el directorio en el cmd e ingresar el siguiente comando, tomando el archivo .txt que se encuentra en la carpeta:

```bash
  python codigo.py texto.txt
```

Esto leerá el contenido del archivo, lo limpiará y mostrará un diccionario con información del texto.

## Uso desde pruebas.py
Dentro de la carpeta 'Prueba', se encuentra un archivo llamado pruebas.py, el cual contiene 2 ejemplos de párrafos.

Basta con correr dicho archivo para comprobar el funcionamiento del programa.





## Ejemplo de salida

Ejecutando el siguiente comando:
```bash
  python codigo.py texto.txt
```
Se obtendrá una salida como esta:

```python
{'Numero total de palabras': 10,
 'Palabra mas larga': 'teniendo',
 'Lista de palabras': ['hola', 'estas', 'teniendo', 'semana', ...],
 'Numero de apariciones': [['hola', 1], ['estas', 1], ...]}

```

