from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HallsList, StaffsList, StudentsList, ComplaintsList, StudentsDetail, ComplaintsDetail, StaffsDetail, HallsDetail

urlpatterns = [
    path('halls/', HallsList.as_view()),
    path('staffs/', StaffsList.as_view()),
    path('students/', StudentsList.as_view()),
    path('complaints/', ComplaintsList.as_view()),
    path('halls/<int:pk>/', HallsDetail.as_view()),
    path('staffs/<int:pk>/', StaffsDetail.as_view()),
    path('students/<int:pk>/', StudentsDetail.as_view()),
    path('complaints/<int:pk>/', ComplaintsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)