import objects.Symbol as Symbol
import objects.Token as Token
import objects.Program as Program
import parser.ParseDFA as ParseDFA
import re

class Parser:
    def parse(self, tokens, debug):
        main_program = Program.Program(['', '', '', '', '', ''])
        error_list = []
        len_tokens = len(tokens)

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
                main_program.list_nodes[0] = tokens[0]
                main_program.list_nodes[1] = tokens[1]
                main_program.list_nodes[2] = tokens[2]
                main_program.list_nodes[5] = tokens[len_tokens-1]

                if(tokens[3].symbol_type.name != 'type' and tokens[3].symbol_type.name != 'void'):
                    error_list.append("Unexpected token " + tokens[3].symbol_type.name + " at line " + str(tokens[3].line))
                else:
                    print("go")
                    counter_field_decl = 3
                    counter_last_index = 3
                    while((tokens[counter_field_decl].symbol_type.name == 'id' or tokens[counter_field_decl].symbol_type.name == ','
                     or tokens[counter_field_decl].symbol_type.name == ';' or tokens[counter_field_decl].symbol_type.name == 'type') and counter_field_decl<len_tokens-1):
                        print(tokens[counter_field_decl].symbol_type.name)
                        print(counter_field_decl)
                        if(tokens[counter_field_decl].symbol_type.name == ';'):
                            counter_last_index = counter_field_decl
                        counter_field_decl+=1
                    print(counter_field_decl)
                    print(tokens[counter_field_decl].symbol_type.name)
                    print('3 - '+str(counter_last_index))

                    
        # for token in tokens:
        #     print(token.symbol_type.name)
        #tokens --> same structure should be got (class Program { list1 list2 } )

        dfa = ParseDFA.ParseDFA()
        #dfa.accepts(tokens)
        print(debug)
        print(error_list)
        print(main_program.list_nodes)