from django.contrib import admin

# Register your models here.

from .models import Staff, Hall, HMCChairman, Room, Student, Complaint

admin.site.register(Staff)
admin.site.register(Hall)
admin.site.register(HMCChairman)
admin.site.register(Room)
admin.site.register(Student)
admin.site.register(Complaint)


