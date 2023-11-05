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
    primary_doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, blank=True, null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, blank=True, null=True, related_name="patients")
    # appointments = models.ManyToManyField('Appointment', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Doctor(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # General Information
    medical_specialization = models.CharField(max_length=256)
    hospital = models.CharField(max_length=256)
    years_of_experience = models.PositiveIntegerField()

    # Contact Information
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.medical_specialization}'


    
class Room(models.Model):
    # General Room information
    capacity = models.PositiveIntegerField()
    temperature = models.IntegerField() 

    # Occupant Information
    priority = models.CharField(max_length=10, choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')])
    is_empty = models.BooleanField(default=False)
    is_patient_room = models.BooleanField(default= True)

    def __str__(self):
        return f'Room, Capacity: {self.capacity}'

