from django.shortcuts import render
from django.http import HttpResponse

from .models import Department
# Create your views here.
def index(request):
	department_list = Department.objects.all()
	output = ', '.join([dept.name for dept in department_list])
	return HttpResponse(output)
