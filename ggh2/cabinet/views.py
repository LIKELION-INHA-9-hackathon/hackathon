from django.shortcuts import render,redirect,get_object_or_404
from user.models import *
from cabinet.models import *
from goods.models import *
from pay.models import *
from wish.models import *

def cabinet_read_all(req):
    cabinet = Cabinet_manage.objects.all()
    context={
        'data' : cabinet
    }
    return render(req,'location.html',context)

def cabinet_read_one(req,id):
    if id == 1:
        cabinet = Cabinet_1.objects.all()
    elif id == 2:
        cabinet = Cabinet_2.objects.all()
    elif id == 3:
        cabinet = Cabinet_3.objects.all()
    context = {
        'data' : cabinet
    }
    return render(req,'cabinet_read_one.html',context)

def cabinet_update(req,id):
    if id == 1:
        cabinet = get_object_or_404(Cabinet_1,pk=id)
    elif id == 2:
        cabinet = get_object_or_404(Cabinet_2,pk=id)
    elif id == 3:
        cabinet = get_object_or_404(Cabinet_3,pk=id)
    if req.method == 'POST':
        cabinet.can_id = req.POST['can_id']
        cabinet.in_use = req.POST['in_use']
        cabinet.weight = req.POST['weight']
        cabinet.save()
        return redirect('/cabinet/'+str(cabinet.id))
    return render(req,'cabinet_update.html',{'data':cabinet})

def cabinet_delete(req,id):
    if id == 1:
        cabinet = get_object_or_404(Cabinet_1,pk=id)
    elif id == 2:
        cabinet = get_object_or_404(Cabinet_2,pk=id)
    elif id == 3:
        cabinet = get_object_or_404(Cabinet_3,pk=id)
    cabinet.delete()
    return redirect('/cabinet/')
