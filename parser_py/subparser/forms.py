
from subparser.cmm_token import Token


ASSIGN = "{},=,{}"
LESS_ASSIGN = "{},=,{},<,{}"

class Quadruple(object):

    def __init__(self, op, arg0, arg1, result):
        self.op = op
        self.arg0 = arg0
        self.arg1 = arg1
        self.result = result

nextstm = 0
codes = []

commands = []

def gen(op, arg0, arg1, result):
    global nextstm
    nextstm += 1
    cmd = Quadruple(op, arg0, arg1, result)
    commands.append(cmd)

    return cmd

def generate():
    temp_count = 0

    def newtemp():
        nonlocal temp_count
        name = "0t{}".format(temp_count)
        temp_count += 1
        return name
    
    return newtemp

newtemp = generate()

def backpatch(j_cmds, stm):

    for cmd in j_cmds:
        cmd.result = stm

# P->Ed(V){C}P
def reduce_0(*args):
    return Token(idt="P")

# P->Ed(V){C}
def reduce_1(*args):
    return Token(idt="P")

# V->@
def reduce_2(*args):
    return Token(idt="V")

# V->F
def reduce_3(*args):
    return Token(idt="V")

# V->V`F
def reduce_4(*args):
    return Token(idt="V")

# L->qX;
def reduce_5(*args):
    return Token(idt="L")

# C->L
def reduce_6(*args):
    return Token(idt="C")

# C->LC
def reduce_7(*args):
    return Token(idt="C")

# C->@
def reduce_8(*args):
    return Token(idt="C")

# L->F;
def reduce_9(*args):
    return Token(idt="L")

# L->I
def reduce_10(*args):
    return Token(idt="L")

# L->A
def reduce_11(*args):
    return Token(idt="L")

# L->W;
def reduce_12(*args):
    return Token(idt="L")

# L->T;
def reduce_13(*args):
    return Token(idt="L")

# F->Ed=X
def reduce_14(*args):
    return Token(idt="F")

# F->Ed
def reduce_15(*args):
    return Token(idt="F")

# F->Ed[n]={nN}
def reduce_16(*args):
    return Token(idt="F")

# F->Ed[n]={}
def reduce_17(*args):
    return Token(idt="F")

# F->Ed[n]
def reduce_18(*args):
    return Token(idt="F")

# F->d[X]=X
def reduce_19(*args):
    return Token(idt="F")

# N->@
def reduce_20(*args):
    return Token(idt="N")

# N->`nN
def reduce_21(*args):
    return Token(idt="N")

# F->d=X
def reduce_22(*args):
    return Token(idt="F")

# F->F`F
def reduce_23(*args):
    return Token(idt="F")

# E->r
def reduce_24(*args):
    return Token(idt="E")

# E->i
def reduce_25(*args):
    return Token(idt="E")

# I->f(O)MBHsMB
def reduce_26(*args):
    return Token(idt="I")

# I->f(O)MB
def reduce_27(*args):
    return Token(idt="I")

# I->f(O)ML
def reduce_28(*args):
    return Token(idt="I")

# M->@
def reduce_29(*args):
    return Token(idt="M")

# H->@
def reduce_30(*args):
    return Token(idt="H")

# O->XSX
def reduce_31(*args):
    return Token(idt="O")

# X->G
def reduce_32(*args):
    return Token(idt="X")

# X->d(v)
def reduce_33(*args):
    return Token(idt="X")

# v->@
def reduce_34(*args):
    return Token(idt="v")

# v->X
def reduce_35(*args):
    return Token(idt="v")

# v->v`X
def reduce_36(*args):
    return Token(idt="v")

# X->X+G
def reduce_37(*args):
    return Token(idt="X")

# X->X-G
def reduce_38(*args):
    return Token(idt="X")

# G->R
def reduce_39(*args):
    return Token(idt="G")

# G->G*R
def reduce_40(*args):
    return Token(idt="G")

# G->G/R
def reduce_41(*args):
    return Token(idt="G")

# R->d
def reduce_42(*args):
    return Token(idt="R")

# R->n
def reduce_43(*args):
    return Token(idt="R")

# R->(X)
def reduce_44(*args):
    return Token(idt="R")

# R->d[X]
def reduce_45(*args):
    return Token(idt="R")

# S-><
def reduce_46(*args):
    return Token(idt="S")

# S->.
def reduce_47(*args):
    return Token(idt="S")

# S->>
def reduce_48(*args):
    return Token(idt="S")

# S->~
def reduce_49(*args):
    return Token(idt="S")

# S->&
def reduce_50(*args):
    return Token(idt="S")

# S->!
def reduce_51(*args):
    return Token(idt="S")

# A->w(MO)MB
def reduce_52(*args):
    return Token(idt="A")

# W->e(X)
def reduce_53(*args):
    return Token(idt="W")

# T->t(X)
def reduce_54(*args):
    return Token(idt="T")

forms = [(9, reduce_0), (8, reduce_1), (0, reduce_2), (1, reduce_3), (3, reduce_4), (3, reduce_5), (1, reduce_6), (2, reduce_7), (0, reduce_8), (2, reduce_9), (1, reduce_10), (1, reduce_11), (2, reduce_12), (2, reduce_13), (4, reduce_14), (2, reduce_15), (10, reduce_16), (8, reduce_17), (5, reduce_18), (6, reduce_19), (0, reduce_20), (3, reduce_21), (3, reduce_22), (3, reduce_23), (1, reduce_24), (1, reduce_25), (10, reduce_26), (6, reduce_27), (6, reduce_28), (0, reduce_29), (0, reduce_30), (3, reduce_31), (1, reduce_32), (4, reduce_33), (0, reduce_34), (1, reduce_35), (3, reduce_36), (3, reduce_37), (3, reduce_38), (1, reduce_39), (3, reduce_40), (3, reduce_41), (1, reduce_42), (1, reduce_43), (3, reduce_44), (4, reduce_45), (1, reduce_46), (1, reduce_47), (1, reduce_48), (1, reduce_49), (1, reduce_50), (1, reduce_51), (7, reduce_52), (4, reduce_53), (4, reduce_54)]