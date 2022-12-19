from django.shortcuts import redirect, render
from .models import Albert,Nikola,Raman
# Create your views here.

def albert(request):
    sci = Albert.objects.all();
    context={
        'sci': sci
    }
    if request.method == "POST":
        details = request.POST.get('albertdetails','')
        name=request.POST.get('name','')
        scientist = Albert(id='1',name=name, details = details)
        scientist.save()
    return render(request, 'albert.html',context)

def nikola(request):
    sci = Nikola.objects.all();
    context={
        'sci': sci
    }
    if request.method == "POST":
        details = request.POST.get('nikoladetails','')
        name=request.POST.get('name','')
        scientist = Nikola(id='1',name=name, details = details)
        scientist.save()
    return render(request, 'nikola.html',context)

def raman(request):
    sci = Raman.objects.all();
    context={
        'sci': sci
    }
    if request.method == "POST":
        details = request.POST.get('ramandetails','')
        name=request.POST.get('name','')
        scientist = Raman(id='1',name=name, details = details)
        scientist.save()
    return render(request, 'cvraman.html',context)

def finish(request):
    return render(request,'finish.html')