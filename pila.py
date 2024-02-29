
import tkinter as tk
from tkinter import font

terminals = {'{', '}', 'var', 'int', 'float', 'string', 'takeData', '()' }
no_terminals = {'S', 'I', 'V', 'T', 'G', 'N', 'R', 'O', 'P', 'F', 'L'}

class Tabla:
    def __init__(self):
        self.tabla = {}
        self.tabla['S'] = {'{': ['I', 'V', 'F']}
        self.tabla['I'] = {'{': ['{']}
        self.tabla['V'] = {'var': ['var', 'T', 'G']}
        self.tabla['T'] = {'string': ['string'], 'int': ['int'], 'float': ['float']}
        self.tabla['G'] = {'a-z': ['N', '=', 'O']}
        self.tabla['N'] = {'a-z': ['L', 'R']}
        self.tabla['R'] = {'a-z': ['L', 'R']}
        self.tabla['O'] = {'takeData': ['takeData', 'P']}
        self.tabla['P'] = {'()': ['()']}
        self.tabla['F'] = {'}': ['}']}
        self.tabla['L'] = {'a-z': ['letra']}

    def get(self, no_terminal, terminal):
        return self.tabla[no_terminal].get(terminal, [])

def a_pila(entrada):
    pila = ['$', 'S']
    tabla = Tabla()
    entrada = entrada.split(' ')
    entrada.append('$')
    entrada.reverse()

    while len(pila) > 0:
        if pila[-1] == entrada[-1]:
            print(pila[-1], entrada[-1])
            pila.pop()
            entrada.pop()
        elif pila[-1] in terminals:
            return False
        else:
            try:
                if entrada[-1].isalpha() and entrada[-1] not in terminals:
                    entrada.pop()
                    if pila[-1] == 'G':
                        entrada.append('a-z')
                    continue

                if entrada[-1] == 'a-z' and pila[-1] == 'letra':
                    entrada.pop()
                    pila.pop()
                    pila.pop()
                    continue

                produccion = tabla.get(pila[-1], entrada[-1])
                if not produccion:
                    return False
                print(pila[-1], entrada[-1])
                pila.pop()
                produccion.reverse()
                pila.extend(produccion)
            except:
                return False
    return True

def verificar_cadena():
    cadena = entrada.get()
    if a_pila(cadena):
        resultado.config(text="Cadena válida", fg="green")
    else:
        resultado.config(text="Cadena inválida", fg="red")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Validador de Cadena")
ventana.geometry("500x300")  # Tamaño de la ventana

# Espacio vertical
tk.Label(ventana).pack()

# Crear etiqueta para ingresar la cadena
etiqueta = tk.Label(ventana, text="Ingrese la cadena:", font=("Arial", 14))
etiqueta.pack()

# Espacio vertical
tk.Label(ventana).pack()

# Crear campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 14), width=30)
entrada.pack()

# Espacio vertical
tk.Label(ventana).pack()

# Botón para validar la cadena
boton_validar = tk.Button(ventana, text="Validar", command=verificar_cadena, bg="blue", fg="white")
boton_validar.config(font=("Arial", 14))
boton_validar.pack()

# Espacio vertical
tk.Label(ventana).pack()

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="", fg="black", font=("Arial", 14))
resultado.pack()

# Ejecutar la aplicación
ventana.mainloop()