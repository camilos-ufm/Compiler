class Program:

    def __init__(self, list_nodes):
        self.list_nodes = list_nodes
        self.type = "Program"

    def getFieldDeclList(self):
        return self.list_nodes[3]

    def getMethodDeclList(self):
        return self.list_nodes[4]    