from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello world. This is the Django homepage.")
    return render(request, 'website/index.html')


def about(request):
    #return HttpResponse("Hello world. This is the Django about page.")
    return render(request, 'website/about.html')


def contact(request):
    #return HttpResponse("Hello world. This is the Django contact page.")
    return render(request, 'website/contact.html')