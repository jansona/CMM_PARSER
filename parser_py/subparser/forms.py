from subparser.cmm_token import Token

# P->Ed()BP$
def reduce_0():
    return Token(idt="P")

# P->Ed(F)BP$
def reduce_1():
    return Token(idt="P")

# P->@$
def reduce_2():
    return Token(idt="P")

# B->{C}$
def reduce_3():
    return Token(idt="B")

# C->@$
def reduce_4():
    return Token(idt="C")

# C->LC$
def reduce_5():
    return Token(idt="C")

# L->F;$
def reduce_6():
    return Token(idt="L")

# L->I$
def reduce_7():
    return Token(idt="L")

# L->A$
def reduce_8():
    return Token(idt="L")

# L->W;$
def reduce_9():
    return Token(idt="L")

# L->T;$
def reduce_10():
    return Token(idt="L")

# L->uF$
def reduce_11():
    return Token(idt="L")

# L->uX$
def reduce_12():
    return Token(idt="L")

# F->Ed=X$
def reduce_13():
    return Token(idt="F")

# F->Ed$
def reduce_14():
    return Token(idt="F")

# F->Ed[X]={N}$
def reduce_15():
    return Token(idt="F")

# F->Ed[X]$
def reduce_16():
    return Token(idt="F")

# F->d[X]$
def reduce_17():
    return Token(idt="F")

# F->d[X]=n$
def reduce_18():
    return Token(idt="F")

# N->n`N$
def reduce_19():
    return Token(idt="N")

# N->@$
def reduce_20():
    return Token(idt="N")

# F->d=X$
def reduce_21():
    return Token(idt="F")

# F->F`F$
def reduce_22():
    return Token(idt="F")

# E->r$
def reduce_23():
    return Token(idt="E")

# E->i$
def reduce_24():
    return Token(idt="E")

# I->f(O)BsB$
def reduce_25():
    return Token(idt="I")

# I->f(O)B$
def reduce_26():
    return Token(idt="I")

# I->f(O)L$
def reduce_27():
    return Token(idt="I")

# O->XSX$
def reduce_28():
    return Token(idt="O")

# X->G$
def reduce_29():
    return Token(idt="X")

# X->X+G$
def reduce_30():
    return Token(idt="X")

# X->X-G$
def reduce_31():
    return Token(idt="X")

# G->R$
def reduce_32():
    return Token(idt="G")

# G->G*R$
def reduce_33():
    return Token(idt="G")

# G->G/R$
def reduce_34():
    return Token(idt="G")

# R->d$
def reduce_35():
    return Token(idt="R")

# R->n$
def reduce_36():
    return Token(idt="R")

# R->(X)$
def reduce_37():
    return Token(idt="R")

# S-><$
def reduce_38():
    return Token(idt="S")

# S->.$
def reduce_39():
    return Token(idt="S")

# S->>$
def reduce_40():
    return Token(idt="S")

# S->~$
def reduce_41():
    return Token(idt="S")

# S->&$
def reduce_42():
    return Token(idt="S")

# S->!$
def reduce_43():
    return Token(idt="S")

# A->w(O)B$
def reduce_44():
    return Token(idt="A")

# W->e(X)$
def reduce_45():
    return Token(idt="W")

# T->t(X)$def reduce_46():
    return Token(idt="T")

forms = [(6, reduce_0), (7, reduce_1), (0, reduce_2), (3, reduce_3), (0, reduce_4), (2, reduce_5), (2, reduce_6), (1, reduce_7), (1, reduce_8), (2, reduce_9), (2, reduce_10), (2, reduce_11), (2, reduce_12), (4, reduce_13), (2, reduce_14), (9, reduce_15), (5, reduce_16), (4, reduce_17), (6, reduce_18), (3, reduce_19), (0, reduce_20), (3, reduce_21), (3, reduce_22), (1, reduce_23), (1, reduce_24), (7, reduce_25), (5, reduce_26), (5, reduce_27), (3, reduce_28), (1, reduce_29), (3, reduce_30), (3, reduce_31), (1, reduce_32), (3, reduce_33), (3, reduce_34), (1, reduce_35), (1, reduce_36), (3, reduce_37), (1, reduce_38), (1, reduce_39), (1, reduce_40), (1, reduce_41), (1, reduce_42), (1, reduce_43), (5, reduce_44), (4, reduce_45), (3, reduce_46)]