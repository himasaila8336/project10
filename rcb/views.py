from django.shortcuts import render

# Create your views here.
def rcb(request):
    d={'name':'virat'}
    return render(request,'rcb.html',context=d)
