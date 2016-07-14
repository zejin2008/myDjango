from django.shortcuts import render
from django.http.response import HttpResponse

from models import *
from django.template.context_processors import request
# Create your views here.
def index(request):
    return HttpResponse('Index')


def login(request,name,id):
    return HttpResponse('login: '+str(name)+' '+str(id))


def add(request,name):
    users.objects.create(name=name)
    return HttpResponse('add ok:'+str(name))


def delete(request,id):
    users.objects.get(id=id).delete()
    return HttpResponse('delete ok:'+str(id))


def update(request,id,name):
    
#     method 1    
    obj = users.objects.get(id=id)
    obj.name = name
    obj.save()
    
#    method 2 
#    users.objects.filter(id__gt=id).update(name=name)
    
    return HttpResponse('update ok:'+str(id))


def get(request,id):

#  method 1    
#    userlist = users.objects.filter(id__gt=id)

#  method 2    
    userlist = users.objects.all().order_by('-id')[0:id]
    
    output=[]
    for item in userlist:
        print output.append(item.name)
    
    return HttpResponse('get ok:'+str(output))
    














