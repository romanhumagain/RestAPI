from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Persons
from .serializers import PersonSerializer
from rest_framework.views import APIView
from rest_framework import viewsets

@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def index(request):
  courses = {
    "course_name":"Python", 
    "Learning": ['AI',"Machine Learning", "Django", "Flast"], 
    "provider":"PCPS College"
  }
  
  if request.method == 'GET':
    searched_data = request.GET.get("search")
    print()
    print(f"You searched for {searched_data}")
    print()
    courses["searched_for"]= searched_data
    
    return Response(courses[searched_data])
 
  if request.method == 'POST':
    # to get the data from the front-end
    data = request.data
    print("****")
    print(data)
    print(data['name'])
    print("****")
    
    context = {"message":"You hit POST method. We are not working with POST method now !",
               "data":data, 
               'status':status.HTTP_201_CREATED}
    
    return Response(context)

  if request.method == 'PUT':
    return Response("You hit PUT method. We are not working with PUT method now !")
  
  if request.method == 'PATCH':
    return Response("You hit PATCH method. We are not working with PATCH method now !")
  
 
# Performing the CRUD operations
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
  if request.method == 'GET':
    person_obj = Persons.objects.all()
    
    serializer = PersonSerializer(person_obj, many = True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    data = request.data
    serializer = PersonSerializer(data=data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors)
  
  '''
  ========== DIFFERENCE BETWEEN PUT AND PATCH ===========
  -> PUT doesn't support partial update but PATCH support partial update
  '''
  
  if request.method == 'PUT':
    data = request.data
    person_obj = Persons.objects.get(id = data['id'])
    
    serializer = PersonSerializer(person_obj,data=data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.errors)
  
  if request.method == 'PATCH':
    data = request.data
    
    person_obj = Persons.objects.get(id = data['id'])
    
    serializer = PersonSerializer(person_obj, data=data, partial = True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.errors)
  
  if request.method == 'DELETE':
    data = request.data
    person_obj = Persons.objects.get(id = data['id'])
    person_obj.delete()
    
    return Response({'message':'Successfully Deleted Person !'})

  
  
# Using the APIView Class to perform CURD operations
class PersonView(APIView):
  def get(self, request):
    person_obj = Persons.objects.all()
    serializer = PersonSerializer(person_obj, many = True)
    
    return Response({'message':"You Hit GET Method !", 'data': serializer.data})

  def post(self, request):
    data = request.data
    serializer = PersonSerializer(data = data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
          
    return Response(serializer.errors)
  
  def put(self, request):
    data = request.data
    person_obj = Persons.objects.get(id = data["id"])
    
    serializer = PersonSerializer(person_obj, data = data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.errors)
  
  def patch(self, request):
    data = request.data
    person_obj = Persons.objects.get(id = data["id"])
    
    serializer = PersonSerializer(person_obj, data= data, partial = True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.errors)
  
  def delete(self, request):
    data = request.data
    person_obj = Persons.objects.get(id = data['id'])
    person_obj.delete()
    
    return Response({'message':'Successfully Deleted Person !'})
  
  
