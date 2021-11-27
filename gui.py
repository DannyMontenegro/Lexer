from sintactico import parser
from sintactico import errors
from tkinter import *
raiz = Tk()

def verificar():
    entrada = textArea.get(1.0,"end-1c")
    print(entrada.count('\n'))
    print(entrada)
    resultado = str(parser.parse(entrada))
    # print("Analizando")
    # print(resultado)
    if(resultado=='None' and len(errors)==0):
        varSalida.set("Salida: No hay errores sintácticos en su código")
    else:
        salida = '\n'.join(errors)
        varSalida.set(salida)
        errors.clear()
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