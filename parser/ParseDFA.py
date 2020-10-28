import objects.Node as Node
import objects.FieldDecl as FieldDecl
import objects.MethodDecl as MethodDecl
import objects.VarDeclList as VarDeclList
import objects.Block as Block
from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter

class ParseDFA:

    states_stack = [0]

    tokens_stack = ['$']

    grammar = [
        {'<program>': ['class','Program', '{', '}']}
        # {'<X>': ['(', '<X>', ')']},
        # {'<X>': ['(', ')']}
    ]

    dfa_parse = {
            0:{'class':['shift', 1], '<program>':['goto', 5]},
            1:{'Program':['shift', 2]},
            2:{'{':['shift', 3]},
            3:{'}':['shift', 4]},
            4:{'}':['reduce', 1]},
            5:{'$':['accept', 2]}
            # 5:{'(':['reduce', 2], ')':['reduce', 2], '$':['reduce', 2]},
    }

    def parse_field(self, program, main_node, type_dfa):
        error_list = []
        node_list = main_node.node_list
        # print(main_node.type_node)
        if(type_dfa == 'field_decl_list'):
            new_node_list = []
            node_index = 0
            split_indexes = []
            for node in node_list:
                if(node.object_node.symbol_type.name == ';'):
                    split_indexes.append(node_index)
                node_index+=1          
            fields_list = []
            for split in range(len(split_indexes)):
                if(split == 0):
                    fields_list.append(node_list[0:split_indexes[split]+1])
                else:
                    fields_list.append(node_list[split_indexes[split-1]+1:split_indexes[split]+1])
            for field_decl in fields_list:
                if(len(field_decl)<3):
                    error_list.append("Not enough tokens in field declaration at line "+str(field_decl[0].object_node.line))
                if(len(field_decl)==3):
                    if(field_decl[0].object_node.symbol_type.name!='type'):
                        error_list.append("Unexpected token "+ field_decl[0].object_node.symbol_type.name +" at line "+str(field_decl[0].object_node.line))
                    if(field_decl[1].object_node.symbol_type.name!='id'):
                        error_list.append("Unexpected token "+ field_decl[1].object_node.symbol_type.name +" at line "+str(field_decl[1].object_node.line))
                    if(field_decl[2].object_node.symbol_type.name!=';'):
                        error_list.append("Unexpected token "+ field_decl[2].object_node.symbol_type.name +" at line "+str(field_decl[2].object_node.line))
                    if(field_decl[0].object_node.symbol_type.name=='type'
                        and field_decl[1].object_node.symbol_type.name=='id'
                        and field_decl[2].object_node.symbol_type.name==';'):
                        field_obj = FieldDecl.FieldDecl()
                        new_node_list.append(Node.Node(field_obj, "field_decl", [field_decl[0], field_decl[1], field_decl[2]]))
                if(len(field_decl)>3):
                    temp_ids = []
                    id_list_bool = True
                    if(field_decl[0].object_node.symbol_type.name!='type'):
                        error_list.append("Unexpected token "+ field_decl[0].object_node.symbol_type.name +" at line "+str(field_decl[0].object_node.line))
                        id_list_bool = False
                    for id_index in range(1, len(field_decl)-1):
                        if(id_index%2!=0):
                            if(field_decl[id_index].object_node.symbol_type.name != 'id'):
                                error_list.append("Unexpected token "+ field_decl[id_index].object_node.symbol_type.name +" at line "+str(field_decl[id_index].object_node.line))
                                id_list_bool = False
                            else:
                                temp_ids.append(field_decl[id_index])
                        else:
                            if(field_decl[id_index].object_node.symbol_type.name != ','):
                                error_list.append("Unexpected token "+ field_decl[id_index].object_node.symbol_type.name +" at line "+str(field_decl[id_index].object_node.line))
                                id_list_bool = False
                    if(id_list_bool):
                        for temp_id in temp_ids:
                            field_obj = FieldDecl.FieldDecl()
                            new_node_list.append(Node.Node(field_obj, "field_decl", [field_decl[0], temp_id, field_decl[len(field_decl)-1]]))
                # for field in field_decl:
                #     print(field.object_node.symbol_type.name)
            # print(new_node_list)
            # for new_node in new_node_list:
            #     print(new_node.type_node)
            main_node.node_list = new_node_list
            program.node_list[3] = main_node
            # print(main_node.type_node)
        # print(program)

        # program_ui = Node_any("Program")
        # counter=0
        # for node in program.node_list:
        #     nodex = Node_any(node.type_node + str(counter), parent=program_ui)
        #     counter+=1
        #     if(len(node.node_list)!=0 and node.type_node!='method_decl_list'):
        #         for node1 in node.node_list:
        #             nodey = Node_any(node1.type_node + str(counter), parent=nodex)
        #             counter+=1
        #             if(len(node1.node_list)!=0):
        #                 for node2 in node1.node_list:
        #                     nodez = Node_any(node2.type_node + str(counter), parent=nodey)
        #                     counter+=1
        # ceo = Node_any("CEO") #root
        # vp_1 = Node_any("VP_1", parent=ceo)
        # vp_2 = Node_any("VP_2", parent=ceo)
        # gm_1 = Node_any("GM_1", parent=vp_1)
        # gm_2 = Node_any("GM_2", parent=vp_2)

        #DotExporter(program_ui).to_picture("AST.png")
        # print(type_dfa)
        print("error list", error_list)

    def parse_method(self, program, main_node, type_dfa):
        new_node_list_method = []
        error_list = []
        node_list = main_node.node_list
        print(main_node.type_node)
        if(len(node_list)<6):
            error_list.append("Not enough tokens to parse a valid method decl")
        else:
            if(node_list[0].object_node.symbol_type.name != "type" and node_list[0].object_node.symbol_type.name != "void"):
                error_list.append("Unexpected token "+ node_list[0].object_node.symbol_type.name +" at line "+str(node_list[0].object_node.line))
            if(node_list[1].object_node.symbol_type.name != "id"):
                error_list.append("Unexpected token "+ node_list[1].object_node.symbol_type.name +" at line "+str(node_list[1].object_node.line))
            if(node_list[2].object_node.symbol_type.name != "("):
                error_list.append("Unexpected token "+ node_list[2].object_node.symbol_type.name +" at line "+str(node_list[2].object_node.line))
            
            for node_index in range(len(node_list)):
                if(node_index<len(node_list)-3):
                    if(
                        (node_list[node_index].object_node.symbol_type.name == "type" or node_list[node_index].object_node.symbol_type.name == "void") and
                         node_list[node_index+1].object_node.symbol_type.name == "id" and
                         node_list[node_index+2].object_node.symbol_type.name == "("
                    ):
                        #crear nodo method decl
                        method_decl_obj = MethodDecl.MethodDecl()
                        method_decl_node = Node.Node(method_decl_obj, "method_decl", [node_list[node_index], node_list[node_index+1], node_list[node_index+2]])
                        new_node_list_method.append(method_decl_node)
                        print("method decl ", node_list[node_index].object_node.symbol_type.name)
                        print("method decl ", node_list[node_index+1].object_node.symbol_type.name)
                        print("method decl ", node_list[node_index+2].object_node.symbol_type.name)
                        counter_1 = node_index+3
                        child_var_decl_list=[]
                        while(node_list[counter_1].object_node.symbol_type.name != ")" and counter_1<len(node_list)-3):
                            tout_bien = True
                            if(node_list[counter_1].object_node.symbol_type.name == "type"):
                                if(node_list[counter_1+1].object_node.symbol_type.name != "id" 
                                    or (node_list[counter_1+2].object_node.symbol_type.name != "," and node_list[counter_1+2].object_node.symbol_type.name != ")")):
                                    error_list.append("Unexpected token "+ node_list[counter_1].object_node.symbol_type.name +" at line "+str(node_list[counter_1].object_node.line))
                                    tout_bien = False
                                else:
                                    child_var_decl_list.append(node_list[counter_1])
                                    print("node", node_list[counter_1].object_node.symbol_type.name)
                                    print("child var decl list", child_var_decl_list)
                                    print("todo bien")
                            elif(node_list[counter_1].object_node.symbol_type.name == "id"):
                                if((node_list[counter_1+1].object_node.symbol_type.name != "," and node_list[counter_1+1].object_node.symbol_type.name != ")")
                                    or node_list[counter_1-1].object_node.symbol_type.name != "type" ):
                                    error_list.append("Unexpected token "+ node_list[counter_1].object_node.symbol_type.name +" at line "+str(node_list[counter_1].object_node.line))
                                    tout_bien = False
                                else:
                                    child_var_decl_list.append(node_list[counter_1])
                                    print("node", node_list[counter_1].object_node.symbol_type.name)
                                    print("child var decl list", child_var_decl_list)
                                    print("todo bien")   
                            elif(node_list[counter_1].object_node.symbol_type.name == ","):
                                if(node_list[counter_1+1].object_node.symbol_type.name != "type"
                                    or node_list[counter_1-1].object_node.symbol_type.name != "id" ):
                                    error_list.append("Unexpected token "+ node_list[counter_1].object_node.symbol_type.name +" at line "+str(node_list[counter_1].object_node.line))
                                    tout_bien = False
                                else:
                                    child_var_decl_list.append(node_list[counter_1])
                                    print("node", node_list[counter_1].object_node.symbol_type.name)
                                    print("child var decl list", child_var_decl_list)
                                    print("todo bien")  
                            else:
                                error_list.append("Unexpected token "+ node_list[counter_1].object_node.symbol_type.name +" at line "+str(node_list[counter_1].object_node.line))
                                tout_bien = False
                            print(node_list[counter_1].object_node.symbol_type.name)
                            counter_1+=1
                        if(node_list[counter_1].object_node.symbol_type.name != ")"):
                            error_list.append("Missing closing ) in method declaration args")
                        var_decl_object = VarDeclList.VarDeclList()
                        var_decl_node = Node.Node(var_decl_object, "var_decl_list", [])
                        if(tout_bien):
                            var_decl_node.node_list = child_var_decl_list
                        method_decl_node.node_list.append(var_decl_node)
                        method_decl_node.node_list.append(node_list[counter_1])
                        print("counter", counter_1, node_list[counter_1].object_node.symbol_type.name)
                        counter_1+=1
                        block_children_list = []
                        if(node_list[counter_1].object_node.symbol_type.name == "{"):
                                #create block node
                                block_children_list.append(node_list[counter_1])
                                while not(
                                        (node_list[counter_1].object_node.symbol_type.name == "type" or node_list[counter_1].object_node.symbol_type.name == "void") and
                                        node_list[counter_1+1].object_node.symbol_type.name == "id" and
                                        node_list[counter_1+2].object_node.symbol_type.name == "("
                                    ) and counter_1<len(node_list)-2:
                                    print("block", counter_1, node_list[counter_1].object_node.value)
                                    block_children_list.append(node_list[counter_1])
                                    counter_1+=1
                                if(counter_1==len(node_list)-2):
                                    block_children_list.append(node_list[counter_1])
                                    print("block", counter_1, node_list[counter_1].object_node.value) 
                                    block_children_list.append(node_list[counter_1+1])                              
                                    print("block", counter_1, node_list[counter_1+1].object_node.value)
                        #create block node
                        block_object = Block.Block()
                        block_node = Node.Node(block_object, "block", block_children_list)
                        method_decl_node.node_list.append(block_node)
                        # if not(
                        #     (node_list[counter_1].object_node.symbol_type.name == "type" or node_list[counter_1].object_node.symbol_type.name == "void") and
                        #     node_list[counter_1+1].object_node.symbol_type.name == "id" and
                        #     node_list[counter_1+2].object_node.symbol_type.name == "("
                        # ):
            main_node.node_list=new_node_list_method
        print(error_list)

    def accepts(self, token_list):
        #print(''.join(list(self.grammar[1].values())[0]))
        state = 0
        index = 0
        param_list=[]
        print(len(token_list))
        current_token = token_list[index].symbol_type.name
        param_list = self.dfa_parse.get(state).get(current_token)
        print(param_list)
        while index<=len(token_list):
            #print(token_list[index].symbol_type.name)
            print(state)
            if (param_list != None):
                if(param_list[0]=='shift'):
                    current_token = token_list[index].symbol_type.name
                    self.tokens_stack.append(current_token)
                    param_list = self.dfa_parse.get(self.states_stack[-1]).get(current_token)
                    self.states_stack.append(param_list[1])
                    index+=1
                    if(index<len(token_list)):
                        current_token = token_list[index].symbol_type.name
                    param_list = self.dfa_parse.get(self.states_stack[-1]).get(current_token)
                    print("shift")
                elif(param_list[0]=='goto'):
                    print(current_token)
                    print(param_list[1])
                    self.states_stack.append(param_list[1])
                    if(index<len(token_list)):
                        current_token = token_list[index].symbol_type.name
                        param_list = self.dfa_parse.get(self.states_stack[-1]).get(current_token)
                    else:
                        #param_list = self.dfa_parse.get(self.states_stack[-1]).get()
                        print(param_list)
                        self.tokens_stack.pop(-1)
                        self.states_stack.pop(-1)
                        break
                    print('goto')
                elif(param_list[0]=='reduce'):
                    print(param_list[1])
                    node = Node.Node(list(self.grammar[param_list[1]-1].keys())[0], list(self.grammar[param_list[1]-1].values())[0])
                    count = len(list(self.grammar[param_list[1]-1].values())[0])
                    self.tokens_stack = self.tokens_stack[:-count]
                    self.states_stack = self.states_stack[:-(count)]
                    self.tokens_stack.append(list(self.grammar[param_list[1]-1].keys())[0])
                    current_token = self.tokens_stack[-1]
                    print(self.states_stack)
                    param_list = self.dfa_parse.get(self.states_stack[-1]).get(current_token)
                    #self.states_stack.append(param_list[1])
                    print("node list", node.token_list)
                    print("node", node)
                    print("reduce")
                elif(param_list[0]=='accept'):
                    print("accept :)")
            else:
                print("state not defined")
                if(index<len(token_list)):
                    print("unexpected token",token_list[index].symbol_type.name,"at line",token_list[index].line)
                else:
                    print("unexpected token",token_list[index-1].symbol_type.name,"at line",token_list[index-1].line)
                break
            print(self.tokens_stack)
            print(self.states_stack)
            print("------")

        # while index<=len(token_list):
        #     #print(token_list[index].symbol_type.name)
        #     # if(index<len(token_list)):
        #     #     print(token_list[index].symbol_type.name)
        #     #     param_list = self.dfa_parse.get(state).get(token_list[index].symbol_type.name)
        #     # else:
        #     print("TOKEN"+self.tokens_stack[-1])
        #     if(index<len(token_list)):
        #         param_list = self.dfa_parse.get(state).get(token_list[index].symbol_type.name)
        #     else:
        #         param_list = self.dfa_parse.get(state).get(self.tokens_stack[-1])
            
        #     if (param_list != None):
        #         print("param_list:", param_list)
        #         if(param_list[0]=='shift'):
        #             state=param_list[1]
        #             if(index<len(token_list)):
        #                 self.states_stack.append(state)
        #                 self.tokens_stack.append(token_list[index].symbol_type.name)
        #             print("shift")
        #             index+=1
        #         elif(param_list[0]=='goto'):
        #             state=param_list[1]
        #             self.states_stack.append(state)
        #             print("goto")
        #         elif(param_list[0]=='reduce'):
        #             count = len(list(self.grammar[param_list[1]-1].values())[0])
        #             self.tokens_stack = self.tokens_stack[:-count]
        #             self.states_stack = self.states_stack[:-(count-1)]
        #             #state=self.states_stack[-1]
        #             self.tokens_stack.append(list(self.grammar[param_list[1]-1].keys())[0])
        #             print(count)
        #             print("reduce")
        #             index+=1
        #         elif(param_list[0]=='accept'):
        #             print("accept :)")
        #     else:
        #         print("state not defined")
        #     print("state: "+str(state))
        #     print(self.tokens_stack)
        #     print(self.states_stack)
        #     print(index)
        #     print("------")
        print(self.states_stack)
        print(self.tokens_stack)
        if(len(self.tokens_stack)==1 and len(self.states_stack)==1):
            print("NICEEE")
        else:
            print("invalid parsing")
        return True
