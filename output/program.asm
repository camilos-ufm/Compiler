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
    # intermidate operetions to var 1
    sw $t9, 16($fp)
    # load immediate literal into var1
    li $t1, 1
    sw $t1, 20($fp)
    # moving var2 into var1
    lw $t1, 20($fp)
    sw $t1, 24($fp)
    # sums var1 + var2, saves in var1
    lw $t0, 20($fp)
    lw $t1, 8($fp)
    add $t3, $t0, $t1
    sw $t3, 20($fp)
    # loads data into t1, t0, set s_ to verify ifs
    lw $t0, 20($fp)
    li $t1, 5
    sle $s0, $t0, $t1
    # jump if condition
    li $t0, 1
    beq $s0, $t0, _L33
    # jump if not condition
    beq $s0, $zero, _L34
_L33:
    # loads data into t1, t0, set s_ to verify ifs
    # jump if condition
    li $t0, 1
    beq $s1, $t0, _L38
    # jump if not condition
    beq $s1, $zero, _L39
_L38:
    # sums var1 + immediate, saves in var1
    lw $t0, 8($fp)
    li $t1, 1
    add $t3, $t0, $t1
    sw $t3, 8($fp)
_L39:
    # subs var1 + immediate, saves in var1
    lw $t0, 8($fp)
    li $t1, 1
    sub $t3, $t0, $t1
    sw $t3, 8($fp)
_L40:
    # sums var1 + immediate, saves in var1
    lw $t0, 20($fp)
    li $t1, 1
    add $t3, $t0, $t1
    sw $t3, 20($fp)
    # loads data into t1, t0, set s_ to verify ifs
    lw $t0, 20($fp)
    li $t1, 5
    sle $s2, $t0, $t1
    # jump if condition
    li $t0, 1
    beq $s2, $t0, _L33
    # jump if not condition
    beq $s2, $zero, _L34
_L34:
    # end of program
    jr $ra
