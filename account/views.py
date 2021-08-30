from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import StudentProfile
from .forms import StudentProfileForm, UserRegistrationForm
# Create your views here.


class IndexView(TemplateView):
    template_name = 'account/index.html'

class DashboardView(TemplateView):
    template_name = 'account/dashboard.html'

class RegisterUserView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('dashboard')
    template_name = 'account/register.html'

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        First, set passwords first
        """
        self.object = form.save()
        self.object.set_password(self.object.password)
        messages.success(self.request, 'Registration Successful')
        return super().form_valid(form)

class StudentProfileView(CreateView):
    model = StudentProfile
    form_class = StudentProfileForm
    template_name = 'account/update-profile.html'