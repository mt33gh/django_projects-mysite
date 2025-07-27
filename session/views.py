from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone

# https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/', 
#     domain=None, secure=None, httponly=False, samesite=None)

def cookie(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    resp = HttpResponse('In a view - the zap cookie value is '+str(oldval))
    if oldval : 
        resp.set_cookie('zap', int(oldval)+1) # No expired date = until browser close
    else : 
        resp.set_cookie('zap', 42) # No expired date = until browser close
    resp.set_cookie('sakaicar', 42, max_age=1000) # seconds until expire
    return resp

def seelog(request):
    print(f"[{timezone.now().strftime('%d/%b%H:%M:%S')}] \"{request.method} {request.path}HTTP/1.1\"")
    print(request.COOKIES)  # Shows all cookies sent by the browser
    print(request.session.items())  # Shows session data (dict-like)
    return HttpResponse("Hello")

def sessfun(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits 
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    return resp
