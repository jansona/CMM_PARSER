from 语义服务器.subparser.cmm_token import Token
from 语义服务器.subparser.forms import forms
from 语义服务器.subparser.actions import action_part
from 语义服务器.subparser.gotos import goto_part


action_table_data = {"forms": forms, "action": action_part, "goto": goto_part}

def check_action_part():
    keys = []

    datas = action_part.values()
    pass


if __name__ == "__main__":
    check_action_part()