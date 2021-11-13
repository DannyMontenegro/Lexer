import ply.lex as lex

reserved = {
    #Parte de Miguel Licea
    'if':'IF',
    'else':'ELSE',
    'for':'FOR',
    'while':'WHILE',
    'import':'IMPORT',
    'print':'PRINT',
    'int':'INT',
    'double':'DOUBLE',
    'String':'STRING',
    'bool':'BOOL',
    #Termina parte de Miguel Licea
    #Parte de Danny Montenegro
    'dynamic':'DYNAMIC',
    'var':'VAR',
    'Map':'MAP',
    'void':'VOID',
    'Set':'SET',
    'new':'NEW',
    'add':'ADD',
    'List':'LIST',
    'true':'TRUE',
    #Termina parte de Danny Montenegro

    #Parte Raul Villao
    'do':'DO',
    'null':'NULL',
    'is':'IS',
    'required':'REQUIRED',
    'export':'EXPORT',
    'return':'RETURN',
    'in':'IN',
    'super':'SUPER',
    'final':'FINAL',
    'this':'THIS',
    #Termina parte Raul Villao
}

tokens = (
    #Parte de Danny Montenegro
    'NUMERO',
    'VARIABLE',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'LPAREN',
    'RPAREN',
    #Termina parte de Danny Montenegro
    #Parte de Miguel Licea
    'MAYORQUE',
    'NOT',
    'DIVENTERA',
    'RESIDUO',
    'PUNTOCOMA',
    'LLAVEABRE',
    'LLAVECIERRA',
    'COMA',
    'DOSPUNTOS',
    #Termina parte de Miguel LiceA
    #Parte Raul
    'IGUAL',
    'COMILLASDOBLES',
    'COMILLASSIMPLES',
    'PUNTO',
    'CORCHETEABRE',
    'CORCHETECIERRA',
    'IGUALQUE',
    'DIFERENTEQUE',
    'ASIGNACIONAUMENTADA',
    'ASIGNACIONDISMINUIDA',
    'FLECHA'
    #Termina parte Raul
)+ tuple(reserved.values())


#Parte de Danny Montenegro

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_VARIABLE(t):
    r'[a-zA-Z$_][a-zA-Z\d$_]*'
    t.type = reserved.get(t.value,'VARIABLE')
    return t


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t
#Termina parte de Danny Montenegro


#Empiezaa parte de Miguel
t_MAYORQUE = r'\>'
t_NOT = r'!'
t_DIVENTERA = r'\~/'
t_RESIDUO = r'\%'
t_PUNTOCOMA = r'\;'
t_LLAVEABRE = r'\{'
t_LLAVECIERRA = r'\}'
t_COMA = r'\,'
t_DOSPUNTOS = r'\:'
#Termina parte de Miguel









# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
#Parte de Miguel
data = '''
123
@asa_AS
a14$
15#A
~
%
()
;
import "dart:io";
if(){}else{}
for (){} , : =
Map<String,int> mapa = { 
       "lenguajes":10 
}; 
mapa.remove("hola");
mapa.clear();

void saludar (String saludo){ 

print (saludo+ "hola"); 

} 
int numero() => 4;
'''

data ='''
Set numberSet = new  Set(); 
numberSet.add(100); 
numberSet.add(200); 
print(numberSet.join(";"));
'''

data = '''
List<int> lista = [1,2,3]; 
lista.add(5); 
lista.clear();
String str = stdin.readLineSync(); 
a % b 
A != B 
'''
#Pruebas de Operadores de asignacion
data = '''
    int x = 4;
    bool session = true;
    x+=1;
    x-=3;
    >
'''
#Termina parte de Miguel

#Parte pruebas de Danny Montenegro
#Pruebas de Operadores de comparacion
data = '''
    int a = 4; 
    var b = 6; 
    bool compare; 
    compare = a < b;
    compare = a > b;
    compare= a == b;
    compare= a != b;
'''
#Pruebas de Operadores aritmeticos
data = '''
    int a = 4; 
    int b = 6; 
    int c = a + b;
    int c = a – b; 
    int c = a * b; 
    int c = a / b; 
    int c = a ~/ b; 
    int c = a % b;  
'''
#Pruebas de Metodo Impresion
data = '''print("Hello World");'''
#Pruebas de Lectura por consola
data = '''
import "dart:io"; 
String str = stdin.readLineSync(); 
'''
#Termina parte de pruebas de Danny Montenegro

#Parte Raul
#Pruebas If
data = '''
if(5>1){ 
  a = 25; 
} else{ 
  a = 5 
} 
'''
#Pruebas While
data = '''
    while (x > 0) { 
   q=q+x; 
   x=x-1; 
} 
'''

#Puebas de palabras reservadas agregadas recientemente
data = '''
    class point{
        int x;
        int y;   
        Point(double x, double y) {
          this.x = x;
          this.y = y;
        }
    }     
    do { 
        printLine();
        if(varible==0){
            return variable;
        }
    } while (variable!=null);    
    const Scrollbar({required int numero});    
    export 'src/cascade.dart' show Cascade;    
    if (employee is Person) {
      employee.firstName = 'Bob';
    }    
    for (final candidate in candidates) {
      candidate.interview();
    }
    super.turnOn();
'''

#Prueba funciones
data = '''
void saludar (String saludo){ 

print (saludo+ "hola"); 

}

String salidar(String saludo){
    return saludo+"hola"
}

int numero() => 4; 
print(numero()); 
'''
#Termina Parte Raul

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
