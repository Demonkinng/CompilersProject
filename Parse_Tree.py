"""
    Clase: Nodo
    Descripción: clase que permite la creación de un árbol de análisis sintáctico
"""
class Nodo:
    def __init__(self, tipo, hijo=None):
        self.tipo = tipo
        self.hijo = hijo if hijo else []

    def __repr__(self, nivel=0):
        ret = "\t" * nivel + repr(self.tipo) + "\n"
        for hijo in self.hijo:
            if isinstance(hijo, Nodo):
                ret += hijo.__repr__(nivel + 1)
            else:
                ret += "\t" * (nivel + 1) + repr(hijo) + "\n"
        return ret
