from action_table import ActionTable
from action_table_data import action_table_data


class SyntaxParser(object):

    def __init__(self):
        pass

    def parse_tokens(tokens):
        
        table = ActionTable(action_table_data)

        analysis_stack = []
        # TODO 赋予结束标志token更有意义的值
        analysis_stack.append((0, Token()))

        for token in tokens:
            status = analysis_stack[-1][0]

            action = table.goto(status, token)

            if 's' is action[0]:
                analysis_stack.append((action[1], action[2]))
            elif 'r' is action[0]:
                num2reduce = action[1]
                for _ in range(num2reduce):
                    analysis_stack.pop()

                token = action[2]
                status = table.goto(analysis_stack[-1][0], token)
                analysis_stack.append((status, token))
            else:
                pass

