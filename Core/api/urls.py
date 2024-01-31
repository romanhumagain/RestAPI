from django.urls import path, include
from home.views import index, person, PersonView, PersonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'persons', viewset=PersonViewSet, basename="persons")


urlpatterns = [
  path('index/', index, name="index"),
  path('person/', person, name="person"),
  path('person_view/',PersonView.as_view(), name="person_view" ),
  path('person_viewset/', include(router.urls), name="person_viewset")]