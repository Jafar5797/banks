from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('',views.index ,name='home'),
   path('logout/',LogoutView.as_view(),name='logout'),
   path('login/', LoginView.as_view(redirect_authenticated_user=True),name='login'),

   path('consultant-register/',views.consultant_register,name='consultant-register'),
   path('consultant-list/',views.list_of_consultants,name='clist'),
   path('users-list/',views.list_of_users,name='slist'),

   path('remove-as-spoc/',views.remove_as_spoc,name='remove_as_spoc'),
   path('make-as-spoc/',views.make_as_spoc,name='make_as_spoc'),
   path('user/<int:pk>/delete/', views.user_delete,name='user delete'),
   path('user/change-password/',views.change_password,name='change_password'),
   


   # path('myprofile/<str:username>/edit', views.user_update,name='update'),
   # path('myprofile-settings/',views.user_settings,name='mysettings'),


   # #path('checker-register/',views.checker_register ,name='cregister'),
   # path('login-success/',views.login_success,name='login-success'),
   
   
   
]
