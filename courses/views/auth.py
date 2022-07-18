from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from courses.forms import RegistrationForm as UserCreationForm
from courses.forms import LoginForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.views.generic.edit import FormView






class SignupView(FormView):
    template_name = 'courses/signup.html'
    form_class = UserCreationForm
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



'''
class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'courses/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            if (user is not None):
                return redirect('login')
        return render(request, 'courses/signup.html', {'form': form})
'''




class LoginView(FormView):
    template_name = 'courses/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.cleaned_data)
        next_page = self.request.GET.get('next')
        if next_page is not None:
            return redirect(next_page)
        return super().form_valid(form)

'''
class LoginView(View):
    next_url = None
    def get(self, request):
        LoginView.next_url = request.GET.get('next')

        if (request.user.is_authenticated):
            return redirect('homepage')

        form = LoginForm()
        return render(request, 'courses/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, request.POST)
        if (form.is_valid()):

            if (request.user.is_authenticated):

                if LoginView.next_url:
                    return HttpResponseRedirect(LoginView.next_url)

                return redirect('homepage')

        return render(request, 'courses/login.html', {'form': form})
'''

def logout_view(request):
    logout(request)
    return redirect('homepage')
