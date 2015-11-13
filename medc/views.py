from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.


@login_required(login_url='/users/login/')
def home(request):
    context = {}
    return redirect(reverse('home_view'))


def home_view(request):

    return render(request,'agenda/home.html',{})
def error404(request):
    return render(request, '404.html')

def error400(request):
    return render(request, '404.html')

def error500(request):
    return render(request, '404.html')
