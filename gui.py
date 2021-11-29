from sintactico import parser
from sintactico import errors, errores_semanticos, variables, funciones
from main import errores_lexicos, lexer

from tkinter import *
raiz = Tk()

def verificar():

    entrada = textArea.get(1.0,"end-1c")
    #print(entrada.count('\n'))
    #print(entrada)
    lexer.lineno = 1
    resultado = str(parser.parse(entrada))
    if "main" not in funciones:
        errors.append("No se ha declarado la función main en el documento")
    # print("Analizando")
    #print(resultado)
    if(resultado=='None' and (len(errors)==0) and len(errores_lexicos)==0 and len(errores_semanticos)==0):
        varSalida.set("Salida: No hay errores sintácticos en su código")
    else:
        lexicos = '\n'.join(errores_lexicos)
        sintacticos = '\n'.join(errors)
        semanticos = '\n'.join(errores_semanticos)
        salida = "Errores lexicos: "+ lexicos + '\nErrores sintáticos: ' + sintacticos + '\nErrores Semánticos' + semanticos
        varSalida.set(salida)
        errors.clear()
        errores_lexicos.clear()
        errores_semanticos.clear()
        variables.clear()
        funciones.clear()
        parser.defaulted_states = {}
        

raiz.title("Proyecto LP")
raiz.geometry("500x500")

var = StringVar()
label = Label( raiz, textvariable=var, relief=RAISED )

var.set("ANALIZADOR SINTACTICO")
label.pack()
textArea = Text(raiz,width=40,height=15)
textArea.pack()

Button(raiz,text="Analisis Sintactico",command=verificar).pack()
varSalida = StringVar()
labelSalida = Label( raiz, textvariable=varSalida,)
varSalida.set("Salida:")
labelSalida.pack()

raiz.mainloop()