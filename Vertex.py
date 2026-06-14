class Vertex:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def __str__(self):
        return f"{self.name} ({self.strength})"
    
    def __hash__(self): # need this so i can put stuff in a dictionary
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Vertex):
            return False

        return self.name == other.name
    def __repr__(self): # weird niche python thing lol
        return self.__str__()
    