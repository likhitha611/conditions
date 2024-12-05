from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':10,'name':'likhitha'}
    return render(request,'conditions.html',context=d)
