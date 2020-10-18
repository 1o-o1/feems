from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib import messages
from .form import StudentForm, SemisterForm, StaffForm, UpdateStudentByTeacher, UpdateStudentByRegister
from .models import Student, Semister_Fee, Semister
from .decorator import exists_student
from .filters import StudentFilter
# Create your views here.


def homepage(request):
    return render(request, 'final/homepage.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.info(request, f"{username} signup completed")
            user = authenticate(username=username, password=password)
            dj_login(request, user)
            return redirect("final:homepage")
    else:
        form = UserCreationForm()

    cont = {
        'form': form
    }
    return render(request, 'final/signup.html', cont)


@exists_student
def studentform(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.info(
                request, f"Your Student Verify form submitted Successfully")
            return redirect("final:student_verify")

    else:
        form = StudentForm()

    return render(request, 'final/student_form.html', {"form": form})


def student_verify_alert(request):
    student = Student.objects.get(user=request.user)

    permission = student.is_student

    return render(request, 'final/student_verify.html', {"permission": permission})


def semister_form(request):
    if request.method == "POST":
        form = SemisterForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.student = Student.objects.get(user=request.user)
            form.save()
            return redirect('final:attendence_verify', semister_no=form.semister)
    else:
        form = SemisterForm()

    cont = {
        'form': form
    }

    return render(request, 'final/semister_form.html', cont)


def attendence_verify(request, semister_no):
    student = Student.objects.get(user=request.user)
    student_semister = Semister.objects.filter(
        student=student, semister=semister_no).first()
    student_attendence = student_semister.have_attendence
    print(student_attendence)
    return render(request, 'final/attendence_verify.html', {"permission": student_attendence})


def payment_form(request):
    student = Student.objects.get(user=request.user)
    semister = Semister.objects.filter(student=student).last().semister
    if request.method == "POST":
        admission_fee = request.POST.get("admission_fee")
        session_charge = request.POST.get("session_charge")
        exam_fee = request.POST.get("exam_fee")
        hall_fee = request.POST.get("hall_fee")
        library_fee = request.POST.get("library_fee")
        transport_fee = request.POST.get("transport_fee")
        medical_fee = request.POST.get("medical_fee")

        form = Semister_Fee(student=student,
                            semister=semister,
                            admission_fee=admission_fee,
                            session_charge=session_charge,
                            exam_fee=exam_fee,
                            hall_fee=hall_fee,
                            library_fee=library_fee,
                            transport_fee=transport_fee,
                            medical_fee=medical_fee)
        form.save()
        messages.info(request, f"Your Payment Is completed")
        return redirect("final:payment_verify")
    return render(request, 'final/payment_form.html')


def payment_verify(request):

    cont = {
        'permission': True
    }

    return render(request, 'final/payment_verify.html', cont)


def staffform(request):
    form = StaffForm()

    if request.method == 'POST':
        form = StaffForm(request.POST)

        if form.is_valid():
            dept = form.cleaned_data.get("department")
            role = form.cleaned_data.get("Role")
            print(role)
            if role == "Teacher":
                return redirect('final:teacher_students', dept=dept)
            else:
                return redirect('final:register_students')

    return render(request, 'final/staff_form.html', {'form': form})


def teacher_students(request, dept):
    students = Student.objects.filter(dept=dept)
    myfilter = StudentFilter(request.GET, students)
    students = myfilter.qs
    cont = {
        'students': students,
        'myfilter': myfilter
    }
    return render(request, 'final/teacher_student.html', cont)


def register_students(request):

    students = Student.objects.all()
    myfilter = StudentFilter(request.GET, students)
    students = myfilter.qs
    cont = {
        'students': students,
        'myfilter': myfilter
    }

    return render(request, 'final/register_students.html', cont)


def update_student_by_teacher(request, semister_no):
    student = Student.objects.get(user=request.user)
    semister_for_student = Semister.objects.filter(
        student=student, semister=semister_no).first()

    if request.method == "POST":
        form = UpdateStudentByTeacher(
            request.POST, instance=semister_for_student)

        if form.is_valid():
            form.save()
            messages.info(request, f"Student Info Updated")
            return redirect('final:teacher_students', student.dept)
    else:
        form = UpdateStudentByTeacher(instance=semister_for_student)

    cont = {
        'form': form
    }

    return render(request, 'final/update_student_by_teacher.html', cont)


def update_student_by_register(request, student_id):
    student = Student.objects.get(pk=student_id)

    if request.method == "POST":
        form = UpdateStudentByRegister(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.info(request, f"Student Update By Register Office")
            return redirect('final:register_students')
    else:
        form = UpdateStudentByRegister(instance=student)

    return render(request, 'final/update_student_by_register.html', {"form": form})