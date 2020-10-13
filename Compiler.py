# imports
import sys
import scanner.Scanner as Scanner
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

    if(stage=="parse" or stage=="ast" or stage=="semantic" or stage=="irt" or stage=="codegen"):
        debug=False
        if(("parse" in debug_stage)):
            debug=True
        print("PARSE not ready")
        print("With debug"+str(debug))
    if(stage=="ast" or stage=="semantic" or stage=="irt" or stage=="codegen"):
        print("AST not ready")
    if(stage=="semantic" or stage=="irt" or stage=="codegen"):
        print("SEMANTIC not ready")
    if(stage=="irt" or stage=="codegen"):
        print("IRT not ready")
    if(stage=="codegen"):
        print("CODEGEN not ready")
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
