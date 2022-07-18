from django.shortcuts import render, HttpResponse, redirect
from courses.models import course, UserCourse, Course, user_course
from courses.models.video import Video
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView


def coursePage(request, slug):
    single_course = course.get_course_by_slug(slug)
    serial_number = request.GET.get('lecture')

    if serial_number is None:
        serial_number = 1

    video = Video.objects.get(serial_number=serial_number, course=single_course)

    videos = single_course.video_set.all().order_by('serial_number')


    if video.is_preview == False:
        if request.user.is_authenticated is False:
            return redirect('login')
        else:
            try:
                user = request.user
                UserCourse.objects.get(user=user, course=single_course)
            except:
                return redirect('checkout', slug=slug)
        


    context = {}
    context['course'] = single_course
    context['video'] = video
    context['videos'] = videos

    return render(request=request, template_name='courses/course-page.html', context=context)




@method_decorator(login_required(login_url='login'), name='dispatch')
class MyCoursesList(ListView):
    template_name = 'courses/my-courses.html'
    context_object_name = 'user_courses'

    def get_queryset(self):
        return UserCourse.objects.filter(user=self.request.user)
    





'''
@login_required(login_url='login')
def my_courses(request):
    user = request.user
    user_courses = UserCourse.objects.filter(user=user)



    
    context = {
        'user_courses': user_courses,
    }
    return render(request, 'courses/my-courses.html', context=context)
'''