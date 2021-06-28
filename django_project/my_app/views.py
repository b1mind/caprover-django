from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("<h1>Just another server down!</h1>")
