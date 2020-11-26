import objects.Symbol as Symbol
import objects.Token as Token
import objects.Node as Node
import objects.Program as Program
import parser.ParseDFA as ParseDFA
import re
from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter

class Codegen:
    def codegen(self, main_program, debug):
        # program_ui = main_program.program_tree
        # for pre, fill, node in RenderTree(program_ui):
        #     print("%s%s" % (pre, node.name))
        print("debug", debug)
        for node_irt in main_program.irt_list:
            print(node_irt.instruction)

        
