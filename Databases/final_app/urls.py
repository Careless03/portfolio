from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.member_list, name='member_list'),
    path('instructors/', views.instructor_list, name='instructor_list'),
    path('classes/', views.class_list, name='class_list'),
    path('classes/<int:class_id>/', views.class_detail, name='class_detail'),
    path('login_or_register/', views.login_or_register, name='login_or_register'),
    path('logout/', views.logout, name='logout'),
    path('manage_classes/', views.manage_classes, name = 'manage_classes'),
    path('delete_class/<int:class_id>/', views.delete_class, name='delete_class'),
    path('manage_staff/', views.manage_staff, name = 'manage_staff')
]
