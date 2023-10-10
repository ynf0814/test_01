from django.shortcuts import render, HttpResponse
import random

topics = [
    {'id' : 1, 'title' : '전자통신컴퓨터공학부', 'body' : '전자통신컴퓨터공학부에 오신 것을 환영합니다.'},
    {'id' : 2, 'title' : '간호학과', 'body' : '간호학과에 오신 것을 환영합니다.'},
    {'id' : 3, 'title' : '유아교육학과', 'body' : '유아교육학과에 오신 것을 환영합니다.'},
]

def HTML_Template(articleTag):
    global topics 
    ol = ''
    for topic in topics:
        ol += f'<li> <a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
    </body>
    </html>
    '''


def index(request):
    article='''<h2>Welcome</h2>
    안녕하세요. 장고입니다. '''
    return HttpResponse(HTML_Template(article))

def creat(request):
    return HttpResponse('안녕하세요 Creat 홈페이지에 오신 것을 환영합니다. ')

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTML_Template(article))

def lotto(request):
    c = ''
    b = random.sample(range(1,46), 6)
    b.sort()
    for i in range(6):
        c += str(b[i]) + ' '
    return HttpResponse('<h1>오늘의 행운의 번호 = '+c+' 입니다.</h1>')