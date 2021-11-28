import ply.yacc as yacc
from main import tokens

#Regla semántica Danny
variables = []
funciones = []


def verificarvariable( variable):
    if variable not in variables:
        print("La variable " + variable + " esta siendo utilizada, pero no ha sido declarada")

def verificarFunciones(funcion):
    if funcion in funciones:
        print("La función "+ funcion +" ya ha sido declarada previamente")
    else:
        funciones.append(funcion)


errors = []

# Regla Dart: aportación de los 3          
def p_dart(p):
    '''dart : import funcion main
            | import main funcion
            | import funcion main funcion'''
#Terminada regla Dart

def p_dart_error(p):
    '''dart : import funcion'''
    print("Error: Falta creacion de funcion main en el archivo")
    errors.append("Error: Falta creacion de funcion main en el archivo")

#Aportación de Danny
def p_main(p):
    '''main : VOID MAIN LPAREN RPAREN LLAVEABRE bloque LLAVECIERRA'''

#Aportación de Miguel
def p_bloque(p):
    '''bloque : expresion
               | bloque expresion
               | empty'''

# Regla expresion: aportación de los 3 
def p_expresion(p):
    '''expresion : estructurasDato PUNTOCOMA
                | estructurasFunciones PUNTOCOMA
                | asignacion PUNTOCOMA
                | llamadaFunciones PUNTOCOMA
                | estructurasControl
                | entradaSalidaDatos PUNTOCOMA
                | funcionFlecha PUNTOCOMA'''

# Aportación de Raul
def p_entradaSalidaDatos(p):
    ''' entradaSalidaDatos : print
                           | readPant'''

#Aportación de Danny
def p_estructuraWhile(p):
    ''' estructuraWhile : WHILE LPAREN argumentoEstructura RPAREN LLAVEABRE bloque LLAVECIERRA
                        '''

#Aportación de Danny
def p_estructuraFor(p):
    ''' estructuraFor : FOR LPAREN asignacion PUNTOCOMA comparacion  PUNTOCOMA aumento RPAREN LLAVEABRE bloque LLAVECIERRA'''

def p_estructuraFor_error(p):
    ''' estructuraFor : FOR LPAREN asignacion error comparacion  PUNTOCOMA aumento RPAREN LLAVEABRE bloque LLAVECIERRA
                      | FOR LPAREN asignacion error comparacion  error aumento RPAREN LLAVEABRE bloque LLAVECIERRA
                      | FOR LPAREN asignacion PUNTOCOMA comparacion  error aumento RPAREN LLAVEABRE bloque LLAVECIERRA'''
    print("Error: Los argumentos de la estructura for deben estar separados por ';' Linea"+str(p.lineno(1)))              
    errors.append("Error: Los argumentos de la estructura for deben estar separados por ';' Línea:"+str(p.lineno(1)))

#Aportación de Miguel
def p_funciones(p):
    '''funcion : tipoDato VARIABLE LPAREN parametros RPAREN LLAVEABRE  bloque RETURN valoresRetorno LLAVECIERRA
                | VOID VARIABLE LPAREN parametros RPAREN LLAVEABRE bloque LLAVECIERRA
                | empty
                | funcion funcion'''
    if(len(p)>3):
        verificarFunciones(p[2])

#Aportación de Miguel
def p_parametrosFuncion(p):
    ''' parametrosFuncion : valores
                          | parametrosFuncion COMA valores
                          '''


#Aportación de Danny
def p_valoresRetorno(p):
    ''' valoresRetorno : valores
                       | VARIABLE IGUAL valores
                       | VARIABLE operadores_asignacion NUMERO
                       | VARIABLE IGUAL operacion_aritmetica
                       | operacion_aritmetica'''
#Aportación de Danny
def p_funcionFlecha(p):
    ''' funcionFlecha : tipoDato VARIABLE LPAREN parametros RPAREN FLECHA expresion'''

#Aportación de los 3
def p_llamadaFunciones(p):
    ''' llamadaFunciones : VARIABLE PUNTO VARIABLE LPAREN parametrosLlamada RPAREN
                         | VARIABLE LPAREN parametrosLlamada RPAREN '''
    # Regla semántica Danny
    if(p[2]=='.'):
        verificarvariable(p[1])
    #if(len(p)==5):
        #funciones_llamadas[p[1]] = 0


#Aportación de Danny
def p_parametrosLlamada(p):
    ''' parametrosLlamada : parametrosFuncion
                          | empty'''



#Aportación de Danny
def p_estructurasControl(p):
    ''' estructurasControl : estructuraFor
                    | estructuraWhile
                    | estructuraIf
                    | estructuraIfElse'''
#Aportación de Miguel
def p_aumento(p):
    ''' aumento : VARIABLE IGUAL operacion_aritmetica
                | VARIABLE operadores_asignacion valores'''
    #Regla semántica Danny
    verificarvariable(p[1])

#Aportación de Danny
def p_estructuraIf(p):
    ''' estructuraIf : IF LPAREN argumentoEstructura  RPAREN LLAVEABRE bloque LLAVECIERRA
                    | estructuraIfElse'''
#Aportación de Danny
def p_estructuraIfElse(p):
    '''  estructuraIfElse : estructuraIf ELSE LLAVEABRE bloque LLAVECIERRA'''

#Error creado por Miguel
def p_estrcuturaIf_error(p):
    ''' estructuraIf : IF LPAREN error RPAREN LLAVEABRE bloque LLAVECIERRA'''
    line = p.lineno(3)
    print("Error en el argumento de comparación del if. Línea:"+str(line))
    errors.append("Error en el argumento de comparación del if. Línea:"+str(line))
    # for att in dir(p):
    #     print (att, getattr(p,att))
    # print(p.stack)


#Aportación de Danny
def p_argumentoEstructura(p):
    ''' argumentoEstructura : booleano
                           | comparacion'''

def p_argumentoEstructuraVariable(p):
    ''' argumentoEstructura : VARIABLE'''
    verificarvariable(p[1])

#Aportación de los 3
def p_estructurasDato(p):
    ''' estructurasDato : mapa
                       | set
                       | list'''
#Aportación de los 3
def p_parametros(p):
    '''parametros : parametros COMA tipoDato VARIABLE
                    | tipoDato VARIABLE
                    | empty'''



#Aportación de Miguel
def p_import(p):
    '''import : IMPORT CADENA PUNTOCOMA
              | import IMPORT CADENA PUNTOCOMA
              | empty'''    

#Aportación de Miguel
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

    if ( (p[2] != '=')  and (p[2] != '+=') and (p[2] != '-=') ):
        variables.append(p[2])
    else:
        verificarvariable(p[1])

#Aportación de Miguel
def p_operadores_asignacion(p):
    '''operadores_asignacion : IGUAL
                             | ASIGNACIONAUMENTADA
                             | ASIGNACIONDISMINUIDA'''
#Aportación de Miguel
def p_operacion_aritmetica(p):
    '''operacion_aritmetica : valores operadores_aritmeticos valores
                            | operacion_aritmetica operadores_aritmeticos valores'''



#Aportación de Miguel
def p_operadores_aritmeticos(p):
    '''operadores_aritmeticos : SUMA
                                | RESTA
                                | MULTIPLICACION
                                | DIVISION
                                | DIVENTERA
                                | RESIDUO'''

#Aportación de Raul
def p_comparacion(p):
    '''comparacion : valores comparador valores
                    | comparacion comparador valores
                    | valores IS tipoDato'''
    
#Aportación de Raul
def p_comparador(p):
    '''comparador : MENORQUE
                    | MAYORQUE
                    | IGUALQUE
                    | DIFERENTEQUE'''

#Aportación de Raul
def p_set(p):
    ''' set : SET MENORQUE tipoDato MAYORQUE VARIABLE IGUAL creacionSet
            | VAR VARIABLE IGUAL creacionSet
            | SET MENORQUE tipoDato MAYORQUE VARIABLE IGUAL LLAVEABRE collecionObjetos LLAVECIERRA'''
    #Regla semántica Danny
    variables.append(p[5])

#Aportación de Danny
def p_list(p):
    ''' list : LIST MENORQUE tipoDato MAYORQUE VARIABLE IGUAL CORCHETEABRE collecionObjetos CORCHETECIERRA
             | LIST MENORQUE tipoDato MAYORQUE VARIABLE IGUAL LIST PUNTO VARIABLE LPAREN NUMERO COMA valores RPAREN '''
    #Regla semántica Danny
    variables.append(p[5])

#Aportación de Raul
def p_coleccionObj(p):
    ''' collecionObjetos : valores
                         | valores COMA collecionObjetos
                         | empty
                         '''
#Aportación de Raul                         
def p_creacionSet(p):
    ''' creacionSet : SET LPAREN RPAREN'''

#Aportación de Raul
def p_estructurasFunciones(p):
    ''' estructurasFunciones : VARIABLE PUNTO ADD LPAREN valores RPAREN
                            | VARIABLE PUNTO JOIN LPAREN CADENA RPAREN'''
    #Regla semántica Danny
    verificarvariable(p[1])

#Aportación de Miguel
def p_mapa(p):
    '''mapa : MAP MENORQUE tipoDato COMA tipoDato MAYORQUE VARIABLE IGUAL  creacionMapa'''

#Aportación de Miguel
def p_creacion_mapa(p):
    '''creacionMapa : LLAVEABRE paresClaveValor LLAVECIERRA
                    | VARIABLE'''
#Aportación de Miguel
def p_pares_clave_valor(p):
    '''paresClaveValor : valores DOSPUNTOS valores
                        | paresClaveValor COMA valores DOSPUNTOS valores'''


#Aportación de los 3
def p_valores(p):
    '''valores : NUMERO
                | VARIABLE
                | CADENA
                | booleano
                | llamadaFunciones
                | VARIABLE PUNTO VARIABLE
                '''
    if(len(p) == 4):
        verificarvariable(p[1])


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
#Aportación de Raul  
def p_empty(p):
     'empty :'
#Aportación de Raul  
def p_nullValue(p):
    'nulValue : NULL'
#Aportación de Raul  
def p_print(p):
    ''' print : PRINT LPAREN valores RPAREN'''
    
#Aportación de Raul  
def p_readPant(p):
    ''' readPant : STRING VARIABLE IGUAL STDIN PUNTO READLINE LPAREN RPAREN PUNTOCOMA'''

# Error rule for syntax errors
#Aportación de Danny  3
def p_error(p):
    for att in dir(p):     
        print (att, getattr(p,att))
#Termia parte de Miguel
 # Build the parser

#Tests
code = '''import "A"; import "B"; 
int suma(int a, int b){return a+b} 
void main(){ 
    int suma = suma(5,a,b); 
    int calculo = 5;
    List<int> lista = [];
     if(s.length>0){ 
        suma = 10;
     }else{
        suma = 0;
     } 
     for(int i=0 i<10; i+=1){
        suma += suma(i,i);
     }
     hola =7;
}

void vacio(){ } 
int suma(int a, int b){return a+b} 
int suma(int a, int b){return a+b}
'''

parser = yacc.yacc()
# parser.parse(code)
# parser.restart()
# for att in dir(parser):     
#     print (att, getattr(parser,att))
# parser = yacc.yacc()
# parser.parse(code)
# for att in dir(parser):     
#     print (att, getattr(parser,att))
# def restar_parser(self):
#     self.parser = yacc.yacc()

# flag= True
# while flag:
#     # try:
#     #     # s = input('calc > ')
#     # except EOFError:
#     #     break
#     # if not s: continue
#     result = parser.parse(code)
#     print(code)
#     print(result)
#     flag=False

