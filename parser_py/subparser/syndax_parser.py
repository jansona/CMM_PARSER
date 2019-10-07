from subparser.action_table import ActionTable
from subparser.action_table_data import action_table_data
from subparser.cmm_token import Token


class SyntaxParser(object):

    def __init__(self):
        pass

    def parse_tokens(self, tokens):
        
        table = ActionTable(action_table_data)

        analysis_stack = []
        # TODO 赋予结束标志token更有意义的值
        analysis_stack.append((0, Token(idt="#")))

        i = 0
        length = len(tokens)
        while i < length:
            token = tokens[i]
            state = analysis_stack[-1][0]

            print(token.idt, analysis_stack[-1][0])
            action = table.action(state, token)

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

