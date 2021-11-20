import ply.yacc as yacc
from main import tokens

# def p_bloque_codigo(p):
#     '''bloque : expresion
#                 | bloque expresion
#                 | empty
#                 | estructuras
#                 | bloque estructuras
#                 '''


def p_estructuraWhile(p):
    ''' estructuraWhile : WHILE LPAREN argumentoEstructura RPAREN LLAVEABRE bloque LLAVECIERRA
                        | list'''

def p_estructuraFor(p):
    ''' estructuraFor : FOR LPAREN asignacion PUNTOCOMA comparacion  PUNTOCOMA aumento RPAREN LLAVEABRE bloque LLAVECIERRA'''

def p_funciones(p):
    '''funcion : tipoDato VARIABLE LPAREN parametros RPAREN LLAVEABRE       bloque RETURN valores PUNTOCOMA LLAVECIERRA
                | VOID VARIABLE LPAREN parametros RPAREN LLAVEABRE bloque LLAVECIERRA
                | VOID VARIABLE LPAREN parametros RPAREN LLAVEABRE bloque RETURN PUNTOCOMA LLAVECIERRA'''
def p_funcionFlecha(p):
    ''' funcionFlecha : tipoDato VARIABLE LPAREN parametros RPAREN FLECHA expresiones'''

def p_llamadaFunciones(p):
    ''' llamadaFunciones : VARIABLE PUNTO VARIABLE LPAREN parametrosLlamada RPAREN
                         | VARIABLE LPAREN parametrosLlamada RPAREN '''

def p_parametrosLlamada(p):
    ''' parametrosLlamada : parametrosFuncion
                          | empty'''

def p_parametrosFuncion(p):
    ''' parametrosFuncion : valores
                          | parametrosFuncion COMA valores
                          '''
def p_parametros(p):
    '''parametros : tipoDato VARIABLE
                    | REQUIRED tipoDato VARIABLE
                    | parametros COMA tipoDato VARIABLE
                    | empty'''

def p_estructuras(p):
    ''' estructuras : estructuraFor
                    | estructuraWhile
                    | estructuraIf'''

def p_aumento(p):
    ''' aumento : VARIABLE IGUAL operacion_aritmetica
                | VARIABLE operadores_asignacion valores'''

def p_estructuraIf(p):
    ''' estructuraIf : IF LPAREN argumentoEstructura  RPAREN LLAVEABRE bloque LLAVECIERRA
                    | estructuraIfElse'''

def p_estructuraIfElse(p):
    '''  estructuraIfElse : estructuraIf ELSE LLAVEABRE bloque LLAVECIERRA'''

def p_argumentoEstructura(p):
    ''' argumentoEstructura : VARIABLE
                           | booleano
                           | comparacion'''

def p_bloque(p):
    '''bloque : expresiones
                | bloque expresiones
                | empty'''

def p_expresiones(p):
    '''expresiones : asignacion PUNTOCOMA
                | mapa PUNTOCOMA
                | mapaFunciones PUNTOCOMA
                | setFunciones PUNTOCOMA
                | print
                | readPant
                | set'''


def p_expresion(p):
    '''expresion : mapa PUNTOCOMA
                | mapaFunciones PUNTOCOMA
                | setFunciones PUNTOCOMA
                | asignacion PUNTOCOMA
                | import
                | export'''

def p_parametros(p):
    '''parametros : parametros COMA tipoDato VARIABLE
                    | tipoDato VARIABLE
                    | empty'''


def p_import(p):
    '''import : IMPORT CADENA PUNTOCOMA'''

def p_export(p):
    ''' export : EXPORT CADENA PUNTOCOMA'''

def p_asignacion(p):
    '''asignacion : VARIABLE IGUAL valores
                     | tipoDato VARIABLE IGUAL valores
                     | VARIABLE IGUAL comparacion
                     | BOOL VARIABLE IGUAL comparacion
                     | tipoDato VARIABLE IGUAL operacion_aritmetica
                     | VARIABLE IGUAL operacion_aritmetica
                     | VARIABLE ASIGNACIONAUMENTADA valores
                     | VARIABLE ASIGNACIONDISMINUIDA valores
                     '''

def p_operadores_asignacion(p):
    '''operadores_asignacion : IGUAL
                             | ASIGNACIONAUMENTADA
                             | ASIGNACIONDISMINUIDA'''

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



def p_comparacion(p):
    '''comparacion : valores comparador valores
                    | comparacion comparador valores
                    | valores IS tipoDato'''

def p_comparador(p):
    '''comparador : MENORQUE
                    | MAYORQUE
                    | IGUALQUE
                    | DIFERENTEQUE'''

def p_set(p):
    ''' set : SET MENORQUE tipoDato MAYORQUE VARIABLE IGUAL creacionSet
            | VAR VARIABLE IGUAL creacionSet
            | SET MENORQUE tipoDato MAYORQUE VARIABLE IGUAL LLAVEABRE collecionObjetos LLAVECIERRA'''
def p_list(p):
    ''' list : LIST MENORQUE tipoDato MAYORQUE VARIABLE IGUAL CORCHETEABRE collecionObjetos CORCHETECIERRA
             | LIST MENORQUE tipoDato MAYORQUE VARIABLE IGUAL LIST PUNTO VARIABLE LPAREN NUMERO COMA valores RPAREN '''

def p_coleccionObj(p):
    ''' collecionObjetos : valores
                         | valores COMA collecionObjetos
                         | empty
                         '''
def p_creacionSet(p):
    ''' creacionSet : SET LPAREN RPAREN'''

def p_setFunciones(p):
    ''' setFunciones : VARIABLE PUNTO ADD LPAREN valores RPAREN
                     | VARIABLE PUNTO JOIN LPAREN CADENA RPAREN'''


def p_mapa(p):
    '''mapa : MAP MENORQUE tipoDato COMA tipoDato MAYORQUE VARIABLE IGUAL      creacionMapa'''

def p_mapa_funciones(p):
    '''mapaFunciones : VARIABLE PUNTO VARIABLE LPAREN RPAREN
                    | VARIABLE PUNTO VARIABLE LPAREN valores RPAREN'''

def p_creacion_mapa(p):
    '''creacionMapa : LLAVEABRE paresClaveValor LLAVECIERRA
                        | VARIABLE'''

def p_pares_clave_valor(p):
    '''paresClaveValor : valores DOSPUNTOS valores
                        | paresClaveValor COMA valores DOSPUNTOS valores'''

def p_valores(p):
    '''valores : NUMERO
                | CADENA
                | booleano
                | VARIABLE
                | llamadaFunciones
                '''

def p_booleano(p):
    '''booleano : TRUE
                | FALSE'''

def p_tipo_dato(p):
    '''tipoDato : STRING
                | INT
                | BOOL
                | DOUBLE
                | DYNAMIC
                | VAR
                | nulValue
                '''

def p_empty(p):
     'empty :'

def p_nullValue(p):
    'nulValue : NULL'

def p_print(p):
    ''' print : PRINT LPAREN valores RPAREN'''

def p_readPant(p):
    ''' readPant : STRING VARIABLE IGUAL STDIN PUNTO READLINE LPAREN RPAREN PUNTOCOMA'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
#Termia parte de Miguel
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
