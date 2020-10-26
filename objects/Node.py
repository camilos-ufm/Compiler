from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter

class Node:
    def __init__(self, object_node, type_node, node_list):
        self.object_node = object_node
        self.type_node = type_node
        self.node_list = node_list

    def getChildNodes(self, Program, counter):
        for child in self.node_list:
            if child.node_list:
                child.getChildNodes(Program, counter)
                Program.append(child.type_node + str(counter))
                counter += 1
            else:
                Program.append(child.type_node + str(counter))
                counter+=1

    def getNodes(self, Program, counter, parent_node):
        if(len(self.node_list)!=0 and self.type_node!='method_decl_list'):
            for node1 in self.node_list:
                nodey = Node_any(node1.type_node + str(counter), parent=parent_node)
                Program.append(node1.type_node + str(counter))
                counter+=1
                if(len(node1.node_list)!=0):
                    counter = node1.getNodes(Program, counter, nodey)
        return counter


    def __iter__(self):
        # first, yield everthing every one of the child nodes would yield.
        for child in self.node_list:
            for item in child:
                # the two for loops is because there's multiple children, and we need to iterate
                # over each one.
                yield item

        # finally, yield self
        yield self