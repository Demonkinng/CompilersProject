"""
    Class: Parser
    Description: clase que permite realizar el análisis léxico
    Autor: Angel David Chuncho Jimenez
"""
from Token import *
from Parse_Tree import Node

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.tokenizador()
        self.tokens_list = []

    def error(self):
        raise Exception('Error de análisis sintáctico')

    def eat(self, token_type):
        """
        Compara el tipo de token actual con el tipo de token pasado
        y si coinciden, entonces "consume" el token actual y asigna
        el siguiente token al self.current_token; de lo contrario, genera una excepción.
        """
        if self.current_token.tipo == token_type:
            self.tokens_list.append(self.current_token)
            self.current_token = self.lexer.tokenizador()
        else:
            self.error()

    def factor(self):
        """
        factor : INTEGER | LPAREN expr RPAREN
        """
        token = self.current_token
        if token.tipo == TT_INT:
            self.eat(TT_INT)
            return Node('INTEGER', [token.valor])
        elif token.tipo == TT_PARENIZQ:
            self.eat(TT_PARENIZQ)
            node = self.expr()
            self.eat(TT_PARENDER)
            return node

    def term(self):
        """
        term : factor ((MUL | DIV) factor)*
        """
        node = self.factor()

        while self.current_token.tipo in (TT_MUL, TT_DIV):
            token = self.current_token
            if token.tipo == TT_MUL:
                self.eat(TT_MUL)
            elif token.tipo == TT_DIV:
                self.eat(TT_DIV)

            node = Node(token.tipo, [node, self.factor()])

        return node

    def expr(self):
        """
        expr : term ((PLUS | MINUS) term)*
        """
        node = self.term()

        while self.current_token.tipo in (TT_SUM, TT_RES):
            token = self.current_token
            if token.tipo == TT_SUM:
                self.eat(TT_SUM)
            elif token.tipo == TT_RES:
                self.eat(TT_RES)

            node = Node(token.tipo, [node, self.term()])

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
        if node.type == 'INTEGER':
            return node.children[0]
        elif node.type == 'SUM':
            return self.evaluate(node.children[0]) + self.evaluate(node.children[1])
        elif node.type == 'RES':
            return self.evaluate(node.children[0]) - self.evaluate(node.children[1])
        elif node.type == 'MUL':
            return self.evaluate(node.children[0]) * self.evaluate(node.children[1])
        elif node.type == 'DIV':
            return self.evaluate(node.children[0]) / self.evaluate(node.children[1])
