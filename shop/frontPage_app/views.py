from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def frontPageView(request):
    return render(request, 'index.html', {})
