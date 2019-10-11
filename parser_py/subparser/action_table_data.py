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
    return Token(idt="C")

def reduce_5():
    return Token(idt="L")

def reduce_6():
    return Token(idt="C")

def reduce_7():
    return Token(idt="C")

def reduce_8():
    return Token(idt="L")

def reduce_9():
    return Token(idt="L")

def reduce_10():
    return Token(idt="C")

def reduce_11():
    return Token(idt="F")

def reduce_12():
    return Token(idt="F")

def reduce_13():
    return Token(idt="E")

def reduce_14():
    return Token(idt="E")

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

forms = [(4, reduce_0), (3, reduce_1), (0, reduce_2), (3, reduce_3), (3, reduce_4), (1, reduce_5), (1, reduce_6), (1, reduce_7), (1, reduce_8), (1, reduce_9), (5, reduce_10), (4, reduce_11), (3, reduce_12), (1, reduce_13), (1, reduce_14), (7, reduce_15), (6, reduce_16), (3, reduce_17), (1, reduce_18), (3, reduce_19), (3, reduce_20), (1, reduce_21), (3, reduce_22), (3, reduce_23), (1, reduce_24), (1, reduce_25), (3, reduce_26), (1, reduce_27), (1, reduce_28), (1, reduce_29), (1, reduce_30), (1, reduce_31), (1, reduce_32), (6, reduce_33), (4, reduce_34), (3, reduce_35)]

action_part = {0: {'identity': 's1'}, 1: {'(': 's3'}, 2: {'#': '#'}, 3: {')': 's4'}, 4: {'{': 's5'}, 5: {'}': 'r3', 'identity': 's8', 'read': 's9', 'int': 's11', 'real': 's13', 'write': 's14', '/': 's7', 'if': 's10', 'do': 's12'}, 6: {'#': 'r1'}, 7: {'*': 's23'}, 8: {'=': 's24'}, 9: {'(': 's25'}, 10: {'(': 's26'}, 11: {'identity': 'r15'}, 12: {'{': 's27'}, 13: {'identity': 'r14'}, 14: {'(': 's29'}, 15: {'}': 'r8', 'identity': 'r8', 'read': 'r8', 'int': 'r8', 'real': 'r8', 'write': 'r8'}, 16: {'identity': 's8', 'read': 's9', 'int': 's11', 'real': 's13', 'write': 's14', '}': 's30'}, 17: {'identity': 's32'}, 18: {';': 'r6'}, 19: {'}': 'r7', 'identity': 'r7', 'read': 'r7', 'int': 'r7', 'real': 'r7', 'write': 'r7'}, 20: {';': 's33'}, 21: {';': 'r10'}, 22: {';': 'r9'}, 23: {'constnum': 's34'}, 24: {'(': 's35', 'identity': 's36', 'constnum': 's37'}, 25: {'(': 's41', 'identity': 's42', 'constnum': 's43'}, 26: {'(': 's45', 'identity': 's46', 'constnum': 's47'}, 27: {'}': 'r3', 'identity': 's8', 'read': 's9', 'int': 's11', 'real': 's13', 'write': 's14', '/': 's7', 'if': 's10', 'do': 's12'}, 28: {'while': 's53'}, 29: {'(': 's41', 'identity': 's42', 'constnum': 's43'}, 30: {'#': 'r2'}, 31: {';': 's55'}, 32: {'=': 's56'}, 33: {'}': 'r3', 'identity': 's8', 'read': 's9', 'int': 's11', 'real': 's13', 'write': 's14', '/': 's7', 'if': 's10', 'do': 's12'}, 34: {'*': 's58'}, 35: {'(': 's59', 'identity': 's60', 'constnum': 's61'}, 36: {';': 'r25', '*': 'r25', '/': 'r25', '+': 'r25', '-': 'r25'}, 37: {';': 'r26', '*': 'r26', '/': 'r26', '+': 'r26', '-': 'r26'}, 38: {';': 'r19', '+': 'r19', '-': 'r19', '*': 's65', '/': 's66'}, 39: {';': 'r22', '*': 'r22', '/': 'r22', '+': 'r22', '-': 'r22'}, 40: {';': 'r13', '+': 's67', '-': 's68'}, 41: {'(': 's59', 'identity': 's60', 'constnum': 's61'}, 42: {')': 'r25'}, 43: {')': 'r26'}, 44: {')': 's70'}, 45: {'(': 's59', 'identity': 's60', 'constnum': 's61'}, 46: {'<>': 'r25', '==': 'r25', '>=': 'r25', '<=': 'r25', '<': 'r25', '>': 'r25', '*': 'r25', '/': 'r25', '+': 'r25', '-': 'r25'}, 47: {'<>': 'r26', '==': 'r26', '>=': 'r26', '<=': 'r26', '<': 'r26', '>': 'r26', '*': 'r26', '/': 'r26', '+': 'r26', '-': 'r26'}, 48: {'<>': 'r19', '==': 'r19', '>=': 'r19', '<=': 'r19', '<': 'r19', '>': 'r19', '+': 'r19', '-': 'r19', '*': 's72', '/': 's73'}, 49: {')': 's74'}, 50: {'<>': 'r22', '==': 'r22', '>=': 'r22', '<=': 'r22', '<': 'r22', '>': 'r22', '*': 'r22', '/': 'r22', '+': 'r22', '-': 'r22'}, 51: {'<>': 's75', '==': 's76', '+': 's77', '>=': 's78', '-': 's79', '<=': 's80', '<': 's81', '>': 's82', 'identity': 's83'}, 52: {'identity': 's8', 'read': 's9', 'int': 's11', 'real': 's13', 'write': 's14', '}': 's86'}, 53: {'(': 's87'}, 54: {')': 's88'}, 55: {'}': 'r4', 'identity': 'r4', 'read': 'r4', 'int': 'r4', 'real': 'r4', 'write': 'r4'}, 56: {'(': 's35', 'identity': 's36', 'constnum': 's37'}, 57: {'}': 'r5', 'identity': 's8', 'read': 's9', 'int': 's11', 'real': 's13', 'write': 's14'}, 58: {'/': 's90'}, 59: {'(': 's59', 'identity': 's60', 'constnum': 's61'}, 60: {')': 'r25', '*': 'r25', '/': 'r25', '+': 'r25', '-': 'r25'}, 61: {')': 'r26', '*': 'r26', '/': 'r26', '+': 'r26', '-': 'r26'}, 62: {')': 'r19', '+': 'r19', '-': 'r19', '*': 's92', '/': 's93'}, 63: {')': 'r22', '*': 'r22', '/': 'r22', '+': 'r22', '-': 'r22'}, 64: {')': 's94', '+': 's95', '-': 's96'}, 65: {'(': 's35', 'identity': 's36', 'constnum': 's37'}, 66: {'(': 's35', 'identity': 's36', 'constnum': 's37'}, 67: {'(': 's35', 'identity': 's36', 'constnum': 's37'}, 68: {'(': 's35', 'identity': 's36', 'constnum': 's37'}, 69: {')': 's101', '+': 's95', '-': 's96'}, 70: {';': 'r35'}, 71: {')': 's102', '+': 's95', '-': 's96'}, 72: {'(': 's45', 'identity': 's46', 'constnum': 's47'}, 73: {'(': 's45', 'identity': 's46', 'constnum': 's47'}, 74: {'identity': 's8', 'read': 's9', 'int': 's11', 'real': 's13', 'write': 's14', '{': 's105'}, 75: {'(': 'r33', 'identity': 'r33', 'constnum': 'r33'}, 76: {'(': 'r32', 'identity': 'r32', 'constnum': 'r32'}, 77: {'(': 's45', 'identity': 's46', 'constnum': 's47'}, 78: {'(': 'r31', 'identity': 'r31', 'constnum': 'r31'}, 79: {'(': 's45', 'identity': 's46', 'constnum': 's47'}, 80: {'(': 'r29', 'identity': 'r29', 'constnum': 'r29'}, 81: {'(': 'r28', 'identity': 'r28', 'constnum': 'r28'}, 82: {'(': 'r30', 'identity': 'r30', 'constnum': 'r30'}, 83: {'(': 's110'}, 84: {'(': '#', 'identity': '#', 'constnum': '#'}, 85: {'(': 's59', 'identity': 's60', 'constnum': 's61'}, 86: {'while': 'r2'}, 87: {'(': 's45', 'identity': 's46', 'constnum': 's47'}, 88: {';': 'r36'}, 89: {';': 'r12', '+': 's67', '-': 's68'}, 90: {'}': 'r11', 'identity': 'r11', 'read': 'r11', 'int': 'r11', 'real': 'r11', 'write': 'r11'}, 91: {')': 's113', '+': 's95', '-': 's96'}, 92: {'(': 's59', 'identity': 's60', 'constnum': 's61'}, 93: {'(': 's59', 'identity': 's60', 'constnum': 's61'}, 94: {';': 'r27', '*': 'r27', '/': 'r27', '+': 'r27', '-': 'r27'}, 95: {'(': 's59', 'identity': 's60', 'constnum': 's61'}, 96: {'(': 's59', 'identity': 's60', 'constnum': 's61'}, 97: {';': 'r23', '*': 'r23', '/': 'r23', '+': 'r23', '-': 'r23'}, 98: {';': 'r24', '*': 'r24', '/': 'r24', '+': 'r24', '-': 'r24'}, 99: {';': 'r20', '+': 'r20', '-': 'r20', '*': 's65', '/': 's66'}, 100: {';': 'r21', '+': 'r21', '-': 'r21', '*': 's65', '/': 's66'}, 101: {')': 'r27'}, 102: {'<>': 'r27', '==': 'r27', '>=': 'r27', '<=': 'r27', '<': 'r27', '>': 'r27', '*': 'r27', '/': 'r27', '+': 'r27', '-': 'r27'}, 103: {'<>': 'r23', '==': 'r23', '>=': 'r23', '<=': 'r23', '<': 'r23', '>': 'r23', '*': 'r23', '/': 'r23', '+': 'r23', '-': 'r23'}, 104: {'<>': 'r24', '==': 'r24', '>=': 'r24', '<=': 'r24', '<': 'r24', '>': 'r24', '*': 'r24', '/': 'r24', '+': 'r24', '-': 'r24'}, 105: {'}': 'r3', 'identity': 's8', 'read': 's9', 'int': 's11', 'real': 's13', 'write': 's14', '/': 's7', 'if': 's10', 'do': 's12'}, 106: {'else': 's119'}, 107: {';': 's120'}, 108: {'<>': 'r20', '==': 'r20', '>=': 'r20', '<=': 'r20', '<': 'r20', '>': 'r20', '+': 'r20', '-': 'r20', '*': 's72', '/': 's73'}, 109: {'<>': 'r21', '==': 'r21', '>=': 'r21', '<=': 'r21', '<': 'r21', '>': 'r21', '+': 'r21', '-': 'r21', '*': 's72', '/': 's73'}, 110: {')': 's121'}, 111: {')': 'r18', '+': 's95', '-': 's96'}, 112: {')': 's122'}, 113: {')': 'r27', '*': 'r27', '/': 'r27', '+': 'r27', '-': 'r27'}, 114: {')': 'r23', '*': 'r23', '/': 'r23', '+': 'r23', '-': 'r23'}, 115: {')': 'r24', '*': 'r24', '/': 'r24', '+': 'r24', '-': 'r24'}, 116: {')': 'r20', '+': 'r20', '-': 'r20', '*': 's92', '/': 's93'}, 117: {')': 'r21', '+': 'r21', '-': 'r21', '*': 's92', '/': 's93'}, 118: {'identity': 's8', 'read': 's9', 'int': 's11', 'real': 's13', 'write': 's14', '}': 's123'}, 119: {'{': 's124'}, 120: {'}': 'r17', 'identity': 'r17', 'read': 'r17', 'int': 'r17', 'real': 'r17', 'write': 'r17'}, 121: {'{': 's126'}, 122: {'}': 'r34', 'identity': 'r34', 'read': 'r34', 'int': 'r34', 'real': 'r34', 'write': 'r34'}, 123: {'else': 'r2'}, 124: {'}': 'r3', 'identity': 's8', 'read': 's9', 'int': 's11', 'real': 's13', 'write': 's14', '/': 's7', 'if': 's10', 'do': 's12'}, 125: {'}': 'r16', 'identity': 'r16', 'read': 'r16', 'int': 'r16', 'real': 'r16', 'write': 'r16'}, 126: {'}': 'r3', 'identity': 's8', 'read': 's9', 'int': 's11', 'real': 's13', 'write': 's14', '/': 's7', 'if': 's10', 'do': 's12'}, 127: {'(': 'r1', 'identity': 'r1', 'constnum': 'r1'}, 128: {'identity': 's8', 'read': 's9', 'int': 's11', 'real': 's13', 'write': 's14', '}': 's130'}, 129: {'identity': 's8', 'read': 's9', 'int': 's11', 'real': 's13', 'write': 's14', '}': 's131'}, 130: {'}': 'r2', 'identity': 'r2', 'read': 'r2', 'int': 'r2', 'real': 'r2', 'write': 'r2'}, 131: {'(': 'r2', 'identity': 'r2', 'constnum': 'r2'}}

goto_part = {0: {'P': 2}, 4: {'B': 6}, 5: {'A': 15, 'C': 16, 'E': 17, 'F': 18, 'I': 19, 'L': 20, 'T': 21, 'W': 22}, 12: {'B': 28}, 16: {'E': 17, 'F': 18, 'L': 31, 'T': 21, 'W': 22}, 24: {'G': 38, 'R': 39, 'X': 40}, 25: {'R': 44}, 26: {'G': 48, 'O': 49, 'R': 50, 'X': 51}, 27: {'A': 15, 'C': 52, 'E': 17, 'F': 18, 'I': 19, 'L': 20, 'T': 21, 'W': 22}, 29: {'R': 54}, 33: {'A': 15, 'C': 57, 'E': 17, 'F': 18, 'I': 19, 'L': 20, 'T': 21, 'W': 22}, 35: {'G': 62, 'R': 63, 'X': 64}, 41: {'G': 62, 'R': 63, 'X': 69}, 45: {'G': 62, 'R': 63, 'X': 71}, 51: {'P': 84, 'S': 85}, 52: {'E': 17, 'F': 18, 'L': 31, 'T': 21, 'W': 22}, 56: {'G': 38, 'R': 39, 'X': 89}, 57: {'E': 17, 'F': 18, 'L': 31, 'T': 21, 'W': 22}, 59: {'G': 62, 'R': 63, 'X': 91}, 65: {'R': 97}, 66: {'R': 98}, 67: {'G': 99, 'R': 39}, 68: {'G': 100, 'R': 39}, 72: {'R': 103}, 73: {'R': 104}, 74: {'B': 106, 'E': 17, 'F': 18, 'L': 107, 'T': 21, 'W': 22}, 77: {'G': 108, 'R': 50}, 79: {'G': 109, 'R': 50}, 85: {'G': 62, 'R': 63, 'X': 111}, 87: {'G': 48, 'O': 112, 'R': 50, 'X': 51}, 92: {'R': 114}, 93: {'R': 115}, 95: {'G': 116, 'R': 63}, 96: {'G': 117, 'R': 63}, 105: {'A': 15, 'C': 118, 'E': 17, 'F': 18, 'I': 19, 'L': 20, 'T': 21, 'W': 22}, 118: {'E': 17, 'F': 18, 'L': 31, 'T': 21, 'W': 22}, 119: {'B': 125}, 121: {'B': 127}, 124: {'A': 15, 'C': 128, 'E': 17, 'F': 18, 'I': 19, 'L': 20, 'T': 21, 'W': 22}, 126: {'A': 15, 'C': 129, 'E': 17, 'F': 18, 'I': 19, 'L': 20, 'T': 21, 'W': 22}, 128: {'E': 17, 'F': 18, 'L': 31, 'T': 21, 'W': 22}, 129: {'E': 17, 'F': 18, 'L': 31, 'T': 21, 'W': 22}}

action_table_data = {"forms": forms, "action": action_part, "goto": goto_part}


def check_action_part():
    keys = []

    datas = action_part.values()
    pass


if __name__ == "__main__":
    check_action_part()