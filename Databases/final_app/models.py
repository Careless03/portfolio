from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Member(models.Model):
    # Associate each member with a user account
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='membership')
    email = models.EmailField(max_length=255, unique=True, null=True, blank=False)
    MEMBERSHIP_TYPE_CHOICES = (
        ('Regular', 'Regular'),
        ('Premium', 'Premium'),
    )
    name = models.CharField(max_length=255)
    membership_type = models.CharField(max_length=7, choices=MEMBERSHIP_TYPE_CHOICES)
    expiration_date = models.DateField()
    attendance_record = models.JSONField()

    def __str__(self):
        return f"{self.name} has a {self.membership_type} membership"

    class Meta:
        db_table = "Members"


class Instructor(models.Model):
    # Automatically create a unique primary key for instructor
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    class_schedule = models.JSONField()

    def __str__(self):
        return f"{self.name} "

    class Meta:
        db_table = "Instructors"


class Classes(models.Model):
    # Automatically create a unique primary key for class
    class_name = models.CharField(max_length=255)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='classes')
    schedule = models.DateField()
    max_capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.class_name

    class Meta:
        db_table = "Classes"


class Booking(models.Model):
    BOOKING_STATUS_CHOICES = (
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('No-Show', 'No-Show'),
    )
    # Automatically create a unique primary key for booking
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='bookings')
    gym_class = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField(default=now)
    status = models.CharField(max_length=9, choices=BOOKING_STATUS_CHOICES)

    def __str__(self):
        return f"Booking for {self.member.name} in {self.gym_class.class_name} on {self.booking_date}"

    class Meta:
        unique_together = ('member', 'gym_class')  # Ensure a member can't book the same class twice
        db_table = "Bookings"
