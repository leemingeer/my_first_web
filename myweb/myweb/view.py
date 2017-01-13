from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world! ")

def blog(request):
    return HttpResponse("this is my blog! ")
