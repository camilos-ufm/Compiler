class Symbol:

    def __init__(self, type_num, name, regEx):
        self.type_num = type_num
        self.name = name
        self.regEx = regEx


    def pretty_print(self):
        print("<Type: " + self.type_num + ", Name: " + self.name+">")