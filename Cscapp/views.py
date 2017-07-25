from django.shortcuts import render
from Cscapp.models import Course
from Cscapp.models import Textbook
from Cscapp.models import Video

# Create your views here.

def course(request):
    course_list = Course.objects.all()[:10]
    context_dict = {'courses': course_list}
    template = 'Cscapp/course.html'
    return render(request, template, context_dict)

def show_course(request, course_code):
    context_dict = {}
    template = 'Cscapp/show_course.html'

    try:
        course = Course.objects.get(code=course_code)
        thetextbook = Textbook.objects.filter(course=course)
        thevideo = Video.objects.filter(course=course)
        context_dict['course'] = course
        context_dict['textbook'] = thetextbook
        context_dict['video'] = thevideo
    except Course.DoesNotExist:
        context_dict['course'] = None
        context_dict['textbook'] = None
        context_dict['video'] = None

    return render(request, template, context_dict)