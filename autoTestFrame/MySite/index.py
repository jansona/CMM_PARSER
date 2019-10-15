from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http.request import HttpRequest

# 表单
from MySite.lex_parser import LexParser, parse_sentence
from MySite.sig_table import get_key


def test_page(request):
    return render_to_response('test_page.html')


# 接收请求数据
def test(request):
    request.encoding = 'utf-8'
    if 'code' in request.GET and request.GET['code']:
        code = request.GET['code']
        parser = LexParser()
        tokens = parse_sentence(code)
        message = '代码:' + code + '<br>' + '词法分析结果: <br>'
        for token in tokens:
            message += (get_key(token.idt))[0]
            if token.name != '':
                message += (" name = " + '\n')
                message += (token.name + '<br>')
            elif token.val is not None:
                message += " value = "
                message += (token.val + '<br>')
            else:
                message += '<br>'

    else:
        message = '你提交了空表单'
    return HttpResponse(message)
