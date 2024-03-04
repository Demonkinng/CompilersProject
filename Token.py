"""
    Class: Token
    Description: creating token objects to specify each token generated in lexical analysis
    Author: Angel David Chuncho Jimenez
"""

# Token identifiers
TT_INT    = 'INT'       # Type Token: Integer           [0, 1, 2, ...]
TT_PLUS   = 'PLUS'      # Type Token: Plus              [+]
TT_MINUS  = 'MINUS'     # Type Token: Minus             [-]
TT_MUL    = 'MUL'       # Type Token: Multiplication    [*]
TT_DIV    = 'DIV'       # Type Token: Division          [/]
TT_LPAREN = 'LPAREN'    # Type Token: Left Parentheses  [(]
TT_RPAREN = 'RPAREN'    # Type Token: Right             [)]
TT_EOF    = 'EOF'       # Type Token: End Of File       [no more input]

class Token:
    def __init__(self, type, value):
        # token type
        self.type = type
        # token value
        self.value = value

    def __str__(self):
        """
            String representation of the class instance.
            Examples:
            Token(INT, 5)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        """
            Method for representing the objects in a class as a string
        """
        return self.__str__()
