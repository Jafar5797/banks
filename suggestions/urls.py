from django.urls import path
from . import views


urlpatterns = [

   path('submit-suggestion/',views.create_suggestion),
   path('suggestions-list/',views.suggestionslist),

]

