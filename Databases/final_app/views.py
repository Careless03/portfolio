from django.shortcuts import render, get_object_or_404, redirect
from .models import Member, Instructor, Classes, Booking
from django.utils.timezone import now
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.timezone import timedelta
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ClassForm


def index(request):
    """Homepage listing all available classes."""
    classes = Classes.objects.all()
    context = {'classes': classes}
    return render(request, 'final_app/main.html', context)


@login_required
def member_list(request):
    """View for members or staff to see member information."""
    if request.user.is_staff:
        # Staff sees all members
        members = Member.objects.all()
        context = {"members": members}
    else:
        # Regular users see only their own membership
        try:
            member = request.user.membership  # Access the related Member object
            context = {"members": [member]}  # Wrap in a list for template consistency
        except Member.DoesNotExist:
            messages.error(request, "You do not have an active membership.")
            return redirect('index')

    return render(request, 'final_app/member_list.html', context)


@login_required
def instructor_list(request):
    """View for staff to list all instructors."""
    if not request.user.is_staff:
        messages.error(request, "Access denied.")
        return redirect('index')

    instructors = Instructor.objects.all()
    context = {'instructors': instructors}
    return render(request, 'final_app/instructor_list.html', context)

@login_required
def class_list(request):
    """View to list all available classes."""
    classes = Classes.objects.all()
    context = {'classes': classes}
    return render(request, "final_app/class_list.html", context)

@login_required
def class_detail(request, class_id):
    """View details of a specific class and allow members to join."""
    gym_class = get_object_or_404(Classes, id=class_id)
    bookings = Booking.objects.filter(gym_class=gym_class)

    if request.method == 'POST':
        member = request.user.membership  # Get the current user's Member object
        # Check if the user is already booked for the class
        if bookings.filter(member=member).exists():
            messages.error(request, "You are already enrolled in this class.")
        else:
            # Create a new booking
            Booking.objects.create(
                member=member,
                gym_class=gym_class,
                booking_date=now().date(),
                status="Confirmed"
            )
            # Update attendance record
            member.attendance_record[str(now().date())] = f"Attended {gym_class.class_name}"
            member.save()

            messages.success(request, f"You have successfully joined {gym_class.class_name}.")

    context = {
        'class': gym_class,
        'instructor': gym_class.instructor,
        'bookings': bookings
    }
    return render(request, 'final_app/class_detail.html', context)


def login(request):
    """Login functionality."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'final_app/login.html')

def logout(request):
    """Logout functionality."""
    if request.user.is_authenticated:
        auth_logout(request)
        messages.success(request, "Logged out successfully.")
    return redirect('index')

def login_or_register(request):
    """Combined login and registration functionality."""
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('member_list')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('login_or_register')

        elif action == 'register':
            username = request.POST.get('new_username')
            email = request.POST.get('email', '').strip()
            password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return redirect('login_or_register')

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect('login_or_register')

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
                return redirect('login_or_register')

            try:
                user = User.objects.create_user(username=username, password=password, email=email)
                Member.objects.create(
                    user=user,
                    name=username,
                    email=email,
                    membership_type="Regular",
                    expiration_date=now().date() + timedelta(days=365),
                    attendance_record={}
                )
                auth_login(request, user)
                messages.success(request, "Registration successful! You are now logged in.")
                return redirect('member_list')
            except Exception as e:
                messages.error(request, f"An error occurred during registration: {e}")
                return redirect('login_or_register')

    return render(request, 'final_app/register_and_login.html')


@login_required
def manage_classes(request):
    """View for staff to create and delete classes."""
    if not request.user.is_staff:
        messages.error(request, "Access denied.")
        return redirect('index')

    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Class created successfully!")
            return redirect('manage_classes')
        else:
            messages.error(request, "There was an error creating the class.")
    else:
        form = ClassForm()

    classes = Classes.objects.all()
    context = {'form': form, 'classes': classes}
    return render(request, 'final_app/manage_classes.html', context)


@login_required
def delete_class(request, class_id):
    """View for staff to delete a class."""
    if not request.user.is_staff:
        messages.error(request, "Access denied.")
        return redirect('index')

    gym_class = get_object_or_404(Classes, id=class_id)
    gym_class.delete()
    messages.success(request, "Class deleted successfully!")
    return redirect('manage_classes')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def manage_staff(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        action = request.POST.get("action")
        user = User.objects.get(id=user_id)
        if action == "grant":
            user.is_staff = True
        elif action == "revoke":
            user.is_staff = False
        user.save()
        return redirect('manage_staff')

    users = User.objects.all()
    return render(request, 'final_app/manage_staff.html', {'users': users})