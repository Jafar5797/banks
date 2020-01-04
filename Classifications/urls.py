from django.urls import include, path
from Classifications import views

urlpatterns = [
    path('td-list/', views.Tlist, name='tlist'),
    path('dt-list/', views.Dlist, name='dlist'),

    path('td/create/', views.create_technology_domain , name='tcreate'),
    # path('td/<int:id>/', views.technology_domain_detail,name='tdetail'),
    path('td/<int:id>/delete/', views.technology_delete,name='tdelete'),

    path('dt/create/', views.create_document_type , name='dcreate'),
    # path('dt/<int:id>/', views.document_type_detail,name='ddetail'),
    path('dt/<int:id>/delete/', views.document_delete,name='ddelete'),
    path('testing/', views.test),
   
]