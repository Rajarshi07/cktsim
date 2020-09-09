from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')
def allckts(request):
    return render(request, 'allckts.html')
def hadd(request):
    return render(request,'hadd.html')
def fadd(request):
    return render(request,'fadd.html')
def hsub(request):
    return render(request,'hsub.html')
def fsub(request):
    return render(request,"fsub.html")