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
def gate_and(request):
    return render(request,"gate_and.html")
def gate_or(request):
    return render(request,"gate_or.html")
def gate_xor(request):
    return render(request,"gate_xor.html")
def gate_xnor(request):
    return render(request,"gate_xnor.html")
def gate_nand(request):
    return render(request,"gate_nand.html")
def gate_nor(request):
    return render(request,"gate_nor.html")
def gate_not(request):
    return render(request,"gate_not.html")
