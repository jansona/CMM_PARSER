from sig_table import SIG_TABLE_DICT as STD, get_key
# from token import *


# 我也是日了狗了，放在token.py下蜜汁失效
class Token(object):

    def __init__(self, idt=0, name="", val=None):
        
        self.idt = idt
        self.name = name
        self.val = val


def parse_sentence(sentence):

    tokens = []

    length = len(sentence)
    # for i in range(len(sentence)):
    i = 0
    while i < length:

        char = sentence[i]

        if str.isalpha(char) or char is '_':
            word = ""

            def is_alpha_ul_num(char):

                return str.isalpha(char) or char is '_' or str.isdigit(char)

            while is_alpha_ul_num(char):

                word += char
                i += 1

                if i >= length:
                    break

                char = sentence[i]

            if word in STD.keys():
                token = Token(idt=STD[word])
            else:
                token = Token(idt=STD['identity'], name=word)

            tokens.append(token)

            i -= 1
        elif str.isdigit(char):
            number_str = ""
            flag = False

            def is_num_dot(char):

                return str.isdigit(char) or char is '.'

            while is_num_dot(char):

                number_str += char

                if char is '.':
                    flag = True

                i += 1

                if i >= length:
                    break

                char = sentence[i]

            token = Token(idt=STD["constnum"], val=number_str)
            tokens.append(token)

            i -= 1
        elif str.isspace(char):
            pass
        elif char in r"+->(){}[];":
            sig_token = Token(idt=STD[char])
            tokens.append(sig_token)
        elif char in r"*/=<":
            sig_str = char + sentence[i+1]

            token = None
            if sig_str in STD.keys():
                token = Token(idt=STD[sig_str])
                i += 1
            else:
                token = Token(idt=STD[char])

            tokens.append(token)

        i += 1

    return tokens


class LexParser(object):

    def __init__(self):
        pass

    @staticmethod
    def check_tokens(tokens):

        for token in tokens:
            print(get_key(token.idt), end=' ')
            if(token.name!=''):
                print("name = ", end='')
                print(token.name, end=' ')
            if(token.val!=None):
                print("value = ", end='')
                print((token.val))
            else:
                print()


def test():
    code = "int main(){int a = write(x)?main(abc23);}"
    parser = LexParser()
    print(code)
    LexParser.check_tokens(parse_sentence(code))

if __name__ == "__main__":
    test()
