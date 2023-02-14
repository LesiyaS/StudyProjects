from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    objects=Team.objects.all()
    return render(request,"index.html",{'result':obj,'results':objects})



# def result(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     Add=x+y
#     Sub = x - y
#     Mul = x * y
#     Div = x / y
#     return render(request,"about.html",{'Add':Add,'Sub':Sub,'Mul':Mul,'Div':Div})


