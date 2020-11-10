import objects.Symbol as Symbol
import objects.Token as Token
import scanner.Dfa as Dfa
import re

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
    SYMBOL_LIST.append(Symbol.Symbol(19, "assign_op", "(+=)|(-=)|(=)"))
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
    SYMBOL_LIST.append(Symbol.Symbol(31, "!", "!"))


    def scan(self, input_string, debug):
        error_list = []
        token_list = []
        for object_list in input_string:
            for word in object_list[0].split(" "):
                invalid_token = True
                if(word=="class"):
                    tk = Token.Token(self.SYMBOL_LIST[1], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="Program"):
                    tk = Token.Token(self.SYMBOL_LIST[2], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="{"):
                    tk = Token.Token(self.SYMBOL_LIST[3], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="}"):
                    tk = Token.Token(self.SYMBOL_LIST[4], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word==","):
                    tk = Token.Token(self.SYMBOL_LIST[5], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="["):
                    tk = Token.Token(self.SYMBOL_LIST[6], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="]"):
                    tk = Token.Token(self.SYMBOL_LIST[7], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word==";"):
                    tk = Token.Token(self.SYMBOL_LIST[8], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="boolean" or word=="int" or word=="char" or word=="string"):
                    tk = Token.Token(self.SYMBOL_LIST[9], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="void"):
                    tk = Token.Token(self.SYMBOL_LIST[10], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="if"):
                    tk = Token.Token(self.SYMBOL_LIST[11], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="("):
                    tk = Token.Token(self.SYMBOL_LIST[12], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word==")"):
                    tk = Token.Token(self.SYMBOL_LIST[13], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="else"):
                    tk = Token.Token(self.SYMBOL_LIST[14], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="for"):
                    tk = Token.Token(self.SYMBOL_LIST[15], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="return"):
                    tk = Token.Token(self.SYMBOL_LIST[16], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="break"):
                    tk = Token.Token(self.SYMBOL_LIST[17], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="continue"):
                    tk = Token.Token(self.SYMBOL_LIST[18], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="+=" or word=="-="  or word == "="):
                    tk = Token.Token(self.SYMBOL_LIST[19], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="callout"):
                    tk = Token.Token(self.SYMBOL_LIST[20], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="+" or word=="*" or word == "/" or word == "%"):
                    tk = Token.Token(self.SYMBOL_LIST[21], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="<" or word == ">" or word == ">=" or word == "<="):
                    tk = Token.Token(self.SYMBOL_LIST[22], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="==" or word == "!="):
                    tk = Token.Token(self.SYMBOL_LIST[23], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="cond_op"):
                    tk = Token.Token(self.SYMBOL_LIST[24], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="true" or word=="false"):
                    tk = Token.Token(self.SYMBOL_LIST[25], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="-"):
                    tk = Token.Token(self.SYMBOL_LIST[30], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                elif(word=="!"):
                    tk = Token.Token(self.SYMBOL_LIST[31], object_list[1], word)
                    token_list.append(tk)
                    invalid_token = False
                else:
                    valid_word = False
                    #TODO:
                    # regEx for ID ([alpha] [alpha_num]*)
                        # alpha = [a-zA-Z]
                        # alpha_num = [alpha] or [digit]
                            # digit = [0-9]
                    # regEx for hex_digit
                        # [digit] or [a-fA-F]
                    # regex for int_literal (hex_literal or decimal_literal)
                        # hex_literal = 0x [hex_digit] [hex_digit]*
                        # decimal_literal = [digit] [digit]*
                    # condition for string_literal
                        # " [char]* "
                    # condition for char_literal
                        # ' [char] '
                    
                    # ID
                    # if(bool(re.match("([a-zA-Z_]([a-zA-Z_]|[0-9])*)", word))):
                    dfa = Dfa.Dfa()

                    if(dfa.accepts("id", word)):
                        valid_word=True
                        tk = Token.Token(self.SYMBOL_LIST[29], object_list[1], word)
                        token_list.append(tk)
                        invalid_token = False

                    # INT_LITERAL
                    # if(bool(re.match("(0x[0-9a-fA-F]+)|([0-9]+)", word))):
                    if(dfa.accepts("int", word)):
                        valid_word=True
                        tk = Token.Token(self.SYMBOL_LIST[28], object_list[1], word)
                        token_list.append(tk)
                        invalid_token = False

                    if("[" in word):
                        if("]" in word):
                            if(bool(re.match("^([a-z]|[A-Z])+\[[0-9]+\]$", word))):
                                valid_word=True
                                tk = Token.Token(self.SYMBOL_LIST[29], object_list[1], word)
                                token_list.append(tk)
                                invalid_token = False
                        else:
                            error_list.append(f"Missing one ] in line {object_list[1]}")

                    if ("\"" in word):
                        if(word[-1]=="\""):
                            tk = Token.Token(self.SYMBOL_LIST[27], object_list[1], word)
                            token_list.append(tk)
                            invalid_token = False
                        else:
                            error_list.append(f"wrong string, missing one \" in line {object_list[1]}")
                    if ("\'" in word):
                        if(word[-1]=="\'" and len(word)==3):
                            tk = Token.Token(self.SYMBOL_LIST[26], object_list[1], word)
                            token_list.append(tk)
                            invalid_token = False
                        else:
                            error_list.append(f"wrong char, missing one \' or too many chars in line {object_list[1]}")
                    #print("RIP TOKEN: " + word)
                if(invalid_token):
                    error_list.append("invalid token found in line " + str(object_list[1]))
        if(debug):
            for token in token_list:
                print(token.pretty_print())
        for error in error_list:
            print("Lexical error: "+error)

        return token_list, error_list