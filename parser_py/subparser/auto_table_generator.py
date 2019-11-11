replace_dict = {
    '.': '<=',
    ',': '>=',
    'i': 'int',
    'r': 'real',
    '&': '==',
    '!': '<>',
    '~': '>=',
    'f': 'if',
    'd': 'identity',
    'n': 'constnum',
    'o': 'do',
    'w': 'while',
    'e': 'read',
    't': 'write',
    's': 'else',
    '`': ',',
    'q': 'return'
}

def replace_symbol(c):
    if c in replace_dict.keys():
        return replace_dict[c]
    return c

def replace_symbol_reverse(c):
    for key in replace_dict.keys():
        if replace_dict[key] == c:
            return key
    
    return c

import_str = """
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

"""

def generate_forms(filename='forms.txt'):

    funcs = []
    nums = []

    with open(filename, 'r') as fin:
        for (i, line) in enumerate(fin):
            left, right = line.split("->")

            func_str = 'def reduce_{}(*args):\n'.format(str(i)) + ' '*4 + 'return Token(idt="{}")\n'.format(left)
            print(right)
            if '@' in right:
                num2reduce = 0
            else:
                num2reduce = len(right) - 2

            funcs.append((line[:-1].replace('$', "")+'\n', func_str))
            nums.append(num2reduce)

    with open("{}.py".format(filename.split(".txt")[0]), 'w') as fout:
        fout.write(import_str)
        for form, func in funcs:
            fout.write('# ' + form + func + "\n")

        func_names = [func.split('(*args)')[0].split(" ")[1] for _, func in funcs]

        forms = [(num, func) for num, func in zip(nums, func_names)]

        fout.write("forms = " + str(forms).replace("'", ""))
        fout.flush()

def generate_actions(filename='action_goto.txt'):

    actions = dict()

    with open(filename, 'r') as fin:
        for line in fin:
            print(line)
            print(len(line))
            line = line[1:-2] + line[-1]
            print(line)
            state, token_idt, action = line.split(",")

            if str.isupper(token_idt):
                continue

            token_idt = replace_symbol(token_idt)

            state = eval(state)

            if state == 92:
                print()

            action = eval(action)

            if action == 0:
                action = '#'
            else:
                action = ('s' if action > 0 else 'r') + str(abs(action))

            if state in actions.keys():
                actions[state][token_idt] = action
            else:
                actions[state] = {token_idt: action}
        
        with open("./subparser/actions.py", 'w') as fout:
            fout.write("action_part = " + str(actions))

def generate_gotos(filename='action_goto.txt'):

    gotos = dict()

    with open(filename, 'r') as fin:
        for line in fin:
            print(line)
            line = line[1:-2] + line[-1]
            state, token_idt, action = line.split(",")

            if not str.isupper(token_idt):
                continue

            state = eval(state)
            action = eval(action)

            if action == 0:
                action = '#'
            else:
                action = abs(action)

            if state in gotos.keys():
                gotos[state][token_idt] = action
            else:
                gotos[state] = {token_idt: action}
        
        with open("./subparser/gotos.py", 'w') as fout:
            fout.write("goto_part = " + str(gotos))

if __name__ == "__main__":
    generate_forms(filename="./subparser/forms.txt")
    generate_actions(filename="./subparser/action_goto.txt")
    generate_gotos(filename="./subparser/action_goto.txt")