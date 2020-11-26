        .data
msg:    .asciiz "Hello World"
        .text
fib:
    # load immediate literal into var1
    li $t1, 1
    sw $t1, 8($fp)
    # load immediate literal into var1
    li $t1, 1
    sw $t1, 12($fp)
    # load immediate literal into var1
    li $t1, 0
    sw $t1, 16($fp)
    # load immediate literal into var1
    li $t1, 0
    sw $t1, 20($fp)
    # load immediate literal into var1
    li $t1, 0
    sw $t1, 20($fp)
    # loads data into t1, t0, set s_ to verify ifs
    lw $t0, 20($fp)
    li $t1, 10
    slt $s0, $t0, $t1
    # jump if condition
    li $t0, 1
    beq $s0, $t0, _L25
    # jump if not condition
    beq $s0, $zero, _L26
_L25:
    # intermidate operetions to var 1
    lw $t8, 8($fp)
    lw $t0, 12($fp)
    add $t9, $t8, $t0
    sw $t9, 16($fp)
    # moving var2 into var1
    lw $t1, 12($fp)
    sw $t1, 8($fp)
    # moving var2 into var1
    lw $t1, 16($fp)
    sw $t1, 12($fp)
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
    beq $s1, $t0, _L25
    # jump if not condition
    beq $s1, $zero, _L26
_L26:
    # end of program
    jr $ra
