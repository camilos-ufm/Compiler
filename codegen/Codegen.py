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
    def __init__(self):
        self.if_bool_counter = 0
        self.method_counter_python = 0
        self.first_method = ""

    def codegen(self, main_program, debug):
        code_list = []
        code_list_2 = []
        # program_ui = main_program.program_tree
        # for pre, fill, node in RenderTree(program_ui):
        #     print("%s%s" % (pre, node.name))
        # print("debug", debug)
        for node_irt in main_program.irt_list:
            return_code = self.translateASM(node_irt.instruction)
            if(return_code != None):
                if(type(return_code) is list):
                    for return_code_item in return_code:
                        code_list.append(return_code_item)
                else:
                    code_list.append(return_code)
        for node_irt in main_program.irt_list:
            return_code = self.translatePython(node_irt.instruction)
            if(return_code != None):
                if(type(return_code) is list):
                    for return_code_item in return_code:
                        code_list_2.append(return_code_item)
                else:
                    code_list_2.append(return_code)
        return code_list,code_list_2
    def translatePython(self, instruction):
        if(instruction[0]=="LABEL"):
            if(self.method_counter_python == 0):
                self.method_counter_python+=1
                # ins0 = "if __name__ == \"__main__\":"
                self.first_method = "   "+instruction[1]+"()"
                ins1 = "def "+instruction[1]+"():"
                ins2 = "    print(\"holarip\")"
                return [ins1,ins2]
            else:
                ins1 = "def "+instruction[1]+"():"
                ins2 = "    pass"
                return [ins1,ins2]
        if(instruction[0]=="EndProgram"):
            ins0 = "if __name__ == \"__main__\":"
            return [ins0,self.first_method]
            
    def translateASM(self, instruction):
        # print("ASM:", instruction)
        #analyze instruction, create new instruction in ASM
        if(instruction[0]=="StartProgram"):
            ins1 = "        .data"
            ins2 = "msg:    .asciiz \"Hello World\""
            ins3 = "        .text"
            return [ins1, ins2, ins3]
        elif(instruction[0]=="LABEL"):
            ins1 = instruction[1]+":"
            return ins1
        elif(instruction[0]=="MOVE"):
            if(len(instruction)==4):
                if(type(instruction[3]) is not list):
                    if(instruction[3][0:4] == "$fp-"):
                        ins4 = "    # moving var2 into var1"
                        ins2 = "    lw $t1, "+instruction[3][4:]+"($fp)"
                        ins3 = "    sw $t1, " +instruction[1][4:]+"($fp)"
                        return [ins4, ins2, ins3]
                    else:
                        ins4 = "    # load immediate literal into var1"
                        ins1 = "    li $t1, "+instruction[3]
                        ins2 = "    sw $t1, "+instruction[1][4:]+"($fp)"
                        return [ins4, ins1, ins2]
                else:
                    ins1 = "    # intermidate operetions to var 1"
                    instruction_list = []
                    instruction_list.append(ins1)

                    temp_instruction_list = []

                    temp_instruction_list.append("    sw $t9, " +instruction[1][4:]+"($fp)")
                    deep_level = 9
                    current_list = instruction[3]
                    while(deep_level>=0 and (type(current_list) is list)):
                        # print(current_list, deep_level)
                        if(current_list[1] == '+'):
                            #add save, s1, s2
                            temp_instruction_list.append("    add $t"+str(deep_level) +", $t"+str(deep_level-1) + ", $t0")
                            if(current_list[2][0:4] == "$fp-"):
                                temp_instruction_list.append("    lw $t0, " +current_list[2][4:]+"($fp)")
                            else:
                                temp_instruction_list.append("    li $t0, " +current_list[2])
                            if(type(current_list[0]) is not list):
                                if(current_list[0][0:4] == "$fp-"):
                                    temp_instruction_list.append("    lw $t"+ str(deep_level-1) +", " +current_list[0][4:]+"($fp)")
                                else:
                                    temp_instruction_list.append("    li $t"+ str(deep_level-1) +", " +current_list[0])
                        elif(current_list[1] == '-'):
                            #sub save, r1, r2
                            temp_instruction_list.append("    sub $t"+str(deep_level) +", $t"+str(deep_level-1) + ", $t0")
                            if(current_list[2][0:4] == "$fp-"):
                                temp_instruction_list.append("    lw $t0, " +current_list[2][4:]+"($fp)")
                            else:
                                temp_instruction_list.append("    li $t0, " +current_list[2])
                            if(type(current_list[0]) is not list):
                                if(current_list[0][0:4] == "$fp-"):
                                    temp_instruction_list.append("    lw $t"+ str(deep_level-2) +", " +current_list[2][4:]+"($fp)")
                                else:
                                    temp_instruction_list.append("    li $t"+ str(deep_level-2) +", " +current_list[2])
                        elif(current_list[1] == '*'):
                            #mul save, m1, m2
                            temp_instruction_list.append("    mul $t"+str(deep_level) +", $t"+str(deep_level-1) + ", $t0")
                            if(current_list[2][0:4] == "$fp-"):
                                temp_instruction_list.append("    lw $t0, " +current_list[2][4:]+"($fp)")
                            else:
                                temp_instruction_list.append("    li $t0, " +current_list[2])
                            if(type(current_list[0]) is not list):
                                if(current_list[0][0:4] == "$fp-"):
                                    temp_instruction_list.append("    lw $t"+ str(deep_level-2) +", " +current_list[2][4:]+"($fp)")
                                else:
                                    temp_instruction_list.append("    li $t"+ str(deep_level-2) +", " +current_list[2])
                        elif(current_list[1] == '/'):
                            #div d1/d2
                            #sw lo save
                            temp_instruction_list.append("    move $t"+str(deep_level) + ", mflo")
                            temp_instruction_list.append("    div $t"+str(deep_level-1) + ", $t0")
                            if(current_list[2][0:4] == "$fp-"):
                                temp_instruction_list.append("    lw $t0, " +current_list[2][4:]+"($fp)")
                            else:
                                temp_instruction_list.append("    li $t0, " +current_list[2])
                            if(type(current_list[0]) is not list):
                                if(current_list[0][0:4] == "$fp-"):
                                    temp_instruction_list.append("    lw $t"+ str(deep_level-2) +", " +current_list[2][4:]+"($fp)")
                                else:
                                    temp_instruction_list.append("    li $t"+ str(deep_level-2) +", " +current_list[2])
                        current_list = current_list[0]
                        deep_level-=1

                    for temp_instruction in temp_instruction_list[::-1]:
                        instruction_list.append(temp_instruction)
                    return instruction_list
        elif(instruction[0]=="SUM"):
            if(instruction[3][0:4] == "$fp-"):
                ins1 = "    # sums var1 + var2, saves in var1"
                ins2 = "    lw $t0, "+instruction[1][4:]+"($fp)"
                ins3 = "    lw $t1, "+instruction[3][4:]+"($fp)"
                ins4 = "    add $t3, $t0, $t1"
                ins5 = "    sw $t3, "+instruction[1][4:]+"($fp)"
                return [ins1, ins2, ins3, ins4, ins5]
            else:
                ins1 = "    # sums var1 + immediate, saves in var1"
                ins2 = "    lw $t0, "+instruction[1][4:]+"($fp)"
                ins3 = "    li $t1, "+instruction[3]
                ins4 = "    add $t3, $t0, $t1"
                ins5 = "    sw $t3, "+instruction[1][4:]+"($fp)"
                return [ins1, ins2, ins3, ins4, ins5]                
        elif(instruction[0]=="MINUS"):
            if(instruction[3][0:4] == "$fp-"):
                ins1 = "    # subs var1 + var2, saves in var1"
                ins2 = "    lw $t0, "+instruction[1][4:]+"($fp)"
                ins3 = "    lw $t1, "+instruction[3][4:]+"($fp)"
                ins4 = "    sub $t3, $t0, $t1"
                ins5 = "    sw $t3, "+instruction[1][4:]+"($fp)"
                return [ins1, ins2, ins3, ins4, ins5]
            else:
                ins1 = "    # subs var1 + immediate, saves in var1"
                ins2 = "    lw $t0, "+instruction[1][4:]+"($fp)"
                ins3 = "    li $t1, "+instruction[3]
                ins4 = "    sub $t3, $t0, $t1"
                ins5 = "    sw $t3, "+instruction[1][4:]+"($fp)"
                return [ins1, ins2, ins3, ins4, ins5]
        elif(instruction[0]=="IF_BOOL"):
            instruction_list = []
            instruction_list.append("    # loads data into t1, t0, set s_ to verify ifs")
            if(instruction[3][1]=='=='):
                if(instruction[3][0][0:4] == "$fp-"):
                    instruction_list.append("    lw $t0, " +instruction[3][0][4:]+"($fp)")
                else:
                    instruction_list.append("    li $t0, " +instruction[3][0])
                if(instruction[3][2][0:4] == "$fp-"):
                    instruction_list.append("    lw $t1, " +instruction[3][2][4:]+"($fp)")
                else:
                    instruction_list.append("    li $t1, " +instruction[3][2])
                instruction_list.append("    seq $s"+str(self.if_bool_counter) + ", $t0, $t1")
            elif(instruction[3][1]=='<'):
                if(instruction[3][0][0:4] == "$fp-"):
                    instruction_list.append("    lw $t0, " +instruction[3][0][4:]+"($fp)")
                else:
                    instruction_list.append("    li $t0, " +instruction[3][0])
                if(instruction[3][2][0:4] == "$fp-"):
                    instruction_list.append("    lw $t1, " +instruction[3][2][4:]+"($fp)")
                else:
                    instruction_list.append("    li $t1, " +instruction[3][2])
                instruction_list.append("    slt $s"+str(self.if_bool_counter) + ", $t0, $t1")
            elif(instruction[3][1]=='>'):
                if(instruction[3][0][0:4] == "$fp-"):
                    instruction_list.append("    lw $t0, " +instruction[3][0][4:]+"($fp)")
                else:
                    instruction_list.append("    li $t0, " +instruction[3][0])
                if(instruction[3][2][0:4] == "$fp-"):
                    instruction_list.append("    lw $t1, " +instruction[3][2][4:]+"($fp)")
                else:
                    instruction_list.append("    li $t1, " +instruction[3][2])
                instruction_list.append("    sgt $s"+str(self.if_bool_counter) + ", $t0, $t1")
            elif(instruction[3][1]=='<='):
                if(instruction[3][0][0:4] == "$fp-"):
                    instruction_list.append("    lw $t0, " +instruction[3][0][4:]+"($fp)")
                else:
                    instruction_list.append("    li $t0, " +instruction[3][0])
                if(instruction[3][2][0:4] == "$fp-"):
                    instruction_list.append("    lw $t1, " +instruction[3][2][4:]+"($fp)")
                else:
                    instruction_list.append("    li $t1, " +instruction[3][2])
                instruction_list.append("    sle $s"+str(self.if_bool_counter) + ", $t0, $t1")
            elif(instruction[3][1]=='>='):
                if(instruction[3][0][0:4] == "$fp-"):
                    instruction_list.append("    lw $t0, " +instruction[3][0][4:]+"($fp)")
                else:
                    instruction_list.append("    li $t0, " +instruction[3][0])
                if(instruction[3][2][0:4] == "$fp-"):
                    instruction_list.append("    lw $t1, " +instruction[3][2][4:]+"($fp)")
                else:
                    instruction_list.append("    li $t1, " +instruction[3][2])
                instruction_list.append("    sge $s"+str(self.if_bool_counter) + ", $t0, $t1")
            #todo && and ||
            # print(self.if_bool_counter)
            self.if_bool_counter+=1
            return instruction_list
        elif(instruction[0]=="if"):
            instruction_list = []
            instruction_list.append("    # jump if condition")
            instruction_list.append("    li $t0, 1")
            instruction_list.append("    beq $s"+str(self.if_bool_counter-1) + ", $t0, "+ instruction[3])
            return instruction_list
        elif(instruction[0]=="if not"):
            instruction_list = []
            instruction_list.append("    # jump if not condition")
            instruction_list.append("    beq $s"+str(self.if_bool_counter-1) + ", $zero, "+ instruction[3])
            return instruction_list
        elif(instruction[0]=="EndProgram"):
            instruction_list = []
            instruction_list.append("    # end of program")
            instruction_list.append("    jr $ra")
            return instruction_list