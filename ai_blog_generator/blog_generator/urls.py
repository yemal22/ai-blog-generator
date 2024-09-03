from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_user, name='signup-user'),
    path('login/', views.login_user, name='login-user'),
    path('logout/', views.logout_user, name='logout-user'),

    path('', views.index, name='index'),
    path('generate-blog/', views.generate_blog, name='generate-blog')
]