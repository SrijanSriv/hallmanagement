from contextlib import nullcontext
from os import error
from django.contrib.admin.utils import lookup_field
from django.db.utils import pkgutil
from rest_framework.response import Response
from rest_framework import generics, status
from django.http import Http404
from rest_framework.utils import serializer_helpers
from rest_framework.utils.representation import serializer_repr


from  .serializers import HallSerializer, StaffSerializer, StudentSerializer, ComplaintSerializer
from .models import Hall, Staff, Student, Complaint
# Create your views here.

class HallsList(generics.views.APIView):
    
    def get(self, request, format=None):
        queryset = Hall.objects.all()
        serializer = HallSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HallsDetail(generics.RetrieveAPIView):

    def get_object(self, pk):
        try:
            return Hall.objects.get(_id=pk)
        except Hall.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        hall = self.get_object(pk)
        serializer = HallSerializer(hall)
        return Response(serializer.data)
    
    def put(self, request, pk):
        hall = self.get_object(pk)
        serializer = HallSerializer(hall, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hall = self.get_object(pk)
        hall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StaffsList(generics.views.APIView):
    
    def get(self, request, format=None):
        queryset = Staff.objects.all()
        serializer = StaffSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffsDetail(generics.RetrieveAPIView):

    def get_object(self, pk):
        try:
            return Staff.objects.get(_id=pk)
        except Staff.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        staff = self.get_object(pk)
        serializer = StaffSerializer(staff)
        return Response(serializer.data)
    
    def put(self, request, pk):
        staff = self.get_object(pk)
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        staff = self.get_object(pk)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentsList(generics.views.APIView):

    def get(self, request, format=None):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentsDetail(generics.RetrieveAPIView):

    def get_object(self, pk):
        try:
            return Student.objects.get(_id=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ComplaintsList(generics.views.APIView):

    def get(self, request, format=None):
        queryset = Complaint.objects.all()
        serializer = ComplaintSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComplaintsDetail(generics.RetrieveAPIView):

    def get_object(self, pk):
        try:
            return Complaint.objects.get(_id=pk)
        except Complaint.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        complaint = self.get_object(pk)
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)
    
    def put(self, request, pk):
        complaint = self.get_object(pk)
        serializer = ComplaintSerializer(complaint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        complaint = self.get_object(pk)
        complaint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)