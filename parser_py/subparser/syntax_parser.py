from subparser.action_table import ActionTable
from subparser.action_table_data import action_table_data
from subparser.cmm_token import Token
import sys


class SyntaxParser(object):

    def __init__(self):
        pass

    def parse_tokens(self, tokens, show_syntax=False, file_name=None):
        
        table = ActionTable(action_table_data)

        analysis_stack = []
        # TODO 赋予结束标志token更有意义的值
        analysis_stack.append((0, Token(idt="#")))

        i = 0
        length = len(tokens)

        if file_name:
            fout = open(file_name + ".syn", 'w')
            outstream = fout
        else:
            outstream = sys.stdout
        
        while i < length:
            token = tokens[i]
            state = analysis_stack[-1][0]

            action = table.action(state, token)

            if show_syntax:

                def show_stack():
                    print("analysis stack:", end="\t", file=outstream)
                    print(" ".join(["{}:{}".format(elem[0], elem[1].idt) for elem in analysis_stack]), file=outstream)

                show_stack()
                print("token incoming: {}".format(token.idt), file=outstream)
                print("action: {}".format(action[0]), file=outstream)
                print(file=outstream)
                # input() 单步好像没啥意义

            if 's' is action[0]:
                analysis_stack.append((action[1], action[2]))
                i += 1
            elif 'r' is action[0]:
                num2reduce = action[1]

                reduce_action_args = []
                for _ in range(num2reduce):
                    reduce_action_args.append(analysis_stack.pop())
                reduce_action_args.reverse()

                # TODO 规约动作暂时没有利用参数
                token = action[2]()
                state = table.goto(analysis_stack[-1][0], token)
                analysis_stack.append((state, token))
            elif '#' in action[0]:
                return True
            else:
                return False

        if outstream is not sys.stdout:
            outstream.close()
            outstream = sys.stdout

