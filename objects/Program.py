class Program:

    def __init__(self, node_list):
        self.node_list = node_list
        self.type = "Program"
        self.symbol_table = []

    def getFieldDeclList(self):
        return self.node_list[3].node_list

    def getMethodDeclList(self):
        return self.node_list[4].node_list 