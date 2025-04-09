
# Text analysis in Python

This project performs a text analysis by removing written accents,  punctuation marks and special characters. After that, it processes the content and show some information such as:


- Number of words.
- List of words without repetition.
- The largest word.
- How many times does the word appear?
 


## Requirements

To run this project , it is necessary to install Python 3.6 or later.

If you want to verify your Python version, you can use the following command:

```bash
  python --version
```



## Console execution

Navigate to the project folder in the command prompt and type the following command using the .txt file in the folder.

```bash
  python codigo.py texto.txt
```

This is going to read the content, clean it and display a dictionary with information about the text.

## pruebas.py execution

Inside the 'prueba' folder, there's a file called pruebas.py, which contains two example paragraphs.

Just by running the file, you can check that the program works correctly.




## Execution example

Runnig this command:
```bash
  python codigo.py texto.txt
```
The deployment will look something like this:

```python
{'Numero total de palabras': 10,
 'Palabra mas larga': 'teniendo',
 'Lista de palabras': ['hola', 'estas', 'teniendo', 'semana', ...],
 'Numero de apariciones': [['hola', 1], ['estas', 1], ...]}

```

