from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Department, Post

def index(request):
	department_list = Department.objects.all()
	context = {'department_list': department_list}

	return render(request, 'core/index.html', context)

def department(request, name):
	dept = Department.objects.get(name=name).post_set.all()
	context = { 'posts': dept }

	return render(request, 'core/department.html', context)
