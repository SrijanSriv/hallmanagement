# Generated by Django 4.0.5 on 2023-04-22 17:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
                ('_type', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('total_rooms', models.IntegerField()),
                ('rooms_available', models.IntegerField()),
                ('amenities', models.IntegerField()),
                ('salary_grant', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('maintainance_grant', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='HMC_Chaiman',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('total_grant', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_capacity', models.IntegerField()),
                ('occupancy', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('hall_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hallmanage.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=50)),
                ('mess_charge', models.IntegerField()),
                ('amenity_charge', models.IntegerField()),
                ('room_rent', models.IntegerField()),
                ('hall_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hallmanage.hall')),
                ('room_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hallmanage.room')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('position', models.TextField(blank=True, choices=[('mess_incharge', 'mess_incharge'), ('warden', 'warden'), ('misc', 'misc')], max_length=300, null=True)),
                ('salary', models.IntegerField()),
                ('hall_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hallmanage.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1000)),
                ('is_resolved', models.BooleanField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hallmanage.student')),
            ],
        ),
    ]