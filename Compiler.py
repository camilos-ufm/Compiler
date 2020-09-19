# imports
import sys
import scanner.Scanner as Scanner


def showHelp():
    print("Show Help\n"
          "-o <outname>     Escribir el output a <outname>\n"
          "-target <stage>  <stage> es uno de los siguientes elementos: scan, parse, ast, semantic, irt, codegen\n"
          "-opt <opt_stage> <opt_stage> es uno de: constant, algebraic\n"
          "-debug <stage>   Debugging <stage>\n")


def runCompiler(input_file, file_name, stage, opt_stage, debug_stage):
    sc = Scanner.Scanner()
    sc.holaScanner()
    print(input_file, file_name, stage, opt_stage, debug_stage)


if __name__ == "__main__":
    input_file = ""
    file_name = "out"
    stage = "codegen"
    opt_stage = ""
    debug_stage = ""
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
                    debug_stage = (sys.argv[i+1])
                else:
                    valid = False
                    print('invalid param')
        if(valid):
            runCompiler(input_file, file_name, stage, opt_stage, debug_stage)

    elif (len(sys.argv) == 2):
        input_file = sys.argv[1]
        runCompiler(input_file, file_name, stage, opt_stage, debug_stage)
    else:
        showHelp()
