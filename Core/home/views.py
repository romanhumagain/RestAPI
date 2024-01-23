from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def index(request):
  courses = {
    "course_name":"Python", 
    "Learning": ['AI',"Machine Learning", "Django", "Flast"], 
    "provider":"PCPS College"
  }
  if request.method == 'GET':
    return Response(courses)
    
  if request.method == 'POST':
    return Response("You hit POST method. We are not working with POST method now !")

  if request.method == 'PUT':
    return Response("You hit PUT method. We are not working with PUT method now !")
  
  if request.method == 'PATCH':
    return Response("You hit PATCH method. We are not working with PATCH method now !")
  
  
  