from App import views
from django.urls import path
#写上app_name
app_name = 'App01'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('mark/',views.reply,name='mark'),
    path('home/',views.index,name='home'),
    path('logout/',views.logout,name='logout'),
]