from django.shortcuts import render

# Create your views here.
def print(request):
    d={'name':'malini','age':21,'favactor':'vijay'}
    return render(request,'print.html',context=d)
