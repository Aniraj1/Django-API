from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse



#  Get API
def student_api(request):
  if request.method == 'GET':
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythonData = JSONParser().parse(stream)
    id = pythonData.get('id', None)
    
    if id is not None:
      #Creating a object
      stu = Student.objects.get(id=id)
      serializer = StudentSerializer(stu)
      # json_data = JSONRenderer().render(serializer.data)
      
      # return HttpResponse(json_data, content_type = 'application/json')
      return JsonResponse(serializer.data, status=200)
      
  # for getting all data
  stu = Student.objects.all()
  serializer = StudentSerializer(stu, many = True)
  # return JsonResponse(serializer.data, status=200)

  json_data = JSONRenderer().render(serializer.data)
  return HttpResponse(json_data, content_type = 'application/json')
