from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter

class Program:

    def __init__(self, node_list):
        self.node_list = node_list
        self.type = "Program"
        self.symbol_table = []
        self.all_nodes = []
        self.program_tree = ''
        self.irt_list = []

    def getAllNodes(self):
        program_ui = Node_any("Program")
        self.program_tree = program_ui
        counter=0
        for node in self.node_list:
            nodex = Node_any(node.type_node + ' ' + str(counter), parent=program_ui)
            self.all_nodes.append(node.type_node + ' ' +str(counter))
            counter+=1
            if (len(node.node_list)!=0):
                counter = node.getNodes(self.all_nodes, counter, nodex)
   
    def getAllNodesIrt(self):
        counter=0
        for node in self.node_list:
            self.irt_list.append(node)
            counter+=1
            if (len(node.node_list)!=0):
                counter = node.getNodesIrt(self.irt_list, counter)

    def getFieldDeclList(self):
        return self.node_list[3].node_list

    def getMethodDeclList(self):
        return self.node_list[4].node_list 