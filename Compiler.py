# imports
import sys

if (len(sys.argv) >= 4):
    print("file: " + sys.argv[0])
    print("<filename>: " + sys.argv[1])
    print("[-flag]: " + sys.argv[2])
    print("[option value]: " + sys.argv[3])

elif (len(sys.argv) == 2):
    print("Show Help\n"
        "-o <outname>     Escribir el output a <outname>\n"
        "-target <stage>  <stage> es uno de los siguientes elementos: scan, parse, ast, semantic, irt, codegen\n"
        "-opt <opt_stage> <opt_stage> es uno de: constant, algebraic\n"
        "-debug <stage>   Debugging <stage>\n")
else:
    print("'option' parameter missing.")
