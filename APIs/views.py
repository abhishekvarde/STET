from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import User_model, user_model_serializer, registration_model_serializer
from .models import Registration_form
# from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from Teacher.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def user_register(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    phone_no = request.POST.get('phone_no')

    if User.objects.filter(username=email) or User.objects.filter(phone_no=phone_no):
        error = 'true'
        message = 'Entered username is already present'
        token = 'empty'
        return Response({'error': error, 'message': message, 'token': token})

    user = User.objects.create_user(username=email, email=email, first_name=first_name, last_name=last_name,
                                    phone_no=phone_no, password=password)
    # user.set_password(password)
    # user.first_name = first_name
    # user.last_name = last_name
    user.save()
    token = Token.objects.create(user=user)
    token = token.key
    error = 'false'
    message = 'User is register'
    token = token
    data = {'error': error, 'message': message, 'token': token}
    return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    email = request.POST.get('email')
    print(email)
    if User.objects.filter(username=email):
        user = User.objects.get(username=email)
        # data = user_model_serializer(user)
        if Token.objects.filter(user=user):
            token_obj = Token.objects.get(user=user)
            token_obj.delete()
        token_obj = Token.objects.create(user=user)
        error = 'true'
        message = 'User is login'
        token = token_obj.key
        data = {'error': error, 'message': message, 'token': token}
        return Response(data)
    else:
        error = 'false'
        message = 'User information is not valid'
        token = 'empty'
        data = {'error': error, 'message': message, 'token': token}
        return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_profile(request):
    token = request.POST.get('token')
    if Token.objects.filter(key=token):
        token_obj = Token.objects.get(key=token)
        user = token_obj.user
        user_details = user_model_serializer(user)
        error = 'false'
        message = 'Profile is sent'
        token = 'empty'
        data = {'error': error, 'message': message, 'token': token, 'user_profile': user_details.data}
        return Response(data)
    else:
        error = 'true'
        message = 'Profile is not sent'
        token = 'empty'
        data = {'error': error, 'message': message, 'token': token}
        return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_form(request):
    token = request.POST.get('token')
    if Token.objects.filter(key=token):
        token_obj = Token.objects.get(key=token)
        user = token_obj.user
        if Registration_form.objects.filter(user=user):
            form_obj = Registration_form.objects.get(user=user)
            data = registration_model_serializer(form_obj)
            error = 'false'
            message = 'Form is sent'
            token = 'empty'
            data = {'error': error, 'message': message, 'token': token, 'form_data': data.data}
            return Response(data)
        else:
            error = 'true'
            message = 'Form is not present'
            token = 'empty'
            data = {'error': error, 'message': message, 'token': token}
            return Response(data)
    else:
        error = 'true'
        message = 'User is not present / Token is not valid.'
        token = 'empty'
        data = {'error': error, 'message': message, 'token': token}
        return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def save_form(request):
    token = request.POST.get('token')
    if Token.objects.filter(key=token):
        token_obj = Token.objects.get(key=token)
        user = token_obj.user
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
        district = request.POST.get('district')
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

        if Registration_form.objects.filter(user=user):
            form_obj = Registration_form.objects.get(user=user)
            flag = 1
        else:
            form_obj = Registration_form()

        if user:
            form_obj.user = user
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
        if district:
            form_obj.district = district
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
        data = registration_model_serializer(form_obj)
        error = 'false'
        if flag:
            message = 'Form is updated'
        else:
            message = 'Form is saved'
        token = 'empty'
        data = {'error': error, 'message': message, 'token': token, 'form_data': data.data}
        return Response(data)
    else:
        error = 'true'
        message = 'token is not valid'
        token = 'empty'
        data = {'error': error, 'message': message, 'token': token}
        return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def submit_form(request):
    token = request.POST.get('token')
    if Token.objects.filter(key=token):
        user = Token.objects.get(key=token)
    pass

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def fun(requset):
#     yeh_lo = 'user=models.OneToOneField(User,on_delete=models.CASCADE),,respect=models.CharField(max_length=20,default=""),,first_name=models.CharField(max_length=30,default=""),,last_name=models.CharField(max_length=30,default=""),,father_first_name=models.CharField(max_length=30,default=""),,father_last_name=models.CharField(max_length=30,default=""),,mother_first_name=models.CharField(max_length=30,default=""),,mother_last_name=models.CharField(max_length=30,default=""),,dob=models.CharField(max_length=20,default="00-00-0000"),,address_line_1=models.TextField(max_length=100,default=""),,address_line_2=models.TextField(max_length=100,default=""),,district=models.CharField(max_length=30,default=""),,state=models.CharField(max_length=30,default=""),,email=models.CharField(max_length=30,default=""),,phone_no=models.CharField(max_length=10,default=""),,paper_language=models.CharField(max_length=30,default=""),,category_of_teacher=models.CharField(max_length=100,default=""),,#user_image=models.ImageField(upload_to="form_images/"),,orthopedically_or_locomotor_impaired=models.BooleanField(default=False),,degree_of_disability=models.IntegerField(default=0),,already_appeared=models.BooleanField(default=False),,receipt=models.CharField(max_length=100,default=""),,amount=models.FloatField(default=0),,name_of_bank=models.CharField(max_length=100,default=""),,#signature_image=models.ImageField(upload_to="form_images/"),,'
#     yeh_lo = yeh_lo.split(",,")
#     for i in range(len(yeh_lo)):
#         voh_lo = yeh_lo[i].split("=")
#         print("if " + voh_lo[0] + ":\n\tform_obj." + voh_lo[0] + " = " + voh_lo[0] + "")
