from django.shortcuts import render
from django.http import HttpResponse
from .models import Model1, Model2


def homme(request):
    return render(request, "index.html")



def faq(request):
    return render(request, "FAQ.html")


def actu(request):
    return render(request, "Actualite.html")


def show_prof(request):
    profs = Model1.objects.all()
    prof_list = []
    for prof in profs:
        prof_list.append({'prof': prof})
    context = {'prof_list': prof_list}
    return render(request, 'ProfPage.html', context)




def show_module(request):
    modules = Model2.objects.all()
    module_list = []
    for module in modules:
        module_list.append({'module': module})
    context2 = {'module_list': module_list}
    return render(request, 'ModulePage.html', context2)


def show_sqi(request):
    siq_mod = Model1.objects.filter(promo="SIQ")
    siq_mlist = []
    for siq in siq_mod:
        siq_mlist.append({'siq': siq})
    context3 = {'siq_mlist': siq_mlist}
    return render(request, 'L3SIQ.html', context3)


def show_isil(request):
    isil_mod = Model1.objects.filter(promo="ISIL")
    isil_mlist = []
    for isil in isil_mod:
        isil_mlist.append({'isil': isil})
    context4 = {'isil_mlist': isil_mlist}
    return render(request, 'L3Isil.html', context4)

