from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape


# functions:
def funky(request):
    response = """<html><body><h1>Funky Function</h1>
    <p>This is a funky function created under views2/.</p>
    </body><html>""" 
    return HttpResponse(response)

def danger(request):
    response = """<html><body><h1>Danger Function</h1>
    <p>This page is dangerous.  Your guess was """ + request.GET['guess'] + """</p> 
    </body></html>"""
    return HttpResponse(response)

def game(request):
    guess = request.GET.get('guess', '')  # Use empty string as default if 'guess' is not provided
    safe_guess = escape(guess)
    response = f"""
    <html><body><h1>Modified Danger Function</h1><p>Now this page is safe.</p>
    <form method="get" action=""><label for="guess">Enter your guess</label>
    <input type="text" id="guess" name="guess" value="{safe_guess}"><input type="submit" value="Submit">
    </form><p>Your guess was: {safe_guess}</p></body></html>
    """
    return HttpResponse(response)

def game2(request):
    if request.method == "POST":
        guess = request.POST.get('guess', '')  # Use empty string as default if 'guess' is not provided
        safe_guess = escape(guess)
        return HttpResponse(f"Your guess was: {safe_guess}")     # Only this line is displayed on the browser
    return render(request, 'views2/game2.html')  # If not submitted, game2.html is displayed on the browser

def game3(request):
    if request.method == "POST":
        guess = request.POST.get('guess', '')  # Use empty string as default if 'guess' is not provided
        safe_guess = escape(guess)
        return render(request, 'views2/game3.html', {'safe_guess':safe_guess})  # displays game3.html and safe_guess
    return render(request, 'views2/game3.html')  # If not submitted, game3.html is displayed on the browser

def rest(request, guess):
    safe_guess = escape(guess)
    response = f"""
    <html><body><h1>Parsing the URL without GET or POST methods</h1><p>There is no input box.</p>
    <p>Put your guess after the URL and a slash</p><p>Your guess was: {safe_guess}</p></body></html>
    """
    return HttpResponse(response)

def bounce(request):
    # This is a command to the browser
    return HttpResponseRedirect('https://englishforengineers.jimdofree.com/2025/05/28/django-slug-guess/')


# classes:
class MainView(View):
    def get(self, request):
        return render(request, 'views2/main.html')

class MainView2(View):
    def get(self, request):
        response = """
        <html><body><p>Hello world MainView2 in HTML</p>
        <p>This sample code is available at 
        <a href="https://github.com/csev/dj4e-samples">https://github.com/csev/dj4e-samples</a></p>
        </body></html>"""
        return HttpResponse(response)

class RestMainView2(View):
    def get(self, request, guess):
        safe_guess = escape(guess)
        response = f"""
        <html><body><p>Hello world RestMainView2 in HTML</p>
        <p>Put your guess after the URL and a slash</p><p>Your guess was: {safe_guess}</p>
        </body></html>"""
        return HttpResponse(response)

