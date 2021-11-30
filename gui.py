from sintactico import parser
from sintactico import errors, errores_semanticos, variables, funciones
from main import errores_lexicos, lexer

from tkinter import *
raiz = Tk()

def verificarSintax():
    entrada = textArea.get(1.0,"end-1c")
    #print(entrada.count('\n'))
    #print(entrada)
    lexer.lineno = 1
    resultado = str(parser.parse(entrada))
    if "main" not in funciones:
        errors.append("No se ha declarado la función main en el documento")
    # print("Analizando")
    #print(resultado)
    if(resultado=='None' and (len(errors)==0)):
        varSalida.set("Salida: No hay errores sintácticos en su código")
    else:
        print(errors)
        sintacticos = '\n'.join(errors)
        salida = 'Errores sintáticos: ' + sintacticos
        varSalida.set(salida)
        parser.defaulted_states = {}
    vaciasListas()

def verificarLex():
    entrada = textArea.get(1.0, "end-1c")
    # print(entrada.count('\n'))
    # print(entrada)
    lexer.lineno = 1
    resultado = str(parser.parse(entrada))
    if (resultado == 'None' and len(errores_lexicos)==0):
        varSalida.set("Salida: No hay errores Léxicos en su código")
    else:
        lexicos = '\n'.join(errores_lexicos)
        salida = "Errores lexicos: "+ lexicos + '\n'
        varSalida.set(salida)
        parser.defaulted_states = {}
    vaciasListas()


def verificarSem():
    entrada = textArea.get(1.0, "end-1c")
    # print(entrada.count('\n'))
    # print(entrada)
    lexer.lineno = 1
    resultado = str(parser.parse(entrada))
    if (resultado == 'None' and len(errores_semanticos) == 0):
        varSalida.set("Salida: No hay errores semánticos en su código")
    else:
        semanticos = '\n'.join(errores_semanticos)
        salida = salida = 'Errores Semánticos: ' + semanticos
        varSalida.set(salida)
        parser.defaulted_states = {}
    vaciasListas()

def vaciasListas():
    errors.clear()
    errores_lexicos.clear()
    errores_semanticos.clear()
    variables.clear()
    funciones.clear()

raiz.title("Proyecto LP")
raiz.geometry("700x500")

var = StringVar()
label = Label( raiz, textvariable=var, relief=RAISED )

var.set("DART")
label.pack()
textArea = Text(raiz,width=40,height=15)
textArea.pack()

Button(raiz,text="Analisis Sintactico",command=verificarSintax).pack()
'''
varSalida = StringVar()
labelSalida = Label( raiz, textvariable=varSalida,)
varSalida.set("Salida:")
labelSalida.pack()'''


Button(raiz,text="Analisis Léxico",command=verificarLex).pack()
'''
varSalida = StringVar()
labelSalida = Label( raiz, textvariable=varSalida,)
varSalida.set("Salida:")
labelSalida.pack()'''

Button(raiz,text="Analisis Semántico",command=verificarSem).pack()
varSalida = StringVar()
labelSalida = Label( raiz, textvariable=varSalida,)
varSalida.set("Salida:")
labelSalida.pack()

raiz.mainloop()