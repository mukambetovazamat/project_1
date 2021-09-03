from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', locals())


def generic(request):
    return render(request, 'generic.html', locals())


def elements(request):
    return render(request, 'element.html', locals())


