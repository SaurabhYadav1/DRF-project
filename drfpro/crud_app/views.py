from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
@api_view(http_method_names=['GET','POST'])
def add_api(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

    if request.method == "GET":
        students = Student.objects.all()
        serializer= StudentSerializer(students,many=True)
        return Response (data=serializer.data,status=status.HTTP_200_OK)


@api_view(http_method_names=['GET','PUT','PATCH','DELETE'])
def add_detial_api(request,pk=None):
  student = get_object_or_404(Student,pk=pk)
  if request.method == "GET":
      serializer=StudentSerializer(student)
      return Response(data=serializer.data,status=status.HTTP_200_OK)

  if request.method == "DELETE":
       student.delete()
       return Response ( data=None,status=status.HTTP_204_NO_CONTENT)

  if request.method == "PUT":
          serializer = StudentSerializer(data=request.data, instance=student)
          if serializer.is_valid():
              serializer.save()
              return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
          return Response(data=serializer.errors, status=status.HTTP_204_NO_CONTENT)

  if request.method == "PATCH":
          serializer = StudentSerializer(data=request.data, instance=student, partial=True)
          if serializer.is_valid():
              serializer.save()
              return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
          return Response(data=serializer.errors, status=status.HTTP_204_NO_CONTENT)

