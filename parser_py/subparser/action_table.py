from subparser.action_table_data import action_table_data
from subparser.token import Token



class ActionTable(object):

    def __init__(self, table_data):
        self.table_data = table_data

    def action(self, status: int, token: Token):
        row = self.table_data["action"][status]
        action = row[token.idt]

        if 's' in action:
            return ('s', int(action[1:]), token)   # 第一个“s”暗示调用方进行移入，第二个参数代表移进后的状态，第三个状态是需要移入的tokens
        elif 'r' in action:
            form_num = action[1:]
            (num2reduce, token) = self.table_data["forms"][form_num]
            return ('r', num2reduce, token)
        elif '#' in action:
            return ('#',)
        else:
            return ('err', token)

    def goto(self, status, token):
        return self.table_data["goto"][status][token.idt]