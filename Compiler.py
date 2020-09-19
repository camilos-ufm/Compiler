# imports
import sys

FILE_NAME = "out"
STAGE = "codegen"
OPT_STAGE = ""
DEBUG_STAGE = ""


def output(outname):
    FILE_NAME = outname
    print(FILE_NAME)


def target(stage):
    # scan, parse, ast, semantic, irt, codegen
    STAGE = stage
    print(STAGE)


def opt(opt_stage):
    OPT_STAGE = opt_stage
    print(OPT_STAGE)


def debug(stage):
    DEBUG_STAGE = stage
    print(DEBUG_STAGE)

def runCompiler():
    print(FILE_NAME, STAGE, OPT_STAGE, DEBUG_STAGE)

if __name__ == "__main__":
    if (len(sys.argv) >= 4 and len(sys.argv) % 2 == 0):
        valid = True
        # fixed
        print("file: " + sys.argv[0])
        print("<filename>: " + sys.argv[1])

        # variable
        for i in range(2, len(sys.argv)):
            if(i % 2 == 0):
                if(sys.argv[i] == '-o'):
                    output(sys.argv[i+1])
                    print(FILE_NAME)
                elif(sys.argv[i] == '-target'):
                    target(sys.argv[i+1])
                elif(sys.argv[i] == '-opt'):
                    opt(sys.argv[i+1])
                elif(sys.argv[i] == '-debug'):
                    debug(sys.argv[i+1])
                else:
                    valid = False
                    print('invalid param')
        if(valid):
            runCompiler()

    elif (len(sys.argv) == 2):
        print("Show Help\n"
              "-o <outname>     Escribir el output a <outname>\n"
              "-target <stage>  <stage> es uno de los siguientes elementos: scan, parse, ast, semantic, irt, codegen\n"
              "-opt <opt_stage> <opt_stage> es uno de: constant, algebraic\n"
              "-debug <stage>   Debugging <stage>\n")
    else:
        print("'option' parameter missing.")