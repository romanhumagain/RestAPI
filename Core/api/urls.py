from django.urls import path, include
from home.views import index, person, PersonView, PersonViewSet
from App.views import (UserRegistrationAPIView, 
                       UserLoginAPIView)
from generic.views import (
  ListProductAPIView,
  CreateProductAPIView, 
  RetriveProduceAPIView,
  UpdateProductAPIView,
  DestroyProductAPIView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'persons', viewset=PersonViewSet, basename="persons")


urlpatterns = [
  path('index/', index, name="index"),
  path('person/', person, name="person"),
  path('person_view/',PersonView.as_view(), name="person_view" ),
  path('person_viewset/', include(router.urls), name="person_viewset"),
  
  path('list/', ListProductAPIView.as_view(), name="product-list"),
  path('create/', CreateProductAPIView.as_view(), name="product-create"),
  path('retrive/<slug:slug>', RetriveProduceAPIView.as_view(), name="product-retrive"),
  path('update/<slug:slug>', UpdateProductAPIView.as_view(), name="product-update"),
  path('delete/<slug:slug>', DestroyProductAPIView.as_view(), name="product-delete"),
  
  path('user/registration/', UserRegistrationAPIView.as_view(), name="user_registration"),
  path('user/login/', UserLoginAPIView.as_view(), name="user_login"),
  
  ]