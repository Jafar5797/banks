"""PROPERTYSALE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginPage, name="login"),
    path('logincheck/', views.loginCheck, name="logincheck"),
    path('newplot/', views.plotregistration, name="newplot"),
    path('newplotsave/', views.plotSave, name="newplotsave"),
    path('logout/', views.logouts, name="logout"),
    path('showplot/', views.detailplot, name="showplot"),
    path('viewdetails/', views.viewOneDetail, name="viewdetails"),
    path('editplot/', views.plotedit, name="editplot"),
    path('detailsedit/', views.editemployee, name="detailsedit"),
    path('saveeditplot/', views.saveEditPlot, name="saveeditplot"),
    path('newappartment/', views.bookappartment, name="newappartment"),
    path('appartmentreg/', views.regappartment, name="appartmentreg"),
    path('viewappartment/', views.apartmentview, name="viewappartment"),
    path('viewapp_details/', views.appdetailsshow, name="viewapp_details"),
    path('editappartment/', views.eeditapartment, name="editappartment"),
    path('editsavedetail/', views.editdetails, name="editsavedetail"),
    path('editingavailable/', views.editingdata, name="editingavailable"),
    path('detailabout/', views.aboutdetail, name="detailabout"),
    path('home/', views.homePage, name="home")
]
