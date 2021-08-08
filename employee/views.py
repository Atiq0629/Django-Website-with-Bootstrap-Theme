from django.http.response import HttpResponse
from django.shortcuts import render

def profile(request):
    return render(request, 'employee/profile.html')
