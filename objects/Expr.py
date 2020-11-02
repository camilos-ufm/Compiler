from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter

class Expr:
    def __init__(self, object_node="", type_node="expr", node_list=""):
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

    def typeCheck(self, node_list, symbol_table, error_list):
        if(len(node_list)==1):
            type_return = ""
            is_decl = False
            for decls in symbol_table[::-1]:
                for decl in decls:
                    if node_list[0].object_node.value == decl[1]:
                        type_return = decl[0]
                        is_decl = True
                        break
            if not is_decl:
                error_list.append("Semantic error, Uniqueness check: Var not declared in line "+str(node_list[0].object_node.line))
            return type_return
        if(len(node_list)==3):
            if(node_list[1].object_node.symbol_type.name == "arit_op"):
                if(node_list[0].object_node.typeCheck(node_list[0].node_list, symbol_table, error_list) == "int" and node_list[1].object_node.typeCheck(node_list[1].node_list, symbol_table, error_list)=="int"):
                    return "int"
                else:
                    error_list.append("Semantic error, Type check: failed in line "+str(node_list[1].object_node.line))