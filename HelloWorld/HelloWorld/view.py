from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world! \n\t\t---made by mtli ")
