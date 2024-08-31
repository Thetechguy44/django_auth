from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.signin, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.signout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
]