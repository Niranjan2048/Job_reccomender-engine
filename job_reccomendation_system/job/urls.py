from django.urls import path
from job import views

urlpatterns = [
    #path("", views.home, name="home"),
    path('', views.signIn),
    path('signIn/', views.signIn),
    path('login/',views.signIn),
    path('postsignIn/', views.postsignIn),
    path('logout/', views.logout, name="log"),
    path('postsignUp/', views.postsignUp),
    path('reset/', views.reset),
    path('postReset/', views.postReset),
    path('opentabs/',views.opentabs, name="opentabs"),
]