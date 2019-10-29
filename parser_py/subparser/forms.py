
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

# F->Ed=X
def reduce_11(*args):
    E = args[0]
    d = args[1]
    X = args[3]
    d.place = d.name
    gen('new', E.value, None, d.place)
    gen('=', X.place, None, d.place)
    return Token(idt="F")

# F->Ed
def reduce_12(*args):
    E = args[0]
    d = args[1]
    d.place = d.name
    gen('new', E.value, None, d.place)
    gen('=', 0, None, d.place)
    return Token(idt="F")

# F->Ed[n]={nN}
def reduce_13(*args):
    E = args[0]
    d = args[1]
    n0 = args[3]
    n1 = args[7]
    N = args[8]
    d.place = d.name
    for i in range(int(n0.value)):
        gen('new', E.value, None, "{}+{}".format(d.place, i))
    gen('=', n1.value, None, "{}+{}".format(d.place, 0))
    for index, n in enumerate(N.value):
        gen('=', n, None, "{}+{}".format(d.place, index+1))
    return Token(idt="F")

# F->Ed[n]={}
def reduce_14(*args):
    return Token(idt="F")

# F->Ed[n]
def reduce_15(*args):
    E = args[0]
    d = args[1]
    n = args[3]
    d.place = d.name
    for i in range(int(n.value)):
        gen('new', E.value, None, "{}+{}".format(d.place, i))
    return Token(idt="F")

# F->d[X]=X
def reduce_16(*args):
    d = args[0]
    X0 = args[2]
    X1 = args[5]
    d.place = d.name
    gen('=', X1.place, None, "{}+{}".format(d.place, X0.place))
    return Token(idt="F")

# N->@
def reduce_17(*args):
    N = Token(idt="N")
    N.value = []
    return N

# N->`nN
def reduce_18(*args):
    n = args[1]
    N0 = args[2]
    N = Token(idt="N")
    N.value = [n.value] + N0.value
    return N

# F->d=X
def reduce_19(*args):
    d = args[0]
    X = args[2]
    d.place = d.name
    gen('=', X.place, None, d.place)
    return Token(idt="F")

# F->F`F
def reduce_20(*args):
    return Token(idt="F")

# E->r
def reduce_21(*args):
    E = Token(idt="E")
    E.value = "real"
    return E

# E->i
def reduce_22(*args):
    E = Token(idt="E")
    E.value = "int"
    return E

# I->f(O)MBHsMB
def reduce_23(*args):
    O = args[2]
    M0 = args[4]
    B0 = args[5]
    H = args[6]
    M1 = args[8]
    B1 = args[9]
    I = Token(idt="I")
    backpatch(O.truelist, M0.gotostm)
    backpatch(O.falselist, M1.gotostm)
    I.nextlist += (B0.nextlist + H.nextlist + B1.nextlist)
    return I

# I->f(O)MB
def reduce_24(*args):
    O = args[2]
    M = args[4]
    B = args[5]
    I = Token(idt="I")
    backpatch(O.truelist, M.gotostm)
    I.nextlist += O.falselist + B.nextlist
    return I

# I->f(O)ML
def reduce_25(*args):
    O = args[2]
    M = args[4]
    L = args[5]
    I = Token(idt="I")
    backpatch(O.truelist, M.gotostm)
    I.nextlist += O.falselist + L.nextlist
    return I

# M->@
def reduce_26(*args):
    M = Token(idt="M")
    M.gotostm = nextstm
    return M

# H->@
def reduce_27(*args):
    j_command = gen('j', None, None, None)
    H = Token(idt="H")
    H.nextlist += [j_command]
    return H

# O->XSX
def reduce_28(*args):
    X0 = args[0]
    S = args[1]
    X1 = args[2]
    O = Token(idt="O")
    js_command = gen(S.value, X0.place, X1.place, None)
    j_command = gen('j', None, None, None)
    O.truelist.append(js_command)
    O.falselist.append(j_command)
    return O

# X->G
def reduce_29(*args):
    G = args[0]
    X = Token(idt="X")
    X.place = G.place
    return X

# X->X+G
def reduce_30(*args):
    X0 = args[0]
    G = args[2]
    X = Token(idt="X")
    X.place = newtemp()
    gen('+', X0.place, G.place, X.place)
    return X

# X->X-G
def reduce_31(*args):
    X0 = args[0]
    G = args[2]
    X = Token(idt="X")
    X.place = newtemp()
    gen('-', X0.place, G.place,X.place)
    return X

# G->R
def reduce_32(*args):
    R = args[0]
    G = Token(idt="G")
    G.place = R.place
    return G

# G->G*R
def reduce_33(*args):
    G0 = args[0]
    R = args[2]
    G = Token(idt="G")
    G.place = newtemp()
    gen('*', G0.place, R.place, G.place)
    return Token(idt="G")

# G->G/R
def reduce_34(*args):
    G0 = args[0]
    R = args[2]
    G = Token(idt="G")
    G.place = newtemp()
    gen('/', G0.place, R.place, G.place)
    return G

# R->d
def reduce_35(*args):
    d = args[0]
    R = Token(idt="R")
    d.place = d.name
    R.place = d.place
    return R

# R->n
def reduce_36(*args):
    n = args[0]
    R = Token(idt="R")
    R.place = newtemp()
    gen('=', n.value, None, R.place)
    return R

# R->(X)
def reduce_37(*args):
    X = args[1]
    R = Token(idt="R")
    R.place = X.place
    return R

# R->d[X]
def reduce_38(*args):
    d = args[0]
    X = args[2]
    R = Token(idt="R")
    d.place = d.name
    R.place = "{}+{}".format(d.place, X.place)
    return R

# S-><
def reduce_39(*args):
    S = Token(idt="S")
    S.value = '<'
    return S

# S->.
def reduce_40(*args):
    S = Token(idt="S")
    S.value = '<='
    return S

# S->>
def reduce_41(*args):
    S = Token(idt="S")
    S.value = '>'
    return S

# S->~
def reduce_42(*args):
    S = Token(idt="S")
    S.value = '>='
    return S

# S->&
def reduce_43(*args):
    S = Token(idt="S")
    S.value = '=='
    return S

# S->!
def reduce_44(*args):
    S = Token(idt="S")
    S.value = '<>'
    return S

# A->w(MO)MB
def reduce_45(*args):
    M0 = args[2]
    O = args[3]
    M1 = args[5]
    B = args[6]
    backpatch(B.nextlist, M0.gotostm)
    backpatch(O.truelist, M1.gotostm)
    A = Token(idt="A")
    A.nextlist += O.falselist
    gen('j', None, None, M0.gotostm)
    return A

# W->e(X)
def reduce_46(*args):
    X = args[2]
    gen('read', X.place, None, None)
    return Token(idt="W")

# T->t(X)
def reduce_47(*args):
    X = args[2]
    gen('write', X.place, None, None)
    return Token(idt="T")

forms = [(6, reduce_0), (7, reduce_1), (0, reduce_2), (3, reduce_3), (0, reduce_4), (2, reduce_5), (2, reduce_6), (1, reduce_7), (1, reduce_8), (2, reduce_9), (2, reduce_10), (4, reduce_11), (2, reduce_12), (10, reduce_13), (8, reduce_14), (5, reduce_15), (6, reduce_16), (0, reduce_17), (3, reduce_18), (3, reduce_19), (3, reduce_20), (1, reduce_21), (1, reduce_22), (10, reduce_23), (6, reduce_24), (6, reduce_25), (0, reduce_26), (0, reduce_27), (3, reduce_28), (1, reduce_29), (3, reduce_30), (3, reduce_31), (1, reduce_32), (3, reduce_33), (3, reduce_34), (1, reduce_35), (1, reduce_36), (3, reduce_37), (4, reduce_38), (1, reduce_39), (1, reduce_40), (1, reduce_41), (1, reduce_42), (1, reduce_43), (1, reduce_44), (7, reduce_45), (4, reduce_46), (4, reduce_47)]