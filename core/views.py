from django.shortcuts import render
from django.http import HttpResponse

from .models import Department

def index(request):
	department_list = Department.objects.all()
	context = {'department_list': department_list}

	return render(request, 'core/index.html', context)

def department(request, pk):
	return HttpResponse("Hello From Department")
