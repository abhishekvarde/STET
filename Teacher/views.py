from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from .models import User
from django.core.mail import send_mass_mail, send_mail


# Create your views here.


def home(request):
    return render(request, "teacher/index.html")


def register(request):
    if request.method == 'POST':
        print('11')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        password = request.POST.get('password')

        # request['email'] = email

        if not User.objects.filter(username=email).exists():
            user_obj = User.objects.create_user(username=email, password=password, email=email,first_name=first_name,last_name=last_name,phone_no=phone_no)
            user_obj.save()
            # send_email();
        return redirect('/teacher/otp')
    else:
        return render(request, 'teacher/register.html')


def login_teacher(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        user_obj = User.objects.get(username=username)
        print("i am in login")

        if user is None:
            return redirect('/teacher/login_teacher')

        if user_obj.is_staff == 1:
            login(request, user)
            print("i am in login")
            return redirect('/teacher/instructions')
        else:
            return redirect('/teacher/otp')

    logout(request)
    return render(request, 'teacher/login.html')


def instructions(request):
    if not request.user.is_authenticated:
        return redirect('/teacher/login_teacher')
    return render(request, 'teacher/instructions.html')


def otp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        otp = request.POST.get('otp');
        print(68)
        if otp == '1234':
            print(70)
            user_obj = User.objects.get(username=username)
            user_obj.is_staff = 1
            user_obj.save()

            return render(request, 'teacher/login.html')

        else:
            return render(request, 'teacher/otp.html')
    return render(request, 'teacher/otp.html')


def send_email():
    send_mail(
        'Subject',
        '1234',
        'roylamba1793@gmail.com',
        ['prajwalpmahale@gmail.com']
    )
