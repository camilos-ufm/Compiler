class Semantic:
    def semantic(self, main_program, debug):
        error_list = []
        #analyze the scope and decl of the variables
        #type of the elements, e.g. EXP

        ### generate symbol table
        counter = 0
        for node in main_program.node_list:
            if(len(node.node_list)==0 and node.object_node.symbol_type.name == "{"):
                print("push scope")
                main_program.symbol_table.append([])
            if(len(node.node_list)==0 and node.object_node.symbol_type.name == "}"):
                #del main_program.symbol_table[-1]
                print("pop scope")
            counter+=1
            if (len(node.node_list)!=0):
                counter = node.semanticAnalysis(main_program.symbol_table, counter, error_list)
        # clprint(main_program.node_list)
        for symbol in main_program.symbol_table:
            print(symbol)
        #print(main_program.symbol_table)
        if(debug):
            print("error_list", error_list)
        # print(main_program, debug)