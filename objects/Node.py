from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter

class Node:
    def __init__(self, object_node, type_node, node_list):
        self.object_node = object_node
        self.type_node = type_node
        self.node_list = node_list

    def getNodes(self, Program, counter, parent_node):
        if(len(self.node_list)!=0 and self.type_node!=''):
            for node1 in self.node_list:
                nodey = Node_any(node1.type_node + ' ' + str(counter), parent=parent_node)
                Program.append(node1.type_node + ' ' + str(counter))
                counter+=1
                if(len(node1.node_list)!=0):
                    counter = node1.getNodes(Program, counter, nodey)
        return counter

    def typeCheck(self, symbol_table, counter, error_list):
        print(symbol_table, counter, error_list)

    def semanticAnalysis(self, symbol_table, counter, error_list):
        if(len(self.node_list)!=0 and self.type_node!=''):
            inner_counter = 0
            for node1 in self.node_list:
                # print(type(node1.object_node))
                if(len(node1.node_list)==0 and str(type(node1.object_node)) == "<class 'objects.Token.Token'>" and node1.object_node.symbol_type.name=="id"):
                    if(inner_counter!=0 and (self.node_list[inner_counter-1].object_node.symbol_type.name == 'type' or self.node_list[inner_counter-1].object_node.symbol_type.name == 'void')):
                        is_unique = True
                        for symbol_verify in symbol_table[-1]:
                            if node1.object_node.value == symbol_verify[1]:
                                is_unique=False
                        if(is_unique):
                            symbol_table[-1].append([self.node_list[inner_counter-1].object_node.value, node1.object_node.value, node1.object_node.line, 0])
                        else:
                            error_list.append("Semantic error, Uniqueness check: identifier already used in line " + str(node1.object_node.line))
                    else:
                        # print("lookup")
                        is_decl = False
                        for decls in symbol_table[::-1]:
                            for decl in decls:
                                if node1.object_node.value == decl[1]:
                                    is_decl = True
                        if not(is_decl):
                            error_list.append("Semantic error, Uniqueness check: Var not declared in line "+str(node1.object_node.line))
                
                if(len(node1.node_list)==0 and str(type(node1.object_node)) == "<class 'objects.Token.Token'>" and node1.object_node.symbol_type.name=="("):
                    if(inner_counter!=0 and inner_counter!=1):
                        if(self.node_list[inner_counter-1].object_node.symbol_type.name == 'id' and 
                            (self.node_list[inner_counter-2].object_node.symbol_type.name == 'void' or self.node_list[inner_counter-2].object_node.symbol_type.name == 'type')):
                            # print("push scope")
                            symbol_table.append([])

                if(len(node1.node_list)==0 and str(type(node1.object_node)) == "<class 'objects.Token.Token'>" and node1.object_node.symbol_type.name=="{"):
                    # print("push scope")
                    symbol_table.append([])

                if(len(node1.node_list)==0 and str(type(node1.object_node)) == "<class 'objects.Token.Token'>" and node1.object_node.symbol_type.name=="}"):
                    pass
                    # print("pop scope")
                    #del main_program.symbol_table[-1]

                if(node1.type_node == "expr"):
                    if(len(node1.node_list) > 0):
                        if(node1.node_list[0].type_node == 'expr'):
                            if(node1.node_list[1].type_node == 'bin_op'):
                                if(node1.node_list[1].node_list[0].type_node == 'arit_op'):
                                    print("check arit op")
                                    for child_exp in node1.node_list:
                                        print("         " + child_exp.type_node)
                                if(node1.node_list[1].node_list[0].type_node == 'rel_op'):
                                    print("check rel op")
                                    for child_exp in node1.node_list:
                                        print("         " + child_exp.type_node)
                                if(node1.node_list[1].node_list[0].type_node == 'eq_op'):
                                    print("check eq op")
                                    for child_exp in node1.node_list:
                                        print("         " + child_exp.type_node)
                                if(node1.node_list[1].node_list[0].type_node == 'cond_op'):
                                    print("check cond op")
                                    for child_exp in node1.node_list:
                                        print("         " + child_exp.type_node)
                            elif(node1.node_list[1].type_node == 'minus_op'):
                                    print("check minus op")
                                    for child_exp in node1.node_list:
                                        print("         " + child_exp.type_node)
                        if(node1.node_list[0].type_node == 'minus_op'):
                            print("check - expr op")
                            for child_exp in node1.node_list:
                                print("         " + child_exp.type_node)
                        if(node1.node_list[0].type_node == '!'):
                            print("check ! expr op")
                            for child_exp in node1.node_list:
                                print("         " + child_exp.type_node)

                    # node1.object_node.typeCheck(node1.node_list, symbol_table, error_list)

                if(node1.type_node == "statement"):
                    if(len(node1.node_list) > 0):
                        if(node1.node_list[0].type_node == 'if'):
                            print("check if")
                            for child_exp in node1.node_list:
                                print("         " + child_exp.type_node)
                        if(node1.node_list[0].type_node == 'for'):
                            print("check for")
                            for child_exp in node1.node_list:
                                print("         " + child_exp.type_node)
                        if(node1.node_list[0].type_node == 'location'):
                            print("check location")
                            for child_exp in node1.node_list:
                                print("         " + child_exp.type_node)

                        # node1.object_node.typeCheck(node1.node_list, symbol_table, error_list)

                counter+=1
                inner_counter+=1
                if(len(node1.node_list)!=0):
                    counter = node1.semanticAnalysis(symbol_table, counter, error_list)
        return counter