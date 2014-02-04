#FILE: roster/views.py
from django.shortcuts import render

# Create your views here.

def home(request):
	context = {'message': 'This is a dynamic message variable!'}
	return render(request, "base.html", context)
