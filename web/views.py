from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Index')


def login(request,name,id):
    return HttpResponse('login: '+str(name)+' '+str(id))



