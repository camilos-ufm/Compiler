# imports
import sys
import scanner.Scanner as Scanner
import parser.Parser as Parser
import ast.Ast as Ast
import semantic.Semantic as Semantic
import irt.Irt as Irt
import codegen.Codegen as Codegen
import utils.ReadFile as ReadFile
import utils.WriteFile as WriteFile


def showHelp():
    print("Show Help\n"
          "-o <outname>     Escribir el output a <outname>\n"
          "-target <stage>  <stage> es uno de los siguientes elementos: scan, parse, ast, semantic, irt, codegen\n"
          "-opt <opt_stage> <opt_stage> es uno de: constant, algebraic\n"
          "-debug <stage>   Debugging <stage>\n")


def runCompiler(input_file, file_name, stage, opt_stage, debug_stage):
    # scan, parse, ast, semantic, irt, codegen

    if(stage=="scan" or stage=="parse" or stage=="ast" or stage=="semantic" or stage=="irt" or stage=="codegen"):
        debug=False
        if(("scan" in debug_stage)):
            debug=True

        sc = Scanner.Scanner()
        rf = ReadFile.ReadFile()
        wf = WriteFile.WriteFile()

        # set de input file
        rf.set_file(f"decafs/{input_file}.decaf")

        # call scanner class and scan for tokens in input file
        token_list, error_list = sc.scan(rf.file_to_string(), debug)
        string_list = []
        for token in token_list:
            string_list.append(token.pretty_print())

        # write file in output/
        wf.write_file(file_name, string_list)
        # write file in output/
        error1 = len(error_list)
        wf.write_file_append("error_list", error_list)

    if(stage=="parse" or stage=="ast" or stage=="semantic" or stage=="irt" or stage=="codegen"):
        debug=False
        if(("parse" in debug_stage)):
            debug=True

        pr = Parser.Parser()
        main_program, error_list = pr.parse(token_list, debug)
        # write file in output/
        wf.write_file_append("error_list", error_list)
        error2 = len(error_list)

    if(stage=="ast" or stage=="semantic" or stage=="irt" or stage=="codegen"):
        debug=False
        if(("ast" in debug_stage)):
            debug=True
        ast = Ast.Ast()
        ast.ast(main_program,debug)

    if(stage=="semantic" or stage=="irt" or stage=="codegen"):
        debug=False
        if(("semantic" in debug_stage)):
            debug=True
        sm = Semantic.Semantic()
        error_list = sm.semantic(main_program, debug)
        # write file in output/
        wf.write_file_append("error_list", error_list)
        error3 = len(error_list)
    if(stage=="irt" or stage=="codegen"):
        if(error1 == 0 and error2 == 0 and error3 == 0):
            debug=False
            if(("irt" in debug_stage)):
                debug=True
            irt = Irt.Irt()
            irt_list = irt.irt(main_program, debug)
        else:
            print("There are errors in the error_log")

    if(stage=="codegen"):
        if(error1 == 0 and error2 == 0 and error3 == 0):
            codegen = Codegen.Codegen()
            code_list,code_list_2 = codegen.codegen(main_program, debug)
            wf.write_file_no_extension("program.asm", code_list)
            
            wf.write_file_no_extension("program.py", code_list_2)
        else:
            print("There are errors in the error_log")
        # TODO write file asm or py from code_list
        # print("CODEGEN not ready")

    if (stage!="scan" and stage!="parse" and stage!="ast" and stage!="semantic" and stage!="irt" and stage!="codegen"):
        print("stage value not defined")

    print(input_file, file_name, stage, opt_stage, debug_stage)


if __name__ == "__main__":
    input_file = ""
    file_name = "out"
    stage = "parse"
    opt_stage = ""
    debug_stage = []
    if (len(sys.argv) >= 4 and len(sys.argv) % 2 == 0):
        valid = True
        # fixed
        print("file: " + sys.argv[0])
        print("<filename>: " + sys.argv[1])
        input_file = sys.argv[1]
        # variable
        for i in range(2, len(sys.argv)):
            if(i % 2 == 0):
                if(sys.argv[i] == '-o'):
                    file_name = sys.argv[i+1]
                elif(sys.argv[i] == '-target'):
                    stage = (sys.argv[i+1])
                elif(sys.argv[i] == '-opt'):
                    opt_stage = sys.argv[i+1]
                elif(sys.argv[i] == '-debug'):
                    string_stages = sys.argv[i+1].split(":")
                    debug_stage = string_stages
                else:
                    valid = False
                    print('invalid param')
                    showHelp()
        if(valid):
            runCompiler(input_file, file_name, stage, opt_stage, debug_stage)

    elif (len(sys.argv) == 2):
        input_file = sys.argv[1]
        runCompiler(input_file, file_name, stage, opt_stage, debug_stage)
    else:
        showHelp()
