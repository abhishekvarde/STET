from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Registration_form(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    respect = models.CharField(max_length=20, default="")
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    father_first_name = models.CharField(max_length=30, default="")
    father_last_name = models.CharField(max_length=30, default="")
    mother_first_name = models.CharField(max_length=30, default="")
    mother_last_name = models.CharField(max_length=30, default="")
    dob = models.CharField(max_length=20, default="00-00-0000")
    address_line_1 = models.TextField(max_length=100, default="")
    address_line_2 = models.TextField(max_length=100, default="")
    district = models.CharField(max_length=30, default="")
    pin_code = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=30, default="")
    phone_no = models.CharField(max_length=10, default="")
    paper_language = models.CharField(max_length=30, default="")
    category_of_teacher = models.CharField(max_length=100, default="")
    # user_image = models.ImageField(upload_to="form_images/")
    orthopedically_or_locomotor_impaired = models.BooleanField(default=False)
    degree_of_disability = models.IntegerField(default=0)
    already_appeared = models.BooleanField(default=False)
    receipt = models.CharField(max_length=100, default="")
    amount = models.FloatField(default=0)
    name_of_bank = models.CharField(max_length=100, default="")
    # signature_image = models.ImageField(upload_to="form_images/")
