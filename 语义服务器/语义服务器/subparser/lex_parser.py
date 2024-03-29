from 语义服务器.subparser.sig_table import SIG_TABLE_DICT as STD, get_key
from 语义服务器.subparser.ParseErrData import LEX_ERR, ParseErrData
from 语义服务器.subparser.cmm_token import *
import sys


class LexParser(object):

    def __init__(self):
        self.err_mark = False

    def parse_sentence(self, sentence):

        err_list = []

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

                # TODO 数字开头，后跟没空白符
                if is_alpha_ul_num(char):
                    self.err_mark = True
                    err_list.append(ParseErrData(LEX_ERR, int(line), "Variable shouldn't begin with number"))
                    i += 1
                    continue

                token = Token(idt=STD["constnum"], value=number_str, line=line)
                tokens.append(token)

                i -= 1
            elif str.isspace(char):
                if char is '\n':
                    line += 0.5         # 这里注意！！！ 我真是服了，windows下结尾两个\n
                pass
            elif char in r"+-(){}[];,":
                sig_token = Token(idt=STD[char], line=line)
                tokens.append(sig_token)
            elif char in r"*/=<>":
                sig_str = char + sentence[i+1]

                token = None
  
                if sig_str in ("/*",):
                    i += 1
                    find_right_comment = False
                    while i < length-1:
                        two_char = sentence[i:i+2]

                        if two_char == "\n\n":
                            line += 1

                        if two_char in ("*/",):
                            find_right_comment = True
                            i += 2
                            break
                        i += 1
                    if find_right_comment:
                        continue
                    else:
                        self.err_mark = True
                        self.err_list.append(ParseErrData(LEX_ERR, int(line), "Unpaired comment"))
                        i += 1
                        exit(1)
                elif sig_str in STD.keys():
                    token = Token(idt=STD[sig_str], line=line)
                    i += 1
                else:
                    token = Token(idt=STD[char], line=line)

                tokens.append(token)
            else:
                self.err_mark = True
                err_list.append(ParseErrData(LEX_ERR, int(line), "Unexpected character"))
                i += 1
                continue

            i += 1

        for err in err_list:
            print(err)

        tokens.append(Token(idt=STD['#'], line=line))
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
    def check_tokens_2(tokens, file_name=None):

        if file_name:
            fout = open(file_name + ".lex", 'w')
            outstream = fout
        else:
            outstream = sys.stdout
        
        for token in tokens:
            print("idt:<{}>".format(token.idt), end='', file=outstream)
            if(token.name!=''):
                print(", name:'{}'".format(token.name), end='', file=outstream)
            if(token.value!=None):
                print(", value:'{}'".format(token.value), end='', file=outstream)
            else:
                print(file=outstream)

        if outstream is not sys.stdout:
            outstream.close()
            outstream = sys.stdout

def test():
    code = "main()"

    parser = LexParser()
    
    LexParser.check_tokens_2(parser.parse_sentence(code))


if __name__ == "__main__":
    test()
