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
        self.current_token = self.lexer.tokenizer()
        self.tokens_list = []

    def error(self):
        raise Exception('Error de análisis sintáctico')

    def eat(self, token_type):
        """
        Compare the current token type with the passed token type
        and if they match, then "eat" the current token and assign
        the next token to the self.current_token, otherwise raise an exception.
        """
        if self.current_token.type == token_type:
            self.tokens_list.append(self.current_token)
            self.current_token = self.lexer.tokenizer()
        else:
            self.error()

    def factor(self):
        """
        factor : INTEGER | LPAREN expr RPAREN
        """
        token = self.current_token
        if token.type == TT_INT:
            self.eat(TT_INT)
            return Node('INTEGER', [token.value])
        elif token.type == TT_LPAREN:
            self.eat(TT_LPAREN)
            node = self.expr()
            self.eat(TT_RPAREN)
            return node

    def term(self):
        """
        term : factor ((MUL | DIV) factor)*
        """
        node = self.factor()

        while self.current_token.type in (TT_MUL, TT_DIV):
            token = self.current_token
            if token.type == TT_MUL:
                self.eat(TT_MUL)
            elif token.type == TT_DIV:
                self.eat(TT_DIV)

            node = Node(token.type, [node, self.factor()])

        return node

    def expr(self):
        """
        expr : term ((PLUS | MINUS) term)*
        """
        node = self.term()

        while self.current_token.type in (TT_PLUS, TT_MINUS):
            token = self.current_token
            if token.type == TT_PLUS:
                self.eat(TT_PLUS)
            elif token.type == TT_MINUS:
                self.eat(TT_MINUS)

            node = Node(token.type, [node, self.term()])

        return node

    def evaluate(self, node):
        """
        Evaluate the expression tree recursively.
        """
        if node.type == 'INTEGER':
            return node.children[0]
        elif node.type == 'PLUS':
            return self.evaluate(node.children[0]) + self.evaluate(node.children[1])
        elif node.type == 'MINUS':
            return self.evaluate(node.children[0]) - self.evaluate(node.children[1])
        elif node.type == 'MUL':
            return self.evaluate(node.children[0]) * self.evaluate(node.children[1])
        elif node.type == 'DIV':
            return self.evaluate(node.children[0]) / self.evaluate(node.children[1])

    def parse(self):
        """
        Parse the expression.
        """
        parse_tree = self.expr()
        return self.evaluate(parse_tree), self.tokens_list, parse_tree
