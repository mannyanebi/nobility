from django.conf.urls import url
from django.urls import path, include
from .views import IndexView, StudentProfileView, DashboardView, RegisterUserView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]