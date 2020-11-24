from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter
import objects.IrtNode as IrtNode


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
    
    def getIrtInstructions(self, irt_list, symbol_table, counter, label=""):
        counter += 1
        if(self.type_node == "field_decl_list"):
            for field_decl_i in self.node_list:
                counter = field_decl_i.getIrtInstructions(irt_list, symbol_table, counter)
        if(self.type_node == "method_decl_list"):
            for method_decl_i in self.node_list:
                counter = method_decl_i.getIrtInstructions(irt_list, symbol_table, counter)
        if(self.type_node == "field_decl"):
            irt_list.append(IrtNode.IrtNode(self.type_node, str(counter) + " Instructions for: " + self.type_node))
        if(self.type_node == "method_decl"):
            irt_list.append(IrtNode.IrtNode(self.type_node + str(counter), "LABEL$"+self.node_list[1].object_node.value))
            irt_list.append(IrtNode.IrtNode(self.type_node + str(counter), "BeginFuncMT"))
            if(len(self.node_list[3].node_list) != 0):
                counter = self.node_list[3].getIrtInstructions(irt_list, symbol_table, counter)
            counter = self.node_list[5].getIrtInstructions(irt_list, symbol_table, counter)
            irt_list.append(IrtNode.IrtNode(self.type_node + str(counter), "EndFuncMT"))
            # irt_list.append(IrtNode.IrtNode(self.type_node, str(counter) + "Instructions for: " + self.type_node))
        # return ""
        if(self.type_node == "block"):
            irt_list.append(IrtNode.IrtNode(self.type_node + str(counter), "StartBlock"))

            if(len(self.node_list[1].node_list) != 0):
                for statement_i in self.node_list[1].node_list:
                    counter = statement_i.getIrtInstructions(irt_list, symbol_table, counter)

            irt_list.append(IrtNode.IrtNode(self.type_node + str(counter), "EndBlock"))

        if(self.type_node == "statement"):
            counter+=1
            irt_list.append(IrtNode.IrtNode(self.type_node + str(counter), "StartStatement"))
            irt_list.append(IrtNode.IrtNode(self.type_node, str(counter) + " Instructions for: " + self.type_node))
            #if is if -->
            if(self.node_list[0].type_node == "if" and len(self.node_list)==5):
                print("IF WO ELSE")
                if_label_expr = "_T"+str(counter)
                if_label = "_L"+str(counter)
                if_label_continue = "_L"+str(counter+1)
                counter = self.node_list[2].getIrtInstructions(irt_list, symbol_table, counter, if_label_expr)
                irt_list.append(IrtNode.IrtNode(self.type_node, "if "+if_label_expr+ " Goto "+if_label))
                irt_list.append(IrtNode.IrtNode(self.type_node, "if not "+if_label_expr+ " Goto "+if_label_continue))
                irt_list.append(IrtNode.IrtNode(self.type_node + str(counter), "LABEL$"+if_label))
                counter = self.node_list[4].getIrtInstructions(irt_list, symbol_table, counter)
                irt_list.append(IrtNode.IrtNode(self.type_node + str(counter), "Goto "+if_label_continue))
                irt_list.append(IrtNode.IrtNode(self.type_node + str(counter), "EndStatement"))
                irt_list.append(IrtNode.IrtNode(self.type_node + str(counter), "LABEL$"+if_label_continue))                
            else:
                irt_list.append(IrtNode.IrtNode(self.type_node + str(counter), "EndStatement"))
            if(self.node_list[0].type_node == "if" and len(self.node_list)==7):
                counter = self.node_list[2].getIrtInstructions(irt_list, symbol_table, counter)
                print("IF W ELSE")
            #vard_decl -->

            #for --> 

            #location;assign;expr -->

            #methodcall -->

            #return;break;continue

            #block -->
            
        if(self.type_node == "expr"):
            counter+=1
            irt_list.append(IrtNode.IrtNode(self.type_node, str(counter) + " Instructions for: " + self.type_node))
            #expr binop expr 
            #expr.getValue ; binop getValue ; expr get value


            #suma -- >
            #compare -- >
            #method call -- >
        return counter

    def getNodesIrt(self, irt_list, symbol_table, counter):
        if(len(self.node_list)!=0 and self.type_node!=''):
            for node1 in self.node_list:
                node1.getIrtInstructions(irt_list, symbol_table, counter)
                counter+=1
                if(len(node1.node_list)!=0):
                    counter = node1.getNodesIrt(irt_list, symbol_table, counter)
        return counter

    def typeCheck(self, symbol_table, counter, error_list):
        print(symbol_table, counter, error_list)

    def getType(self, symbol_table, error_list):
        if(self.type_node == 'expr'):
            if(self.node_list[0].type_node == 'location'):
                return_type = ""
                for decls in symbol_table[::-1]:
                    for decl in decls:
                        if self.node_list[0].node_list[0].object_node.value == decl[1]:
                            return_type = decl[0]
                            break
                return return_type
            if(self.node_list[0].type_node == 'method_call'):
                return_type = ""
                for decls in symbol_table[::-1]:
                    for decl in decls:
                        if node1.node_list[0].node_list[0].object_node.value == decl[1]:
                            return_type = decl[0]
                            break
                return return_type
            if(self.node_list[0].type_node == 'literal'):
                if(self.node_list[0].node_list[0].type_node == "int_literal"):
                    return "int"
                if(self.node_list[0].node_list[0].type_node == "char_literal"):
                    return "char"
                if(self.node_list[0].node_list[0].type_node == "string_literal"):
                    return "string"
                if(self.node_list[0].node_list[0].type_node == "bool_literal"):
                    return "boolean"
            if(self.node_list[0].type_node == 'expr'):
                if(self.node_list[1].type_node == 'bin_op'):
                    if(self.node_list[1].node_list[0].type_node == 'arit_op'):
                        if(self.node_list[0].getType(symbol_table, error_list) == "int" 
                            and self.node_list[2].getType(symbol_table, error_list) == "int"):
                            return "int"
                        else:
                            error_list.append("Type error: cannot arit_op two things !int")
                            return "type_error"
                    if(self.node_list[1].node_list[0].type_node == 'rel_op'):
                        if(self.node_list[0].getType(symbol_table, error_list) == "int" 
                            and self.node_list[2].getType(symbol_table, error_list) == "int"):
                            return "boolean"
                        else:
                            error_list.append("Type error: cannot rel_op two things !int")
                            return "type_error"
                    if(self.node_list[1].node_list[0].type_node == 'eq_op'):
                        if(self.node_list[0].getType(symbol_table, error_list) == 
                            self.node_list[2].getType(symbol_table, error_list)):
                            return "boolean"
                        else:
                            error_list.append("Type error: cannot eq_op two things with diff type")
                            return "type_error"
                    if(self.node_list[1].node_list[0].type_node == 'cond_op'):
                        if(self.node_list[0].getType(symbol_table, error_list) == "boolean" 
                            and self.node_list[2].getType(symbol_table, error_list) == "boolean"):
                            return "boolean"
                        else:
                            error_list.append("Type error: cannot cond_op two things !boolean")
                            return "type_error"
                elif(self.node_list[1].type_node == 'minus_op'):
                    if(self.node_list[0].getType(symbol_table, error_list) == "int" 
                        and self.node_list[2].getType(symbol_table, error_list) == "int"):
                        return "int"
                    else:
                        error_list.append("Type error: cannot arit_op two things !int")
                        return "type_error"
                    return "minus"
            if(self.node_list[0].type_node == 'minus_op'):
                if(self.node_list[1].getType(symbol_table, error_list) == 'int'):
                    return "int"
                else:
                    error_list.append("Cannot - a thing that is !int")
                    return "type_error"
            if(self.node_list[0].type_node == '!'):
                if(self.node_list[1].getType(symbol_table, error_list) == 'boolean'):
                    return "boolean"
                else:
                    error_list.append("Cannot ! a thing that is !boolean")
                    return "type_error"
            if(self.node_list[0].type_node == '('):
                return self.node_list[1].getType(symbol_table, error_list)
        elif(self.type_node == 'location'):
            return_type = ""
            for decls in symbol_table[::-1]:
                for decl in decls:
                    if self.node_list[0].object_node.value == decl[1]:
                        return_type = decl[0]
                        break
            return return_type
        elif(self.type_node == 'id'):
            return_type = ""
            for decls in symbol_table[::-1]:
                for decl in decls:
                    if self.object_node.value == decl[1]:
                        return_type = decl[0]
                        break
            return return_type
        elif(self.type_node == 'literal'):
            if(self.node_list[0].type_node == "int_literal"):
                return "int"
            if(self.node_list[0].type_node == "char_literal"):
                return "char"
            if(self.node_list[0].type_node == "string_literal"):
                return "string"
            if(self.node_list[0].type_node == "bool_literal"):
                return "boolean"
        else:   
            return "default"

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
                    # type_expr = node1.getType(symbol_table, error_list)
                    # print(type_expr)
                    if(len(node1.node_list) > 0):
                        if(node1.node_list[0].type_node == 'expr'):
                            if(node1.node_list[1].type_node == 'bin_op'):
                                if(node1.node_list[1].node_list[0].type_node == 'arit_op'):
                                    # print("check arit op")
                                    # for child_exp in node1.node_list:
                                    #     print("         " + child_exp.type_node)
                                    type_exp1 = node1.node_list[0].getType(symbol_table, error_list)
                                    type_exp2 = node1.node_list[2].getType(symbol_table, error_list)
                                    if(type_exp1 != "type_error" and type_exp2!="type_error" and 
                                        type_exp1 != "int" and type_exp2!="int"):
                                        error_list.append("Type error: cannot arit op two !ints")
                                if(node1.node_list[1].node_list[0].type_node == 'rel_op'):
                                    # print("check rel op")
                                    # for child_exp in node1.node_list:
                                    #     print("         " + child_exp.type_node)
                                    type_exp1 = node1.node_list[0].getType(symbol_table, error_list)
                                    type_exp2 = node1.node_list[2].getType(symbol_table, error_list)
                                    if(type_exp1 != "type_error" and type_exp2!="type_error" and 
                                        type_exp1 != "int" and type_exp2!="int"):
                                        error_list.append("Type error: cannot rel op two !ints")
                                if(node1.node_list[1].node_list[0].type_node == 'eq_op'):
                                    # print("check eq op")
                                    # for child_exp in node1.node_list:
                                    #     print("         " + child_exp.type_node)
                                    type_exp1 = node1.node_list[0].getType(symbol_table, error_list)
                                    type_exp2 = node1.node_list[2].getType(symbol_table, error_list)
                                    if(type_exp1 != "type_error" and type_exp2!="type_error" and 
                                        type_exp1 != type_exp2):
                                        error_list.append("Type error: cannot eq op two things with diff type")
                                if(node1.node_list[1].node_list[0].type_node == 'cond_op'):
                                    # print("check cond op")
                                    # for child_exp in node1.node_list:
                                    #     print("         " + child_exp.type_node)
                                    type_exp1 = node1.node_list[0].getType(symbol_table, error_list)
                                    type_exp2 = node1.node_list[2].getType(symbol_table, error_list)
                                    if(type_exp1 != "type_error" and type_exp2!="type_error" and 
                                        type_exp1 != "boolean" and type_exp2!="boolean"):
                                        error_list.append("Type error: cannot cond op two things !boolean")
                            elif(node1.node_list[1].type_node == 'minus_op'):
                                    # print("check minus op")
                                    # for child_exp in node1.node_list:
                                    #     print("         " + child_exp.type_node)
                                    type_exp1 = node1.node_list[0].getType(symbol_table, error_list)
                                    type_exp2 = node1.node_list[2].getType(symbol_table, error_list)
                                    if(type_exp1 != "type_error" and type_exp2!="type_error" and 
                                        type_exp1 != "int" and type_exp2!="int"):
                                        error_list.append("Type error: cannot minus op two !ints")
                        if(node1.node_list[0].type_node == 'minus_op'):
                            # print("check - expr op")
                            # for child_exp in node1.node_list:
                            #     print("         " + child_exp.type_node)
                            type_exp = node1.node_list[1].getType(symbol_table, error_list)
                            if(type_exp != "type_error" and type_exp!="int"):
                                error_list.append("Type error: cannot minus op a thing that is !int")
                        if(node1.node_list[0].type_node == '!'):
                            # print("check ! expr op")
                            # for child_exp in node1.node_list:
                            #     print("         " + child_exp.type_node)
                            type_exp = node1.node_list[1].getType(symbol_table, error_list)
                            # print("type exp", type_exp)
                            if(type_exp != "type_error" and type_exp!="boolean"):
                                error_list.append("Type error: cannot ! op a thing that is !boolean")

                    # node1.object_node.typeCheck(node1.node_list, symbol_table, error_list)

                if(node1.type_node == "statement"):
                    if(len(node1.node_list) > 0):
                        if(node1.node_list[0].type_node == 'if'):
                            # print("check if")
                            # for child_exp in node1.node_list:
                            #     print("         " + child_exp.type_node)
                            type_exp = node1.node_list[2].getType(symbol_table, error_list)
                            if(type_exp != "type_error" and type_exp != "boolean"):
                                error_list.append("Type error: cannot IF without boolean")
                        if(node1.node_list[0].type_node == 'for'):
                            # print("check for")
                            # for child_exp in node1.node_list:
                            #     print("         " + child_exp.type_node)
                            type_exp_1 = node1.node_list[3].getType(symbol_table, error_list)
                            type_exp_2 = node1.node_list[5].getType(symbol_table, error_list)
                            type_id = node1.node_list[1].getType(symbol_table, error_list)

                            if(type_exp_2 != "type_error" and type_exp_2 != "boolean"):
                                error_list.append("Type error: cannot FOR without boolean")
                            if(type_exp_1 != "type_error" and type_exp_1 != "int"):
                                error_list.append("Type error: cannot FOR without int decl")
                            if(type_id != "type_error" and type_id != "int"):
                                error_list.append("Type error: cannot FOR without id int decl")
                            
                        if(node1.node_list[0].type_node == 'location'):
                            # print("check location")
                            location_type = ""
                            # for child_exp in node1.node_list:
                            #     print("         " + child_exp.type_node)
                            type_1 = node1.node_list[0].getType(symbol_table, error_list)
                            type_2 = node1.node_list[2].getType(symbol_table, error_list)
                            if(type_1 != type_2 and (type_1 != "type_error" and type_2 != "type_error")):
                                error_list.append("Type error: cannot assign " + 
                                node1.node_list[2].getType(symbol_table, error_list) + " in "
                                + node1.node_list[0].getType(symbol_table, error_list))
                        # node1.object_node.typeCheck(node1.node_list, symbol_table, error_list)

                counter+=1
                inner_counter+=1
                if(len(node1.node_list)!=0):
                    counter = node1.semanticAnalysis(symbol_table, counter, error_list)
        return counter