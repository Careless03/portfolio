import csv
import os
from datetime import datetime
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from final_app.models import Member, Instructor, Classes, Booking
from django.conf import settings
from django.utils.timezone import now
import json


class Command(BaseCommand):
    help = "Import CSV data into the database and clean corrupted data."

    def handle(self, *args, **kwargs):
        self.import_members('members.csv')
        self.import_instructors('instructors.csv')
        self.import_classes('classes.csv')
        self.import_bookings('bookings.csv')
        self.stdout.write(self.style.SUCCESS("Data imported successfully!"))

    def clean_data(self, field, default=None, field_type=str):
        """
        Clean data by checking if it exists and is of the correct type.
        Returns the default value if the data is invalid.
        """
        if not field or field.strip() == "":
            return default
        try:
            if field_type == int:
                return int(field)
            elif field_type == float:
                return float(field)
            elif field_type == datetime:
                return datetime.strptime(field, "%Y-%m-%d").date()
            elif field_type == json:
                return json.loads(field)
            return field.strip()
        except (ValueError, TypeError, json.JSONDecodeError):
            return default

    def import_members(self, file_path):
        file_path = os.path.join(settings.BASE_DIR, 'final_app', 'data', file_path)
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                email = self.clean_data(row.get('email'), default='unknown@example.com')
                name = self.clean_data(row.get('name'), default='Unknown Member')
                membership_type = self.clean_data(row.get('membership_type'), default='Regular')
                expiration_date = self.clean_data(row.get('expiration_date'), default=now().date(), field_type=datetime)
                attendance_record = self.clean_data(row.get('attendance_record'), default={}, field_type=json)

                user, _ = User.objects.get_or_create(
                    username=email,
                    email=email
                )
                Member.objects.update_or_create(
                    user=user,
                    defaults={
                        'name': name,
                        'email': email,
                        'membership_type': membership_type,
                        'expiration_date': expiration_date,
                        'attendance_record': attendance_record,
                    },
                )
                self.stdout.write(f"Imported member: {name}")

    def import_instructors(self, file_path):
        file_path = os.path.join(settings.BASE_DIR, 'final_app', 'data', file_path)
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = self.clean_data(row.get('name'), default='Unknown Instructor')
                specialty = self.clean_data(row.get('specialty'), default='General')
                class_schedule = self.clean_data(row.get('class_schedule'), default={}, field_type=json)

                Instructor.objects.update_or_create(
                    name=name,
                    defaults={
                        'specialty': specialty,
                        'class_schedule': class_schedule,
                    },
                )
                self.stdout.write(f"Imported instructor: {name}")

    def import_classes(self, file_path):
        file_path = os.path.join(settings.BASE_DIR, 'final_app', 'data', file_path)
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                class_name = self.clean_data(row.get('class_name'), default='Unnamed Class')
                instructor_name = self.clean_data(row.get('instructor'), default='Unknown Instructor')
                schedule = self.clean_data(row.get('schedule'), default=now(), field_type=datetime)
                max_capacity = self.clean_data(row.get('max_capacity'), default=10, field_type=int)

                try:
                    instructor = Instructor.objects.get(name=instructor_name)
                except Instructor.DoesNotExist:
                    self.stderr.write(f"Instructor {instructor_name} does not exist. Skipping class {class_name}.")
                    continue

                try:
                    # Use unique constraints to avoid duplicate classes
                    class_obj, created = Classes.objects.get_or_create(
                        class_name=class_name,
                        instructor=instructor,
                        schedule=schedule,
                        defaults={'max_capacity': max_capacity},
                    )
                    if created:
                        self.stdout.write(f"Imported class: {class_name}")
                    else:
                        self.stdout.write(f"Class already exists: {class_name}")
                except Exception as e:
                    self.stderr.write(f"Error importing class {class_name}: {e}")


    from datetime import timedelta

    def import_bookings(self, file_path):
        file_path = os.path.join(settings.BASE_DIR, 'final_app', 'data', file_path)
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                member_email = self.clean_data(row.get('email'), default=None)
                gym_class_name = self.clean_data(row.get('class_name'), default=None)
                booking_date = self.clean_data(row.get('schedule'), default=None, field_type=datetime)
                status = self.clean_data(row.get('status'), default='Confirmed')

                if not member_email or not gym_class_name or not booking_date:
                    self.stderr.write(f"Skipping booking due to missing data: {row}")
                    continue

                try:
                    member = Member.objects.get(email=member_email)
                    gym_class = Classes.objects.get(
                        class_name=gym_class_name,
                        schedule=booking_date,  # Match by both name and schedule
                    )
                    Booking.objects.get_or_create(
                        member=member,
                        gym_class=gym_class,
                        defaults={'booking_date': booking_date, 'status': status},
                    )
                    self.stdout.write(f"Imported booking for {member_email} in {gym_class_name} on {booking_date}")
                except Member.DoesNotExist:
                    self.stderr.write(f"Member with email {member_email} does not exist. Skipping booking.")
                except Classes.DoesNotExist:
                    self.stderr.write(f"Class {gym_class_name} does not exist on {booking_date}. Ensure classes.csv is correct.")
                except Exception as e:
                    self.stderr.write(f"Unexpected error: {e}. Skipping booking.")


