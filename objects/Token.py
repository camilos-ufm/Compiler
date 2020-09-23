class Token:

    def __init__(self, symbol_type, line, value=""):
        self.symbol_type = symbol_type
        self.value = value
        self.line = line

    def pretty_print(self):
        pretty_string = "~ Type: " + self.symbol_type.name + ", Line: " + str(self.line)
        if(self.value != ""):
            pretty_string += ", Value: " + self.value+" ~"
        else:
            pretty_string += " ~"
        print(pretty_string)
