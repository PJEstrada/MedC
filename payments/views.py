from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import InvoiceForm
from .models import Invoice
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.db.models import  Q

from users.models import PatientUser as Record
from django.core.urlresolvers import reverse
# Create your views here.

@login_required
def payments_all(request):


    if not User.objects.filter(Q(pk=request.user.id),Q(groups__name='Doctor') | Q(groups__name='Cajero')).exists():
        print("No hay permisos!!")
        return render(request,'agenda/permisos.html',{})
    else:
        pagos = Invoice.objects.all().order_by('-date')[:50]
        suma =0
        for p in pagos:
            suma = suma + p.total
        return render(request,'caja/payments_all.html',{'pagos':pagos,'suma':suma})




@login_required
def payments_add(request):


    if not User.objects.filter(Q(pk=request.user.id),Q(groups__name='Doctor') | Q(groups__name='Cajero')).exists():
        print("No hay permisos!!")
        return render(request,'agenda/permisos.html',{})
    else:

        form = InvoiceForm()
        return render(request,'caja/new_payment.html',{'form':form})

@login_required
def payments_create(request):


    if not User.objects.filter(Q(pk=request.user.id),Q(groups__name='Doctor') | Q(groups__name='Cajero')).exists():
        print("No hay permisos!!")
        return render(request,'agenda/permisos.html',{})
    else:
        if request.POST:
            form = InvoiceForm(data=request.POST)
            if form.is_valid():
                form.save(commit=True)
                exito = "Pago ingresado exitosamente."

                pagos = Invoice.objects.all().order_by('date')
                return render(request,'caja/payments_all.html',{'exito':exito,'pagos':pagos})
            else:
                print("form invalido")
                print(form.errors)
                messages.add_message(request,
                                     messages.ERROR
                                     ,("ERROR: Por favor revise los campos Ingresados."))
                return render(request,'caja/new_payment.html',{'form':form})
        else:
            form = InvoiceForm()
            return render(request,'caja/new_payment.html',{'form':form})

@login_required
def payments_search(request):


    if not User.objects.filter(Q(pk=request.user.id),Q(groups__name='Doctor') | Q(groups__name='Cajero')).exists():
        print("No hay permisos!!")
        return render(request,'agenda/permisos.html',{})
    else:

        if request.POST:
            if request.POST['inicio']:

                inicio = request.POST['inicio']
            else:
                inicio = -1
            if request.POST['fin']:

                fin = request.POST['fin']
            else:
                fin = -1

            pagos = Invoice.objects.filter(date__range=(inicio,fin))
            suma =0
            for p in pagos:
                suma = suma + p.total
            return render(request,'caja/payments_all.html',{'pagos':pagos,'suma':suma})
        else:
            pagos = Invoice.objects.all().order_by('-date')[:50]
            return render(request,'caja/payments_all.html',{'pagos':pagos})