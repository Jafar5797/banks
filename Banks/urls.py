from django.urls import include, path
from Banks import views

urlpatterns = [
    path('banks-list', views.Bankslist, name='banks-list'),
    path('bank/create/', views.create_bank , name='create'),
    path('bank/<int:id>/update/', views.bank_update,name='edit'),
    path('bank/<int:id>/', views.bank_detail,name='detail'),
    path('bank/<int:id>/delete/', views.bank_delete,name='delete'),
    path('make-inactive/',views.make_inactive,name='make_inactive'),
    path('make-active/',views.make_active,name='make_active'),
   
]