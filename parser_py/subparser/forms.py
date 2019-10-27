from subparser.cmm_token import Token

# P->Ed()BP
def reduce_0(**args):
    return Token(idt="P")

# P->Ed(F)BP
def reduce_1(**args):
    return Token(idt="P")

# P->@
def reduce_2(**args):
    return Token(idt="P")

# B->{C}
def reduce_3(**args):
    return Token(idt="B")

# C->@
def reduce_4(**args):
    return Token(idt="C")

# C->LC
def reduce_5(**args):
    return Token(idt="C")

# L->F;
def reduce_6(**args):
    return Token(idt="L")

# L->I
def reduce_7(**args):
    return Token(idt="L")

# L->A
def reduce_8(**args):
    return Token(idt="L")

# L->W;
def reduce_9(**args):
    return Token(idt="L")

# L->T;
def reduce_10(**args):
    return Token(idt="L")

# L->uF
def reduce_11(**args):
    return Token(idt="L")

# L->uX
def reduce_12(**args):
    return Token(idt="L")

# F->Ed=X
def reduce_13(**args):
    return Token(idt="F")

# F->Ed
def reduce_14(**args):
    return Token(idt="F")

# F->Ed[X]={N}
def reduce_15(**args):
    return Token(idt="F")

# F->Ed[X]
def reduce_16(**args):
    return Token(idt="F")

# F->d[X]
def reduce_17(**args):
    return Token(idt="F")

# F->d[X]=n
def reduce_18(**args):
    return Token(idt="F")

# N->n`N
def reduce_19(**args):
    return Token(idt="N")

# N->@
def reduce_20(**args):
    return Token(idt="N")

# F->d=X
def reduce_21(**args):
    return Token(idt="F")

# F->F`F
def reduce_22(**args):
    return Token(idt="F")

# E->r
def reduce_23(**args):
    return Token(idt="E")

# E->i
def reduce_24(**args):
    return Token(idt="E")

# I->f(O)BsB
def reduce_25(**args):
    return Token(idt="I")

# I->f(O)B
def reduce_26(**args):
    return Token(idt="I")

# I->f(O)L
def reduce_27(**args):
    return Token(idt="I")

# O->XSX
def reduce_28(**args):
    return Token(idt="O")

# X->G
def reduce_29(**args):
    return Token(idt="X")

# X->X+G
def reduce_30(**args):
    return Token(idt="X")

# X->X-G
def reduce_31(**args):
    return Token(idt="X")

# G->R
def reduce_32(**args):
    return Token(idt="G")

# G->G*R
def reduce_33(**args):
    return Token(idt="G")

# G->G/R
def reduce_34(**args):
    return Token(idt="G")

# R->d
def reduce_35(**args):
    return Token(idt="R")

# R->n
def reduce_36(**args):
    return Token(idt="R")

# R->(X)
def reduce_37(**args):
    return Token(idt="R")

# S-><
def reduce_38(**args):
    return Token(idt="S")

# S->.
def reduce_39(**args):
    return Token(idt="S")

# S->>
def reduce_40(**args):
    return Token(idt="S")

# S->~
def reduce_41(**args):
    return Token(idt="S")

# S->&
def reduce_42(**args):
    return Token(idt="S")

# S->!
def reduce_43(**args):
    return Token(idt="S")

# A->w(O)B
def reduce_44(**args):
    return Token(idt="A")

# W->e(X)
def reduce_45(**args):
    X = args['X']
    print("Please input the {}".format(X.name))
    X.value = input()

    return Token(idt="W")

# T->t(X)
def reduce_46(**args):
    X = args['X']
    print(X.value)
    return Token(idt="T")

forms = [(6, reduce_0), (7, reduce_1), (0, reduce_2), (3, reduce_3), (0, reduce_4), (2, reduce_5), (2, reduce_6), (1, reduce_7), (1, reduce_8), (2, reduce_9), (2, reduce_10), (2, reduce_11), (2, reduce_12), (4, reduce_13), (2, reduce_14), (9, reduce_15), (5, reduce_16), (4, reduce_17), (6, reduce_18), (3, reduce_19), (0, reduce_20), (3, reduce_21), (3, reduce_22), (1, reduce_23), (1, reduce_24), (7, reduce_25), (5, reduce_26), (5, reduce_27), (3, reduce_28), (1, reduce_29), (3, reduce_30), (3, reduce_31), (1, reduce_32), (3, reduce_33), (3, reduce_34), (1, reduce_35), (1, reduce_36), (3, reduce_37), (1, reduce_38), (1, reduce_39), (1, reduce_40), (1, reduce_41), (1, reduce_42), (1, reduce_43), (5, reduce_44), (4, reduce_45), (3, reduce_46)]