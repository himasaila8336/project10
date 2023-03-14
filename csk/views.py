from django.shortcuts import render

# Create your views here.
def csk(request):
    d={'name':'dhoni'}
    return render(request,'csk.html',context=d)
