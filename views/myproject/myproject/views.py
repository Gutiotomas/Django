from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse("404: Page not found!")

def error(request):
    return HttpResponseNotFound('<h1>Little Lemon</h1>')