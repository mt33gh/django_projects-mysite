from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def index(request):
#    return HttpResponse("Hello, world. You're at the tmpl index.")
    return render(request, 'tmpl/main.html')

def simple(request):
    return render(request, 'tmpl/simple.html')

def guess(request):
    context = {'zap' : '42'}
    return render(request, 'tmpl/guess.html', context)

def special(request):
    context = {'txt':'<b>bold</b>', 'zap':'42'}
    return render(request, 'tmpl/special.html', context)

def loop(request):
    f = ['apple', 'orange', 'banana', 'lychee']
    n = ['peanut', 'cashew']
#    n = []
    context = {'fruits' : f, 'nuts' : n, 'zap' : '42' }
    return render(request, 'tmpl/loop.html', context)

def nested(request):
    context = {'outer':{'inner':{'innermost':'42'}}}
    return render(request, 'tmpl/nested.html', context)


class GameView(View):
    def get(self, request, guess):
        x= {'guess': int(guess) }
        return render(request, 'tmpl/cond.html', x)

class GameView2(View):
    def get(self, request, guess):
        x = {'guess': int(guess) }
        return render(request, 'tmpl/cond2.html', x)


