from subparser.sig_table import SIG_TABLE_DICT as STD, get_key
from subparser.cmm_token import *


class LexParser(object):

    def __init__(self):
        pass

    def parse_sentence(self, sentence):

        tokens = []
        line = 1

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
                    token = Token(idt=STD[word], line=line)
                else:
                    token = Token(idt=STD['identity'], name=word, line=line)

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

                token = Token(idt=STD["constnum"], value=number_str, line=line)
                tokens.append(token)

                i -= 1
            elif str.isspace(char):
                if char is '\n':
                    line += 1
                pass
            elif char in r"+->(){}[];":
                sig_token = Token(idt=STD[char])
                tokens.append(sig_token)
            elif char in r"*/=<":
                sig_str = char + sentence[i+1]

                token = None
  
                if sig_str in ("/*",):
                    i += 1
                    find_right_comment = False
                    while i < length-1:
                        two_char = sentence[i:i+2]
                        if two_char in ("*/",):
                            find_right_comment = True
                            i += 2
                            break
                        i += 1
                    if find_right_comment:
                        continue
                    else:
                        print("err")
                        exit(1) # handle error of unpaired comments
                elif sig_str in STD.keys():
                    token = Token(idt=STD[sig_str], line=line)
                    i += 1
                else:
                    token = Token(idt=STD[char], line=line)

                tokens.append(token)

            i += 1

        tokens.append(Token(idt=STD['#']))
        return tokens

    # @staticmethod
    # def check_tokens(tokens):
        
    #     for token in tokens:
    #         print("idt:{}".format(get_key(token.idt)), end=' ')
    #         if(token.name!=''):
    #             print("name:{}".format(token.name), end=' ')
    #         if(token.value!=None):
    #             print("value:{}".format(token.value), end=' ')
    #         else:
    #             print()
    
    @staticmethod
    def check_tokens_2(tokens):
        
        for token in tokens:
            print("idt:<{}>".format(token.idt), end='')
            if(token.name!=''):
                print(", name:'{}'".format(token.name), end='')
            if(token.value!=None):
                print(", value:'{}'".format(token.value), end='')
            else:
                print()

def test():
    code = "main()"

    parser = LexParser()
    
    LexParser.check_tokens_2(parser.parse_sentence(code))


if __name__ == "__main__":
    test()
