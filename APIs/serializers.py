from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Registration_form


class User_model(object):
    def __init__(self, email, username):
        self.email = email
        self.username = username


class user_model_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class registration_model_serializer(serializers.ModelSerializer):
    class Meta:
        model = Registration_form
        fields = '__all__'


# class RegistrationSerializer(serializers.Serializer):
#
#     def restore_form(self, attrs, instance=None):
#         if instance is not None:
#             instance.first_name = attrs.get('email', instance.first_name)
#             instance.last_name = attrs.get('last_name', instance.last_name)
#             instance.email = attrs.get('email', instance.email)
#             instance.address = attrs.get('address', instance.address)
#             instance.save()
#             return instance
#         return User_model(**attrs)


# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=30)
#     email = serializers.EmailField(max_length=30)
#
#     def restore_user(self, attrs, instance=None):
#         if instance is not None:
#             instance.email = attrs.get('email', instance.email)
#             instance.content = attrs.get('username', instance.username)
#             return instance
#         return User_model(**attrs)
