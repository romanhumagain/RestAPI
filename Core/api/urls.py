from django.urls import path, include
from home.views import index, person, PersonView, PersonViewSet, StudentViewSet
from App.views import (UserRegistrationAPIView, 
                       UserLoginAPIView)
from generic.views import (
  ListProductAPIView,
  CreateProductAPIView, 
  RetriveProduceAPIView,
  UpdateProductAPIView,
  DestroyProductAPIView
)

from jwt_auth.views import RegisterAPIView, LoginAPIView, UserAPIView, LogoutUserAPI

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'persons', viewset=PersonViewSet, basename="persons")

router.register(r'students', viewset = StudentViewSet, basename="persons")


urlpatterns = [
  path('index/', index, name="index"),
  path('person/', person, name="person"),
  path('person_view/',PersonView.as_view(), name="person_view" ),
  path('person_viewset/', include(router.urls), name="person_viewset"),
  
  path('student_viewset/', include(router.urls), name="student_viewset"),
  
  path('list/', ListProductAPIView.as_view(), name="product-list"),
  path('create/', CreateProductAPIView.as_view(), name="product-create"),
  path('retrive/<slug:slug>', RetriveProduceAPIView.as_view(), name="product-retrive"),
  path('update/<slug:slug>', UpdateProductAPIView.as_view(), name="product-update"),
  path('delete/<slug:slug>', DestroyProductAPIView.as_view(), name="product-delete"),
  
  path('user/registration/', UserRegistrationAPIView.as_view(), name="user_registration"),
  path('user/login/', UserLoginAPIView.as_view(), name="user_login"),
  
  path('register/', RegisterAPIView.as_view(), name="register"),
  path('login/', LoginAPIView.as_view(), name="login"),
  path('get/user/', UserAPIView.as_view(), name="get_user"),
  path('logout/user/', LogoutUserAPI.as_view(), name="logout_user")

  ]