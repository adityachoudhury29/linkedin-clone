from django.urls import path
from chat import views

urlpatterns=[
    path("<str:room_name>/", views.roomin, name="room"),
]