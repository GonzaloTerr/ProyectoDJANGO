from django.shortcuts import render
from .models import Course
# Create your views here.
def course_list(request):
    all_course=Course.objects.all()
    context={
        "course":all_course
    }
    return render(request,"courses/course_list.html",context)
    
def course_detail(request, id):
    course=Course.objects.get(pk=id)
    context={
        "course":course
    }
    return render(request,"courses/course_detail.html",context)