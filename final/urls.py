from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = "final"
urlpatterns = [
    path("", views.signup, name='signup'),
    path("signin/", auth_views.LoginView.as_view(
        template_name='final/signin.html'), name='signin'),
    path("homepage", views.homepage, name='homepage'),
    path("logout/", auth_views.LogoutView.as_view(
        template_name='final/logout.html'), name='logout'),

    path('student-form', views.studentform, name='studentform'),
    path('student-verify-alert', views.student_verify_alert, name='student_verify'),


    path('semister-form-fillup/', views.semister_form, name='semister_form'),
    path("semister-attendence-check/<str:semister_no>",
         views.attendence_verify, name='attendence_verify'),


    path('payment-form/', views.payment_form, name='payment_form'),
    path('payment-verify/', views.payment_verify, name='payment_verify'),


    path('staff-create-form', views.staffform, name='staff_create'),

    path('teacher-students/<str:dept>',
         views.teacher_students, name='teacher_students'),
    path('register-students/',
         views.register_students, name='register_students'),


    path('update-student-by-teacher/<str:semister_no>/',
         views.update_student_by_teacher, name='update_student_by_teacher'),

    path('update-student-by-register/<str:student_id>/',
         views.update_student_by_register, name='up')

]