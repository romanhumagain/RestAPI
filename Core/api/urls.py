from django.urls import path
from home.views import index, person, PersonView


urlpatterns = [
  path('index/', index, name="index"),
  path('person/', person, name="person"),
  path('person_view/',PersonView.as_view(), name="person_view" )
  ]