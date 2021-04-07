from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample1(request):
    return render(request,'sample1.html')