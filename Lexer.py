from tkinter import messagebox

from Token import *

"""
    Clase: Lexer
    Descripcion: clase que permite realizar el analisis lexico
"""
class Lexer:
    def __init__(self, texto):
        # entrada de texto, por ejemplo: "5 + 5"
        self.texto = texto
        # posicion del caracter en el texto
        self.pos = 0
        # caracter actual en el texto
        self.caracter_actual = self.texto[self.pos] if self.pos < len(self.texto) else None

    def error(self):
        """
            Método para generar una excepción si la sintaxis es invalida
        """
        # raise messagebox.showerror("Error", f"Error de análisis léxico. Caracter no reconocido: '{self.caracter_actual}'")
        raise Exception(messagebox.showerror("Error", f"Error de análisis léxico. Caracter no reconocido: '{self.caracter_actual}'"))

    def consumir(self):
        """
            Avanza el puntero 'pos' y establece la variable 'caracter_actual'
        """
        self.pos += 1
        if self.pos < len(self.texto):
            self.caracter_actual = self.texto[self.pos]
        else:
            self.caracter_actual = None

    def ignorar_espacios(self):
        """
            Omite los espacios en blanco en el texto de entrada
        """
        while self.caracter_actual is not None and self.caracter_actual.isspace():
            self.consumir()

    def integer(self):
        """
            Devuelve un numero entero consumido desde la entrada
        """
        resultado = ''
        while self.caracter_actual is not None and self.caracter_actual.isdigit():
            resultado += self.caracter_actual
            self.consumir()
        return int(resultado)

    def tokenizador(self):
        """
            analizador léxico (también conocido como "scanner" o "lexer")
            se encarga de segmentar el texto en tokens (uno a la vez)
        """
        while self.caracter_actual is not None:
            # ignora los espacios en blanco
            if self.caracter_actual.isspace():
                self.ignorar_espacios()
                continue

            # si el caracter actual es un digito,
            # entonces retorna un token de tipo entero
            if self.caracter_actual.isdigit():
                return Token(TT_INT, self.integer())

            # si el caracter actual es un signo de suma, resta,
            # multiplicacion, division, parentesis izquierdo o derecho
            # entonces retorna un token acorde al tipo
            if self.caracter_actual == '+':
                self.consumir()
                return Token(TT_SUM, '+')

            if self.caracter_actual == '-':
                self.consumir()
                return Token(TT_RES, '-')

            if self.caracter_actual == '*':
                self.consumir()
                return Token(TT_MUL, '*')

            if self.caracter_actual == '/':
                self.consumir()
                return Token(TT_DIV, '/')

            if self.caracter_actual == '(':
                self.consumir()
                return Token(TT_PARENIZQ, '(')

            if self.caracter_actual == ')':
                self.consumir()
                return Token(TT_PARENDER, ')')

            # si el caracter actual no es reconocido,
            # entonces genera una excepción
            self.error()

        # Si es caracter actual es None
        # retorna un token de fin del texto
        return Token(TT_EOF, None)
