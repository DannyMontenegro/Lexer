from sintactico import parser
from tkinter import *
raiz = Tk()

def verificar():
    entrada = textArea.get(1.0,"end-1c")
    resultado = str(parser.parse(entrada))
    print("Analizando")
    print(resultado)
    if(resultado=='None'):
        varSalida.set("Salida: No hay errores sintácticos en su código")
    else:
        varSalida.set(resultado)

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