from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'testprod/home.html', {'foo': 'bar',})
