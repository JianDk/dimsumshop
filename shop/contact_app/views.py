from django.shortcuts import render
from django.shortcuts import HttpResponse   

# Create your views here.
def contactView(request):
    return HttpResponse("<p1>This is the contact site. Needs to use page rendering still</p>")