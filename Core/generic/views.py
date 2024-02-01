from rest_framework.generics import (
  ListAPIView, 
  RetrieveAPIView,
  CreateAPIView, 
  UpdateAPIView, 
  DestroyAPIView
)
from .models import Products
from .serializers import ProductSerializer


class ListProductAPIView(ListAPIView):
  queryset = Products.objects.all()
  serializer_class = ProductSerializer
  
class CreateProductAPIView(CreateAPIView):
  queryset = Products.objects.all()
  serializer_class = ProductSerializer
  
  
class RetriveProduceAPIView(RetrieveAPIView):
  queryset = Products.objects.all()
  serializer_class = ProductSerializer
  
  lookup_field = "slug"
  
class UpdateProductAPIView(UpdateAPIView):
  queryset = Products.objects.all()
  serializer_class = ProductSerializer
  
  lookup_field = "slug"
  
class DestroyProductAPIView(DestroyAPIView):
  queryset = Products.objects.all()
  serializer_class = ProductSerializer
  
  lookup_field = "slug"
  
  
  

