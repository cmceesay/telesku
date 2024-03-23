from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
'''
def home(request):
    if request.method == "POST":
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        return redirect('add', num1=num1, num2=num2)
    name = 'Siri H.'
    return render(request, "home.html", {'username':name})

def add(request, num1=None, num2=None):
    result = num1 + num2
    return render(request,'result.html', {'num1' : num1, 'num2' : num2, 'result':result})
'''

# Create your views here.
def home(request):
    name = 'Siri H.'
    return render(request, "home.html", {'username':name})

def add(request):
    print(request.method)
    if request.method == "POST":
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        result = num1 + num2
    else:
        num1 = None
        num2 = None
        result = None
    return render(request,'result.html', {'num1' : num1, 'num2' : num2, 'result':result})