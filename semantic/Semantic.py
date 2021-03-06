class Semantic:
    def semantic(self, main_program, debug):
        error_list = []
        #analyze the scope and decl of the variables
        #type of the elements, e.g. EXP

        ### generate symbol table
        counter = 0
        for node in main_program.node_list:
            if(len(node.node_list)==0 and str(type(node.object_node)) == "<class 'objects.Token.Token'>" and node.object_node.symbol_type.name == "{"):
                # print("push scope")
                main_program.symbol_table.append([])
            if(len(node.node_list)==0 and str(type(node.object_node)) == "<class 'objects.Token.Token'>" and node.object_node.symbol_type.name == "}"):
                #del main_program.symbol_table[-1]
                # print("pop scope")
                pass
            counter+=1
            if (len(node.node_list)!=0):
                counter = node.semanticAnalysis(main_program.symbol_table, counter, error_list, main_program.frame_pointer)
        # clprint(main_program.node_list)
        fp = 4
        for symbol in main_program.symbol_table:
            for symbol_in in symbol:
                symbol_in[3] = "$fp-"+str(fp)
                fp+=4

        #print(main_program.symbol_table)
        if(debug):
            for symbol in main_program.symbol_table:
                print(symbol)
            print("error_list", error_list)
        return error_list
        # print(main_program, debug)