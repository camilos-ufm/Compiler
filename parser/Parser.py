import objects.Symbol as Symbol
import objects.Token as Token
import objects.Node as Node
import objects.Program as Program
import parser.ParseDFA as ParseDFA
import re
from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter

class Parser:
    def parse(self, tokens, debug):
        main_program = Program.Program(['', '', '', '', '', ''])
        error_list = []
        len_tokens = len(tokens)
        first_step = False 

        if(len_tokens<4):
            print("Not enough tokens to parse")
        else:
            if(tokens[0].symbol_type.name != 'class'):
                error_list.append("Parse error, missing class token")
            
            if(tokens[1].symbol_type.name != 'Program'):
                error_list.append("Parse error, missing Name of class token")

            if(tokens[2].symbol_type.name != '{'):
                error_list.append("Parse error, missing first { token")

            if(tokens[len_tokens-1].symbol_type.name != '}'):
                error_list.append("Parse error, missing last closing } token")

            if(tokens[0].symbol_type.name == 'class' and tokens[1].symbol_type.name == 'Program'
                and tokens[2].symbol_type.name == '{' and tokens[len_tokens-1].symbol_type.name == '}'):
                main_program.node_list[0] = Node.Node(tokens[0], tokens[0].symbol_type.name, [])
                main_program.node_list[1] = Node.Node(tokens[1],tokens[1].symbol_type.name,[])
                main_program.node_list[2] = Node.Node(tokens[2],tokens[2].symbol_type.name,[])
                main_program.node_list[5] = Node.Node(tokens[len_tokens-1],tokens[len_tokens-1].symbol_type.name,[])

                if(tokens[3].symbol_type.name != 'type' and tokens[3].symbol_type.name != 'void' and len_tokens>=5):
                    error_list.append("Unexpected token " + tokens[3].symbol_type.name + " at line " + str(tokens[3].line))
                else:
                    counter_field_decl = 3
                    counter_last_index = 3
                    while((tokens[counter_field_decl].symbol_type.name == 'id' or tokens[counter_field_decl].symbol_type.name == ','
                     or tokens[counter_field_decl].symbol_type.name == ';' or tokens[counter_field_decl].symbol_type.name == 'type') and counter_field_decl<len_tokens-1):
                        if(tokens[counter_field_decl].symbol_type.name == ';'):
                            counter_last_index = counter_field_decl
                        counter_field_decl+=1
                    field_decl_list = []
                    if(3!=counter_last_index):
                        field_decl_list = tokens[3:counter_last_index +1]

                    field_decl_node_list = []
                    for token in field_decl_list:
                        field_decl_node_list.append(Node.Node(token, token.symbol_type.name, []))

                    field_decl_node = Node.Node("<field_decl_list>", "field_decl_list", field_decl_node_list)
                    main_program.node_list[3] = field_decl_node

                    method_decl_list = tokens[counter_last_index+1:len_tokens-1]
                    method_decl_node_list = []
                    for token in method_decl_list:
                        method_decl_node_list.append(Node.Node(token, token.symbol_type.name, []))              

                    method_decl_node = Node.Node("<method_decl_list>", "method_decl_list", method_decl_node_list)
                    main_program.node_list[4] = method_decl_node
                    first_step = True

        if(first_step):
            dfa = ParseDFA.ParseDFA()
            # print("before parse", len(main_program.node_list[3].node_list))
            dfa.parse_field(main_program, main_program.node_list[3], 'field_decl_list', debug)
            # print("after parse", len(main_program.node_list[3].node_list))
            
            # print(main_program.node_list)

            # print("before parse", len(main_program.node_list[4].node_list))
            dfa.parse_method(main_program, main_program.node_list[4], 'method_decl_list', debug)
            # print("after parse", len(main_program.node_list[4].node_list))


            # DotExporter(program_ui).to_picture("AST.png")
            # print(main_program.symbol_table)
            # for field_decl in main_program.getFieldDeclList():
            #     print(field_decl.type_node)      

            # print("---------------")
            # for method_decl in main_program.getMethodDeclList():
            #     print(method_decl.object_node) 
              
        # for token in tokens:
        #     print(token.symbol_type.name)

        #dfa.accepts(tokens)
        if(debug):
            print(error_list)
        #print(main_program.node_list)
        return main_program