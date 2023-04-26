from contextlib import nullcontext
from os import error
from django.contrib.admin.utils import lookup_field
from django.db.utils import pkgutil
from rest_framework.response import Response
from rest_framework import generics, status
from django.http import Http404
from rest_framework.utils import serializer_helpers
from rest_framework.utils.representation import serializer_repr

import jwt
import datetime
from .decorators import check_authentication
from django.utils.decorators import method_decorator


from  .serializers import HallSerializer, StaffSerializer, StudentSerializer, ComplaintSerializer
from .models import Hall, Staff, Student, Complaint
# Create your views here.


# @method_decorator(check_authentication(), name='get')
class HallsList(generics.views.APIView):
    @method_decorator(check_authentication())
    def get(self, request, **kwargs):
        try:
            queryset = Hall.objects.all()
            serializer = HallSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as err:
            return Response({'message': f"{err}"}, status=status.HTTP_400_BAD_REQUEST)  
        
    @method_decorator(check_authentication())
    def post(self, request,**kwargs ):
        serializer = HallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HallsDetail(generics.RetrieveAPIView):
    serializer_class = HallSerializer
    def get_object(self, pk):
        try:
            return Hall.objects.get(_id=pk)
        except Hall.DoesNotExist:
            raise Http404

    @method_decorator(check_authentication())
    def get(self, request, pk, **kwargs):
        hall = self.get_object(pk)
        serializer = HallSerializer(hall)
        return Response(serializer.data)
    
    @method_decorator(check_authentication())
    def put(self, request, pk, **kwargs):
        hall = self.get_object(pk)
        serializer = HallSerializer(hall, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @method_decorator(check_authentication())
    def delete(self, request, pk, **kwargs):
        hall = self.get_object(pk)
        hall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StaffsList(generics.views.APIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    @method_decorator(check_authentication())
    def get(self, request, **kwargs):
        hall = Hall.objects.get(_id=kwargs['hallId'])
        staff = hall.staff_set.all()
        staffSerializer = StaffSerializer(staff , many=True)
        return Response(staffSerializer.data)

    @method_decorator(check_authentication())
    def post(self, request, **kwargs):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffsDetail(generics.RetrieveAPIView):
    serializer_class = StaffSerializer
    def get_object(self, pk):
        try:
            return Staff.objects.get(_id=pk)
        except Staff.DoesNotExist:
            raise Http404

    @method_decorator(check_authentication())
    def get(self, request, pk, **kwargs):
        staff = self.get_object(pk)
        serializer = StaffSerializer(staff)
        return Response(serializer.data)
    
    @method_decorator(check_authentication())
    def put(self, request, pk,**kwargs):
        staff = self.get_object(pk)
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(check_authentication())
    def delete(self, request, pk, **kwargs):
        staff = self.get_object(pk)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StudentsList(generics.views.APIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    @method_decorator(check_authentication())
    def get(self, request, **kwargs):
        hall = Hall.objects.get(_id=kwargs['hallId'])
        students = hall.student_set.all()
        studentSerializer = StudentSerializer(students, many=True)
        return Response(studentSerializer.data)
        

    @method_decorator(check_authentication())
    def post(self, request, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentsDetail(generics.RetrieveAPIView):
    serializer_class = StudentSerializer

    def get_object(self, pk):
        try:
            return Student.objects.get(_id=pk)
        except Student.DoesNotExist:
            raise Http404

    @method_decorator(check_authentication())
    def get(self, request, pk, **kwargs):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    @method_decorator(check_authentication())
    def put(self, request, pk, **kwargs):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @method_decorator(check_authentication())
    def delete(self, request, pk, **kwargs):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#################### complaint list

class ComplaintsList(generics.views.APIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    @method_decorator(check_authentication())
    def get(self, request, **kwargs):
        hall = Hall.objects.get(_id=kwargs['hallId'])
        complaints = hall.complaint_set.all()
        complaintSerializer = ComplaintSerializer(complaints, many=True)
        return Response(complaintSerializer.data)

    @method_decorator(check_authentication())
    def post(self, request, **kwargs):
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComplaintsDetail(generics.RetrieveAPIView):
    serializer_class = ComplaintSerializer
    def get_object(self, pk ):
        try:
            return Complaint.objects.get(_id=pk)
        except Complaint.DoesNotExist:
            raise Http404

    @method_decorator(check_authentication())
    def get(self, request, pk, **kwargs):
        complaint = self.get_object(pk)
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)

    @method_decorator(check_authentication())
    def put(self, request, pk, **kwargs):
        complaint = self.get_object(pk)
        serializer = ComplaintSerializer(complaint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(check_authentication())
    def delete(self, request, pk, **kwargs):
        complaint = self.get_object(pk)
        complaint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#  login 

class ProfileLogin(generics.CreateAPIView):
    queryset = [ Hall.objects.all(), Staff.objects.all() ]
    serializer_class = [ Staff.objects.all(), Staff.objects.all() ]

    def post(self, request):
        username = request.data.get('username')
        hallId = request.data.get('hallId')
        password = request.data.get('password')
        #  check role also because only mess incharge can login
        # username can be like messincharge<hall no.>

        try:
            staff = Staff.objects.get(name = username)
            hall = Hall.objects.get(_id = hallId)
            getStaff_hall = hall.staff_set.get(name = username)
            if not staff and staff.password !=password :
                raise Exception("Invlaid Details")
            if not hall:
                raise Exception("Invlaid Hall ID")
            if getStaff_hall != staff:
                raise Exception("Please provide valid details")
            payload = {
                'hallId':hallId,
                'username':username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
                'iat': datetime.datetime.utcnow()
            }

            key = "hallmanagementSystemProject"
            token = jwt.encode(payload, key, algorithm="HS256")
            return Response({'message': "logged in successfully", "token": token}, status=status.HTTP_200_OK)
            
        except Exception as err:
            return Response({"message": f"{err}"}, status=status.HTTP_400_BAD_REQUEST)
        

class ProfileRegister(generics.CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    def post(self, request):
        username = request.data.get('username')
        hallId = request.data.get('hallId')
        position = request.data.get('role')
        password = request.data.get('password')

        salary = 10000  #added as it is manadatory in models

        staff = {
            "name":username,
            "hall_no":hallId,
            "position": position,
            "salary":salary,
            "user_password":password
        }
        try:
            serializer = StaffSerializer(data=staff)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "successfully registerd"},status=status.HTTP_200_OK)
        except Exception as err:
            return Response({"message":f"{err}"}, status=status.HTTP_400_BAD_REQUEST)
