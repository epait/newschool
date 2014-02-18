#FILE: roster/views.py
from django.shortcuts import render
from roster.models import Course, Student

# Create your views here.

def home(request):
	context = {
		'student_count': Student.objects.count(),
		'course_count': Course.objects.count(),
	}
	return render(request, "roster/home.html", context)

def course(request):
	course = Course.objects.order_by('?')[0]
	return render(request, "roster/course.html", {'course': course})

def student(request):
	student = Student.objects.order_by('?')[0]
	return render(request, "roster/student.html", {'student': student})
