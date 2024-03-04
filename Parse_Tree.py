class Node:
    def __init__(self, type, children=None):
        self.type = type
        self.children = children if children else []

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.type) + "\n"
        for child in self.children:
            if isinstance(child, Node):
                ret += child.__repr__(level + 1)
            else:
                ret += "\t" * (level + 1) + repr(child) + "\n"
        return ret
