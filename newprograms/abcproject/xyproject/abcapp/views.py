from django.http import HttpResponse
from django.shortcuts import render
from .models import Table
from .models import Place
# Create your views here.
def index(request):
    obj=Place.objects.all()
    xyz=Table.objects.all()
    return  render(request,"index.html",{'result':obj,'output':xyz})
# def addition(request):
#     x=int(request.GET['value1'])
#     y=int(request.GET['value2'])
#     a=x*y
#     b=x+y
#     c=x-y
#     d=x/y
#     return render(request,"result.html",{'multiplication':a,'addition':b,'subtration':c,'division':d})