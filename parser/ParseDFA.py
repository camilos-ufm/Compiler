class ParseDFA:

    states_stack = [0]

    tokens_stack = ['$']

    grammar = [
        {'<S>': ['<X>', '$']},
        {'<X>': ['(', '<X>', ')']},
        {'<X>': ['(', ')']}
    ]

    dfa_parse = {
            0:{'(':['shift', 2], '<X>':['goto', 1]},
            1:{'$':['accept', 2]},
            2:{'(':['shift', 2], ')':['shift', 4], '<X>':['goto', 3]},
            3:{')':['shift', 5]},
            4:{'(':['reduce', 3], ')':['reduce', 3], '$':['reduce', 3]},
            5:{'(':['reduce', 2], ')':['reduce', 2], '$':['reduce', 2]},
    }

    def shift_to(self, state, token):
        print(state, token)

    def go_to(self, state):
        print(state)

    def reduce_to(self, index):
        print(index)

    def accepts(self, token_list):
        #print(''.join(list(self.grammar[1].values())[0]))
        state = 0
        index = 0
        param_list=[]
        print(len(token_list))
        current_token = token_list[index].symbol_type.name
        param_list = self.dfa_parse.get(state).get(current_token)
        print(param_list)
        while index<=len(token_list):
            #print(token_list[index].symbol_type.name)
            if (param_list != None):
                if(param_list[0]=='shift'):
                    current_token = token_list[index].symbol_type.name
                    self.tokens_stack.append(current_token)
                    param_list = self.dfa_parse.get(self.states_stack[-1]).get(current_token)
                    self.states_stack.append(param_list[1])
                    param_list = self.dfa_parse.get(self.states_stack[-1]).get(current_token)
                    print("shift")
                    index+=1
                elif(param_list[0]=='goto'):
                    print(current_token)
                    print(param_list[1])
                    self.states_stack.append(param_list[1])
                    if(index<len(token_list)):
                        current_token = token_list[index].symbol_type.name
                        param_list = self.dfa_parse.get(self.states_stack[-1]).get(current_token)
                    else:
                        #param_list = self.dfa_parse.get(self.states_stack[-1]).get()
                        print("hola", self.tokens_stack[-1])
                        print(param_list)
                        self.tokens_stack.pop(-1)
                        self.states_stack.pop(-1)
                        break
                    print('goto')
                elif(param_list[0]=='reduce'):
                    print(param_list[1])
                    count = len(list(self.grammar[param_list[1]-1].values())[0])
                    self.tokens_stack = self.tokens_stack[:-count]
                    self.states_stack = self.states_stack[:-(count)]
                    self.tokens_stack.append(list(self.grammar[param_list[1]-1].keys())[0])
                    current_token = self.tokens_stack[-1]
                    param_list = self.dfa_parse.get(self.states_stack[-1]).get(current_token)
                    #self.states_stack.append(param_list[1])
                    print("reduce")
                elif(param_list[0]=='accept'):
                    print("accept :)")
            else:
                print("state not defined")
            print(self.tokens_stack)
            print(self.states_stack)
            print("------")

        # while index<=len(token_list):
        #     #print(token_list[index].symbol_type.name)
        #     # if(index<len(token_list)):
        #     #     print(token_list[index].symbol_type.name)
        #     #     param_list = self.dfa_parse.get(state).get(token_list[index].symbol_type.name)
        #     # else:
        #     print("TOKEN"+self.tokens_stack[-1])
        #     if(index<len(token_list)):
        #         param_list = self.dfa_parse.get(state).get(token_list[index].symbol_type.name)
        #     else:
        #         param_list = self.dfa_parse.get(state).get(self.tokens_stack[-1])
            
        #     if (param_list != None):
        #         print("param_list:", param_list)
        #         if(param_list[0]=='shift'):
        #             state=param_list[1]
        #             if(index<len(token_list)):
        #                 self.states_stack.append(state)
        #                 self.tokens_stack.append(token_list[index].symbol_type.name)
        #             print("shift")
        #             index+=1
        #         elif(param_list[0]=='goto'):
        #             state=param_list[1]
        #             self.states_stack.append(state)
        #             print("goto")
        #         elif(param_list[0]=='reduce'):
        #             count = len(list(self.grammar[param_list[1]-1].values())[0])
        #             self.tokens_stack = self.tokens_stack[:-count]
        #             self.states_stack = self.states_stack[:-(count-1)]
        #             #state=self.states_stack[-1]
        #             self.tokens_stack.append(list(self.grammar[param_list[1]-1].keys())[0])
        #             print(count)
        #             print("reduce")
        #             index+=1
        #         elif(param_list[0]=='accept'):
        #             print("accept :)")
        #     else:
        #         print("state not defined")
        #     print("state: "+str(state))
        #     print(self.tokens_stack)
        #     print(self.states_stack)
        #     print(index)
        #     print("------")
        print(self.states_stack)
        print(self.tokens_stack)
        if(len(self.tokens_stack)==1 and len(self.states_stack)==1):
            print("NICEEE")
        else:
            print("invalid parsing")
        return True