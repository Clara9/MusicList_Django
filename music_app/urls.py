from django.urls import path
from music_app import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about/',views.about,name="about"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('playlist/<int:id>',views.playlist,name="playlist"),
    path('edit/<int:id>',views.edit,name="edit"),
]