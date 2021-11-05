
from django.urls import path
from login_page import views
 
urlpatterns = [
    
    # Here we are assigning the path of our url
    path('', views.signIn),
    path('postsignIn/', views.postsignIn),
    path('logout/', views.logout, name="log"),
    path('postsignUp/', views.postsignUp),
    path('reset/', views.reset),
    path('postReset/', views.postReset)
]