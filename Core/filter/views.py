from django.shortcuts import render
from home.serializers import StudentSerializer
from rest_framework.generics import ListAPIView 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter
from home.models import Student

class StudentApiView(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  filterset_fields = ['name', 'email']
  search_fields = ['name', '^address']
  ordering_fields = ['name','address']
  ordering  =['-address']
  
  
  def get_queryset(self):
    name = self.request.query_params.get('name')
    print(name)
    if name is not None:
      return self.queryset.filter(name__icontains = name)
    return self.queryset
  
  