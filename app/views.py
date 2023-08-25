from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insert_Topic(request):
    tn=input('Enter topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
def display_topic(request):
    QSTO=Topic.objects.all()
    d={ 'QSTO': QSTO }
    return render(request,'display_topic.html',d)

def insert_Webpage(request):
    tn=input('Enter topic_name : ')
    TO=Topic.objects.get(topic_name=tn)[0]
    TO.save()
    n=input('Enter Name : ')
    u=input('Enter url : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
def display_Webpage(request):
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_Webpage.html',d)
def insert_AccessRecord(request):
    tn=input('Enter topic_name : ')
    TO=Topic.objects.get(topic_name=tn)[0]
    TO.save()
    n=input('Enter Name : ')
    u=input('Enter url : ')
    WO=Webpage.objects.get(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d=input('Enter Date : ')
    a=input('Enter author : ')
    e=input('Enter Email : ')
    Ao=AccessRecord.objects.get_or_create(name=WO,Date=d,author=a,Email=e)[0]
    Ao.save()
def display_Access(request):
    QSAO=AccessRecord.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_Access.html',d)




