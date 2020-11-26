        .data
msg:    .asciiz "Hello World"
        .text
main:
    # load immediate literal into var1
    li $t1, 0
    sw $t1, 8($fp)
    # load immediate literal into var1
    li $t1, 1
    sw $t1, 12($fp)
    # sums var1 + immediate, saves in var1
    lw $t0, 12($fp)
    li $t1, 3
    add $t3, $t0, $t1
    sw $t3, 12($fp)
    # intermidate operetions to var 1
    lw $t6, 8($fp)
    li $t0, 1
    add $t7, $t6, $t0
    li $t0, 2
    div $t7, $t0
    move $t8, mflo
    lw $t0, 12($fp)
    mul $t9, $t8, $t0
    sw $t9, 12($fp)
    # load immediate literal into var1
    li $t1, 1
    sw $t1, 16($fp)
    # moving var2 into var1
    lw $t1, 16($fp)
    sw $t1, 20($fp)
    # sums var1 + var2, saves in var1
    lw $t0, 16($fp)
    lw $t1, 8($fp)
    add $t3, $t0, $t1
    sw $t3, 16($fp)
    # loads data into t1, t0, set s_ to verify ifs
    lw $t0, 16($fp)
    li $t1, 5
    sle $s0, $t0, $t1
    # jump if condition
    li $t0, 1
    beq $s0, $t0, _L29
    # jump if not condition
    beq $s0, $zero, _L30
_L29:
    # loads data into t1, t0, set s_ to verify ifs
    lw $t0, 8($fp)
    lw $t1, 12($fp)
    seq $s1, $t0, $t1
    # jump if condition
    li $t0, 1
    beq $s1, $t0, _L34
    # jump if not condition
    beq $s1, $zero, _L35
_L34:
    # sums var1 + immediate, saves in var1
    lw $t0, 8($fp)
    li $t1, 1
    add $t3, $t0, $t1
    sw $t3, 8($fp)
_L35:
    # subs var1 + immediate, saves in var1
    lw $t0, 8($fp)
    li $t1, 1
    sub $t3, $t0, $t1
    sw $t3, 8($fp)
_L36:
    # sums var1 + immediate, saves in var1
    lw $t0, 16($fp)
    li $t1, 1
    add $t3, $t0, $t1
    sw $t3, 16($fp)
    # loads data into t1, t0, set s_ to verify ifs
    lw $t0, 16($fp)
    li $t1, 5
    sle $s2, $t0, $t1
    # jump if condition
    li $t0, 1
    beq $s2, $t0, _L29
    # jump if not condition
    beq $s2, $zero, _L30
_L30:
    # end of program
    jr $ra
