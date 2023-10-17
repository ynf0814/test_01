from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random

nextId = 4
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
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
    </body>
    </html>
    '''


def index(request):
    article='''<h2>Welcome</h2>
    안녕하세요. 장고입니다. '''
    return HttpResponse(HTML_Template(article))

@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
            <form action = "/create/" method = "POST">
                <p><input type="text" name="title" placeholder="title"></p>    
                <p><textarea name ="body" placeholder ="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
                '''
        return HttpResponse(HTML_Template(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id": nextId, "title":title, "body":body}
        topics.append(newTopic)
        nextId = nextId + 1
        return HttpResponse(HTML_Template(''))
    


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