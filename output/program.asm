        .data
msg:    .asciiz "Hello World"
        .text
fib:
    # var decl, sp=4
    addi $sp, $sp, 4
    # var decl, sp=4
    addi $sp, $sp, 4
    # var decl, sp=4
    addi $sp, $sp, 4
    # load immediate literal into var1
    li $t1, 1
    sw $t1, 16($fp)
    # load immediate literal into var1
    li $t1, 1
    sw $t1, 8($fp)
    # load immediate literal into var1
    li $t1, 0
    sw $t1, 12($fp)
    # var decl, sp=4
    addi $sp, $sp, 4
    # load immediate literal into var1
    li $t1, 0
    sw $t1, 20($fp)
    # loads data into t1, t0, set s_ to verify ifs
    lw $t0, 20($fp)
    li $t1, 10
    slt $s0, $t0, $t1
    # jump if condition
    li $t0, 1
    beq $s0, $t0, _L23
    # jump if not condition
    beq $s0, $zero, _L24
_L23:
    # intermidate operetions to var 1
    lw $t8, 16($fp)
    lw $t0, 8($fp)
    add $t9, $t8, $t0
    sw $t9, 12($fp)
    # moving var2 into var1
    lw $t1, 8($fp)
    sw $t1, 16($fp)
    # moving var2 into var1
    lw $t1, 12($fp)
    sw $t1, 8($fp)
    # sums var1 + immediate, saves in var1
    lw $t0, 20($fp)
    li $t1, 1
    add $t3, $t0, $t1
    sw $t3, 20($fp)
    # loads data into t1, t0, set s_ to verify ifs
    lw $t0, 20($fp)
    li $t1, 10
    slt $s1, $t0, $t1
    # jump if condition
    li $t0, 1
    beq $s1, $t0, _L23
    # jump if not condition
    beq $s1, $zero, _L24
_L24:
    # end of program
    jr $ra
