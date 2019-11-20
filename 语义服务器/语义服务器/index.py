from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http.request import HttpRequest

from 语义服务器.subparser import action_table_data
from 语义服务器.subparser.action_table import ActionTable
from 语义服务器.subparser.cmm_token import Token
from 语义服务器.cmm_parser import CmmParser
from 语义服务器.subparser.forms import commands
from 语义服务器.subparser.lex_parser import LexParser
from 语义服务器.subparser.syntax_parser import SyntaxParser
from 语义服务器.subparser.forms import clear

def test_page(request):
    return render_to_response('test_page.html')


def test(request):
    request.encoding = 'utf-8'
    if 'code' in request.GET and request.GET['code']:
        code = request.GET['code']
        message = '代码:' + code + '<br>' + '语法分析结果: <br>'
        parser = CmmParser(LexParser(), SyntaxParser())
        parser.parse(code, show_lex=False, show_syntax=False)

        for index, cmd in enumerate(commands):
            print(
                "{:3}: ({:^6},{:^6},{:^6},{:^6})".format(index, cmd.op, str(cmd.arg0), str(cmd.arg1), str(cmd.result)))
            message += "{:3}: ({:^6},{:^6},{:^6},{:^6})".format(index, cmd.op, str(cmd.arg0), str(cmd.arg1),
                                                                str(cmd.result))
            message += '<br>'
        clear()

    else:
        message = '你提交了空表单'
    return HttpResponse(message)
