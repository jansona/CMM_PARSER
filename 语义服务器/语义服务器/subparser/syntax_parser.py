import sys
import graphviz
from graphviz import Digraph
from 语义服务器.subparser.action_table import ActionTable
from 语义服务器.subparser.action_table_data import action_table_data
from 语义服务器.subparser.cmm_token import Token
from 语义服务器.subparser.auto_table_generator import replace_symbol_reverse
from 语义服务器.subparser.forms import commands, Quadruple, gen
from 语义服务器.subparser.ParseErrData import SYN_ERR, ParseErrData


dot = Digraph(comment='The Round Table')
dot.format = 'png'

class SyntaxParser(object):


    def __init__(self):
        pass

    def parse_tokens(self, tokens, show_syntax=False, file_name=None, draw_graph=False, checkpoints=[]):

        err_list = []
        sem_err_mark = False

        succeeded = False

        dot.clear()
        
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

        line = 1
        temp_str = ""
        
        while i < length:
            token = tokens[i]

            current_line = token.line

            state = analysis_stack[-1][0]

            # 加入断点
            if int(token.line) in checkpoints:
                gen('check', None, None, None)
                checkpoints.remove(token.line)

            if line != token.line:
                gen('step', None, None, None)
                line = token.line
            # end
            
            try:
                action = table.action(state, token)
            except:
                # TODO 这种处理不妥

                mark = ""
                mark_type = ""
                if token.idt == 'constnum':
                    mark_type = 'const num'
                    mark = token.value
                elif token.idt == 'identity':
                    mark_type = 'variable'
                    mark = token.name
                else:
                    mark_type = 'key word'
                    mark = token.idt

                parse_err = ParseErrData(SYN_ERR, int(token.line),
                 message="Action failed. Unexpected {}: '{}'.".format(mark_type, mark))
                print(parse_err)
                exit(1)

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

                new_nodes = []

                for _ in range(num2reduce):
                    pop_token = analysis_stack.pop()[1]
                    # reduce_action_args[replace_symbol_reverse(pop_token.idt)] = pop_token
                    reduce_action_args.append(pop_token)

                    new_nodes.append(pop_token)

                reduce_action_args.reverse()

                try:
                    token = action[2](*reduce_action_args)
                except ParseErrData as ped:
                    err_list.append(ped)
                    sem_err_mark = True
                    token = ped.token

                # TODO 一种很简单的处理
                try:
                    state = table.goto(analysis_stack[-1][0], token)
                except Exception:
                    parse_err = ParseErrData(SYN_ERR, int(current_line), 
                    message="Reduction failed. Thers's something wrong with the forms usually.")
                    print(parse_err)
                    exit(1)

                analysis_stack.append((state, token))

                if draw_graph:
                    dot.node(str(token.count), token.idt)
                    new_nodes.reverse()
                    for child in new_nodes:
                        dot.node(str(child.count), child.idt)
                        dot.edge(str(token.count), str(child.count))

            elif '#' in action[0]:
                if draw_graph:
                    print(file_name)
                    dot.render(file_name)

                succeeded = True
                break
            else:
                succeeded = False
                break

        if sem_err_mark:
            for err in err_list:
                print(err)
            exit(1)

        if outstream is not sys.stdout:
            outstream.close()
            outstream = sys.stdout

        return succeeded

