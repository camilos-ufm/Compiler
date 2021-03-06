import objects.Symbol as Symbol
import objects.Token as Token
import objects.Node as Node
import objects.Program as Program
import parser.ParseDFA as ParseDFA
import re
from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter

class Irt:
    def irt(self, main_program, debug):
        # print(main_program, debug, main_program.symbol_table)
        main_program.getAllNodes()

        # program_ui = main_program.program_tree
        # for pre, fill, node in RenderTree(program_ui):
        #     print("%s%s" % (pre, node.name))
        # DotExporter(program_ui).to_picture("AST.pdf")
        # print(main_program.all_nodes)

        main_program.getAllNodesIrt()
        # print(main_program.irt_list)
        if(debug):
            for node_irt in main_program.irt_list:
                try:
                    # print(node_irt.type_irt)
                    print(node_irt.instruction)
                except:
                    print("not an irt node")
        
        return main_program.irt_list