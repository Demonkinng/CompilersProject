"""
    Clase: Token
    Descripción: crear objetos tipo token para especificar cada token generado en el análisis léxico
"""
class Token:
    def __init__(self, tipo, valor):
        # tipo de token
        self.tipo = tipo
        # valor del token
        self.valor = valor

    def __str__(self):
        """
            String representation of the class instance.
            Examples:
            Token(INT, 5)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.tipo,
            value=repr(self.valor)
        )


# ENUM para identificadores de token
TT_INT      = 'INT'       # Token Tipo: Entero                [0, 1, 2, ...]
TT_SUM      = 'SUM'       # Token Tipo: Suma                  [+]
TT_RES      = 'RES'       # Token Tipo: Resta                 [-]
TT_MUL      = 'MUL'       # Token Tipo: Multiplicacion        [*]
TT_DIV      = 'DIV'       # Token Tipo: Division              [/]
TT_PARENIZQ = 'PARENIZQ'  # Token Tipo: Parentesis izquierdo  [(]
TT_PARENDER = 'PARENDER'  # Token Tipo: Parentesis derecho    [)]
TT_EOF      = 'EOF'       # Token Tipo: End Of File           [fin del archivo]
