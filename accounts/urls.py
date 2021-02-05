from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from . import forms
app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(
        form_class=forms.LoginForm,
        template_name='accounts/login_form.html',
    ), name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),


    path('signup/', views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
