import objects.Node as Node
import objects.FieldDecl as FieldDecl
import objects.MethodDecl as MethodDecl
import objects.VarDeclList as VarDeclList
import objects.Block as Block
from anytree import Node as Node_any
from anytree import RenderTree
from anytree.exporter import DotExporter

class ParseDFA:

    states_stack = [0]

    tokens_stack = ['$']

    grammar = [
        {'<program>': ['class','Program', '{', '}']}
        # {'<X>': ['(', '<X>', ')']},
        # {'<X>': ['(', ')']}
    ]

    grammer_1 = [
        {'block': ['{', 'statement_list', '}']},  # 1
        {'statement_list': ['statement']},  # 2
        {'statement_list': ['statement', 'statement_list']},  # 3
        {'var_decl': ['type', 'id', ';']},  # 4
        {'statement': ['location', 'assign_op', 'expr', ';']},  # 5
        {'statement': ['method_call', ';']},  # 6
        {'statement': ['if', '(', 'expr', ')', 'block']},  # 7
        {'statement': ['if', '(', 'expr', ')',
                         'block', 'else', 'block']},  # 8
        {'statement': ['for', 'id', '=',
                         'expr', ',', 'expr', 'block']},  # 9
        {'statement': ['return', ';']},  # 10
        {'statement': ['return', 'expr', ';']},  # 11
        {'statement': ['break', ';']},  # 12
        {'statement': ['continue', ';']},  # 13
        {'statement': ['block']},  # 14
        {'statement': ['var_decl']},  # 15
        {'expr': ['location']},  # 16
        {'expr': ['method_call']},  # 17
        {'expr': ['literal']},  # 18
        {'expr': ['expr', 'bin_op', 'expr']},  # 19
        {'expr': ['-', 'expr']},  # 20
        {'expr': ['!', 'expr']},  # 21
        {'expr': ['(', 'expr', ')']},  # 22
        {'location': ['id']},  # 23
        {'location': ['id', '[', 'expr', ']']},  # 24
        {'method_name': ['id']},  # 25
        {'method_call': ['method_name', '(', ')']},  # 26
        {'method_call': ['method_name', '(', 'expr_list', ')']},  # 27
        {'method_call': ['callout', '(', 'string_literal', ')']},  # 28
        {'method_call': [
            'callout', '(', 'string_literal', ',', 'callout_arg_list', ')']},  # 29
        {'callout_arg_list': ['callout_arg']},  # 30
        {'callout_arg_list': ['callout_arg', 'callout_arg_list']},  # 31
        {'expr_list': ['expr']},  # 32
        {'expr_list': ['expr',',', 'expr_list']},  # 33
        {'callout_arg': ['expr']},  # 34
        {'callout_arg': ['string_literal']},  # 35
        {'bin_op': ['arith_op']},  # 36
        {'bin_op': ['rel_op']},  # 37
        {'bin_op': ['eq_op']},  # 38
        {'bin_op': ['cond_op']},  # 39
        {'cond_op': ['cond_op']},  # 40
        {'eq_op': ['eq_op']},  # 41
        {'rel_op': ['rel_op']},  # 42
        {'arith_op': ['arith_op']},  # 43
        {'literal': ['int_literal']},  # 44
        {'literal': ['char_literal']},  # 45
        {'literal': ['bool_literal']},  # 46
        {'string_literal': ['string_literal']},  # 47
        {'char_literal': ['char_literal']},  # 48
        {'bool_literal': ['bool_literal']},  # 49
        {'int_literal': ['int_literal']},  # 50
        {'id': ['id']},  # 51


    ]

    dfa_parse = {
            0:{'class':['shift', 1], '<program>':['goto', 5]},
            1:{'Program':['shift', 2]},
            2:{'{':['shift', 3]},
            3:{'}':['shift', 4]},
            4:{'}':['reduce', 1]},
            5: {'$': ['accept', 2]}
            
            # 5:{'(':['reduce', 2], ')':['reduce', 2], '$':['reduce', 2]},
    }

    dfa_parse_1 = {
            0:{'{':['shift',1]},
            1:{'}':['reduce',2],'{':['shift',1],'type':['shift',17],'if':['shift',8],'for':['shift',9],'return':['shift',10],'break':['shift',11],'continue':['shift',12],'callout':['shift',16],'id':['shift',15],'statement_list':['goto',2],'statement':['goto',4],'location':['goto',5],'method_call':['goto',6],'block':['goto',13],'var_decl':['goto',14],'method_name':['goto',24]},
            2:{'}':['shift',3]},
            3:{'{':['reduce',1],'}':['reduce',1],',':['reduce',1],'[':['reduce',1],']':['reduce',1],';':['reduce',1],'type':['reduce',1],'void':['reduce',1],'if':['reduce',1],'(':['reduce',1],')':['reduce',1],'else':['reduce',1],'for':['reduce',1],'return':['reduce',1],'break':['reduce',1],'continue':['reduce',1],'assign_op':['reduce',1],'callout':['reduce',1],'arit_op':['reduce',1],'rel_op':['reduce',1],'eq_op':['reduce',1],'cond_op':['reduce',1],'bool_literal':['reduce',1],'char_literal':['reduce',1],'string_literal':['reduce',1],'int_literal':['reduce',1],'id':['reduce',1],'minus_op':['reduce',1],'exclamation_op':['reduce',1],'minus_op':['reduce',1],'exclamation_op':['reduce',1],'statement_list':['reduce',1],'statement':['reduce',1],'location':['reduce',1],'method_call':['reduce',1],'block':['reduce',1],'var_decl':['reduce',1],'expr':['reduce',1],'method_name':['reduce',1],'literal':['reduce',1],'-':['reduce',1],'!':['reduce',1],'=':['reduce',1],'expr_list':['reduce',1],'bin_op':['reduce',1],'callout_arg_list':['reduce',1],'callout_arg':['reduce',1]},
            4:{'{':['shift',0],'}':['reduce',2],',':['reduce',2],'[':['reduce',2],']':['reduce',2],';':['reduce',2],'type':['shift',17],'void':['reduce',2],'if':['shift',8],'(':['reduce',2],')':['reduce',2],'else':['reduce',2],'for':['shift',9],'return':['shift',10],'break':['shift',11],'continue':['shift',12],'assign_op':['reduce',2],'callout':['shift',16],'arit_op':['reduce',2],'rel_op':['reduce',2],'eq_op':['reduce',2],'cond_op':['reduce',2],'bool_literal':['reduce',2],'char_literal':['reduce',2],'string_literal':['reduce',2],'int_literal':['reduce',2],'id':['shift',15],'minus_op':['reduce',2],'exclamation_op':['reduce',2],'minus_op':['reduce',2],'exclamation_op':['reduce',2],'statement_list':['goto',18],'statement':['goto',4],'location':['goto',5],'method_call':['goto',6],'block':['goto',13],'var_decl':['goto',14],'expr':['reduce',2],'method_name':['goto',24],'literal':['reduce',2],'-':['reduce',2],'!':['reduce',2],'=':['reduce',2],'expr_list':['reduce',2],'bin_op':['reduce',2],'callout_arg_list':['reduce',2],'callout_arg':['reduce',2]},
            5:{'assign_op':['shift',19]},
            6:{';':['shift',7],'(':['shift',25]},
            7:{'{':['reduce',6],'}':['reduce',6],',':['reduce',6],'[':['reduce',6],']':['reduce',6],';':['reduce',6],'type':['reduce',6],'void':['reduce',6],'if':['reduce',6],'(':['reduce',6],')':['reduce',6],'else':['reduce',6],'for':['reduce',6],'return':['reduce',6],'break':['reduce',6],'continue':['reduce',6],'assign_op':['reduce',6],'callout':['reduce',6],'arit_op':['reduce',6],'rel_op':['reduce',6],'eq_op':['reduce',6],'cond_op':['reduce',6],'bool_literal':['reduce',6],'char_literal':['reduce',6],'string_literal':['reduce',6],'int_literal':['reduce',6],'id':['reduce',6],'minus_op':['reduce',6],'exclamation_op':['reduce',6],'minus_op':['reduce',6],'exclamation_op':['reduce',6],'statement_list':['reduce',6],'statement':['reduce',6],'location':['reduce',6],'method_call':['reduce',6],'block':['reduce',6],'var_decl':['reduce',6],'expr':['reduce',6],'method_name':['reduce',6],'literal':['reduce',6],'-':['reduce',6],'!':['reduce',6],'=':['reduce',6],'expr_list':['reduce',6],'bin_op':['reduce',6],'callout_arg_list':['reduce',6],'callout_arg':['reduce',6]},
            8:{'(':['shift',20]},
            9:{'id':['shift',21]},
            10:{';':['shift',22],'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',27],'expr':['goto',32],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34]},
            11:{';':['shift',36]},
            12:{';':['shift',37]},
            13:{'{':['reduce',14],'}':['reduce',14],',':['reduce',14],'[':['reduce',14],']':['reduce',14],';':['reduce',14],'type':['reduce',14],'void':['reduce',14],'if':['reduce',14],'(':['reduce',14],')':['reduce',14],'else':['reduce',14],'for':['reduce',14],'return':['reduce',14],'break':['reduce',14],'continue':['reduce',14],'assign_op':['reduce',14],'callout':['reduce',14],'arit_op':['reduce',14],'rel_op':['reduce',14],'eq_op':['reduce',14],'cond_op':['reduce',14],'bool_literal':['reduce',14],'char_literal':['reduce',14],'string_literal':['reduce',14],'int_literal':['reduce',14],'id':['reduce',14],'minus_op':['reduce',14],'exclamation_op':['reduce',14],'minus_op':['reduce',14],'exclamation_op':['reduce',14],'statement_list':['reduce',14],'statement':['reduce',14],'location':['reduce',14],'method_call':['reduce',14],'block':['reduce',14],'var_decl':['reduce',14],'expr':['reduce',14],'method_name':['reduce',14],'literal':['reduce',14],'-':['reduce',14],'!':['reduce',14],'=':['reduce',14],'expr_list':['reduce',14],'bin_op':['reduce',14],'callout_arg_list':['reduce',14],'callout_arg':['reduce',14]},
            14:{'{':['reduce',15],'}':['reduce',15],',':['reduce',15],'[':['reduce',15],']':['reduce',15],';':['reduce',15],'type':['reduce',15],'void':['reduce',15],'if':['reduce',15],'(':['reduce',15],')':['reduce',15],'else':['reduce',15],'for':['reduce',15],'return':['reduce',15],'break':['reduce',15],'continue':['reduce',15],'assign_op':['reduce',15],'callout':['reduce',15],'arit_op':['reduce',15],'rel_op':['reduce',15],'eq_op':['reduce',15],'cond_op':['reduce',15],'bool_literal':['reduce',15],'char_literal':['reduce',15],'string_literal':['reduce',15],'int_literal':['reduce',15],'id':['reduce',15],'minus_op':['reduce',15],'exclamation_op':['reduce',15],'minus_op':['reduce',15],'exclamation_op':['reduce',15],'statement_list':['reduce',15],'statement':['reduce',15],'location':['reduce',15],'method_call':['reduce',15],'block':['reduce',15],'var_decl':['reduce',15],'expr':['reduce',15],'method_name':['reduce',15],'literal':['reduce',15],'-':['reduce',15],'!':['reduce',15],'=':['reduce',15],'expr_list':['reduce',15],'bin_op':['reduce',15],'callout_arg_list':['reduce',15],'callout_arg':['reduce',15]},
            15:{'{':['reduce',23],'}':['reduce',23],',':['reduce',23],'[':['shift',38],']':['reduce',23],';':['reduce',23],'type':['reduce',23],'void':['reduce',23],'if':['reduce',23],'(':['reduce',25],')':['reduce',23],'else':['reduce',23],'for':['reduce',23],'return':['reduce',23],'break':['reduce',23],'continue':['reduce',23],'assign_op':['reduce',23],'callout':['reduce',23],'arit_op':['reduce',23],'rel_op':['reduce',23],'eq_op':['reduce',23],'cond_op':['reduce',23],'bool_literal':['reduce',23],'char_literal':['reduce',23],'string_literal':['reduce',23],'int_literal':['reduce',23],'id':['reduce',23],'minus_op':['reduce',23],'exclamation_op':['reduce',23],'minus_op':['reduce',23],'exclamation_op':['reduce',23],'statement_list':['reduce',23],'statement':['reduce',23],'location':['reduce',23],'method_call':['reduce',23],'block':['reduce',23],'var_decl':['reduce',23],'expr':['reduce',23],'method_name':['reduce',23],'literal':['reduce',23],'-':['reduce',23],'!':['reduce',23],'=':['reduce',23],'expr_list':['reduce',23],'bin_op':['reduce',23],'callout_arg_list':['reduce',23],'callout_arg':['reduce',23]},
            16:{'(':['shift',39]},
            17:{'id':['shift',40]},
            18:{'{':['reduce',3],'}':['reduce',3],',':['reduce',3],'[':['reduce',3],']':['reduce',3],';':['reduce',3],'type':['reduce',3],'void':['reduce',3],'if':['reduce',3],'(':['reduce',3],')':['reduce',3],'else':['reduce',3],'for':['reduce',3],'return':['reduce',3],'break':['reduce',3],'continue':['reduce',3],'assign_op':['reduce',3],'callout':['reduce',3],'arit_op':['reduce',3],'rel_op':['reduce',3],'eq_op':['reduce',3],'cond_op':['reduce',3],'bool_literal':['reduce',3],'char_literal':['reduce',3],'string_literal':['reduce',3],'int_literal':['reduce',3],'id':['reduce',3],'minus_op':['reduce',3],'exclamation_op':['reduce',3],'minus_op':['reduce',3],'exclamation_op':['reduce',3],'statement_list':['reduce',3],'statement':['reduce',3],'location':['reduce',3],'method_call':['reduce',3],'block':['reduce',3],'var_decl':['reduce',3],'expr':['reduce',3],'method_name':['reduce',3],'literal':['reduce',3],'-':['reduce',3],'!':['reduce',3],'=':['reduce',3],'expr_list':['reduce',3],'bin_op':['reduce',3],'callout_arg_list':['reduce',3],'callout_arg':['reduce',3]},
            19:{'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',27],'expr':['goto',32],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34]},
            20:{'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',27],'expr':['goto',32],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34],'=':['goto',45]},
            21:{'assign_op':['shift',45]},
            22:{'{':['reduce',10],'}':['reduce',10],',':['reduce',10],'[':['reduce',10],']':['reduce',10],';':['reduce',10],'type':['reduce',10],'void':['reduce',10],'if':['reduce',10],'(':['reduce',10],')':['reduce',10],'else':['reduce',10],'for':['reduce',10],'return':['reduce',10],'break':['reduce',10],'continue':['reduce',10],'assign_op':['reduce',10],'callout':['reduce',10],'arit_op':['reduce',10],'rel_op':['reduce',10],'eq_op':['reduce',10],'cond_op':['reduce',10],'bool_literal':['reduce',10],'char_literal':['reduce',10],'string_literal':['reduce',10],'int_literal':['reduce',10],'id':['reduce',10],'minus_op':['reduce',10],'exclamation_op':['reduce',10],'minus_op':['reduce',10],'exclamation_op':['reduce',10],'statement_list':['reduce',10],'statement':['reduce',10],'location':['reduce',10],'method_call':['reduce',10],'block':['reduce',10],'var_decl':['reduce',10],'expr':['reduce',10],'method_name':['reduce',10],'literal':['reduce',10],'-':['reduce',10],'!':['reduce',10],'=':['reduce',10],'expr_list':['reduce',10],'bin_op':['reduce',10],'callout_arg_list':['reduce',10],'callout_arg':['reduce',10]},
            23:{';':['shift',86]},
            24:{'(':['shift',46]},
            25:{'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',27],'expr':['goto',50],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34],'expr_list':['goto',48]},
            26:{'{':['reduce',16],'}':['reduce',16],',':['reduce',16],'[':['reduce',16],']':['reduce',16],']':['reduce',16],']':['reduce',16],']':['reduce',16],']':['reduce',16],']':['reduce',16],']':['reduce',16],']':['reduce',16],'for':['reduce',16],'return':['reduce',16],'break':['reduce',16],'continue':['reduce',16],'assign_op':['reduce',16],'callout':['reduce',16],'arit_op':['reduce',16],'rel_op':['reduce',16],'eq_op':['reduce',16],'cond_op':['reduce',16],'bool_literal':['reduce',16],'char_literal':['reduce',16],'string_literal':['reduce',16],'int_literal':['reduce',16],'id':['reduce',16],'minus_op':['reduce',16],'exclamation_op':['reduce',16],'minus_op':['reduce',16],'exclamation_op':['reduce',16],'statement_list':['reduce',16],'statement':['reduce',16],'location':['reduce',16],'method_call':['reduce',16],'block':['reduce',16],'var_decl':['reduce',16],'expr':['reduce',16],'method_name':['reduce',16],'literal':['reduce',16],'-':['reduce',16],'!':['reduce',16],'=':['reduce',16],'expr_list':['reduce',16],'bin_op':['reduce',16],'callout_arg_list':['reduce',16],'callout_arg':['reduce',16]},
            27:{'{':['reduce',17],'}':['reduce',17],',':['reduce',17],'[':['reduce',17],']':['reduce',17],';':['reduce',17],'type':['reduce',17],'void':['reduce',17],'if':['reduce',17],'(':['shift',51],')':['reduce',17],'else':['reduce',17],'for':['reduce',17],'return':['reduce',17],'break':['reduce',17],'continue':['reduce',17],'assign_op':['reduce',17],'callout':['reduce',17],'arit_op':['reduce',17],'rel_op':['reduce',17],'eq_op':['reduce',17],'cond_op':['reduce',17],'bool_literal':['reduce',17],'char_literal':['reduce',17],'string_literal':['reduce',17],'int_literal':['reduce',17],'id':['reduce',17],'minus_op':['reduce',17],'exclamation_op':['reduce',17],'minus_op':['reduce',17],'exclamation_op':['reduce',17],'statement_list':['reduce',17],'statement':['reduce',17],'location':['reduce',17],'method_call':['goto',27],'block':['reduce',17],'var_decl':['reduce',17],'expr':['reduce',17],'method_name':['reduce',17],'literal':['reduce',17],'-':['reduce',17],'!':['reduce',17],'=':['reduce',17],'expr_list':['reduce',17],'bin_op':['reduce',17],'callout_arg_list':['reduce',17],'callout_arg':['reduce',17]},
            28:{'{':['reduce',18],'}':['reduce',18],',':['reduce',18],'[':['reduce',18],']':['reduce',18],';':['reduce',18],'type':['reduce',18],'void':['reduce',18],'if':['reduce',18],'(':['reduce',18],')':['reduce',18],'else':['reduce',18],'for':['reduce',18],'return':['reduce',18],'break':['reduce',18],'continue':['reduce',18],'assign_op':['reduce',18],'callout':['reduce',18],'arit_op':['reduce',18],'rel_op':['reduce',18],'eq_op':['reduce',18],'cond_op':['reduce',18],'bool_literal':['reduce',18],'char_literal':['reduce',18],'string_literal':['reduce',18],'int_literal':['reduce',18],'id':['reduce',18],'minus_op':['reduce',18],'exclamation_op':['reduce',18],'minus_op':['reduce',18],'exclamation_op':['reduce',18],'statement_list':['reduce',18],'statement':['reduce',18],'location':['reduce',18],'method_call':['reduce',18],'block':['reduce',18],'var_decl':['reduce',18],'expr':['reduce',18],'method_name':['reduce',18],'literal':['reduce',18],'-':['reduce',18],'!':['reduce',18],'=':['reduce',18],'expr_list':['reduce',18],'bin_op':['reduce',18],'callout_arg_list':['reduce',18],'callout_arg':['reduce',18]},
            29:{'{':['reduce',44],'}':['reduce',44],',':['reduce',44],'[':['reduce',44],']':['reduce',44],';':['reduce',44],'type':['reduce',44],'void':['reduce',44],'if':['reduce',44],'(':['reduce',44],')':['reduce',44],'else':['reduce',44],'for':['reduce',44],'return':['reduce',44],'break':['reduce',44],'continue':['reduce',44],'assign_op':['reduce',44],'callout':['reduce',44],'arit_op':['reduce',44],'rel_op':['reduce',44],'eq_op':['reduce',44],'cond_op':['reduce',44],'bool_literal':['reduce',44],'char_literal':['reduce',44],'string_literal':['reduce',44],'int_literal':['reduce',44],'id':['reduce',44],'minus_op':['reduce',44],'exclamation_op':['reduce',44],'minus_op':['reduce',44],'exclamation_op':['reduce',44],'statement_list':['reduce',44],'statement':['reduce',44],'location':['reduce',44],'method_call':['reduce',44],'block':['reduce',44],'var_decl':['reduce',44],'expr':['reduce',44],'method_name':['reduce',44],'literal':['reduce',44],'-':['reduce',44],'!':['reduce',44],'=':['reduce',44],'expr_list':['reduce',44],'bin_op':['reduce',44],'callout_arg_list':['reduce',44],'callout_arg':['reduce',44]},
            30:{'{':['reduce',45],'}':['reduce',45],',':['reduce',45],'[':['reduce',45],']':['reduce',45],';':['reduce',45],'type':['reduce',45],'void':['reduce',45],'if':['reduce',45],'(':['reduce',45],')':['reduce',45],'else':['reduce',45],'for':['reduce',45],'return':['reduce',45],'break':['reduce',45],'continue':['reduce',45],'assign_op':['reduce',45],'callout':['reduce',45],'arit_op':['reduce',45],'rel_op':['reduce',45],'eq_op':['reduce',45],'cond_op':['reduce',45],'bool_literal':['reduce',45],'char_literal':['reduce',45],'string_literal':['reduce',45],'int_literal':['reduce',45],'id':['reduce',45],'minus_op':['reduce',45],'exclamation_op':['reduce',45],'minus_op':['reduce',45],'exclamation_op':['reduce',45],'statement_list':['reduce',45],'statement':['reduce',45],'location':['reduce',45],'method_call':['reduce',45],'block':['reduce',45],'var_decl':['reduce',45],'expr':['reduce',45],'method_name':['reduce',45],'literal':['reduce',45],'-':['reduce',45],'!':['reduce',45],'=':['reduce',45],'expr_list':['reduce',45],'bin_op':['reduce',45],'callout_arg_list':['reduce',45],'callout_arg':['reduce',45]},
            31:{'{':['reduce',46],'}':['reduce',46],',':['reduce',46],'[':['reduce',46],']':['reduce',46],';':['reduce',46],'type':['reduce',46],'void':['reduce',46],'if':['reduce',46],'(':['reduce',46],')':['reduce',46],'else':['reduce',46],'for':['reduce',46],'return':['reduce',46],'break':['reduce',46],'continue':['reduce',46],'assign_op':['reduce',46],'callout':['reduce',46],'arit_op':['reduce',46],'rel_op':['reduce',46],'eq_op':['reduce',46],'cond_op':['reduce',46],'bool_literal':['reduce',46],'char_literal':['reduce',46],'string_literal':['reduce',46],'int_literal':['reduce',46],'id':['reduce',46],'minus_op':['reduce',46],'exclamation_op':['reduce',46],'minus_op':['reduce',46],'exclamation_op':['reduce',46],'statement_list':['reduce',46],'statement':['reduce',46],'location':['reduce',46],'method_call':['reduce',46],'block':['reduce',46],'var_decl':['reduce',46],'expr':['reduce',46],'method_name':['reduce',46],'literal':['reduce',46],'-':['reduce',46],'!':['reduce',46],'=':['reduce',46],'expr_list':['reduce',46],'bin_op':['reduce',46],'callout_arg_list':['reduce',46],'callout_arg':['reduce',46]},
            32:{';':['shift', 43],')':['reduce',19], 'rel_op':['shift',54],'arit_op':['shift',53],'eq_op':['shift',55],'cond_op':['shift',56],'bin_op':['goto',52]},
            33:{'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',27],'expr':['goto',32],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34]},
            34:{'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',27],'expr':['goto',32],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34]},
            35:{'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',27],'expr':['goto',32],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34]},
            36:{'{':['reduce',12],'}':['reduce',12],',':['reduce',12],'[':['reduce',12],']':['reduce',12],';':['reduce',12],'type':['reduce',12],'void':['reduce',12],'if':['reduce',12],'(':['reduce',12],')':['reduce',12],'else':['reduce',12],'for':['reduce',12],'return':['reduce',12],'break':['reduce',12],'continue':['reduce',12],'assign_op':['reduce',12],'callout':['reduce',12],'arit_op':['reduce',12],'rel_op':['reduce',12],'eq_op':['reduce',12],'cond_op':['reduce',12],'bool_literal':['reduce',12],'char_literal':['reduce',12],'string_literal':['reduce',12],'int_literal':['reduce',12],'id':['reduce',12],'minus_op':['reduce',12],'exclamation_op':['reduce',12],'minus_op':['reduce',12],'exclamation_op':['reduce',12],'statement_list':['reduce',12],'statement':['reduce',12],'location':['reduce',12],'method_call':['reduce',12],'block':['reduce',12],'var_decl':['reduce',12],'expr':['reduce',12],'method_name':['reduce',12],'literal':['reduce',12],'-':['reduce',12],'!':['reduce',12],'=':['reduce',12],'expr_list':['reduce',12],'bin_op':['reduce',12],'callout_arg_list':['reduce',12],'callout_arg':['reduce',12]},
            37:{'{':['reduce',13],'}':['reduce',13],',':['reduce',13],'[':['reduce',13],']':['reduce',13],';':['reduce',13],'type':['reduce',13],'void':['reduce',13],'if':['reduce',13],'(':['reduce',13],')':['reduce',13],'else':['reduce',13],'for':['reduce',13],'return':['reduce',13],'break':['reduce',13],'continue':['reduce',13],'assign_op':['reduce',13],'callout':['reduce',13],'arit_op':['reduce',13],'rel_op':['reduce',13],'eq_op':['reduce',13],'cond_op':['reduce',13],'bool_literal':['reduce',13],'char_literal':['reduce',13],'string_literal':['reduce',13],'int_literal':['reduce',13],'id':['reduce',13],'minus_op':['reduce',13],'exclamation_op':['reduce',13],'minus_op':['reduce',13],'exclamation_op':['reduce',13],'statement_list':['reduce',13],'statement':['reduce',13],'location':['reduce',13],'method_call':['reduce',13],'block':['reduce',13],'var_decl':['reduce',13],'expr':['reduce',13],'method_name':['reduce',13],'literal':['reduce',13],'-':['reduce',13],'!':['reduce',13],'=':['reduce',13],'expr_list':['reduce',13],'bin_op':['reduce',13],'callout_arg_list':['reduce',13],'callout_arg':['reduce',13]},
            38:{'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',27],'expr':['goto',32],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34]},
            39:{'string_literal':['shift',63]},
            40:{';':['shift',41]},
            41:{'{':['reduce',4],'}':['reduce',4],',':['reduce',4],'[':['reduce',4],']':['reduce',4],';':['reduce',4],'type':['reduce',4],'void':['reduce',4],'if':['reduce',4],'(':['reduce',4],')':['reduce',4],'else':['reduce',4],'for':['reduce',4],'return':['reduce',4],'break':['reduce',4],'continue':['reduce',4],'assign_op':['reduce',4],'callout':['reduce',4],'arit_op':['reduce',4],'rel_op':['reduce',4],'eq_op':['reduce',4],'cond_op':['reduce',4],'bool_literal':['reduce',4],'char_literal':['reduce',4],'string_literal':['reduce',4],'int_literal':['reduce',4],'id':['reduce',4],'minus_op':['reduce',4],'exclamation_op':['reduce',4],'minus_op':['reduce',4],'exclamation_op':['reduce',4],'statement_list':['reduce',4],'statement':['reduce',4],'location':['reduce',4],'method_call':['reduce',4],'block':['reduce',4],'var_decl':['reduce',4],'expr':['reduce',4],'method_name':['reduce',4],'literal':['reduce',4],'-':['reduce',4],'!':['reduce',4],'=':['reduce',4],'expr_list':['reduce',4],'bin_op':['reduce',4],'callout_arg_list':['reduce',4],'callout_arg':['reduce',4]},
            42:{';':['shift',43]},
            43:{'{':['reduce',5],'}':['reduce',5],',':['reduce',5],'[':['reduce',5],']':['reduce',5],';':['reduce',5],'type':['reduce',5],'void':['reduce',5],'if':['reduce',5],'(':['reduce',5],')':['reduce',5],'else':['reduce',5],'for':['reduce',5],'return':['reduce',5],'break':['reduce',5],'continue':['reduce',5],'assign_op':['reduce',5],'callout':['reduce',5],'arit_op':['reduce',5],'rel_op':['reduce',5],'eq_op':['reduce',5],'cond_op':['reduce',5],'bool_literal':['reduce',5],'char_literal':['reduce',5],'string_literal':['reduce',5],'int_literal':['reduce',5],'id':['reduce',5],'minus_op':['reduce',5],'exclamation_op':['reduce',5],'minus_op':['reduce',5],'exclamation_op':['reduce',5],'statement_list':['reduce',5],'statement':['reduce',5],'location':['reduce',5],'method_call':['reduce',5],'block':['reduce',5],'var_decl':['reduce',5],'expr':['reduce',5],'method_name':['reduce',5],'literal':['reduce',5],'-':['reduce',5],'!':['reduce',5],'=':['reduce',5],'expr_list':['reduce',5],'bin_op':['reduce',5],'callout_arg_list':['reduce',5],'callout_arg':['reduce',5]},
            44:{')':['shift',64]},
            45:{'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',27],'expr':['goto',32],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34],},
            46:{')':['shift',47]},
            47:{'{':['reduce',26],'}':['reduce',26],',':['reduce',26],'[':['reduce',26],']':['reduce',26],';':['reduce',26],'type':['reduce',26],'void':['reduce',26],'if':['reduce',26],'(':['reduce',26],')':['reduce',26],'else':['reduce',26],'for':['reduce',26],'return':['reduce',26],'break':['reduce',26],'continue':['reduce',26],'assign_op':['reduce',26],'callout':['reduce',26],'arit_op':['reduce',26],'rel_op':['reduce',26],'eq_op':['reduce',26],'cond_op':['reduce',26],'bool_literal':['reduce',26],'char_literal':['reduce',26],'string_literal':['reduce',26],'int_literal':['reduce',26],'id':['reduce',26],'minus_op':['reduce',26],'exclamation_op':['reduce',26],'minus_op':['reduce',26],'exclamation_op':['reduce',26],'statement_list':['reduce',26],'statement':['reduce',26],'location':['reduce',26],'method_call':['reduce',26],'block':['reduce',26],'var_decl':['reduce',26],'expr':['reduce',26],'method_name':['reduce',26],'literal':['reduce',26],'-':['reduce',26],'!':['reduce',26],'=':['reduce',26],'expr_list':['reduce',26],'bin_op':['reduce',26],'callout_arg_list':['reduce',26],'callout_arg':['reduce',26]},
            48:{')':['shift',49]},
            49:{'{':['reduce',27],'}':['reduce',27],',':['reduce',27],'[':['reduce',27],']':['reduce',27],';':['reduce',27],'type':['reduce',27],'void':['reduce',27],'if':['reduce',27],'(':['reduce',27],')':['reduce',27],'else':['reduce',27],'for':['reduce',27],'return':['reduce',27],'break':['reduce',27],'continue':['reduce',27],'assign_op':['reduce',27],'callout':['reduce',27],'arit_op':['reduce',27],'rel_op':['reduce',27],'eq_op':['reduce',27],'cond_op':['reduce',27],'bool_literal':['reduce',27],'char_literal':['reduce',27],'string_literal':['reduce',27],'int_literal':['reduce',27],'id':['reduce',27],'minus_op':['reduce',27],'exclamation_op':['reduce',27],'minus_op':['reduce',27],'exclamation_op':['reduce',27],'statement_list':['reduce',27],'statement':['reduce',27],'location':['reduce',27],'method_call':['reduce',27],'block':['reduce',27],'var_decl':['reduce',27],'expr':['reduce',27],'method_name':['reduce',27],'literal':['reduce',27],'-':['reduce',27],'!':['reduce',27],'=':['reduce',27],'expr_list':['reduce',27],'bin_op':['reduce',27],'callout_arg_list':['reduce',27],'callout_arg':['reduce',27]},
            50:{'{':['reduce',32],'}':['reduce',32],',':['shift',66],'[':['reduce',32],']':['reduce',32],';':['reduce',32],'type':['reduce',32],'void':['reduce',32],'if':['reduce',32],'(':['reduce',32],')':['reduce',32],'else':['reduce',32],'for':['reduce',32],'return':['reduce',32],'break':['reduce',32],'continue':['reduce',32],'assign_op':['reduce',32],'callout':['reduce',32],'arit_op':['reduce',32],'rel_op':['reduce',32],'eq_op':['reduce',32],'cond_op':['reduce',32],'bool_literal':['reduce',32],'char_literal':['reduce',32],'string_literal':['reduce',32],'int_literal':['reduce',32],'id':['reduce',32],'minus_op':['reduce',32],'exclamation_op':['reduce',32],'minus_op':['reduce',32],'exclamation_op':['reduce',32],'statement_list':['reduce',32],'statement':['reduce',32],'location':['reduce',32],'method_call':['reduce',32],'block':['reduce',32],'var_decl':['reduce',32],'expr':['goto',66],'method_name':['reduce',32],'literal':['reduce',32],'-':['reduce',32],'!':['reduce',32],'=':['reduce',32],'expr_list':['reduce',32],'bin_op':['reduce',32],'callout_arg_list':['reduce',32],'callout_arg':['reduce',32]},
            51:{'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'int_literal':['shift',29],'id':['shift',15],'location':['goto',28],'method_call':['goto',27],'expr':['goto',32],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34],'expr_list':['shift',67]},
            52:{'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',51],'expr':['goto',32],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34]},
            53:{'{':['reduce',36],'}':['reduce',36],',':['reduce',36],'[':['reduce',36],']':['reduce',36],';':['reduce',36],'type':['reduce',36],'void':['reduce',36],'if':['reduce',36],'(':['reduce',36],')':['reduce',36],'else':['reduce',36],'for':['reduce',36],'return':['reduce',36],'break':['reduce',36],'continue':['reduce',36],'assign_op':['reduce',36],'callout':['reduce',36],'arit_op':['reduce',36],'rel_op':['reduce',36],'eq_op':['reduce',36],'cond_op':['reduce',36],'bool_literal':['reduce',36],'char_literal':['reduce',36],'string_literal':['reduce',36],'int_literal':['reduce',36],'id':['reduce',36],'minus_op':['reduce',36],'exclamation_op':['reduce',36],'minus_op':['reduce',36],'exclamation_op':['reduce',36],'statement_list':['reduce',36],'statement':['reduce',36],'location':['reduce',36],'method_call':['reduce',36],'block':['reduce',36],'var_decl':['reduce',36],'expr':['reduce',36],'method_name':['reduce',36],'literal':['reduce',36],'-':['reduce',36],'!':['reduce',36],'=':['reduce',36],'expr_list':['reduce',36],'bin_op':['reduce',36],'callout_arg_list':['reduce',36],'callout_arg':['reduce',36]},
            54:{'{':['reduce',37],'}':['reduce',37],',':['reduce',37],'[':['reduce',37],']':['reduce',37],';':['reduce',37],'type':['reduce',37],'void':['reduce',37],'if':['reduce',37],'(':['reduce',37],')':['reduce',37],'else':['reduce',37],'for':['reduce',37],'return':['reduce',37],'break':['reduce',37],'continue':['reduce',37],'assign_op':['reduce',37],'callout':['reduce',37],'arit_op':['reduce',37],'rel_op':['reduce',37],'eq_op':['reduce',37],'cond_op':['reduce',37],'bool_literal':['reduce',37],'char_literal':['reduce',37],'string_literal':['reduce',37],'int_literal':['reduce',37],'id':['reduce',37],'minus_op':['reduce',37],'exclamation_op':['reduce',37],'minus_op':['reduce',37],'exclamation_op':['reduce',37],'statement_list':['reduce',37],'statement':['reduce',37],'location':['reduce',37],'method_call':['reduce',37],'block':['reduce',37],'var_decl':['reduce',37],'expr':['reduce',37],'method_name':['reduce',37],'literal':['reduce',37],'-':['reduce',37],'!':['reduce',37],'=':['reduce',37],'expr_list':['reduce',37],'bin_op':['reduce',37],'callout_arg_list':['reduce',37],'callout_arg':['reduce',37]},
            55:{'{':['reduce',38],'}':['reduce',38],',':['reduce',38],'[':['reduce',38],']':['reduce',38],';':['reduce',38],'type':['reduce',38],'void':['reduce',38],'if':['reduce',38],'(':['reduce',38],')':['reduce',38],'else':['reduce',38],'for':['reduce',38],'return':['reduce',38],'break':['reduce',38],'continue':['reduce',38],'assign_op':['reduce',38],'callout':['reduce',38],'arit_op':['reduce',38],'rel_op':['reduce',38],'eq_op':['reduce',38],'cond_op':['reduce',38],'bool_literal':['reduce',38],'char_literal':['reduce',38],'string_literal':['reduce',38],'int_literal':['reduce',38],'id':['reduce',38],'minus_op':['reduce',38],'exclamation_op':['reduce',38],'minus_op':['reduce',38],'exclamation_op':['reduce',38],'statement_list':['reduce',38],'statement':['reduce',38],'location':['reduce',38],'method_call':['reduce',38],'block':['reduce',38],'var_decl':['reduce',38],'expr':['reduce',38],'method_name':['reduce',38],'literal':['reduce',38],'-':['reduce',38],'!':['reduce',38],'=':['reduce',38],'expr_list':['reduce',38],'bin_op':['reduce',38],'callout_arg_list':['reduce',38],'callout_arg':['reduce',38]},
            56:{'{':['reduce',39],'}':['reduce',39],',':['reduce',39],'[':['reduce',39],']':['reduce',39],';':['reduce',39],'type':['reduce',39],'void':['reduce',39],'if':['reduce',39],'(':['reduce',39],')':['reduce',39],'else':['reduce',39],'for':['reduce',39],'return':['reduce',39],'break':['reduce',39],'continue':['reduce',39],'assign_op':['reduce',39],'callout':['reduce',39],'arit_op':['reduce',39],'rel_op':['reduce',39],'eq_op':['reduce',39],'cond_op':['reduce',39],'bool_literal':['reduce',39],'char_literal':['reduce',39],'string_literal':['reduce',39],'int_literal':['reduce',39],'id':['reduce',39],'minus_op':['reduce',39],'exclamation_op':['reduce',39],'minus_op':['reduce',39],'exclamation_op':['reduce',39],'statement_list':['reduce',39],'statement':['reduce',39],'location':['reduce',39],'method_call':['reduce',39],'block':['reduce',39],'var_decl':['reduce',39],'expr':['reduce',39],'method_name':['reduce',39],'literal':['reduce',39],'-':['reduce',39],'!':['reduce',39],'=':['reduce',39],'expr_list':['reduce',39],'bin_op':['reduce',39],'callout_arg_list':['reduce',39],'callout_arg':['reduce',39]},
            57:{'{':['reduce',20],'}':['reduce',20],',':['reduce',20],'[':['reduce',20],']':['reduce',20],';':['reduce',20],'type':['reduce',20],'void':['reduce',20],'if':['reduce',20],'(':['reduce',20],')':['reduce',20],'else':['reduce',20],'for':['reduce',20],'return':['reduce',20],'break':['reduce',20],'continue':['reduce',20],'assign_op':['reduce',20],'callout':['reduce',20],'arit_op':['reduce',20],'rel_op':['reduce',20],'eq_op':['reduce',20],'cond_op':['reduce',20],'bool_literal':['reduce',20],'char_literal':['reduce',20],'string_literal':['reduce',20],'int_literal':['reduce',20],'id':['reduce',20],'minus_op':['reduce',20],'exclamation_op':['reduce',20],'minus_op':['reduce',20],'exclamation_op':['reduce',20],'statement_list':['reduce',20],'statement':['reduce',20],'location':['reduce',20],'method_call':['reduce',20],'block':['reduce',20],'var_decl':['reduce',20],'expr':['reduce',20],'method_name':['reduce',20],'literal':['reduce',20],'-':['reduce',20],'!':['reduce',20],'=':['reduce',20],'expr_list':['reduce',20],'bin_op':['reduce',20],'callout_arg_list':['reduce',20],'callout_arg':['reduce',20]},
            58:{'{':['reduce',21],'}':['reduce',21],',':['reduce',21],'[':['reduce',21],']':['reduce',21],';':['reduce',21],'type':['reduce',21],'void':['reduce',21],'if':['reduce',21],'(':['reduce',21],')':['reduce',21],'else':['reduce',21],'for':['reduce',21],'return':['reduce',21],'break':['reduce',21],'continue':['reduce',21],'assign_op':['reduce',21],'callout':['reduce',21],'arit_op':['reduce',21],'rel_op':['reduce',21],'eq_op':['reduce',21],'cond_op':['reduce',21],'bool_literal':['reduce',21],'char_literal':['reduce',21],'string_literal':['reduce',21],'int_literal':['reduce',21],'id':['reduce',21],'minus_op':['reduce',21],'exclamation_op':['reduce',21],'minus_op':['reduce',21],'exclamation_op':['reduce',21],'statement_list':['reduce',21],'statement':['reduce',21],'location':['reduce',21],'method_call':['reduce',21],'block':['reduce',21],'var_decl':['reduce',21],'expr':['reduce',21],'method_name':['reduce',21],'literal':['reduce',21],'-':['reduce',21],'!':['reduce',21],'=':['reduce',21],'expr_list':['reduce',21],'bin_op':['reduce',21],'callout_arg_list':['reduce',21],'callout_arg':['reduce',21]},
            59:{')':['shift',60]},
            60:{'{':['reduce',22],'}':['reduce',22],',':['reduce',22],'[':['reduce',22],']':['reduce',22],';':['reduce',22],'type':['reduce',22],'void':['reduce',22],'if':['reduce',22],'(':['reduce',22],')':['reduce',22],'else':['reduce',22],'for':['reduce',22],'return':['reduce',22],'break':['reduce',22],'continue':['reduce',22],'assign_op':['reduce',22],'callout':['reduce',22],'arit_op':['reduce',22],'rel_op':['reduce',22],'eq_op':['reduce',22],'cond_op':['reduce',22],'bool_literal':['reduce',22],'char_literal':['reduce',22],'string_literal':['reduce',22],'int_literal':['reduce',22],'id':['reduce',22],'minus_op':['reduce',22],'exclamation_op':['reduce',22],'minus_op':['reduce',22],'exclamation_op':['reduce',22],'statement_list':['reduce',22],'statement':['reduce',22],'location':['reduce',22],'method_call':['reduce',22],'block':['reduce',22],'var_decl':['reduce',22],'expr':['reduce',22],'method_name':['reduce',22],'literal':['reduce',22],'-':['reduce',22],'!':['reduce',22],'=':['reduce',22],'expr_list':['reduce',22],'bin_op':['reduce',22],'callout_arg_list':['reduce',22],'callout_arg':['reduce',22]},
            61:{',':['shift',70],']':['shift',62],')':['shift',70]},
            62:{'{':['reduce',24],'}':['reduce',24],',':['reduce',24],'[':['reduce',24],']':['reduce',24],';':['reduce',24],'type':['reduce',24],'void':['reduce',24],'if':['reduce',24],'(':['reduce',24],')':['reduce',24],'else':['reduce',24],'for':['reduce',24],'return':['reduce',24],'break':['reduce',24],'continue':['reduce',24],'assign_op':['reduce',24],'callout':['reduce',24],'arit_op':['reduce',24],'rel_op':['reduce',24],'eq_op':['reduce',24],'cond_op':['reduce',24],'bool_literal':['reduce',24],'char_literal':['reduce',24],'string_literal':['reduce',24],'int_literal':['reduce',24],'id':['reduce',24],'minus_op':['reduce',24],'exclamation_op':['reduce',24],'minus_op':['reduce',24],'exclamation_op':['reduce',24],'statement_list':['reduce',24],'statement':['reduce',24],'location':['reduce',24],'method_call':['reduce',24],'block':['reduce',24],'var_decl':['reduce',24],'expr':['reduce',24],'method_name':['reduce',24],'literal':['reduce',24],'-':['reduce',24],'!':['reduce',24],'=':['reduce',24],'expr_list':['reduce',24],'bin_op':['reduce',24],'callout_arg_list':['reduce',24],'callout_arg':['reduce',24]},
            63:{',':['shift',71],')':['shift',71],'string_literal':['shift',63]},
            64:{'{':['shift',1],'block':['goto',72]},
            65:{',':['shift',73]},
            66:{'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',27],'expr':['goto',32],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34],'expr_list':['goto',74]},
            67:{')':['shift',68]},
            68:{'{':['reduce',27],'}':['reduce',27],',':['reduce',27],'[':['reduce',27],']':['reduce',27],';':['reduce',27],'type':['reduce',27],'void':['reduce',27],'if':['reduce',27],'(':['reduce',27],')':['reduce',27],'else':['reduce',27],'for':['reduce',27],'return':['reduce',27],'break':['reduce',27],'continue':['reduce',27],'assign_op':['reduce',27],'callout':['reduce',27],'arit_op':['reduce',27],'rel_op':['reduce',27],'eq_op':['reduce',27],'cond_op':['reduce',27],'bool_literal':['reduce',27],'char_literal':['reduce',27],'string_literal':['reduce',27],'int_literal':['reduce',27],'id':['reduce',27],'minus_op':['reduce',27],'exclamation_op':['reduce',27],'minus_op':['reduce',27],'exclamation_op':['reduce',27],'statement_list':['reduce',27],'statement':['reduce',27],'location':['reduce',27],'method_call':['reduce',27],'block':['reduce',27],'var_decl':['reduce',27],'expr':['reduce',27],'method_name':['reduce',27],'literal':['reduce',27],'-':['reduce',27],'!':['reduce',27],'=':['reduce',27],'expr_list':['reduce',27],'bin_op':['reduce',27],'callout_arg_list':['reduce',27],'callout_arg':['reduce',27]},
            69:{'{':['reduce',19],'}':['reduce',19],',':['reduce',19],'[':['reduce',19],']':['reduce',19],';':['reduce',19],'type':['reduce',19],'void':['reduce',19],'if':['reduce',19],'(':['reduce',19],')':['reduce',19],'else':['reduce',19],'for':['reduce',19],'return':['reduce',19],'break':['reduce',19],'continue':['reduce',19],'assign_op':['reduce',19],'callout':['reduce',19],'arit_op':['reduce',19],'rel_op':['reduce',19],'eq_op':['reduce',19],'cond_op':['reduce',19],'bool_literal':['reduce',19],'char_literal':['reduce',19],'string_literal':['reduce',19],'int_literal':['reduce',19],'id':['reduce',19],'minus_op':['reduce',19],'exclamation_op':['reduce',19],'minus_op':['reduce',19],'exclamation_op':['reduce',19],'statement_list':['reduce',19],'statement':['reduce',19],'location':['reduce',19],'method_call':['reduce',19],'block':['reduce',19],'var_decl':['reduce',19],'expr':['reduce',19],'method_name':['reduce',19],'literal':['reduce',19],'-':['reduce',19],'!':['reduce',19],'=':['reduce',19],'expr_list':['reduce',19],'bin_op':['reduce',19],'callout_arg_list':['reduce',19],'callout_arg':['reduce',19]},
            70:{'{':['reduce',28],'}':['reduce',28],',':['reduce',28],'[':['reduce',28],']':['reduce',28],';':['reduce',28],'type':['reduce',28],'void':['reduce',28],'if':['reduce',28],'(':['reduce',28],')':['reduce',28],'else':['reduce',28],'for':['reduce',28],'return':['reduce',28],'break':['reduce',28],'continue':['reduce',28],'assign_op':['reduce',28],'callout':['reduce',28],'arit_op':['reduce',28],'rel_op':['reduce',28],'eq_op':['reduce',28],'cond_op':['reduce',28],'bool_literal':['reduce',28],'char_literal':['reduce',28],'string_literal':['reduce',28],'int_literal':['reduce',28],'id':['reduce',28],'minus_op':['reduce',28],'exclamation_op':['reduce',28],'minus_op':['reduce',28],'exclamation_op':['reduce',28],'statement_list':['reduce',28],'statement':['reduce',28],'location':['reduce',28],'method_call':['reduce',28],'block':['reduce',28],'var_decl':['reduce',28],'expr':['reduce',28],'method_name':['reduce',28],'literal':['reduce',28],'-':['reduce',28],'!':['reduce',28],'=':['reduce',28],'expr_list':['reduce',28],'bin_op':['reduce',28],'callout_arg_list':['reduce',28],'callout_arg':['reduce',28]},
            71:{'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'string_literal':['shift',79],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',27],'expr':['goto',32],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34],'callout_arg_list':['goto',75],'callout_arg':['goto',77]},
            72:{'{':['reduce',7],'}':['reduce',7],',':['reduce',7],'[':['reduce',7],']':['reduce',7],';':['reduce',7],'type':['reduce',7],'void':['reduce',7],'if':['reduce',7],'(':['reduce',7],')':['reduce',7],'else':['shift',80],'for':['reduce',7],'return':['reduce',7],'break':['reduce',7],'continue':['reduce',7],'assign_op':['reduce',7],'callout':['reduce',7],'arit_op':['reduce',7],'rel_op':['reduce',7],'eq_op':['reduce',7],'cond_op':['reduce',7],'bool_literal':['reduce',7],'char_literal':['reduce',7],'string_literal':['reduce',7],'int_literal':['reduce',7],'id':['reduce',7],'minus_op':['reduce',7],'exclamation_op':['reduce',7],'minus_op':['reduce',7],'exclamation_op':['reduce',7],'statement_list':['reduce',7],'statement':['reduce',7],'location':['reduce',7],'method_call':['reduce',7],'block':['reduce',7],'var_decl':['reduce',7],'expr':['reduce',7],'method_name':['reduce',7],'literal':['reduce',7],'-':['reduce',7],'!':['reduce',7],'=':['reduce',7],'expr_list':['reduce',7],'bin_op':['reduce',7],'callout_arg_list':['reduce',7],'callout_arg':['reduce',7]},
            73:{'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',27],'expr':['goto',32],'method_name':['goto',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34]},
            74:{'{':['reduce',33],'{':['reduce',33],',':['reduce',33],'[':['reduce',33],']':['reduce',33],';':['reduce',33],'type':['reduce',33],'void':['reduce',33],'if':['reduce',33],'(':['reduce',33],')':['reduce',33],'else':['reduce',33],'for':['reduce',33],'return':['reduce',33],'break':['reduce',33],'continue':['reduce',33],'assign_op':['reduce',33],'callout':['reduce',33],'arit_op':['reduce',33],'rel_op':['reduce',33],'eq_op':['reduce',33],'cond_op':['reduce',33],'bool_literal':['reduce',33],'char_literal':['reduce',33],'string_literal':['reduce',33],'int_literal':['reduce',33],'id':['reduce',33],'minus_op':['reduce',33],'exclamation_op':['reduce',33],'minus_op':['reduce',33],'exclamation_op':['reduce',33],'statement_list':['reduce',33],'statement':['reduce',33],'location':['reduce',33],'method_call':['reduce',33],'block':['reduce',33],'var_decl':['reduce',33],'expr':['reduce',33],'method_name':['reduce',33],'literal':['reduce',33],'-':['reduce',33],'!':['reduce',33],'=':['reduce',33],'expr_list':['reduce',33],'bin_op':['reduce',33],'callout_arg_list':['reduce',33],'callout_arg':['reduce',33]},
            75:{')':['shift',78]},
            76:{'{':['reduce',29],'{':['reduce',29],',':['reduce',29],'[':['reduce',29],']':['reduce',29],';':['reduce',29],'type':['reduce',29],'void':['reduce',29],'if':['reduce',29],'(':['reduce',29],')':['reduce',29],'else':['reduce',29],'for':['reduce',29],'return':['reduce',29],'break':['reduce',29],'continue':['reduce',29],'assign_op':['reduce',29],'callout':['reduce',29],'arit_op':['reduce',29],'rel_op':['reduce',29],'eq_op':['reduce',29],'cond_op':['reduce',29],'bool_literal':['reduce',29],'char_literal':['reduce',29],'string_literal':['reduce',29],'int_literal':['reduce',29],'id':['reduce',29],'minus_op':['reduce',29],'exclamation_op':['reduce',29],'minus_op':['reduce',29],'exclamation_op':['reduce',29],'statement_list':['reduce',29],'statement':['reduce',29],'location':['reduce',29],'method_call':['reduce',29],'block':['reduce',29],'var_decl':['reduce',29],'expr':['reduce',29],'method_name':['reduce',29],'literal':['reduce',29],'-':['reduce',29],'!':['reduce',29],'=':['reduce',29],'expr_list':['reduce',29],'bin_op':['reduce',29],'callout_arg_list':['reduce',29],'callout_arg':['reduce',29]},
            77:{'{':['reduce',30],'}':['reduce',30],',':['shift',82],'[':['reduce',30],']':['reduce',30],';':['reduce',30],'type':['reduce',30],'void':['reduce',30],'if':['reduce',30],'(':['reduce',30],')':['reduce',30],'else':['reduce',30],'for':['reduce',30],'return':['reduce',30],'break':['reduce',30],'continue':['reduce',30],'assign_op':['reduce',30],'callout':['reduce',30],'arit_op':['reduce',30],'rel_op':['reduce',30],'eq_op':['reduce',30],'cond_op':['reduce',30],'bool_literal':['reduce',30],'char_literal':['reduce',30],'string_literal':['reduce',30],'int_literal':['reduce',30],'id':['reduce',30],'minus_op':['reduce',30],'exclamation_op':['reduce',30],'minus_op':['reduce',30],'exclamation_op':['reduce',30],'statement_list':['reduce',30],'statement':['reduce',30],'location':['reduce',30],'method_call':['reduce',30],'block':['reduce',30],'var_decl':['reduce',30],'expr':['reduce',30],'method_name':['reduce',30],'literal':['reduce',30],'-':['reduce',30],'!':['reduce',30],'=':['reduce',30],'expr_list':['reduce',30],'bin_op':['reduce',30],'callout_arg_list':['reduce',30],'callout_arg':['reduce',30]},
            78:{'{':['reduce',34],'}':['reduce',34],',':['reduce',34],'[':['reduce',34],']':['reduce',34],';':['reduce',34],'type':['reduce',34],'void':['reduce',34],'if':['reduce',34],'(':['reduce',34],')':['reduce',34],'else':['reduce',34],'for':['reduce',34],'return':['reduce',34],'break':['reduce',34],'continue':['reduce',34],'assign_op':['reduce',34],'callout':['reduce',34],'arit_op':['reduce',34],'rel_op':['reduce',34],'eq_op':['reduce',34],'cond_op':['reduce',34],'bool_literal':['reduce',34],'char_literal':['reduce',34],'string_literal':['reduce',34],'int_literal':['reduce',34],'id':['reduce',34],'minus_op':['reduce',34],'exclamation_op':['reduce',34],'minus_op':['reduce',34],'exclamation_op':['reduce',34],'statement_list':['reduce',34],'statement':['reduce',34],'location':['reduce',34],'method_call':['reduce',34],'block':['reduce',34],'var_decl':['reduce',34],'expr':['reduce',34],'method_name':['reduce',34],'literal':['reduce',34],'-':['reduce',34],'!':['reduce',34],'=':['reduce',34],'expr_list':['reduce',34],'bin_op':['reduce',34],'callout_arg_list':['reduce',34],'callout_arg':['reduce',34]},
            79:{'{':['reduce',35],'}':['reduce',35],',':['reduce',35],'[':['reduce',35],']':['reduce',35],';':['reduce',35],'type':['reduce',35],'void':['reduce',35],'if':['reduce',35],'(':['reduce',35],')':['reduce',35],'else':['reduce',35],'for':['reduce',35],'return':['reduce',35],'break':['reduce',35],'continue':['reduce',35],'assign_op':['reduce',35],'callout':['reduce',35],'arit_op':['reduce',35],'rel_op':['reduce',35],'eq_op':['reduce',35],'cond_op':['reduce',35],'bool_literal':['reduce',35],'char_literal':['reduce',35],'string_literal':['reduce',35],'int_literal':['reduce',35],'id':['reduce',35],'minus_op':['reduce',35],'exclamation_op':['reduce',35],'minus_op':['reduce',35],'exclamation_op':['reduce',35],'statement_list':['reduce',35],'statement':['reduce',35],'location':['reduce',35],'method_call':['reduce',35],'block':['reduce',35],'var_decl':['reduce',35],'expr':['reduce',35],'method_name':['reduce',35],'literal':['reduce',35],'-':['reduce',35],'!':['reduce',35],'=':['reduce',35],'expr_list':['reduce',35],'bin_op':['reduce',35],'callout_arg_list':['reduce',35],'callout_arg':['reduce',35]},
            80:{'{':['shift',1],'block':['goto',83]},
            81:{'{':['shift',1],'block':['goto',84]},
            82:{'(':['shift',35],'callout':['shift',16],'bool_literal':['shift',31],'char_literal':['shift',30],'string_literal':['shift',79],'int_literal':['shift',29],'id':['shift',15],'location':['goto',26],'method_call':['goto',27],'expr':['goto',32],'method_name':['shift',24],'literal':['goto',28],'-':['goto',33],'!':['goto',34],'callout_arg_list':['goto',85],'callout_arg':['goto',77]},
            83:{'{':['reduce',8],'}':['reduce',8],',':['reduce',8],'[':['reduce',8],']':['reduce',8],';':['reduce',8],'type':['reduce',8],'void':['reduce',8],'if':['reduce',8],'(':['reduce',8],')':['reduce',8],'else':['reduce',8],'for':['reduce',8],'return':['reduce',8],'break':['reduce',8],'continue':['reduce',8],'assign_op':['reduce',8],'callout':['reduce',8],'arit_op':['reduce',8],'rel_op':['reduce',8],'eq_op':['reduce',8],'cond_op':['reduce',8],'bool_literal':['reduce',8],'char_literal':['reduce',8],'string_literal':['reduce',8],'int_literal':['reduce',8],'id':['reduce',8],'minus_op':['reduce',8],'exclamation_op':['reduce',8],'minus_op':['reduce',8],'exclamation_op':['reduce',8],'statement_list':['reduce',8],'statement':['reduce',8],'location':['reduce',8],'method_call':['reduce',8],'block':['reduce',8],'var_decl':['reduce',8],'expr':['reduce',8],'method_name':['reduce',8],'literal':['reduce',8],'-':['reduce',8],'!':['reduce',8],'=':['reduce',8],'expr_list':['reduce',8],'bin_op':['reduce',8],'callout_arg_list':['reduce',8],'callout_arg':['reduce',8]},
            84:{'{':['reduce',9],'}':['reduce',9],',':['reduce',9],'[':['reduce',9],']':['reduce',9],';':['reduce',9],'type':['reduce',9],'void':['reduce',9],'if':['reduce',9],'(':['reduce',9],')':['reduce',9],'else':['reduce',9],'for':['reduce',9],'return':['reduce',9],'break':['reduce',9],'continue':['reduce',9],'assign_op':['reduce',9],'callout':['reduce',9],'arit_op':['reduce',9],'rel_op':['reduce',9],'eq_op':['reduce',9],'cond_op':['reduce',9],'bool_literal':['reduce',9],'char_literal':['reduce',9],'string_literal':['reduce',9],'int_literal':['reduce',9],'id':['reduce',9],'minus_op':['reduce',9],'exclamation_op':['reduce',9],'minus_op':['reduce',9],'exclamation_op':['reduce',9],'statement_list':['reduce',9],'statement':['reduce',9],'location':['reduce',9],'method_call':['reduce',9],'block':['reduce',9],'var_decl':['reduce',9],'expr':['reduce',9],'method_name':['reduce',9],'literal':['reduce',9],'-':['reduce',9],'!':['reduce',9],'=':['reduce',9],'expr_list':['reduce',9],'bin_op':['reduce',9],'callout_arg_list':['reduce',9],'callout_arg':['reduce',9]},
            85: {'{': ['reduce', 31], '}': ['reduce', 31], ',': ['reduce', 31], '[': ['reduce', 31], ']': ['reduce', 31], ';': ['reduce', 31], 'type': ['reduce', 31], 'void': ['reduce', 31], 'if': ['reduce', 31], '(': ['reduce', 31], ')': ['reduce', 31], 'else': ['reduce', 31], 'for': ['reduce', 31], 'return': ['reduce', 31], 'break': ['reduce', 31], 'continue': ['reduce', 31], 'assign_op': ['reduce', 31], 'callout': ['reduce', 31], 'arit_op': ['reduce', 31], 'rel_op': ['reduce', 31], 'eq_op': ['reduce', 31], 'cond_op': ['reduce', 31], 'bool_literal': ['reduce', 31], 'char_literal': ['reduce', 31], 'string_literal': ['reduce', 31], 'int_literal': ['reduce', 31], 'id': ['reduce', 31], 'minus_op': ['reduce', 31], 'exclamation_op': ['reduce', 31], 'minus_op': ['reduce', 31], 'exclamation_op': ['reduce', 31], 'statement_list': ['reduce', 31], 'statement': ['reduce', 31], 'location': ['reduce', 31], 'method_call': ['reduce', 31], 'block': ['reduce', 31], 'var_decl': ['reduce', 31], 'expr': ['reduce', 31], 'method_name': ['reduce', 31], 'literal': ['reduce', 31], '-': ['reduce', 31], '!': ['reduce', 31], '=': ['reduce', 31], 'expr_list': ['reduce', 31], 'bin_op': ['reduce', 31], 'callout_arg_list': ['reduce', 31], 'callout_arg': ['reduce', 31]},
            86:{'{':['reduce',11],'}':['reduce',11],',':['reduce',11],'[':['reduce',11],']':['reduce',11],';':['reduce',11],'type':['reduce',11],'void':['reduce',11],'if':['reduce',11],'(':['reduce',11],')':['reduce',11],'else':['reduce',11],'for':['reduce',11],'return':['reduce',11],'break':['reduce',11],'continue':['reduce',11],'assign_op':['reduce',11],'callout':['reduce',11],'arit_op':['reduce',11],'rel_op':['reduce',11],'eq_op':['reduce',11],'cond_op':['reduce',11],'bool_literal':['reduce',11],'char_literal':['reduce',11],'string_literal':['reduce',11],'int_literal':['reduce',11],'id':['reduce',11],'minus_op':['reduce',11],'exclamation_op':['reduce',11],'minus_op':['reduce',11],'exclamation_op':['reduce',11],'statement_list':['reduce',11],'statement':['reduce',11],'location':['reduce',11],'method_call':['reduce',11],'block':['reduce',11],'var_decl':['reduce',11],'expr':['reduce',11],'method_name':['reduce',11],'literal':['reduce',11],'-':['reduce',11],'!':['reduce',11],'=':['reduce',11],'expr_list':['reduce',11],'bin_op':['reduce',11],'callout_arg_list':['reduce',11],'callout_arg':['reduce',11]}  
     }

    def parse_field(self, program, main_node, type_dfa, debug):
        error_list = []
        node_list = main_node.node_list
        # print(main_node.type_node)
        if(type_dfa == 'field_decl_list'):
            new_node_list = []
            node_index = 0
            split_indexes = []
            for node in node_list:
                if(node.object_node.symbol_type.name == ';'):
                    split_indexes.append(node_index)
                node_index+=1          
            fields_list = []
            for split in range(len(split_indexes)):
                if(split == 0):
                    fields_list.append(node_list[0:split_indexes[split]+1])
                else:
                    fields_list.append(node_list[split_indexes[split-1]+1:split_indexes[split]+1])
            for field_decl in fields_list:
                if(len(field_decl)<3):
                    error_list.append("Not enough tokens in field declaration at line "+str(field_decl[0].object_node.line))
                if(len(field_decl)==3):
                    if(field_decl[0].object_node.symbol_type.name!='type'):
                        error_list.append("Unexpected token "+ field_decl[0].object_node.symbol_type.name +" at line "+str(field_decl[0].object_node.line))
                    if(field_decl[1].object_node.symbol_type.name!='id'):
                        error_list.append("Unexpected token "+ field_decl[1].object_node.symbol_type.name +" at line "+str(field_decl[1].object_node.line))
                    if(field_decl[2].object_node.symbol_type.name!=';'):
                        error_list.append("Unexpected token "+ field_decl[2].object_node.symbol_type.name +" at line "+str(field_decl[2].object_node.line))
                    if(field_decl[0].object_node.symbol_type.name=='type'
                        and field_decl[1].object_node.symbol_type.name=='id'
                        and field_decl[2].object_node.symbol_type.name==';'):
                        field_obj = FieldDecl.FieldDecl()
                        new_node_list.append(Node.Node(field_obj, "field_decl", [field_decl[0], field_decl[1], field_decl[2]]))
                if(len(field_decl)>3):
                    temp_ids = []
                    id_list_bool = True
                    if(field_decl[0].object_node.symbol_type.name!='type'):
                        error_list.append("Unexpected token "+ field_decl[0].object_node.symbol_type.name +" at line "+str(field_decl[0].object_node.line))
                        id_list_bool = False
                    for id_index in range(1, len(field_decl)-1):
                        if(id_index%2!=0):
                            if(field_decl[id_index].object_node.symbol_type.name != 'id'):
                                error_list.append("Unexpected token "+ field_decl[id_index].object_node.symbol_type.name +" at line "+str(field_decl[id_index].object_node.line))
                                id_list_bool = False
                            else:
                                temp_ids.append(field_decl[id_index])
                        else:
                            if(field_decl[id_index].object_node.symbol_type.name != ','):
                                error_list.append("Unexpected token "+ field_decl[id_index].object_node.symbol_type.name +" at line "+str(field_decl[id_index].object_node.line))
                                id_list_bool = False
                    if(id_list_bool):
                        for temp_id in temp_ids:
                            field_obj = FieldDecl.FieldDecl()
                            new_node_list.append(Node.Node(field_obj, "field_decl", [field_decl[0], temp_id, field_decl[len(field_decl)-1]]))
                # for field in field_decl:
                #     print(field.object_node.symbol_type.name)
            # print(new_node_list)
            # for new_node in new_node_list:
            #     print(new_node.type_node)
            main_node.node_list = new_node_list
            program.node_list[3] = main_node
            # print(main_node.type_node)
        # print(program)

        # program_ui = Node_any("Program")
        # counter=0
        # for node in program.node_list:
        #     nodex = Node_any(node.type_node + str(counter), parent=program_ui)
        #     counter+=1
        #     if(len(node.node_list)!=0 and node.type_node!='method_decl_list'):
        #         for node1 in node.node_list:
        #             nodey = Node_any(node1.type_node + str(counter), parent=nodex)
        #             counter+=1
        #             if(len(node1.node_list)!=0):
        #                 for node2 in node1.node_list:
        #                     nodez = Node_any(node2.type_node + str(counter), parent=nodey)
        #                     counter+=1
        # ceo = Node_any("CEO") #root
        # vp_1 = Node_any("VP_1", parent=ceo)
        # vp_2 = Node_any("VP_2", parent=ceo)
        # gm_1 = Node_any("GM_1", parent=vp_1)
        # gm_2 = Node_any("GM_2", parent=vp_2)

        #DotExporter(program_ui).to_picture("AST.png")
        # print(type_dfa)
        if(debug):
            print("error list", error_list)

    def parse_method(self, program, main_node, type_dfa, debug):
        new_node_list_method = []
        error_list = []
        node_list = main_node.node_list
        # print(main_node.type_node)
        if(len(node_list)<6):
            error_list.append("Not enough tokens to parse a valid method decl")
        else:
            if(node_list[0].object_node.symbol_type.name != "type" and node_list[0].object_node.symbol_type.name != "void"):
                error_list.append("Unexpected token "+ node_list[0].object_node.symbol_type.name +" at line "+str(node_list[0].object_node.line))
            if(node_list[1].object_node.symbol_type.name != "id"):
                error_list.append("Unexpected token "+ node_list[1].object_node.symbol_type.name +" at line "+str(node_list[1].object_node.line))
            if(node_list[2].object_node.symbol_type.name != "("):
                error_list.append("Unexpected token "+ node_list[2].object_node.symbol_type.name +" at line "+str(node_list[2].object_node.line))
            
            for node_index in range(len(node_list)):
                if(node_index<len(node_list)-3):
                    if(
                        (node_list[node_index].object_node.symbol_type.name == "type" or node_list[node_index].object_node.symbol_type.name == "void") and
                         node_list[node_index+1].object_node.symbol_type.name == "id" and
                         node_list[node_index+2].object_node.symbol_type.name == "("
                    ):
                        #crear nodo method decl
                        method_decl_obj = MethodDecl.MethodDecl()
                        method_decl_node = Node.Node(method_decl_obj, "method_decl", [node_list[node_index], node_list[node_index+1], node_list[node_index+2]])
                        new_node_list_method.append(method_decl_node)
                        # print("method decl ", node_list[node_index].object_node.symbol_type.name)
                        # print("method decl ", node_list[node_index+1].object_node.symbol_type.name)
                        # print("method decl ", node_list[node_index+2].object_node.symbol_type.name)
                        counter_1 = node_index+3
                        child_var_decl_list=[]
                        while(node_list[counter_1].object_node.symbol_type.name != ")" and counter_1<len(node_list)-3):
                            tout_bien = True
                            if(node_list[counter_1].object_node.symbol_type.name == "type"):
                                if(node_list[counter_1+1].object_node.symbol_type.name != "id" 
                                    or (node_list[counter_1+2].object_node.symbol_type.name != "," and node_list[counter_1+2].object_node.symbol_type.name != ")")):
                                    error_list.append("Unexpected token "+ node_list[counter_1].object_node.symbol_type.name +" at line "+str(node_list[counter_1].object_node.line))
                                    tout_bien = False
                                else:
                                    child_var_decl_list.append(node_list[counter_1])
                                    # print("node", node_list[counter_1].object_node.symbol_type.name)
                                    # print("child var decl list", child_var_decl_list)
                                    # print("todo bien")
                            elif(node_list[counter_1].object_node.symbol_type.name == "id"):
                                if((node_list[counter_1+1].object_node.symbol_type.name != "," and node_list[counter_1+1].object_node.symbol_type.name != ")")
                                    or node_list[counter_1-1].object_node.symbol_type.name != "type" ):
                                    error_list.append("Unexpected token "+ node_list[counter_1].object_node.symbol_type.name +" at line "+str(node_list[counter_1].object_node.line))
                                    tout_bien = False
                                else:
                                    child_var_decl_list.append(node_list[counter_1])
                                    # print("node", node_list[counter_1].object_node.symbol_type.name)
                                    # print("child var decl list", child_var_decl_list)
                                    # print("todo bien")   
                            elif(node_list[counter_1].object_node.symbol_type.name == ","):
                                if(node_list[counter_1+1].object_node.symbol_type.name != "type"
                                    or node_list[counter_1-1].object_node.symbol_type.name != "id" ):
                                    error_list.append("Unexpected token "+ node_list[counter_1].object_node.symbol_type.name +" at line "+str(node_list[counter_1].object_node.line))
                                    tout_bien = False
                                else:
                                    child_var_decl_list.append(node_list[counter_1])
                                    # print("node", node_list[counter_1].object_node.symbol_type.name)
                                    # print("child var decl list", child_var_decl_list)
                                    # print("todo bien")  
                            else:
                                error_list.append("Unexpected token "+ node_list[counter_1].object_node.symbol_type.name +" at line "+str(node_list[counter_1].object_node.line))
                                tout_bien = False
                            # print(node_list[counter_1].object_node.symbol_type.name)
                            counter_1+=1
                        if(node_list[counter_1].object_node.symbol_type.name != ")"):
                            error_list.append("Missing closing ) in method declaration args")
                        var_decl_object = VarDeclList.VarDeclList()
                        var_decl_node = Node.Node(var_decl_object, "var_decl_list", [])
                        if(tout_bien):
                            var_decl_node.node_list = child_var_decl_list
                        method_decl_node.node_list.append(var_decl_node)
                        method_decl_node.node_list.append(node_list[counter_1])
                        # print("counter", counter_1, node_list[counter_1].object_node.symbol_type.name)
                        counter_1+=1
                        block_children_list = []
                        if(node_list[counter_1].object_node.symbol_type.name == "{"):
                                #create block node
                                # block_children_list.append(node_list[counter_1])
                                while not(
                                        (node_list[counter_1].object_node.symbol_type.name == "type" or node_list[counter_1].object_node.symbol_type.name == "void") and
                                        node_list[counter_1+1].object_node.symbol_type.name == "id" and
                                        node_list[counter_1+2].object_node.symbol_type.name == "("
                                    ) and counter_1<len(node_list)-2:
                                    # print("block", counter_1, node_list[counter_1].object_node.value)
                                    block_children_list.append(node_list[counter_1])
                                    counter_1+=1
                                if(counter_1==len(node_list)-2):
                                    block_children_list.append(node_list[counter_1])
                                    # print("block", counter_1, node_list[counter_1].object_node.value) 
                                    block_children_list.append(node_list[counter_1+1])                              
                                    # print("block", counter_1, node_list[counter_1+1].object_node.value)
                        #create block node
                        block_object = Block.Block()
                        block_node = Node.Node(block_object, "block", block_children_list)
                        method_decl_node.node_list.append(block_node)
                        # if not(
                        #     (node_list[counter_1].object_node.symbol_type.name == "type" or node_list[counter_1].object_node.symbol_type.name == "void") and
                        #     node_list[counter_1+1].object_node.symbol_type.name == "id" and
                        #     node_list[counter_1+2].object_node.symbol_type.name == "("
                        # ):
            main_node.node_list=new_node_list_method
        if(debug):
            print(error_list)

    def parse_block(self, program, main_node, debug):
        initial_node = Node.Node("$", "$", [])
        states_stack = [0]
        nodes_stack = [initial_node]
        error_list = []

        print(program, main_node.type_node, debug)
        node_list_analize = main_node.node_list
        
        for n in node_list_analize:
            print(n.type_node)

        len_list = len(node_list_analize)
        index = 0
        last_state = states_stack[-1]
        param_list = []
        current_node = node_list_analize[last_state]
        param_list = self.dfa_parse_1.get(last_state).get(current_node.type_node)
        if(param_list==None):
            error_list.append("Missing opening { in line " + str(current_node.object_node.line))

        print(param_list)
        print(len_list, index)
        rip = 0
        while(index<len_list and rip<15):
            #rip += 1
            print(node_list_analize[index])
            print(node_list_analize[index].object_node.symbol_type.name)
            print(last_state)
            if (param_list != None):
                if(param_list[0]=='shift'):

                    print("current", current_node.type_node)
                    print("param", param_list[1])
                    nodes_stack.append(current_node)
                    states_stack.append(param_list[1])
                    index+=1
                    current_node = node_list_analize[index]
                    param_list = self.dfa_parse_1.get(states_stack[-1]).get(current_node.type_node)

                    # current_node = token_list[index].symbol_type.name
                    # self.tokens_stack.append(current_node)
                    # param_list = self.dfa_parse_1.get(self.states_stack[-1]).get(current_node)
                    # self.states_stack.append(param_list[1])
                    # index+=1
                    # if(index<len(token_list)):
                    #     current_node = token_list[index].symbol_type.name
                    # param_list = self.dfa_parse_1.get(self.states_stack[-1]).get(current_node)
                    print("shift")
                elif(param_list[0]=='goto'):
                    states_stack.append(param_list[1])
                    
                    current_node = node_list_analize[index]
                    print("GOTO CURR",current_node.type_node)
                    print(states_stack[-1])
                    param_list = self.dfa_parse_1.get(states_stack[-1]).get(current_node.type_node)
                    print("GOTO PARAM", param_list)
 
                    # print(current_node)
                    # print(param_list[1])
                    # self.states_stack.append(param_list[1])
                    # if(index<len(token_list)):
                    #     current_node = token_list[index].symbol_type.name
                    #     param_list = self.dfa_parse_1.get(self.states_stack[-1]).get(current_node)
                    # else:
                    #     #param_list = self.dfa_parse_1.get(self.states_stack[-1]).get()
                    #     print(param_list)
                    #     self.tokens_stack.pop(-1)
                    #     self.states_stack.pop(-1)
                    #     break
                    print('goto')
                elif(param_list[0]=='reduce'):
                    print(param_list[1])
                    if(param_list[1] == 2):  
                        temp_statement_list = []
                        open_bracket = ""
                        for node_verify in nodes_stack[::-1]:
                            if(node_verify.type_node == "statement"):
                                print("statement found")
                                temp_statement_list.append(node_verify)
                            elif(node_verify.type_node == "{"):
                                open_bracket = node_verify
                                break
                            else:
                                error_list.append("Parsing error, unexpected production "+node_verify.type_node)
                                break
                        print("open", open_bracket.type_node)
                        print("statement_list", temp_statement_list)
                        print("last node", node_list_analize[index].type_node)
                        statement_list_node = Node.Node("statement_list", "statement_list", temp_statement_list[::-1])
                        node_block = Node.Node("block", "block", [open_bracket, statement_list_node, node_list_analize[index]])
                        count = len(temp_statement_list) + 1
                        nodes_stack = nodes_stack[:-count]
                        states_stack = states_stack[:-(count)]
                        nodes_stack.append(node_block)
                        index+=1

                        param_list = self.dfa_parse_1.get(states_stack[-1]).get(node_block.type_node)
                        #create while (statement) ---> {; verify block method
                        #return block with children
                        print("riiiip") 
                        #hacer otro algo rip
                    else:
                        object_node = list(self.grammer_1[param_list[1]-1].keys())[0]
                        type_node = list(self.grammer_1[param_list[1]-1].keys())[0]
                        count = len(list(self.grammer_1[param_list[1]-1].values())[0])

                        child_node_list = nodes_stack[-count:]

                        nodes_stack = nodes_stack[:-count]

                        states_stack = states_stack[:-(count)]
                        new_node = Node.Node(object_node, type_node, child_node_list)

                        nodes_stack.append(new_node)
                        print(new_node.type_node)
                        param_list = self.dfa_parse_1.get(states_stack[-1]).get(new_node.type_node)
                        print("PARAM", param_list)
                        if(param_list!=None and param_list[0]=='goto' and param_list[1]==32):
                            if(node_list_analize[index].type_node == "{" and nodes_stack[-1].type_node == "expr" and nodes_stack[-2].type_node == "," and nodes_stack[-3].type_node == "expr"):
                                param_list = ['goto', 81]
                                print("PARAM2", param_list)
                            print("=[")
                            for xd in nodes_stack:
                                print(xd.type_node)
                            print("=]")
                        if(param_list!=None and param_list[0]=='goto' and param_list[1]==32):
                            if(node_list_analize[index].type_node == ")" and nodes_stack[-1].type_node == "expr" and nodes_stack[-2].type_node == "(" and nodes_stack[-3].type_node != "if"):
                                param_list = ['goto', 59]
                                print("PARAM2", param_list)
                            print("=[")
                            for xd in nodes_stack:
                                print(xd.type_node)
                            print("=]")
                        if(param_list!=None and param_list[0]=='goto' and param_list[1]==32):
                            if(node_list_analize[index].type_node == ")" and nodes_stack[-1].type_node == "expr" and nodes_stack[-2].type_node == "(" and nodes_stack[-3].type_node == "if"):
                                param_list = ['goto', 44]
                                print("PARAM2", param_list)
                            print("=[")
                            for xd in nodes_stack:
                                print(xd.type_node)
                            print("=]")
                        if(param_list!=None and param_list[0]=='goto' and param_list[1]==32):
                            if(node_list_analize[index].type_node == "," and nodes_stack[-1].type_node == "expr" and nodes_stack[-2].type_node == "assign_op"):
                                param_list = ['goto', 65]
                                print("PARAM2", param_list)
                            print("=[")
                            for xd in nodes_stack:
                                print(xd.type_node)
                            print("=]")
                    print("reduce")
                    # print(param_list[1])
                    # node = Node.Node(list(self.grammar[param_list[1]-1].keys())[0], list(self.grammar[param_list[1]-1].values())[0])
                    # count = len(list(self.grammar[param_list[1]-1].values())[0])
                    # self.tokens_stack = self.tokens_stack[:-count]
                    # self.states_stack = self.states_stack[:-(count)]
                    # self.tokens_stack.append(list(self.grammar[param_list[1]-1].keys())[0])
                    # current_node = self.tokens_stack[-1]
                    # print(self.states_stack)
                    # param_list = self.dfa_parse_1.get(self.states_stack[-1]).get(current_node)
                    # #self.states_stack.append(param_list[1])
                    # print("node list", node.token_list)
                    # print("node", node)
                    # print("reduce")
                elif(param_list[0]=='accept'):
                    print("accept :)")
            else:
                print("state not defined")
                if(index<len(node_list_analize)):
                    error_list.append("unexpected token " + node_list_analize[index].type_node + " at line " + str(node_list_analize[index].object_node.line))
                else:
                    error_list.append("unexpected token " + node_list_analize[index-1].type_node + " at line " + str(node_list_analize[index-1].object_node.line))
                break
            print("----[")
            for xd in nodes_stack:
                print(xd.type_node)
            print("----]")
            print(states_stack)
            print("------")
        # for node in node_list_analize:
        #     print(node.object_node.symbol_type.name)


        if(debug):
            print(error_list)

        if(len(error_list) == 0):
            return nodes_stack[-1]
        else:
            return Node.Node("block", "block", [])

        #print(self.dfa_parse_1)
    def accepts(self, token_list):
        #print(''.join(list(self.grammar[1].values())[0]))
        state = 0
        index = 0
        param_list=[]
        print(len(token_list))
        current_token = token_list[index].symbol_type.name
        param_list = self.dfa_parse_1.get(state).get(current_token)
        print(param_list)
        while index<=len(token_list):
            #print(token_list[index].symbol_type.name)
            print(state)
            if (param_list != None):
                if(param_list[0]=='shift'):
                    current_token = token_list[index].symbol_type.name
                    self.tokens_stack.append(current_token)
                    param_list = self.dfa_parse_1.get(self.states_stack[-1]).get(current_token)
                    self.states_stack.append(param_list[1])
                    index+=1
                    if(index<len(token_list)):
                        current_token = token_list[index].symbol_type.name
                    param_list = self.dfa_parse_1.get(self.states_stack[-1]).get(current_token)
                    print("shift")
                elif(param_list[0]=='goto'):
                    print(current_token)
                    print(param_list[1])
                    self.states_stack.append(param_list[1])
                    if(index<len(token_list)):
                        current_token = token_list[index].symbol_type.name
                        param_list = self.dfa_parse_1.get(self.states_stack[-1]).get(current_token)
                    else:
                        #param_list = self.dfa_parse_1.get(self.states_stack[-1]).get()
                        print(param_list)
                        self.tokens_stack.pop(-1)
                        self.states_stack.pop(-1)
                        break
                    print('goto')
                elif(param_list[0]=='reduce'):
                    print(param_list[1])
                    node = Node.Node(list(self.grammar[param_list[1]-1].keys())[0], list(self.grammar[param_list[1]-1].values())[0])
                    count = len(list(self.grammar[param_list[1]-1].values())[0])
                    self.tokens_stack = self.tokens_stack[:-count]
                    self.states_stack = self.states_stack[:-(count)]
                    self.tokens_stack.append(list(self.grammar[param_list[1]-1].keys())[0])
                    current_token = self.tokens_stack[-1]
                    print(self.states_stack)
                    param_list = self.dfa_parse_1.get(self.states_stack[-1]).get(current_token)
                    #self.states_stack.append(param_list[1])
                    print("node list", node.token_list)
                    print("node", node)
                    print("reduce")
                elif(param_list[0]=='accept'):
                    print("accept :)")
            else:
                print("state not defined")
                if(index<len(token_list)):
                    print("unexpected token",token_list[index].symbol_type.name,"at line",token_list[index].line)
                else:
                    print("unexpected token",token_list[index-1].symbol_type.name,"at line",token_list[index-1].line)
                break
            print(self.tokens_stack)
            print(self.states_stack)
            print("------")

        # while index<=len(token_list):
        #     #print(token_list[index].symbol_type.name)
        #     # if(index<len(token_list)):
        #     #     print(token_list[index].symbol_type.name)
        #     #     param_list = self.dfa_parse_1.get(state).get(token_list[index].symbol_type.name)
        #     # else:
        #     print("TOKEN"+self.tokens_stack[-1])
        #     if(index<len(token_list)):
        #         param_list = self.dfa_parse_1.get(state).get(token_list[index].symbol_type.name)
        #     else:
        #         param_list = self.dfa_parse_1.get(state).get(self.tokens_stack[-1])
            
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
