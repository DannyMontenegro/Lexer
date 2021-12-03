import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from sintactico import parser
from sintactico import errors, errores_semanticos, variables, funciones
from main import errores_lexicos, lexer

class App:
    def __init__(self, root):
        #setting title
        root.title("Proyecto LP")
        #setting window size

        width=1000
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        lbl_escribeAqui = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        lbl_escribeAqui["font"] = ft
        lbl_escribeAqui["fg"] = "#333333"
        lbl_escribeAqui["justify"] = "center"
        lbl_escribeAqui["text"] = "ESCRIBE TU CODIGO AQUI:"
        lbl_escribeAqui.place(x=0, y=75, width=300, height=30)

        textArea = Text(root, width=40, height=15)
        textArea["bg"] = "#FFFFFF"
        ft = tkFont.Font(family='Times',size=10)
        textArea["font"] = ft
        textArea["fg"] = "#333333"
        textArea.place(x=20,y=100,width=280,height=472)

        lbl_entrada=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        lbl_entrada["font"] = ft
        lbl_entrada["fg"] = "#333333"
        lbl_entrada["justify"] = "center"
        lbl_entrada["text"] = "ANALIZA TU CODIGO EN DART"
        lbl_entrada.place(x=270,y=10,width=400,height=30)


        varSalida = StringVar()
        lbl_salida = tk.Label(root,textvariable=varSalida)
        varSalida.set("Salida:")
        lbl_salida["bg"] = "#FFFFFF"
        ft = tkFont.Font(family='Times', size=10)
        lbl_salida["font"] = ft
        lbl_salida["fg"] = "#000000"
        lbl_salida["justify"] = "left"
        lbl_salida.place(x=320, y=180, width=600, height=378)

        def verificarSintax():
            entrada = textArea.get(1.0, "end-1c")
            # print(entrada.count('\n'))
            # print(entrada)
            lexer.lineno = 1
            resultado = str(parser.parse(entrada))
            if "main" not in funciones:
                errors.append("No se ha declarado la función main en el documento")
            # print("Analizando")
            # print(resultado)
            if (resultado == 'None' and (len(errors) == 0)):
                varSalida.set("Salida: No hay errores sintácticos en su código")
            else:
                print(errors)
                sintacticos = '\n'.join(errors)
                salida = 'Errores sintáticos: ' + sintacticos
                varSalida.set(salida)
                parser.defaulted_states = {}
            vaciasListas()

        btn_sint=tk.Button(root,command=verificarSintax)
        btn_sint["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        btn_sint["font"] = ft
        btn_sint["fg"] = "#000000"
        btn_sint["justify"] = "center"
        btn_sint["text"] = "Análisis Sintáctico"
        btn_sint.place(x=440,y=130,width=119,height=30)
        #btn_sint["command"] = verificarSintax

        def verificarLex():
            entrada = textArea.get(1.0, "end-1c")
            # print(entrada.count('\n'))
            # print(entrada)
            lexer.lineno = 1
            # resultado = str(parser.parse(entrada))
            resultado = str(lexer.input(entrada))
            salida = ""
            while True:
                tok = lexer.token()
                salida += str(tok)
                salida += "\n"
                if not tok:
                    break
            if (resultado == 'None' and len(errores_lexicos) == 0):
                varSalida.set(salida)
            else:
                lexicos = '\n'.join(errores_lexicos)
                salida = "Errores lexicos: " + lexicos + '\n'
                varSalida.set(salida)
                parser.defaulted_states = {}
            vaciasListas()

        btn_lex=tk.Button(root,command=verificarLex)
        btn_lex["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        btn_lex["font"] = ft
        btn_lex["fg"] = "#000000"
        btn_lex["justify"] = "center"
        btn_lex["text"] = "Análisis Léxico"
        btn_lex.place(x=570,y=130,width=120,height=30)
        #btn_lex["command"] = self.GButton_330_command

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

        btn_sem=tk.Button(root,command=verificarSem)
        btn_sem["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        btn_sem["font"] = ft
        btn_sem["fg"] = "#000000"
        btn_sem["justify"] = "center"
        btn_sem["text"] = "Análisis Semántico"
        btn_sem.place(x=700,y=130,width=121,height=30)
        #btn_sem["command"] = self.GButton_925_command



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
