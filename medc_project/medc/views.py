from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, "base.html", context)


def error404(request):
    return render(request, '404.html')

def error400(request):
    return render(request, '404.html')

def error500(request):
    return render(request, '404.html')
