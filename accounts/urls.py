from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signupUser, name='signup'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]