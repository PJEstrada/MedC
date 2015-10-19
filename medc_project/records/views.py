from django.shortcuts import render
from users.models import PatientUser as Record
# Create your views here.

def records_general(request):

    expedientes_todos = Record.objects.all()

    return render(request,'records/records_all.html',{'expedientes_todos':expedientes_todos})

def records_search(request):
    search_query = request.POST['search_query']

    if(search_query==""):
        expedientes = Record.objects.all()
    else:

        expedientes = Record.objects.filter(user__first_name__icontains=search_query)


    return render(request,'records/records_all.html',{'search_query':search_query,'expedientes':expedientes})


def records_single(request):



    return render(request,'records/records_all.html',{})


def records_add(request):



    return render(request,'records/records_all.html',{})
