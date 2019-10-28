
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

# P->Ed()BP
def reduce_0(*args):
    return Token(idt="P")

# P->Ed(F)BP
def reduce_1(*args):
    return Token(idt="P")

# P->@
def reduce_2(*args):
    return Token(idt="P")

# B->{C}
def reduce_3(*args):
    return Token(idt="B")

# C->@
def reduce_4(*args):
    return Token(idt="C")

# C->LC
def reduce_5(*args):
    return Token(idt="C")

# L->F;
def reduce_6(*args):
    return Token(idt="L")

# L->I
def reduce_7(*args):
    return Token(idt="L")

# L->A
def reduce_8(*args):
    return Token(idt="L")

# L->W;
def reduce_9(*args):
    return Token(idt="L")

# L->T;
def reduce_10(*args):
    return Token(idt="L")

# F->Ed=X
def reduce_11(*args):
    return Token(idt="F")

# F->Ed
def reduce_12(*args):
    return Token(idt="F")

# F->Ed[n]={nN}
def reduce_13(*args):
    return Token(idt="F")

# F->Ed[n]={}
def reduce_14(*args):
    return Token(idt="F")

# F->Ed[n]
def reduce_15(*args):
    return Token(idt="F")

# F->d[X]=X
def reduce_16(*args):
    return Token(idt="F")

# N->@
def reduce_17(*args):
    return Token(idt="N")

# N->`nN
def reduce_18(*args):
    return Token(idt="N")

# F->d=X
def reduce_19(*args):
    return Token(idt="F")

# F->F`F
def reduce_20(*args):
    return Token(idt="F")

# E->r
def reduce_21(*args):
    return Token(idt="E")

# E->i
def reduce_22(*args):
    return Token(idt="E")

# I->f(O)MBHsMB
def reduce_23(*args):
    return Token(idt="I")

# I->f(O)MB
def reduce_24(*args):
    return Token(idt="I")

# I->f(O)ML
def reduce_25(*args):
    return Token(idt="I")

# M->@
def reduce_26(*args):
    return Token(idt="M")

# H->@
def reduce_27(*args):
    return Token(idt="H")

# O->XSX
def reduce_28(*args):
    return Token(idt="O")

# X->G
def reduce_29(*args):
    return Token(idt="X")

# X->X+G
def reduce_30(*args):
    return Token(idt="X")

# X->X-G
def reduce_31(*args):
    return Token(idt="X")

# G->R
def reduce_32(*args):
    return Token(idt="G")

# G->G*R
def reduce_33(*args):
    return Token(idt="G")

# G->G/R
def reduce_34(*args):
    return Token(idt="G")

# R->d
def reduce_35(*args):
    return Token(idt="R")

# R->n
def reduce_36(*args):
    return Token(idt="R")

# R->(X)
def reduce_37(*args):
    return Token(idt="R")

# R->d[X]
def reduce_38(*args):
    return Token(idt="R")

# S-><
def reduce_39(*args):
    return Token(idt="S")

# S->.
def reduce_40(*args):
    return Token(idt="S")

# S->>
def reduce_41(*args):
    return Token(idt="S")

# S->~
def reduce_42(*args):
    return Token(idt="S")

# S->&
def reduce_43(*args):
    return Token(idt="S")

# S->!
def reduce_44(*args):
    return Token(idt="S")

# A->w(MO)MB
def reduce_45(*args):
    return Token(idt="A")

# W->e(X)
def reduce_46(*args):
    return Token(idt="W")

# T->t(X)
def reduce_47(*args):
    return Token(idt="T")

forms = [(6, reduce_0), (7, reduce_1), (0, reduce_2), (3, reduce_3), (0, reduce_4), (2, reduce_5), (2, reduce_6), (1, reduce_7), (1, reduce_8), (2, reduce_9), (2, reduce_10), (4, reduce_11), (2, reduce_12), (10, reduce_13), (8, reduce_14), (5, reduce_15), (6, reduce_16), (0, reduce_17), (3, reduce_18), (3, reduce_19), (3, reduce_20), (1, reduce_21), (1, reduce_22), (10, reduce_23), (6, reduce_24), (6, reduce_25), (0, reduce_26), (0, reduce_27), (3, reduce_28), (1, reduce_29), (3, reduce_30), (3, reduce_31), (1, reduce_32), (3, reduce_33), (3, reduce_34), (1, reduce_35), (1, reduce_36), (3, reduce_37), (4, reduce_38), (1, reduce_39), (1, reduce_40), (1, reduce_41), (1, reduce_42), (1, reduce_43), (1, reduce_44), (7, reduce_45), (4, reduce_46), (4, reduce_47)]