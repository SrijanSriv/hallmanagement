from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class HMCChairman(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    total_grant = models.IntegerField(null=False, blank=False)
    

class Hall(models.Model):
    _id = models.IntegerField(primary_key=True)
    _type = models.CharField(max_length=10, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    total_rooms = models.IntegerField(null=False, blank=False)
    rooms_available = models.IntegerField(null=False, blank=False)
    amenities = models.IntegerField()
    salary_grant = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    maintainance_grant = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

class Staff(models.Model):

    Roles = [
        ("mess_incharge", "mess_incharge"),
        ("warden", "warden"),
        ("misc", "misc"),
    ]

    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    hall_no = models.ForeignKey(Hall, on_delete=models.CASCADE)
    position = models.TextField(max_length=300, choices=Roles, null=True, blank=True)
    salary = models.IntegerField(null=False, blank=False)



class Room(models.Model):
    _id = models.IntegerField(primary_key=True)
    hall_no = models.ForeignKey(Hall, on_delete=models.CASCADE)
    room_capacity = models.IntegerField()
    occupancy = models.IntegerField()
    cost = models.IntegerField()


class Student(models.Model):
    _id = models.CharField(primary_key=True, null=False, blank=False, max_length=50)
    name = models.CharField(null=False, blank=False, max_length=50)
    address = models.CharField(null=False, blank=False, max_length=50)
    contact_no = models.CharField(null=False, blank=False, max_length=50)
    hall_assigned = models.ForeignKey(Hall , on_delete=models.CASCADE)
    room_assigned = models.ForeignKey(Room , on_delete=models.CASCADE)
    mess_charge = models.IntegerField()
    amenity_charge = models.IntegerField()
    room_rent = models.IntegerField()
    

class Complaint(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=1000)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_resolved = models.BooleanField()
