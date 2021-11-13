# Dart Lexer
Analizador léxico y sintactico del lenguaje de programación Dart. Desarrollado en python con la librería PLY (https://www.dabeaz.com/ply/ply.html)

## Requisitos
* Descargar e instalar [python](https://www.python.org/downloads/)
* Instalar [PLY](https://pypi.org/project/ply/)
* Usar la [documentación](https://www.dabeaz.com/ply/ply.html) como guía

## Descripción
El analizador toma como entrada una cadena de caracteres los cuales son reconocidos como tokens en caso de haber sido declarados como token dentro del léxico. 

## Imagenes del lexer funcionando 
La siguiente imagen reconoce los tokens del siguiente fragmento de código:
```
void saludar (String saludo){ 
  print (saludo+ "hola"); 
}
```
![Lexer función](../Imagenes/Lexer función.jpeg)
