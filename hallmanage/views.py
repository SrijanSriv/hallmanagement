from rest_framework.response import Response
from rest_framework import generics

from  .serializers import HallSerializer 
from .models import Hall
# Create your views here.

class GetHallsDetail(generics.ListAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    