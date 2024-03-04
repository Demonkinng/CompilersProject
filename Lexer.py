"""
    Class: Lexer
    Description: class that allows lexical analysis to be performed
    Author: Angel David Chuncho Jimenez
"""
from Token import *
class Lexer:
    def __init__(self, text):
        # input string
        self.text = text
        # current position in the input string
        self.pos = 0
        # current character being pointed to
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def error(self):
        raise Exception('Sintaxis Inválida')

    def advance(self):
        """
        Advance the 'pos' pointer and set the 'current_char' variable.
        """
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        """
        Skip whitespace characters in the input string.
        """
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """
        Return a (multidigit) integer consumed from the input.
        """
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def tokenizer(self):
        """
        Lexical analyzer

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(TT_INT, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(TT_PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(TT_MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(TT_MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(TT_DIV, '/')

            if self.current_char == '(':
                self.advance()
                return Token(TT_LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(TT_RPAREN, ')')

            self.error()

        return Token(TT_EOF, None)
