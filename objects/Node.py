from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter

class Node:
    def __init__(self, object_node, type_node, node_list):
        self.object_node = object_node
        self.type_node = type_node
        self.node_list = node_list

    def getNodes(self, Program, counter, parent_node):
        if(len(self.node_list)!=0 and self.type_node!='method_decl_list'):
            for node1 in self.node_list:
                nodey = Node_any(node1.type_node + str(counter), parent=parent_node)
                Program.append(node1.type_node + str(counter))
                counter+=1
                if(len(node1.node_list)!=0):
                    counter = node1.getNodes(Program, counter, nodey)
        return counter