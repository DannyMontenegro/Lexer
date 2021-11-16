import ply.yacc as yacc
from main import tokens

#Terminado
#Operadores Asignacion
#Operadores Comparacion
#Operadores aritmeticos
#Tipos de Datos
#Mapas
#Funciones(Faltan las arrow functions)

def p_funciones(p):
    '''funcion : tipoDato VARIABLE LPAREN parametros RPAREN LLAVEABRE bloque RETURN valores PUNTOCOMA LLAVECIERRA
                | VOID VARIABLE LPAREN parametros RPAREN LLAVEABRE bloque LLAVECIERRA
                | VOID VARIABLE LPAREN parametros RPAREN LLAVEABRE bloque RETURN PUNTOCOMA LLAVECIERRA'''

def p_parametros(p):
    '''parametros : tipoDato VARIABLE
                    | parametros COMA tipoDato VARIABLE
                    | empty'''

def p_bloque_codigo(p):
    '''bloque : expresion
                | bloque expresion
                | empty'''

def p_expresion(p):
    '''expresion : mapa PUNTOCOMA
                | mapaFunciones PUNTOCOMA
                | asignacion PUNTOCOMA'''

def p_import(p):
    '''import : IMPORT CADENA PUNTOCOMA'''

def p_asignacion(p):
    '''asignacion : VARIABLE operadores_asignacion valores
                     | tipoDato VARIABLE IGUAL valores
                     | VARIABLE IGUAL comparacion
                     | BOOL VARIABLE IGUAL comparacion
                     | VARIABLE operadores_asignacion operacion_aritmetica
                     | tipoDato VARIABLE IGUAL operacion_aritmetica
                     | empty'''

def p_operacion_aritmetica(p):
    '''operacion_aritmetica : valores operadores_aritmeticos valores
                            | operacion_aritmetica operadores_aritmeticos valores'''



def p_operadores_aritmeticos(p):
    '''operadores_aritmeticos : SUMA
                                | RESTA
                                | MULTIPLICACION
                                | DIVISION
                                | DIVENTERA
                                | RESIDUO'''

def p_operadores_asignacion(p):
    '''operadores_asignacion : IGUAL
                                | ASIGNACIONAUMENTADA
                                | ASIGNACIONDISMINUIDA'''

def p_comparacion(p):
    '''comparacion : valores comparador valores
                    | comparacion comparador valores '''

def p_comparador(p):
    '''comparador : MENORQUE
                    | MAYORQUE
                    | IGUALQUE
                    | DIFERENTEQUE'''


def p_mapa(p):
    '''mapa : MAP MENORQUE tipoDato COMA tipoDato MAYORQUE VARIABLE IGUAL creacionMapa
                | mapaFunciones'''

def p_mapa_funciones(p):
    '''mapaFunciones : mapa PUNTO VARIABLE LPAREN RPAREN
                    | mapa PUNTO VARIABLE LPAREN valores
                    | VARIABLE PUNTO VARIABLE LPAREN RPAREN
                    | VARIABLE PUNTO VARIABLE LPAREN valores RPAREN'''

def p_creacion_mapa(p):
    '''creacionMapa : LLAVEABRE paresClaveValor LLAVECIERRA
                        | VARIABLE'''

def p_pares_clave_valor(p):
    '''paresClaveValor : valores DOSPUNTOS valores
                        | paresClaveValor COMA valores DOSPUNTOS valores'''

def p_valores(p):
    '''valores : VARIABLE
                    | NUMERO
                    | CADENA
                    | booleano '''

def p_booleano(p):
    '''booleano : TRUE
                | FALSE'''

def p_tipo_dato(p):
    '''tipoDato : STRING
                | INT
                | BOOL
                | DOUBLE
                | DYNAMIC
                | VAR '''

def p_empty(p):
     'empty :'
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
 
 # Build the parser

parser = yacc.yacc()
flag= True
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(s)
    print(result)
    flag=False
