import ply.yacc as yacc
from main import tokens

#Terminado
#Operadores Asignacion
#Operadores Comparacion
#Operadores aritmeticos
#Tipos de Datos
#Mapas
#Funciones(Faltan las arrow functions)
#Parte de Miguel

# def p_bloque_codigo(p):
#     '''bloque : expresion
#                 | bloque expresion
#                 | empty
#                 | estructuras
#                 | bloque estructuras
#                 '''
# ####AQUI AÑADI ESTRUCTURAS PARA HACER PRUEBAS ^     <-------------
    
def p_funciones(p):
    '''funcion : tipoDato VARIABLE LPAREN parametros RPAREN LLAVEABRE       bloque RETURN valores PUNTOCOMA LLAVECIERRA
                | VOID VARIABLE LPAREN parametros RPAREN LLAVEABRE bloque LLAVECIERRA
                | VOID VARIABLE LPAREN parametros RPAREN LLAVEABRE bloque RETURN PUNTOCOMA LLAVECIERRA'''

def p_estructuras(p):
    ''' estructuras : estructuraFor
                    | estructuraWhile
                    | estructuraIf'''

def p_estructuraFor(p):
    ''' estructuraFor : FOR LPAREN asignacion PUNTOCOMA comparacion  PUNTOCOMA aumento RPAREN LLAVEABRE bloque LLAVECIERRA
    | estructuraWhile'''

def p_aumento(p):
    ''' aumento : VARIABLE IGUAL operacion_aritmetica
                | VARIABLE operadores_asignacion valores'''

def p_estructuraWhile(p):
    ''' estructuraWhile : WHILE LPAREN argumentoEstructura RPAREN LLAVEABRE bloque LLAVECIERRA
    '''

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
                | bloque expresiones'''

def p_expresiones(p):
    '''expresiones : asignacion PUNTOCOMA
                | mapa PUNTOCOMA
                | mapaFunciones PUNTOCOMA'''

def p_parametros(p):
    '''parametros : parametros COMA tipoDato VARIABLE
                    | tipoDato VARIABLE
                    | empty'''

def p_import(p):
    '''import : IMPORT CADENA PUNTOCOMA'''

def p_asignacion(p):
    '''asignacion : VARIABLE IGUAL valores
                     | tipoDato VARIABLE IGUAL valores
                     | VARIABLE IGUAL comparacion
                     | BOOL VARIABLE IGUAL comparacion
                     | tipoDato VARIABLE IGUAL operacion_aritmetica
                     | VARIABLE IGUAL operacion_aritmetica
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
                    | comparacion comparador valores '''

def p_comparador(p):
    '''comparador : MENORQUE
                    | MAYORQUE
                    | IGUALQUE
                    | DIFERENTEQUE'''


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
                | VARIABLE '''

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


#Estructuras if, for y while
#If
# def p_estructuras(p):
#     ''' estructuras : estructuraIf
#                     | estructuraWhile
#                     | estructuraFor'''







# def p_asignacionVacio(p):
#     ''' asignacionVacio : asignacion
#                     | empty'''

# def p_comparacionVacio(p):
#     ''' comparacionVacio : comparacion
#                          | booleano'''






def p_empty(p):
     'empty :'
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
