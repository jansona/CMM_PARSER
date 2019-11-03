import sys
import graphviz
from graphviz import Digraph
from subparser.action_table import ActionTable
from subparser.action_table_data import action_table_data
from subparser.cmm_token import Token
from subparser.auto_table_generator import replace_symbol_reverse
from subparser.forms import commands, Quadruple, gen


dot = Digraph(comment='The Round Table')
dot.format = 'png'

class SyntaxParser(object):

    def __init__(self):
        pass

    def parse_tokens(self, tokens, show_syntax=False, file_name=None, draw_graph=False, checkpoints=[]):

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
                print("Unexpected token: ")
                print("line: {}, '{}'".format(token.line, token.idt))
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

                token = action[2](*reduce_action_args)
                state = table.goto(analysis_stack[-1][0], token)
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
                return True
            else:
                return False

        if outstream is not sys.stdout:
            outstream.close()
            outstream = sys.stdout

