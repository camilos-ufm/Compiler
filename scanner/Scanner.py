import objects.Symbol as Symbol
import objects.Token as Token


class Scanner:
    # symbol list cons
    SYMBOL_LIST = []
    #SYMBOL_LIST.append(Symbol.Symbol(100000, "holaname", "holaregex"))
    SYMBOL_LIST.append(Symbol.Symbol(0, "Token no válido", ""))
    SYMBOL_LIST.append(Symbol.Symbol(1, "class", "class"))
    SYMBOL_LIST.append(Symbol.Symbol(2, "Program", "Program"))
    SYMBOL_LIST.append(Symbol.Symbol(3, "{", "{"))
    SYMBOL_LIST.append(Symbol.Symbol(4, "}", "}"))
    SYMBOL_LIST.append(Symbol.Symbol(5, ",", ","))
    SYMBOL_LIST.append(Symbol.Symbol(6, "[", "["))
    SYMBOL_LIST.append(Symbol.Symbol(7, "]", "]"))
    SYMBOL_LIST.append(Symbol.Symbol(8, ";", ";"))
    SYMBOL_LIST.append(Symbol.Symbol(9, "type", "(boolean)|(int)"))
    SYMBOL_LIST.append(Symbol.Symbol(10, "void", "void"))
    SYMBOL_LIST.append(Symbol.Symbol(11, "if", "if"))
    SYMBOL_LIST.append(Symbol.Symbol(12, "(", "[(]"))
    SYMBOL_LIST.append(Symbol.Symbol(13, ")", "[)]"))
    SYMBOL_LIST.append(Symbol.Symbol(14, "else", "else"))
    SYMBOL_LIST.append(Symbol.Symbol(15, "for", "for"))
    SYMBOL_LIST.append(Symbol.Symbol(16, "return", "return"))
    SYMBOL_LIST.append(Symbol.Symbol(17, "break", "break"))
    SYMBOL_LIST.append(Symbol.Symbol(18, "continue", "continue"))
    SYMBOL_LIST.append(Symbol.Symbol(19, "asign_op", "(+=)|(-=)"))
    SYMBOL_LIST.append(Symbol.Symbol(20, "callout", "callout"))
    SYMBOL_LIST.append(Symbol.Symbol(21, "arit_op", "(+)|(*)|(/)|(%)"))
    SYMBOL_LIST.append(Symbol.Symbol(22, "rel_op", "(<)|(>)|(>=)|(<=)"))
    SYMBOL_LIST.append(Symbol.Symbol(23, "eq_op", "(==)|(!=)"))
    SYMBOL_LIST.append(Symbol.Symbol(24, "cond_op", "[\\|]{2}|[\\&]{2}"))
    SYMBOL_LIST.append(Symbol.Symbol(25, "bool_literal", "(true)|(false)"))
    SYMBOL_LIST.append(Symbol.Symbol(26, "char_literal", "'.'"))
    SYMBOL_LIST.append(Symbol.Symbol(27, "string_literal", ""))
    SYMBOL_LIST.append(Symbol.Symbol(28, "int_literal", ""))
    SYMBOL_LIST.append(Symbol.Symbol(29, "id", ""))
    SYMBOL_LIST.append(Symbol.Symbol(30, "minus_op", "-"))
    SYMBOL_LIST.append(Symbol.Symbol(31, "exclamation_op", "!"))
    SYMBOL_LIST.append(Symbol.Symbol(32, "equal_op", "="))

    def scan(self, input_string):
        token_list = []
        for object_list in input_string:
            for word in object_list[0].split(" "):
                if(word=="class"):
                    tk = Token.Token(self.SYMBOL_LIST[1], object_list[1])
                    token_list.append(tk)
                if(word=="Program"):
                    tk = Token.Token(self.SYMBOL_LIST[2], object_list[1])
                    token_list.append(tk)
                #print(word, object_list[1])
        return token_list