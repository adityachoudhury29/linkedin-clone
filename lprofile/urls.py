from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profilefunc/<str:uname>", views.profilefunc, name="profile1"),
    path("create", views.create, name="create"),
    path("like/<int:pk>", views.like, name="like"),
    path("dislike/<int:pk>", views.dislike, name="dislike"),
    path("followings/<str:uname>", views.foll, name="followings"),
    path("delete/<int:id>",views.deletepost, name="delete"),
    path("addconnection",views.addc, name="addc"),
    path("follow/<str:uname>",views.add, name="follow"),
    path("unfollow/<str:uname>",views.remove, name="unfollow"),
    path("edit",views.editprof, name="edit"),
    path("connect/<str:uname>",views.connect, name="connect"),
    path("disconnect/<str:uname>",views.disconnect, name="disconnect"),
    path("accept/<str:uname>",views.accept, name="accept"),
    path("decline/<str:uname>",views.decline, name="decline"),
    path("comments/<int:id>",views.gotocomments,name="comments"),
    path("job",views.job,name="job"),
    path("jobpost",views.jobpost,name="jobpost"),
    path("apply/<int:id>",views.apply,name="apply"),
    path("applicants/<int:id>",views.applicants,name="applicants"),
    path("chat",views.chatapp,name="chat"),
]