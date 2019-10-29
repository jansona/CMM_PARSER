from subparser.identity_table import TableItem, Table
from subparser.forms import Quadruple


idt_table = Table()


def address_search(*args):

    new_args = []
    for arg in args:
        if (arg is not None and type(arg) is not int) and '+' in arg:
            address = arg.split('+')[1]
            if not str.isdigit(address):
                arg = arg.split('+')[0] + '+' + idt_table.get_item(address).value
        new_args.append(arg)

    return new_args

def get_val_from_table(arg):
    if idt_table.has_item(arg):
        return idt_table.get_item(arg).value
    else:
        return arg

def add_item_or_err(val0, val1, var):

    types = []
    vals = [val0, val1]
    vals = [v for v in vals if v is not None]
    nums = [v for v in vals if not idt_table.has_item(v)]
    vars = [v for v in vals if idt_table.has_item(v)]
    types = [type(eval(v)) for v in nums]
    types += [eval(idt_table.get_item(v).idt_type) for v in vars]

    if (not idt_table.has_item(var)) and (var[0] is not '0'):
        raise Exception("未定义变量")
        exit(1)
    elif not idt_table.has_item(var):

        type_str = None
        if float in types:
            type_str = 'float'
        elif int in types:
            type_str = 'int'
        else:
            raise Exception("未知类型参数")
            exit(1)
        
        idt_table.add_item(name=var, idt_type=type_str)


def assign(arg1, arg2, arg3):
    
    add_item_or_err(arg1, arg2, arg3)

    # idt_table.get_item(name=arg3).value = eval(arg1)
    idt_table.get_item(name=arg3).value = str(eval(get_val_from_table(arg1)))
    
def add(arg1, arg2, arg3):
    
    add_item_or_err(arg1, arg2, arg3)

    idt_table.get_item(name=arg3).value = str(eval(get_val_from_table(arg1)) + eval(get_val_from_table(arg2)))

def minus(arg1, arg2, arg3):
    
    add_item_or_err(arg1, arg2, arg3)

    idt_table.get_item(name=arg3).value = str(eval(get_val_from_table(arg1)) - eval(get_val_from_table(arg2)))

def times(arg1, arg2, arg3):
    
    add_item_or_err(arg1, arg2, arg3)

    idt_table.get_item(name=arg3).value = str(eval(get_val_from_table(arg1)) * eval(get_val_from_table(arg2)))

def div(arg1, arg2, arg3):
    
    add_item_or_err(arg1, arg2, arg3)

    idt_table.get_item(name=arg3).value = str(eval(get_val_from_table(arg1)) / eval(get_val_from_table(arg2)))

def new(arg1, arg2, arg3):

    idt_table.add_item(name=arg3, idt_type=arg1)

def jump(arg1, arg2, arg3):

    return arg3

def jless(arg1, arg2, arg3):

    left = idt_table.get_item(name=arg1)
    right = idt_table.get_item(name=arg2)

    if eval(left.value) < eval(right.value):
        return arg3

def jbigger(arg1, arg2, arg3):

    left = idt_table.get_item(name=arg1)
    right = idt_table.get_item(name=arg2)

    if eval(left.value) > eval(right.value):
        return arg3

def jle(arg1, arg2, arg3):

    left = idt_table.get_item(name=arg1)
    right = idt_table.get_item(name=arg2)

    if eval(left.value) <= eval(right.value):
        return arg3

def jbe(arg1, arg2, arg3):

    left = idt_table.get_item(name=arg1)
    right = idt_table.get_item(name=arg2)

    if eval(left.value) >= eval(right.value):
        return arg3

def jne(arg1, arg2, arg3):

    left = idt_table.get_item(name=arg1)
    right = idt_table.get_item(name=arg2)

    if eval(left.value) != eval(right.value):
        return arg3

def write(arg1, arg2, arg3):

    var = idt_table.get_item(name=arg1)

    print(var.value)

def read(arg1, arg2, arg3):

    var = idt_table.get_item(name=arg1)
    var.value = input("Please input the value of {}:".format(var.name))
    

running_actions = {
    '=': assign,
    'new': new,
    '+': add,
    '-': minus,
    '*': times,
    '/': div,
    'j': jump,
    'write': write,
    'read': read,
    '<': jless,
    '>': jbigger,
    '<>': jne,
    '>=': jbe,
    '<=': jle,
}

class InterRunner(object):

    def __init__(self):

        self.table = Table()

    def __call__(self, commands):

        i = 0
        length = len(commands)

        while i < length:
            
            cmd = commands[i]

            # print(cmd.op, cmd.arg0, cmd.arg1, cmd.result)

            operation = running_actions[cmd.op]

            arg1, arg2, arg3 = address_search(cmd.arg0, cmd.arg1, cmd.result)
            address = operation(arg1, arg2, arg3)

            if address is not None:
                i = address
            else:
                i += 1

