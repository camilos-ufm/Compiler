import objects.Symbol as Symbol
import objects.Token as Token
import parser.ParseDFA as ParseDFA
import re

class Parser:
    def parse(self, tokens, debug):
        print(tokens)

        #tokens --> same structure should be got (class Program { list1 list2 } )

        dfa = ParseDFA.ParseDFA()
        #dfa.accepts(tokens)
        print(debug)