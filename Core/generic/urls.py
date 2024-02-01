from django.urls import path
from .views import (
  ListProductAPIView,
  CreateProductAPIView, 
  RetriveProduceAPIView,
  UpdateProductAPIView,
  DestroyProductAPIView
)

urlpatterns = [
  path('list/', ListProductAPIView.as_view(), name="product-list"),
  path('create/', CreateProductAPIView.as_view(), name="product-create"),
  path('retrive/<slug:slug>', RetriveProduceAPIView.as_view(), name="product-retrive"),
  path('update/<slug:slug>', UpdateProductAPIView.as_view(), name="product-update"),
  path('delete/<slug:slug>', DestroyProductAPIView.as_view(), name="product-delete")
  
]