<h1 align="center">
    <img alt="cpu" src="https://img.icons8.com/bubbles/1000/000000/code.png" width="400">
  <br>🚀 OIKOS COMPILER <br>
</h1>

<div align="center">
  <h4>
    <a href="#Requeriments">Requerimientos</a> |
    <a href="#Fase del proyecto">Fases</a> |
    <a href="#Installing and running">Instalación</a>|
    <a href="#Flags">Flags</a>
  </h4>
</div>

<div align="center">
  <sub>Built with ❤︎ by
  <a href="https://github.com/KateyMG">Katherine Mazariegos</a>,
  <a href="https://github.com/Danisnowman">Daniel Hernández</a> and <a href="https://github.com/andresryes">Andres Bolaños</a>
</div>
<br>

El proyecto para el curso Compiladores consiste en escribir un compilador para un lenguaje llamado Decaf. Decaf es un lenguaje similar a C o Pascal.

# Requeriments
- Python 3


# Installing and Running

```
python Compiler.py <file_name> -flag

Ejemplo:
python Compiler.py ejemplo -target hola

python Compiler.py simple -target parse -debug parse:scan -o out

python Compiler.py semantic -target semantic -debug ast:semantic
python Compiler.py eje -target semantic -debug semantic
python Compiler.py irt2 -target irt
python Compiler.py final -target codegen -debug irt
```

**💡 IMPORTANTE** 
- El archivo debe de estar en la carpeta decafs y debe de tener la extensión .decaf

# Flags
```
-o <outname>     Escribir el output a <outname>
-target <stage>  <stage> es uno de los siguientes elementos: scan, parse, ast, semantic, irt, codegen
-opt <opt_stage> <opt_stage> es uno de: constant, algebrai
-debug <stage>   Debugging <stage>

```

# Fase del proyecto
- [x] Scanner
- [x] Parser
- [x] Semantic Check
- [x] IRT
- [x] Code Gen
- [x] Python && ASM

