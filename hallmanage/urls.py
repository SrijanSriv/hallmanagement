from django.urls import path
from .views import GetHallsDetail

urlpatterns = [
    path('', GetHallsDetail.as_view()),
]
