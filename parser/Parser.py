import objects.Symbol as Symbol
import objects.Token as Token
import parser.ParseDFA as ParseDFA
import re

class Parser:
    def parse(self, tokens, debug):
        print(tokens)
        print(debug)