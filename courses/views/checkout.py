from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from courses.models import Course, Payment, UserCourse
from courses.templatetags.course_custom_tag import apply_discount
from django.contrib.auth.decorators import login_required
from time import time
from Project.settings import KEY_ID, KEY_SECRET
import razorpay





client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))




@login_required(login_url='login')
def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    


    
    action = request.GET.get('action')
    order = None
    error = None
    if action == 'create_order':
        try:
            UserCourse.objects.get(course=course, user=request.user)
            error = "You are alreay Enroll in this course!"
            
        except:
            pass
        if error is None:
            data = {
                'amount': apply_discount((course.price * 100), (course.discount)),
                'currency': 'INR',
                'receipt': f'{course.id}_{int(time())}',
                'notes': {
                    'name': request.user.first_name + ' ' + request.user.last_name,
                    'email': request.user.email,
                }
            }

            order = client.order.create(data=data)

            payment = Payment()
            payment.order_id = order.get('id')
            payment.user = request.user
            payment.course = course
            payment.save()


    context = {
        'course': course,
        'order': order,
        'KEY_ID': KEY_ID,
        'error': error,
    }
    return render(request, 'courses/checkout.html', context=context)







@csrf_exempt
def verify_payment(request):


    if request.method == 'GET':
        return HttpResponse('Sorry, Something went wrong!')


    data = request.POST

    try:
        params_dict = {
            'razorpay_order_id': data['razorpay_order_id'],
            'razorpay_payment_id': data['razorpay_payment_id'],
            'razorpay_signature': data['razorpay_signature']
        }
        client.utility.verify_payment_signature(params_dict)


        payment = Payment.objects.get(order_id=data.get('razorpay_order_id'))
        payment.payment_id = data.get('razorpay_payment_id')
        payment.status = True


        user_course = UserCourse()
        user_course.user = request.user
        user_course.course = payment.course
        user_course.save()


        

        payment.user_course = user_course
        payment.save()



    except:
        return HttpResponse('Payment Faild')



    return redirect('my_courses')