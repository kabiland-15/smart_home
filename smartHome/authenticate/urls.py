from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='index'),
    path('signup/', views.signup, name='signup'),
    path("<str:room_name>/<str:username>", views.room, name="room"),
]
