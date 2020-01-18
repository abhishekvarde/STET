from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from django.template import RequestContext
# from pytesseract import image_to_string
import image

from APIs.models import Registration_form
from APIs.serializers import registration_model_serializer
from .models import User
from django.core.mail import send_mass_mail, send_mail


def img(request):
    print(image_to_string())


def home(request):
    return render(request, "teacher/index.html")


def register(request):
    logout(request)
    if request.method == 'POST':
        print('11')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        password = request.POST.get('password')

        if not User.objects.filter(username=email).exists():
            user_obj = User.objects.create_user(username=email, password=password, email=email, first_name=first_name,
                                                last_name=last_name, phone_no=phone_no)
            user_obj.save()
        else:
            return redirect('/teacher/login_teacher/')
            # send_email();

        request.session['email'] = email
        return redirect('/teacher/otp')
    else:
        return render(request, 'teacher/register.html')


def login_teacher(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)

        if not User.objects.filter(username=email):
            return redirect("/teacher/login_teacher")

        user = authenticate(username=email, password=password)
        user_obj = User.objects.get(username=email)

        request.session['email'] = email

        if user is None:
            return redirect('/teacher/login_teacher')

        if user_obj.is_staff == 1:
            login(request, user)
            print("i am in login")
            return redirect('/teacher/instructions')
        else:
            return redirect('/teacher/otp')
    # logout(request)
    return render(request, 'teacher/login.html')


def instructions(request):
    if not request.user.is_authenticated:
        return redirect('/teacher/login_teacher')
    return render(request, 'teacher/instructions.html')


def otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = request.POST.get('otp')

        if not User.objects.filter(username=email):
            return redirect("/teacher/register/")

        if otp == '1234':
            print(70)
            user = User.objects.get(username=email)
            user.is_staff = 1
            user.save()
            login(request, user)
            return redirect('/teacher/instructions/')
        else:
            return render(request, 'teacher/otp.html')

    if request.session.get('email', 'no_email') == 'no_email':
        return redirect('/teacher/login_teacher/')

    return render(request, 'teacher/otp.html')


def fill_or_edit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':  # here we will submit the application form
            user = request.user
            respect = request.POST.get('respect')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            father_first_name = request.POST.get('father_first_name')
            father_last_name = request.POST.get('father_last_name')
            mother_first_name = request.POST.get('mother_first_name')
            mother_last_name = request.POST.get('mother_last_name')
            dob = request.POST.get('dob')
            address_line_1 = request.POST.get('address_line_1')
            address_line_2 = request.POST.get('address_line_2')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pin_code = request.POST.get('pin_code')
            email = request.POST.get('email')
            phone_no = request.POST.get('phone_no')
            paper_language = request.POST.get('paper_language')
            category_of_teacher = request.POST.get('category_of_teacher')
            orthopedically_or_locomotor_impaired = request.POST.get('orthopedically_or_locomotor_impaired')
            degree_of_disability = request.POST.get('degree_of_disability')
            already_appeared = request.POST.get('already_appeared')
            receipt = request.POST.get('receipt')
            amount = request.POST.get('amount')
            name_of_bank = request.POST.get('name_of_bank')
            # user_image = request.POST.get('#user_image')
            # signature_image = request.POST.get('#signature_image')

            flag = 0

            if Registration_form.objects.filter(user=user):
                form_obj = Registration_form.objects.get(user=user)
                flag = 1
            else:
                form_obj = Registration_form()
                form_obj.user = request.user

            if respect:
                form_obj.respect = respect
            if first_name:
                form_obj.first_name = first_name
            if last_name:
                form_obj.last_name = last_name
            if father_first_name:
                form_obj.father_first_name = father_first_name
            if father_last_name:
                form_obj.father_last_name = father_last_name
            if mother_first_name:
                form_obj.mother_first_name = mother_first_name
            if mother_last_name:
                form_obj.mother_last_name = mother_last_name
            if dob:
                form_obj.dob = dob
            if address_line_1:
                form_obj.address_line_1 = address_line_1
            if address_line_2:
                form_obj.address_line_2 = address_line_2
            if city:
                form_obj.city = city
            if pin_code:
                form_obj.pin_code = pin_code
            if state:
                form_obj.state = state
            if email:
                form_obj.email = email
            if phone_no:
                form_obj.phone_no = phone_no
            if paper_language:
                form_obj.paper_language = paper_language
            if category_of_teacher:
                form_obj.category_of_teacher = category_of_teacher
            if orthopedically_or_locomotor_impaired:
                if orthopedically_or_locomotor_impaired == "True":
                    form_obj.orthopedically_or_locomotor_impaired = True
                else:
                    form_obj.orthopedically_or_locomotor_impaired = False
            if degree_of_disability:
                form_obj.degree_of_disability = degree_of_disability
            if already_appeared:
                if already_appeared == "True":
                    form_obj.already_appeared = True
                else:
                    form_obj.already_appeared = False
            if receipt:
                form_obj.receipt = receipt
            if amount:
                form_obj.amount = amount
            if name_of_bank:
                form_obj.name_of_bank = name_of_bank
            # if  # signature_image:
            #     form_obj.  # signature_image = #signature_image
            # if  # user_image:
            #     form_obj.  # user_image = #user_image

            form_obj.save()
            if flag:
                message = 'Form is updated'
            else:
                message = 'Form is saved'

            if Registration_form.objects.filter(user=request.user):
                form_obj = Registration_form.objects.get(user=request.user)
                data = registration_model_serializer(form_obj)
            else:
                return redirect('/teacher/login_teacher/')
            return render(request, 'teacher/final_form.html', {'data': data})  # redirected to the form page
        else:
            if Registration_form.objects.filter(user=request.user):
                form_obj = Registration_form.objects.get(user=request.user)
                data = registration_model_serializer(form_obj)
            else:
                data = {}
            return render(request, 'teacher/form.html', {'data': data})  # redirected to the form page
    else:
        return redirect('/teacher/login_teacher/')


def send_email():
    send_mail(
        'Subject',
        '1234',
        'roylamba1793@gmail.com',
        ['prajwalpmahale@gmail.com']
    )
