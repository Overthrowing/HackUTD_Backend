from django.db import models

# Create your models here.
class Patient(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])

    # Contact Information
    # email = models.EmailField(blank=True, null=True)
    # phone_number = models.CharField(max_length=20, blank=True, null=True)
    # address = models.TextField(blank=True, null=True)

    # Medical Information
    # medical_history = models.TextField(blank=True, null=True)
    # medications = models.TextField(blank=True, null=True)
    # allergies = models.TextField(blank=True, null=True)
    
    # Relationships
    # primary_doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, blank=True, null=True)
    # appointments = models.ManyToManyField('Appointment', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Doctor(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # Contact Information
    email = models.EmailField(blank=True, null=True)


    
# class Room(models.Model):
#     # Room Information
#     room_number = models.CharField(max_length=10, unique=True)
#     room_type = models.CharField(max_length=50, choices=[('Single', 'Single Room'), ('Double', 'Double Room'), ('ICU', 'Intensive Care Unit')])

#     # Status
#     is_occupied = models.BooleanField(default=False)
#     occupancy_start_date = models.DateField(blank=True, null=True)
#     occupancy_end_date = models.DateField(blank=True, null=True)

#     # Bed Capacity
#     total_beds = models.PositiveIntegerField()
#     available_beds = models.PositiveIntegerField()

#     def __str__(self):
#         return f'Room {self.room_number}'