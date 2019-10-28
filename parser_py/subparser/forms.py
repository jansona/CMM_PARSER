from subparser.cmm_token import Token
from subparser.identity_table import idt_table


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
        name = "v{}".format(temp_count)
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
    C = args[1]
    B = Token(idt="B")
    return B

# C->@
def reduce_4(*args):
    C = Token(idt="C")
    C.code = ""
    return C

# C->LC
def reduce_5(*args):
    L = args[0]
    C = Token(idt="C")
    return C

# L->F;
def reduce_6(*args):
    return Token(idt="L")

# L->I
def reduce_7(*args):
    I = args[0]
    L = Token(idt="L")
    backpatch(I.nextlist, nextstm)
    return L

# L->A
def reduce_8(*args):
    A = args[0]
    backpatch(A.nextlist, nextstm)
    return Token(idt="L")

# L->W;
def reduce_9(*args):
    return Token(idt="L")

# L->T;
def reduce_10(*args):
    return Token(idt="L")

# L->uF
def reduce_11(*args):
    return Token(idt="L")

# L->uX
def reduce_12(*args):
    return Token(idt="L")

# F->Ed=X
def reduce_13(*args):
    E = args[0]
    d = args[1]
    X = args[3]
    d.place = d.name
    gen('new', X.place, None, d.place)
    return Token(idt="F")

# F->Ed
def reduce_14(*args):
    E = args[0]
    d = args[1]
    d.place = d.name
    gen('new', 0, None, d.place)
    return Token(idt="F")

# F->Ed[X]={N}
def reduce_15(*args):
    return Token(idt="F")

# F->Ed[X]
def reduce_16(*args):
    return Token(idt="F")

# F->d[X]
def reduce_17(*args):
    return Token(idt="F")

# F->d[X]=n
def reduce_18(*args):
    return Token(idt="F")

# N->n`N
def reduce_19(*args):
    return Token(idt="N")

# N->@
def reduce_20(*args):
    return Token(idt="N")

# F->d=X
def reduce_21(*args):
    d = args[0]
    X = args[2]
    d.place = d.name
    gen('=', X.place, None, d.place)
    return Token(idt="F")

# F->F`F
def reduce_22(*args):
    return Token(idt="F")

# E->r
def reduce_23(*args):
    E = Token(idt="E")
    E.value = "real"
    return E

# E->i
def reduce_24(*args):
    E = Token(idt="E")
    E.value = "int"
    return E

# I->f(O)MBNsHB
def reduce_25(*args):
    O = args[2]
    M = args[4]
    B0 = args[5]
    N = args[6]
    H = args[8]
    B1 = args[9]
    I = Token(idt="I")
    backpatch(O.truelist, M.gotostm)
    backpatch(O.falselist, H.gotostm)
    I.nextlist += (B0.nextlist + N.nextlist + B1.nextlist)
    return I

# I->f(O)MB
def reduce_26(*args):
    O = args[2]
    M = args[4]
    B = args[5]
    I = Token(idt="I")
    backpatch(O.truelist, M.gotostm)
    I.nextlist += O.falselist + B.nextlist
    return I

# I->f(O)ML
def reduce_27(*args):
    O = args[2]
    M = args[4]
    L = args[5]
    I = Token(idt="I")
    backpatch(O.truelist, M.gotostm)
    I.nextlist += O.falselist + L.nextlist
    return I

# M->@
def reduce_28(*args):
    M = Token(idt="M")
    M.gotostm = nextstm
    return M

# N->@
def reduce_29(*args):
    j_command = gen('j', None, None, None)
    N = Token(idt="N")
    N.nextlist += [j_command]
    return N

# H->@
def reduce_30(*args):
    H = Token(idt="H")
    H.gotostm = nextstm
    return H

# O->XSX
def reduce_31(*args):
    X0 = args[0]
    S = args[1]
    X1 = args[2]
    O = Token(idt="O")
    js_command = gen(S.value, X0.place, X1.place, None)
    j_command = gen('j', None, None, None)
    O.truelist.append(js_command)
    O.falselist.append(j_command)
    return O

# S->>
def reduce_32(*args):
    S = Token(idt="S")
    S.value = '>'
    return S

# S->.
def reduce_33(*args):
    S = Token(idt="S")
    S.value = '<='
    return S

# S-><
def reduce_34(*args):
    S = Token(idt="S")
    S.value = '<'
    return S

# S->~
def reduce_35(*args):
    S = Token(idt="S")
    S.value = '>='
    return S

# S->&
def reduce_36(*args):
    S = Token(idt="S")
    S.value = '=='
    return S

# S->!
def reduce_37(*args):
    S = Token(idt="S")
    S.value = '<>'
    return S

# X->G
def reduce_38(*args):
    G = args[0]
    X = Token(idt="X")
    X.place = G.place
    return X

# X->X+G
def reduce_39(*args):
    X0 = args[0]
    G = args[2]
    X = Token(idt="X")
    X.place = newtemp()
    gen('+', X0.place, G.place,X.place)
    return Token(idt="X")

# X->X-G
def reduce_40(*args):
    X0 = args[0]
    G = args[2]
    X = Token(idt="X")
    X.place = newtemp()
    gen('-', X0.place, G.place,X.place)
    return X

# G->R
def reduce_41(*args):
    R = args[0]
    G = Token(idt="G")
    G.place = R.place
    return G

# G->G*R
def reduce_42(*args):
    G0 = args[0]
    R = args[2]
    G = Token(idt="G")
    G.place = newtemp()
    gen('*', G0.place, R.place, G.place)
    return Token(idt="G")

# G->G/R
def reduce_43(*args):
    G0 = args[0]
    R = args[2]
    G = Token(idt="G")
    G.place = newtemp()
    gen('/', G0.place, R.place, G.place)
    return G

# R->d
def reduce_44(*args):
    d = args[0]
    R = Token(idt="R")
    d.place = d.name
    R.place = d.place
    return R

# R->n
def reduce_45(*args):
    n = args[0]
    R = Token(idt="R")
    R.place = newtemp()
    gen('=', n.value, None, R.place)
    return R

# R->(X)
def reduce_46(*args):
    X = args[1]
    R = Token(idt="R")
    R.place = X.place
    return R

# A->w(MO)HB
def reduce_47(*args):
    M = args[2]
    O = args[3]
    H = args[5]
    B = args[6]
    backpatch(B.nextlist, M.gotostm)
    backpatch(O.truelist, H.gotostm)
    A = Token(idt="A")
    A.nextlist += O.falselist
    gen('j', None, None, M.gotostm)
    return A

# W->e(X)
def reduce_48(*args):
    X = args[2]
    gen('read', X.place, None, None)
    return Token(idt="W")

# T->t(X)
def reduce_49(*args):
    X = args[2]
    gen('write', X.place, None, None)
    return Token(idt="T")

forms = [(6, reduce_0), (7, reduce_1), (0, reduce_2), (3, reduce_3), (0, reduce_4), (2, reduce_5), (2, reduce_6), (1, reduce_7), (1, reduce_8), (2, reduce_9), (2, reduce_10), (2, reduce_11), (2, reduce_12), (4, reduce_13), (2, reduce_14), (9, reduce_15), (5, reduce_16), (4, reduce_17), (6, reduce_18), (3, reduce_19), (0, reduce_20), (3, reduce_21), (3, reduce_22), (1, reduce_23), (1, reduce_24), (10, reduce_25), (6, reduce_26), (6, reduce_27), (0, reduce_28), (0, reduce_29), (0, reduce_30), (3, reduce_31), (1, reduce_32), (1, reduce_33), (1, reduce_34), (1, reduce_35), (1, reduce_36), (1, reduce_37), (1, reduce_38), (3, reduce_39), (3, reduce_40), (1, reduce_41), (3, reduce_42), (3, reduce_43), (1, reduce_44), (1, reduce_45), (3, reduce_46), (7, reduce_47), (4, reduce_48), (3, reduce_49)]