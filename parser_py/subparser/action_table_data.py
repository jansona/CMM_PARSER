from subparser.cmm_token import Token


def reduce_0():
    return Token(idt="P")

def reduce_1():
    return Token(idt="B")

def reduce_2():
    return Token(idt="C")

def reduce_3():
    return Token(idt="C")

def reduce_4():
    return Token(idt="L")

def reduce_5():
    return Token(idt="L")

def reduce_6():
    return Token(idt="L")

def reduce_7():
    return Token(idt="L")

def reduce_8():
    return Token(idt="L")

def reduce_9():
    return Token(idt="Z")

def reduce_10():
    return Token(idt="F")

def reduce_11():
    return Token(idt="F")

def reduce_12():
    return Token(idt="E")

def reduce_13():
    return Token(idt="E")

def reduce_14():
    return Token(idt="I")

def reduce_15():
    return Token(idt="I")

def reduce_16():
    return Token(idt="I")

def reduce_17():
    return Token(idt="O")

def reduce_18():
    return Token(idt="X")

def reduce_19():
    return Token(idt="X")

def reduce_20():
    return Token(idt="X")

def reduce_21():
    return Token(idt="G")

def reduce_22():
    return Token(idt="G")

def reduce_23():
    return Token(idt="G")

def reduce_24():
    return Token(idt="R")

def reduce_25():
    return Token(idt="R")

def reduce_26():
    return Token(idt="R")

def reduce_27():
    return Token(idt="S")

def reduce_28():
    return Token(idt="S")

def reduce_29():
    return Token(idt="S")

def reduce_30():
    return Token(idt="S")

def reduce_31():
    return Token(idt="S")

def reduce_32():
    return Token(idt="S")

def reduce_33():
    return Token(idt="A")

def reduce_34():
    return Token(idt="W")

def reduce_35():
    return Token(idt="T")

forms = [(5, reduce_0), (3, reduce_1), (0, reduce_2), (2, reduce_3), (2, reduce_4), (1, reduce_5), (1, reduce_6), (2, reduce_7), (2, reduce_8), (5, reduce_9), (4, reduce_10), (3, reduce_11), (1, reduce_12), (1, reduce_13), (7, reduce_14), (5, reduce_15), (6, reduce_16), (3, reduce_17), (1, reduce_18), (3, reduce_19), (3, reduce_20), (1, reduce_21), (3, reduce_22), (3, reduce_23), (1, reduce_24), (1, reduce_25), (3, reduce_26), (1, reduce_27), (1, reduce_28), (1, reduce_29), (1, reduce_30), (1, reduce_31), (1, reduce_32), (5, reduce_33), (4, reduce_34), (3, reduce_35)]

action_part = {0: {'int': 's1', 'real': 's2'}, 1: {'identity': 'r14'}, 2: {'identity': 'r13'}, 3: {'identity': 's5'}, 4: {'#': '#'}, 5: {'(': 's6'}, 6: {')': 's7'}, 7: {'{': 's8'}, 8: {'}': 'r3', 'identity': 's10', 'read': 's11', 'if': 's12', 'int': 's13', 'real': 's14', 'write': 's15', 'while': 's16'}, 9: {'#': 'r1'}, 10: {'=': 's25'}, 11: {'(': 's26'}, 12: {'(': 's27'}, 13: {'identity': 'r14'}, 14: {'identity': 'r13'}, 15: {'(': 's28'}, 16: {'(': 's29'}, 17: {'identity': 'r7', 'read': 'r7', 'if': 'r7', 'int': 'r7', 'real': 'r7', 'write': 'r7', 'while': 'r7', '}': 'r7'}, 18: {'}': 's30'}, 19: {'identity': 's31'}, 20: {';': 's32'}, 21: {'identity': 'r6', 'read': 'r6', 'if': 'r6', 'int': 'r6', 'real': 'r6', 'write': 'r6', 'while': 'r6', '}': 'r6'}, 22: {'}': 'r3', 'identity': 's10', 'read': 's11', 'if': 's12', 'int': 's13', 'real': 's14', 'write': 's15', 'while': 's16'}, 23: {';': 's34'}, 24: {';': 's35'}, 25: {'(': 's36', 'identity': 's37', 'constnum': 's38'}, 26: {'(': 's42', 'identity': 's43', 'constnum': 's44'}, 27: {'(': 's46', 'identity': 's47', 'constnum': 's48'}, 28: {'(': 's42', 'identity': 's43', 'constnum': 's44'}, 29: {'(': 's46', 'identity': 's47', 'constnum': 's48'}, 30: {'#': 'r2'}, 31: {'=': 's55'}, 32: {'identity': 'r5', 'read': 'r5', 'if': 'r5', 'int': 'r5', 'real': 'r5', 'write': 'r5', 'while': 'r5', '}': 'r5'}, 33: {'}': 'r4'}, 34: {'identity': 'r9', 'read': 'r9', 'if': 'r9', 'int': 'r9', 'real': 'r9', 'write': 'r9', 'while': 'r9', '}': 'r9'}, 35: {'identity': 'r8', 'read': 'r8', 'if': 'r8', 'int': 'r8', 'real': 'r8', 'write': 'r8', 'while': 'r8', '}': 'r8'}, 36: {'(': 's56', 'identity': 's57', 'constnum': 's58'}, 37: {';': 'r25', '*': 'r25', '/': 'r25', '+': 'r25', '-': 'r25'}, 38: {';': 'r26', '*': 'r26', '/': 'r26', '+': 'r26', '-': 'r26'}, 39: {';': 'r19', '+': 'r19', '-': 'r19', '*': 's62', '/': 's63'}, 40: {';': 'r22', '*': 'r22', '/': 'r22', '+': 'r22', '-': 'r22'}, 41: {';': 'r12', '+': 's64', '-': 's65'}, 42: {'(': 's56', 'identity': 's57', 'constnum': 's58'}, 43: {')': 'r25'}, 44: {')': 'r26'}, 45: {')': 's67'}, 46: {'(': 's56', 'identity': 's57', 'constnum': 's58'}, 47: {'<>': 'r25', '==': 'r25', '>=': 'r25', '<=': 'r25', '<': 'r25', '>': 'r25', '*': 'r25', '/': 'r25', '+': 'r25', '-': 'r25'}, 48: {'<>': 'r26', '==': 'r26', '>=': 'r26', '<=': 'r26', '<': 'r26', '>': 'r26', '*': 'r26', '/': 'r26', '+': 'r26', '-': 'r26'}, 49: {'<>': 'r19', '==': 'r19', '>=': 'r19', '<=': 'r19', '<': 'r19', '>': 'r19', '+': 'r19', '-': 'r19', '*': 's69', '/': 's70'}, 50: {')': 's71'}, 51: {'<>': 'r22', '==': 'r22', '>=': 'r22', '<=': 'r22', '<': 'r22', '>': 'r22', '*': 'r22', '/': 'r22', '+': 'r22', '-': 'r22'}, 52: {'<>': 's72', '==': 's73', '+': 's74', '>=': 's75', '-': 's76', '<=': 's77', '<': 's78', '>': 's79', 'int': 's1', 'real': 's2'}, 53: {')': 's83'}, 54: {')': 's84'}, 55: {'(': 's36', 'identity': 's37', 'constnum': 's38'}, 56: {'(': 's56', 'identity': 's57', 'constnum': 's58'}, 57: {')': 'r25', '*': 'r25', '/': 'r25', '+': 'r25', '-': 'r25'}, 58: {')': 'r26', '*': 'r26', '/': 'r26', '+': 'r26', '-': 'r26'}, 59: {')': 'r19', '+': 'r19', '-': 'r19', '*': 's87', '/': 's88'}, 60: {')': 'r22', '*': 'r22', '/': 'r22', '+': 'r22', '-': 'r22'}, 61: {')': 's89', '+': 's90', '-': 's91'}, 62: {'(': 's36', 'identity': 's37', 'constnum': 's38'}, 63: {'(': 's36', 'identity': 's37', 'constnum': 's38'}, 64: {'(': 's36', 'identity': 's37', 'constnum': 's38'}, 65: {'(': 's36', 'identity': 's37', 'constnum': 's38'}, 66: {')': 's96', '+': 's90', '-': 's91'}, 67: {';': 'r35'}, 68: {')': 's97', '+': 's90', '-': 's91'}, 69: {'(': 's46', 'identity': 's47', 'constnum': 's48'}, 70: {'(': 's46', 'identity': 's47', 'constnum': 's48'}, 71: {'identity': 's10', 'read': 's11', 'if': 's100', 'int': 's13', 'real': 's14', 'write': 's15', 'while': 's101', '{': 's102'}, 72: {'(': 'r33', 'identity': 'r33', 'constnum': 'r33'}, 73: {'(': 'r32', 'identity': 'r32', 'constnum': 'r32'}, 74: {'(': 's46', 'identity': 's47', 'constnum': 's48'}, 75: {'(': 'r31', 'identity': 'r31', 'constnum': 'r31'}, 76: {'(': 's46', 'identity': 's47', 'constnum': 's48'}, 77: {'(': 'r29', 'identity': 'r29', 'constnum': 'r29'}, 78: {'(': 'r28', 'identity': 'r28', 'constnum': 'r28'}, 79: {'(': 'r30', 'identity': 'r30', 'constnum': 'r30'}, 80: {'identity': 's112'}, 81: {'(': '#', 'identity': '#', 'constnum': '#'}, 82: {'(': 's56', 'identity': 's57', 'constnum': 's58'}, 83: {';': 'r36'}, 84: {'{': 's114'}, 85: {';': 'r11', '+': 's64', '-': 's65'}, 86: {')': 's116', '+': 's90', '-': 's91'}, 87: {'(': 's56', 'identity': 's57', 'constnum': 's58'}, 88: {'(': 's56', 'identity': 's57', 'constnum': 's58'}, 89: {';': 'r27', '*': 'r27', '/': 'r27', '+': 'r27', '-': 'r27'}, 90: {'(': 's56', 'identity': 's57', 'constnum': 's58'}, 91: {'(': 's56', 'identity': 's57', 'constnum': 's58'}, 92: {';': 'r23', '*': 'r23', '/': 'r23', '+': 'r23', '-': 'r23'}, 93: {';': 'r24', '*': 'r24', '/': 'r24', '+': 'r24', '-': 'r24'}, 94: {';': 'r20', '+': 'r20', '-': 'r20', '*': 's62', '/': 's63'}, 95: {';': 'r21', '+': 'r21', '-': 'r21', '*': 's62', '/': 's63'}, 96: {')': 'r27'}, 97: {'<>': 'r27', '==': 'r27', '>=': 'r27', '<=': 'r27', '<': 'r27', '>': 'r27', '*': 'r27', '/': 'r27', '+': 'r27', '-': 'r27'}, 98: {'<>': 'r23', '==': 'r23', '>=': 'r23', '<=': 'r23', '<': 'r23', '>': 'r23', '*': 'r23', '/': 'r23', '+': 'r23', '-': 'r23'}, 99: {'<>': 'r24', '==': 'r24', '>=': 'r24', '<=': 'r24', '<': 'r24', '>': 'r24', '*': 'r24', '/': 'r24', '+': 'r24', '-': 'r24'}, 100: {'(': 's121'}, 101: {'(': 's122'}, 102: {'}': 'r3', 'identity': 's10', 'read': 's11', 'if': 's12', 'int': 's13', 'real': 's14', 'write': 's15', 'while': 's16'}, 103: {';': 'r7'}, 104: {'identity': 'r16', 'read': 'r16', 'if': 'r16', 'int': 'r16', 'real': 'r16', 'write': 'r16', 'while': 'r16', '}': 'r16', 'else': 's124'}, 105: {';': 's125'}, 106: {';': 'r6'}, 107: {';': 's126'}, 108: {';': 's127'}, 109: {';': 's128'}, 110: {'<>': 'r20', '==': 'r20', '>=': 'r20', '<=': 'r20', '<': 'r20', '>': 'r20', '+': 'r20', '-': 'r20', '*': 's69', '/': 's70'}, 111: {'<>': 'r21', '==': 'r21', '>=': 'r21', '<=': 'r21', '<': 'r21', '>': 'r21', '+': 'r21', '-': 'r21', '*': 's69', '/': 's70'}, 112: {'(': 's129'}, 113: {')': 'r18', '+': 's90', '-': 's91'}, 114: {'}': 'r3', 'identity': 's10', 'read': 's11', 'if': 's12', 'int': 's13', 'real': 's14', 'write': 's15', 'while': 's16'}, 115: {'identity': 'r34', 'read': 'r34', 'if': 'r34', 'int': 'r34', 'real': 'r34', 'write': 'r34', 'while': 'r34', '}': 'r34'}, 116: {')': 'r27', '*': 'r27', '/': 'r27', '+': 'r27', '-': 'r27'}, 117: {')': 'r23', '*': 'r23', '/': 'r23', '+': 'r23', '-': 'r23'}, 118: {')': 'r24', '*': 'r24', '/': 'r24', '+': 'r24', '-': 'r24'}, 119: {')': 'r20', '+': 'r20', '-': 'r20', '*': 's87', '/': 's88'}, 120: {')': 'r21', '+': 'r21', '-': 'r21', '*': 's87', '/': 's88'}, 121: {'(': 's46', 'identity': 's47', 'constnum': 's48'}, 122: {'(': 's46', 'identity': 's47', 'constnum': 's48'}, 123: {'}': 's133'}, 124: {'{': 's114'}, 125: {';': 'r5'}, 126: {'identity': 'r17', 'read': 'r17', 'if': 'r17', 'int': 'r17', 'real': 'r17', 'write': 'r17', 'while': 'r17', '}': 'r17'}, 127: {';': 'r9'}, 128: {';': 'r8'}, 129: {')': 's135'}, 130: {'}': 's136'}, 131: {')': 's137'}, 132: {')': 's138'}, 133: {'else': 'r2', 'identity': 'r2', 'read': 'r2', 'if': 'r2', 'int': 'r2', 'real': 'r2', 'write': 'r2', 'while': 'r2', '}': 'r2'}, 134: {'identity': 'r15', 'read': 'r15', 'if': 'r15', 'int': 'r15', 'real': 'r15', 'write': 'r15', 'while': 'r15', '}': 'r15'}, 135: {'{': 's139'}, 136: {'identity': 'r2', 'read': 'r2', 'if': 'r2', 'int': 'r2', 'real': 'r2', 'write': 'r2', 'while': 'r2', '}': 'r2'}, 137: {'identity': 's10', 'read': 's11', 'if': 's100', 'int': 's13', 'real': 's14', 'write': 's15', 'while': 's101', '{': 's141'}, 138: {'{': 's144'}, 139: {'}': 'r3', 'identity': 's10', 'read': 's11', 'if': 's12', 'int': 's13', 'real': 's14', 'write': 's15', 'while': 's16'}, 140: {'(': 'r1', 'identity': 'r1', 'constnum': 'r1'}, 141: {'}': 'r3', 'identity': 's10', 'read': 's11', 'if': 's12', 'int': 's13', 'real': 's14', 'write': 's15', 'while': 's16'}, 142: {';': 'r16', 'else': 's148'}, 143: {';': 's149'}, 144: {'}': 'r3', 'identity': 's10', 'read': 's11', 'if': 's12', 'int': 's13', 'real': 's14', 'write': 's15', 'while': 's16'}, 145: {';': 'r34'}, 146: {'}': 's151'}, 147: {'}': 's152'}, 148: {'{': 's144'}, 149: {';': 'r17'}, 150: {'}': 's154'}, 151: {'(': 'r2', 'identity': 'r2', 'constnum': 'r2'}, 152: {'else': 'r2', ';': 'r2'}, 153: {';': 'r15'}, 154: {';': 'r2'}}

goto_part = {0: {'E': 3, 'P': 4}, 7: {'B': 9}, 8: {'A': 17, 'C': 18, 'E': 19, 'F': 20, 'I': 21, 'L': 22, 'T': 23, 'W': 24}, 22: {'A': 17, 'C': 33, 'E': 19, 'F': 20, 'I': 21, 'L': 22, 'T': 23, 'W': 24}, 25: {'G': 39, 'R': 40, 'X': 41}, 26: {'R': 45}, 27: {'G': 49, 'O': 50, 'R': 51, 'X': 52}, 28: {'R': 53}, 29: {'G': 49, 'O': 54, 'R': 51, 'X': 52}, 36: {'G': 59, 'R': 60, 'X': 61}, 42: {'G': 59, 'R': 60, 'X': 66}, 46: {'G': 59, 'R': 60, 'X': 68}, 52: {'E': 80, 'P': 81, 'S': 82}, 55: {'G': 39, 'R': 40, 'X': 85}, 56: {'G': 59, 'R': 60, 'X': 86}, 62: {'R': 92}, 63: {'R': 93}, 64: {'G': 94, 'R': 40}, 65: {'G': 95, 'R': 40}, 69: {'R': 98}, 70: {'R': 99}, 71: {'A': 103, 'B': 104, 'E': 19, 'F': 105, 'I': 106, 'L': 107, 'T': 108, 'W': 109}, 74: {'G': 110, 'R': 51}, 76: {'G': 111, 'R': 51}, 82: {'G': 59, 'R': 60, 'X': 113}, 84: {'B': 115}, 87: {'R': 117}, 88: {'R': 118}, 90: {'G': 119, 'R': 60}, 91: {'G': 120, 'R': 60}, 102: {'A': 17, 'C': 123, 'E': 19, 'F': 20, 'I': 21, 'L': 22, 'T': 23, 'W': 24}, 114: {'A': 17, 'C': 130, 'E': 19, 'F': 20, 'I': 21, 'L': 22, 'T': 23, 'W': 24}, 121: {'G': 49, 'O': 131, 'R': 51, 'X': 52}, 122: {'G': 49, 'O': 132, 'R': 51, 'X': 52}, 124: {'B': 134}, 135: {'B': 140}, 137: {'A': 103, 'B': 142, 'E': 19, 'F': 105, 'I': 106, 'L': 143, 'T': 108, 'W': 109}, 138: {'B': 145}, 139: {'A': 17, 'C': 146, 'E': 19, 'F': 20, 'I': 21, 'L': 22, 'T': 23, 'W': 24}, 141: {'A': 17, 'C': 147, 'E': 19, 'F': 20, 'I': 21, 'L': 22, 'T': 23, 'W': 24}, 144: {'A': 17, 'C': 150, 'E': 19, 'F': 20, 'I': 21, 'L': 22, 'T': 23, 'W': 24}, 148: {'B': 153}}

action_table_data = {"forms": forms, "action": action_part, "goto": goto_part}


def check_action_part():
    keys = []

    datas = action_part.values()
    pass


if __name__ == "__main__":
    check_action_part()