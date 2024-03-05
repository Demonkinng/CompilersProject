from Token import *
from Parse_Tree import Nodo

"""
    Clase: Parser
    Descripción: clase que permite realizar el análisis sintáctico
"""
from Token import *
from Parse_Tree import Node

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.token_actual = self.lexer.tokenizador()
        self.tokens_list = []

    def error(self):
        """
            Método para generar una excepción si el análisis sintáctico es inválido
        """
        raise Exception('Error de análisis sintáctico')

    def consumir(self, token_type):
        """
            Compara el tipo de token actual con el tipo de token pasado
            y si coinciden, entonces "consume" el token actual y asigna
            el siguiente token al self.current_token; de lo contrario, genera una excepción.
        """
        if self.token_actual.tipo == token_type:
            self.tokens_list.append(self.token_actual)
            self.token_actual = self.lexer.tokenizador()
        else:
            self.error()

    def factor(self):
        """
            factor : INTEGER | LPAREN expr RPAREN
        """
        token = self.token_actual
        if token.tipo == TT_INT:
            self.consumir(TT_INT)
            return Nodo('INTEGER', [token.valor])
        elif token.tipo == TT_PARENIZQ:
            self.consumir(TT_PARENIZQ)
            node = self.expr()
            self.consumir(TT_PARENDER)
            return node

    def term(self):
        """
            term : factor ((MUL | DIV) factor)*
        """
        node = self.factor()

        while self.token_actual.tipo in (TT_MUL, TT_DIV):
            token = self.token_actual
            if token.tipo == TT_MUL:
                self.consumir(TT_MUL)
            elif token.tipo == TT_DIV:
                self.consumir(TT_DIV)

            node = Nodo(token.tipo, [node, self.factor()])

        return node

    def expr(self):
        """
        expr : term ((PLUS | MINUS) term)*
        """
        node = self.term()

        while self.token_actual.tipo in (TT_SUM, TT_RES):
            token = self.token_actual
            if token.tipo == TT_SUM:
                self.consumir(TT_SUM)
            elif token.tipo == TT_RES:
                self.consumir(TT_RES)

            node = Nodo(token.tipo, [node, self.term()])

        return node

    def parse(self):
        """
            Analiza la expresión.
        """
        parse_tree = self.expr()
        return self.evaluate(parse_tree), self.tokens_list, parse_tree

    def evaluate(self, node):
        """
        Evalúe el árbol de expresión de forma recursiva.
        """
        if node.tipo == 'INTEGER':
            return node.hijo[0]
        elif node.tipo == 'SUM':
            return self.evaluate(node.hijo[0]) + self.evaluate(node.hijo[1])
        elif node.tipo == 'RES':
            return self.evaluate(node.hijo[0]) - self.evaluate(node.hijo[1])
        elif node.tipo == 'MUL':
            return self.evaluate(node.hijo[0]) * self.evaluate(node.hijo[1])
        elif node.tipo == 'DIV':
            return self.evaluate(node.hijo[0]) / self.evaluate(node.hijo[1])
